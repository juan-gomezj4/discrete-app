from __future__ import annotations

import streamlit as st
from typing import Any, Dict, List
from pathlib import Path
import sys

# Asegurar que el paquete raíz esté en sys.path cuando Streamlit ejecuta por archivo
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from app.utils import load_questions, get_topics, get_questions_for_topic, get_exam_questions, format_correct_answer_display
from app.logic import compute_score


APP_TITLE = "Práctica Interactiva: Matemáticas Discretas"
QUESTIONS_PATH = "data/questions.json"
DEFAULT_QUESTIONS_COUNT = 4  # Número de preguntas por defecto

# Paleta básica para consistencia visual
PALETTE: Dict[str, str] = {
    "primary": "#2563EB",  # azul
    "success": "#16A34A",  # verde
    "warning": "#D97706",  # ámbar
    "danger": "#DC2626",   # rojo
    "muted": "#6B7280",    # gris
}


def init_state() -> None:
    """Inicializa claves en session_state si no existen."""
    if "topic" not in st.session_state:
        st.session_state.topic = None
    if "current_idx" not in st.session_state:
        st.session_state.current_idx = 0
    if "responses" not in st.session_state:
        st.session_state.responses = []
    if "finished" not in st.session_state:
        st.session_state.finished = False
    if "data" not in st.session_state:
        st.session_state.data = None
    if "last_feedback" not in st.session_state:
        st.session_state.last_feedback = None  # (correct: bool, correct_text: str)
    if "mode" not in st.session_state:
        st.session_state.mode = "practice"  # "practice" o "exam"
    if "questions_count" not in st.session_state:
        st.session_state.questions_count = DEFAULT_QUESTIONS_COUNT


def reset_quiz() -> None:
    """Reinicia progreso del cuestionario."""
    st.session_state.current_idx = 0
    st.session_state.responses = []
    st.session_state.finished = False


def render_question(q: Dict[str, Any], idx: int) -> Any:
    """Renderiza controles de la pregunta según su tipo y retorna la respuesta."""
    st.subheader(f"Pregunta {idx + 1}")
    
    # Mostrar enunciado con mejor formato
    question_text = q.get("question", "")
    
    # Si la pregunta contiene símbolos matemáticos, usar markdown
    if any(symbol in question_text for symbol in ["∧", "∨", "¬", "⇒", "⇔", "∀", "∃"]):
        st.markdown(f"**{question_text}**")
    else:
        st.write(question_text)
    
    # Mostrar tema si está en modo examen
    if "_topic" in q:
        st.caption(f"📚 Tema: {q['_topic']}")
    
    q_type = q.get("type", "single")
    key = f"q_{idx}"

    if q_type == "single":
        options: List[str] = q.get("options", [])
        selected = st.radio("Elige una opción:", options=options, index=None, key=key)
        if selected is None:
            return None
        return options.index(selected) if selected in options else None

    if q_type == "multiple":
        options = q.get("options", [])
        selections = []
        for i, opt in enumerate(options):
            if st.checkbox(opt, key=f"{key}_{i}"):
                selections.append(i)
        return selections

    if q_type == "tf":
        choice = st.radio("Selecciona:", options=["Verdadero", "Falso"], index=None, key=key)
        if choice is None:
            return None
        return True if choice == "Verdadero" else False

    if q_type == "input":
        return st.text_input("Respuesta:", key=key)

    st.info("Tipo de pregunta no soportado")
    return None


