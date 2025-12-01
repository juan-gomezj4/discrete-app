from __future__ import annotations

"""Utilidades de carga y formateo para la app.

Incluye funciones para cargar el banco de preguntas desde JSON y presentar
la respuesta correcta en un formato legible para el resumen final.
"""

import json
import random
from pathlib import Path
from typing import Any, Dict, List


def load_questions(json_path: str | Path) -> Dict[str, Any]:
    """Carga el archivo JSON con el banco de preguntas.

    Estructura esperada:
    {
      "topics": { "Tema": [ { ...pregunta... } ] }
    }
    """
    path = Path(json_path)
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo de preguntas: {path}")
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if "topics" not in data or not isinstance(data["topics"], dict):
        raise ValueError("Formato inválido: falta la clave 'topics' o no es un objeto")
    # Validación de esquema básico por pregunta
    _validate_question_schema(data)
    return data


def get_topics(data: Dict[str, Any]) -> List[str]:
    """Retorna lista de temas disponibles."""
    return list(data.get("topics", {}).keys())


def get_questions_for_topic(data: Dict[str, Any], topic: str, max_questions: int = 0, shuffle: bool = False) -> List[Dict[str, Any]]:
    """Obtiene preguntas para un tema; lista vacía si no existe.
    
    Args:
        data: Diccionario con el banco de preguntas
        topic: Nombre del tema
        max_questions: Número máximo de preguntas a retornar (0 = todas)
        shuffle: Si True, sortea las preguntas aleatoriamente
    """
    topics = data.get("topics", {})
    questions = topics.get(topic, [])
    if not isinstance(questions, list):
        return []
    
    # Crear copia para no modificar el original
    result = list(questions)
    
    # Sortear si se solicita
    if shuffle and len(result) > 0:
        result = random.sample(result, len(result))
    
    # Limitar cantidad si se especifica
    if max_questions > 0 and len(result) > max_questions:
        result = result[:max_questions]
    
    return result


def get_exam_questions(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Obtiene una pregunta aleatoria de cada tema disponible para modo examen.
    
    Args:
        data: Diccionario con el banco de preguntas
        
    Returns:
        Lista con una pregunta de cada tema, en orden aleatorio
    """
    exam_questions = []
    topics = data.get("topics", {})
    
    for topic_name, questions in topics.items():
        if isinstance(questions, list) and len(questions) > 0:
            # Seleccionar una pregunta aleatoria del tema
            selected = random.choice(questions)
            # Agregar metadato del tema para referencia
            question_copy = dict(selected)
            question_copy["_topic"] = topic_name
            exam_questions.append(question_copy)
    
    # Sortear el orden de las preguntas del examen
    random.shuffle(exam_questions)
    return exam_questions


def format_correct_answer_display(q: Dict[str, Any]) -> str:
    """Formatea la respuesta correcta para mostrarla al usuario."""
    q_type = q.get("type", "single")
    options: List[str] = q.get("options", [])
    answer = q.get("answer")

    if q_type == "single":
        if isinstance(answer, int) and 0 <= answer < len(options):
            return options[answer]
        return str(answer)
    if q_type == "multiple":
        if isinstance(answer, list):
            labels = []
            for idx in answer:
                if isinstance(idx, int) and 0 <= idx < len(options):
                    labels.append(options[idx])
            if labels:
                return ", ".join(labels)
        return str(answer)
    if q_type in {"tf", "input"}:
        return str(answer)
    return str(answer)


def _validate_question_schema(data: Dict[str, Any]) -> None:
    """Valida estructura mínima de preguntas por tipo.

    Lanza ValueError con mensaje claro si encuentra inconsistencias.
    """
    topics = data.get("topics", {})
    for topic_name, questions in topics.items():
        if not isinstance(questions, list):
            raise ValueError(
                f"El tema '{topic_name}' debe contener una lista de preguntas"
            )
        for idx, q in enumerate(questions):
            if not isinstance(q, dict):
                raise ValueError(
                    f"Pregunta {idx + 1} en '{topic_name}' no es un objeto"
                )
            q_type = q.get("type")
            if q_type not in {"single", "multiple", "tf", "input"}:
                raise ValueError(
                    f"Pregunta {idx + 1} en '{topic_name}': tipo inválido '{q_type}'"
                )
            if not q.get("question"):
                raise ValueError(
                    f"Pregunta {idx + 1} en '{topic_name}': falta 'question'"
                )

            if q_type in {"single", "multiple"}:
                options = q.get("options")
                if not isinstance(options, list) or not options:
                    raise ValueError(
                        f"Pregunta {idx + 1} en '{topic_name}': 'options' debe ser lista no vacía"
                    )

            if q_type == "single":
                ans = q.get("answer")
                if not isinstance(ans, int) or not (
                    0 <= ans < len(q.get("options", []))
                ):
                    raise ValueError(
                        f"Pregunta {idx + 1} en '{topic_name}': 'answer' debe ser índice válido"
                    )
            elif q_type == "multiple":
                ans = q.get("answer")
                if not isinstance(ans, list) or not all(
                    isinstance(i, int) for i in ans
                ):
                    raise ValueError(
                        f"Pregunta {idx + 1} en '{topic_name}': 'answer' debe ser lista de índices"
                    )
                if any(i < 0 or i >= len(q.get("options", [])) for i in ans):
                    raise ValueError(
                        f"Pregunta {idx + 1} en '{topic_name}': índice fuera de rango en 'answer'"
                    )
            elif q_type == "tf":
                if not isinstance(q.get("answer"), bool):
                    raise ValueError(
                        f"Pregunta {idx + 1} en '{topic_name}': 'answer' debe ser booleano"
                    )
            elif q_type == "input":
                if not isinstance(q.get("answer"), str):
                    raise ValueError(
                        f"Pregunta {idx + 1} en '{topic_name}': 'answer' debe ser string"
                    )