def main() -> None:
    st.set_page_config(page_title=APP_TITLE, page_icon="🧠", layout="centered")
    init_state()

    # Estilos mínimos globales
    st.markdown(
        f"""
        <style>
            .badge {{
                display:inline-block;padding:4px 10px;border-radius:999px;
                background:{PALETTE['primary']};color:white;font-size:0.85rem;
            }}
            .ok {{color:{PALETTE['success']};font-weight:600;}}
            .err {{color:{PALETTE['danger']};font-weight:600;}}
            .muted {{color:{PALETTE['muted']};}}
            html, body, [data-testid="stAppViewContainer"] * {{ font-size: 16px; }}
            h1, h2, h3 {{ letter-spacing: 0.2px; }}
            .question-card {{
                background: rgba(37, 99, 235, 0.05);
                border: 1px solid rgba(107, 114, 128, 0.15);
                border-radius: 10px;
                padding: 14px 16px;
                margin: 8px 0 16px;
            }}
            button[kind="primary"] {{
                background: {PALETTE['primary']} !important; color: #fff !important; border: none !important;
            }}
            button[kind="primary"]:hover {{ filter: brightness(0.95); }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title(APP_TITLE)

    if st.session_state.data is None:
        try:
            st.session_state.data = load_questions(QUESTIONS_PATH)
        except Exception as e:
            st.error(f"Error al cargar preguntas: {e}\nAsegúrate de que 'data/questions.json' existe y tiene formato válido.")
            return

    topics = get_topics(st.session_state.data)

    with st.sidebar:
        st.header("Panel de Control")
        
        # Selector de modo
        mode = st.radio(
            "Modo de práctica:",
            options=["Práctica por tema", "Examen (1 de cada tema)"],
            index=0 if st.session_state.mode == "practice" else 1,
            help="Práctica: elige un tema específico. Examen: una pregunta aleatoria de cada tema."
        )
        
        if mode == "Examen (1 de cada tema)":
            st.session_state.mode = "exam"
            topic = None
        else:
            st.session_state.mode = "practice"
            topic = st.selectbox("Tema", options=["(elige)"] + topics, index=0)
            
            # Selector de cantidad de preguntas (solo en modo práctica)
            st.session_state.questions_count = st.slider(
                "Número de preguntas:",
                min_value=3,
                max_value=10,
                value=DEFAULT_QUESTIONS_COUNT,
                help="Cantidad de preguntas a responder (se sortean aleatoriamente si hay más disponibles)"
            )
        
        start = st.button("Iniciar" if not st.session_state.finished else "Reintentar", type="primary")

        st.divider()
        st.caption("💡 Ayuda rápida")
        if st.session_state.mode == "exam":
            st.markdown("- Modo examen: 1 pregunta de cada tema\n- Navega con Siguiente/Anterior\n- Finaliza para ver tu puntaje")
        else:
            st.markdown("- Selecciona un tema y cantidad\n- Navega con Siguiente/Anterior\n- Finaliza para ver tu puntaje")

    if start:
        if st.session_state.mode == "exam":
            st.session_state.topic = "Examen"
            reset_quiz()
        elif topic != "(elige)":
            st.session_state.topic = topic
            reset_quiz()
        else:
            st.warning("Selecciona un tema para iniciar.")

    if st.session_state.topic is None:
        st.info("Selecciona un modo y tema en la barra lateral, luego presiona Iniciar.")
        with st.expander("¿Cómo funciona?", expanded=True):
            st.markdown(
                """
                ### Modo Práctica por Tema
                - Elige un tema específico
                - Selecciona cuántas preguntas quieres (3-10)
                - Las preguntas se sortean aleatoriamente
                - Responde cada pregunta
                - Al final verás tu puntaje y las respuestas correctas
                
                ### Modo Examen
                - Se selecciona automáticamente 1 pregunta de cada tema
                - Las preguntas aparecen en orden aleatorio
                - Evalúa tu conocimiento general de todos los temas
                """
            )
        return

    # Obtener preguntas según el modo
    if st.session_state.topic == "Examen":
        questions = get_exam_questions(st.session_state.data)
    else:
        questions = get_questions_for_topic(
            st.session_state.data, 
            st.session_state.topic,
            max_questions=st.session_state.questions_count,
            shuffle=True
        )
    
    if not questions:
        st.warning("No hay preguntas disponibles.")
        return

    if st.session_state.finished:
        result = compute_score(questions, st.session_state.responses)

        # Resumen con métricas
        st.success("🎉 ¡Cuestionario completado!")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            st.metric("Correctas", result['correct'])
        with col_b:
            st.metric("Incorrectas", result['total'] - result['correct'])
        with col_c:
            percentage = (result["correct"] / max(1, result["total"])) * 100
            st.metric("Porcentaje", f"{percentage:.1f}%")
        
        st.progress(result["correct"] / max(1, result["total"]))
        
        # Mensaje de retroalimentación según el desempeño
        if percentage >= 90:
            st.success("¡Excelente! Dominas muy bien el tema.")
        elif percentage >= 70:
            st.info("¡Buen trabajo! Sigue practicando para mejorar.")
        else:
            st.warning("Sigue estudiando. La práctica hace al maestro.")

        st.divider()
        st.subheader("📊 Detalle de Respuestas")
        
        # Crear tabla resumen
        import pandas as pd
        table_data = []
        for i, (q, resp, det) in enumerate(zip(questions, st.session_state.responses, result["detail"])):
            q_type = q.get("type", "single")
            user_text = None
            
            # Formatear respuesta del usuario
            if q_type == "single":
                opts: List[str] = q.get("options", [])
                if isinstance(resp, int) and 0 <= resp < len(opts):
                    user_text = opts[resp]
            elif q_type == "multiple":
                opts = q.get("options", [])
                labels = []
                for idx in resp or []:
                    if isinstance(idx, int) and 0 <= idx < len(opts):
                        labels.append(opts[idx])
                user_text = ", ".join(labels) if labels else None
            elif q_type == "tf":
                if isinstance(resp, bool):
                    user_text = "Verdadero" if resp else "Falso"
            elif q_type == "input":
                user_text = str(resp or "")
            
            correct_text = format_correct_answer_display(q)
            
            table_data.append({
                "N°": i + 1,
                "Tema": q.get("_topic", st.session_state.topic if st.session_state.topic != "Examen" else "—"),
                "Tu Respuesta": user_text if user_text is not None else "—",
                "Respuesta Correcta": correct_text,
                "Resultado": "✅" if det["correct"] else "❌"
            })
        
        df = pd.DataFrame(table_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Detalle expandible por pregunta
        st.divider()
        with st.expander("🔍 Ver detalle completo de cada pregunta", expanded=False):
            for i, (q, resp, det) in enumerate(zip(questions, st.session_state.responses, result["detail"])):
                st.markdown(f"<span class='badge'>Pregunta {i + 1}</span>", unsafe_allow_html=True)
                
                # Mostrar tema si está disponible
                if "_topic" in q:
                    st.caption(f"📚 Tema: {q['_topic']}")
                
                st.write(q.get('question',''))
                correct_text = format_correct_answer_display(q)

                # Mostrar respuesta del usuario de forma legible
                q_type = q.get("type", "single")
                user_text = None
                if q_type == "single":
                    opts: List[str] = q.get("options", [])
                    if isinstance(resp, int) and 0 <= resp < len(opts):
                        user_text = opts[resp]
                elif q_type == "multiple":
                    opts = q.get("options", [])
                    labels = []
                    for idx in resp or []:
                        if isinstance(idx, int) and 0 <= idx < len(opts):
                            labels.append(opts[idx])
                    user_text = ", ".join(labels) if labels else None
                elif q_type == "tf":
                    if isinstance(resp, bool):
                        user_text = "Verdadero" if resp else "Falso"
                elif q_type == "input":
                    user_text = str(resp or "")

                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Tu respuesta:** {user_text if user_text is not None else '—'}")
                with col2:
                    st.write(f"**Correcta:** {correct_text}")
                
                st.markdown("**Resultado:** " + ("<span class='ok'>✅ Correcta</span>" if det["correct"] else "<span class='err'>❌ Incorrecta</span>"), unsafe_allow_html=True)
                st.divider()

        st.info("💡 Usa 'Reintentar' en la barra lateral para volver a empezar.")
        return

    idx = st.session_state.current_idx
    q = questions[idx]
    # Encabezado contextual del tema y progreso
    if st.session_state.mode == "exam":
        st.markdown(f"<span class='badge'>🎓 Modo Examen</span>", unsafe_allow_html=True)
    else:
        st.markdown(f"<span class='badge'>📚 {st.session_state.topic}</span>", unsafe_allow_html=True)
    
    st.caption(f"Pregunta {idx + 1} de {len(questions)}")
    st.progress((idx) / max(1, len(questions)))

    st.markdown("<div class='question-card'>", unsafe_allow_html=True)
    response = render_question(q, idx)
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Anterior", disabled=idx == 0):
            st.session_state.current_idx = max(0, idx - 1)
    with col2:
        is_last = idx == len(questions) - 1
        next_label = "Finalizar" if is_last else "Siguiente"
        if st.button(next_label, type="primary"):
            if len(st.session_state.responses) <= idx:
                st.session_state.responses.append(response)
            else:
                st.session_state.responses[idx] = response

            # Feedback inmediato sobre la respuesta actual
            try:
                from app.logic import evaluate_question
                is_correct = evaluate_question(q, response)
                correct_text = format_correct_answer_display(q)
                st.session_state.last_feedback = (is_correct, correct_text)
            except Exception:
                st.session_state.last_feedback = None

            if st.session_state.last_feedback is not None:
                ok, correct_text = st.session_state.last_feedback
                if ok:
                    st.success("✅ Respuesta correcta")
                else:
                    st.error("❌ Respuesta incorrecta")
                    st.caption(f"Correcta: {correct_text}")

            if is_last:
                st.session_state.finished = True
            else:
                st.session_state.current_idx = min(len(questions) - 1, idx + 1)


if __name__ == "__main__":
    main()


