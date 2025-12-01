from __future__ import annotations

"""Lógica de evaluación para la app de práctica.

Se prioriza simplicidad y claridad: funciones pequeñas, tipos explícitos y
docstrings que describen comportamiento y supuestos.
"""

from typing import Any, Dict, List, Optional


def evaluate_single_choice(user_answer: Optional[int], correct_index: int) -> bool:
    """Evalúa una pregunta de opción única.

    - user_answer: índice seleccionado por el usuario o None si no respondió.
    - correct_index: índice de la opción correcta.
    """
    if user_answer is None:
        return False
    return int(user_answer) == int(correct_index)


def evaluate_multiple_choice(user_answers: List[int] | None, correct_indices: List[int]) -> bool:
    """Evalúa una pregunta de opción múltiple.

    Es correcta si el conjunto de índices seleccionados coincide exactamente
    con el conjunto de índices correctos (sin extras ni faltantes).
    """
    if not user_answers:
        return False
    return set(map(int, user_answers)) == set(map(int, correct_indices))


def evaluate_true_false(user_answer: Optional[bool], correct_value: bool) -> bool:
    """Evalúa una pregunta de verdadero/falso."""
    if user_answer is None:
        return False
    return bool(user_answer) == bool(correct_value)


def evaluate_free_input(user_answer: Optional[str], correct_text: str) -> bool:
    """Evalúa respuesta libre ignorando mayúsculas/minúsculas y espacios externos."""
    if user_answer is None:
        return False
    return str(user_answer).strip().lower() == str(correct_text).strip().lower()


def evaluate_question(q: Dict[str, Any], user_response: Any) -> bool:
    """Evalúa una pregunta genérica según su tipo.

    Tipos admitidos: "single", "multiple", "tf", "input".
    """
    q_type = q.get("type", "single")
    answer = q.get("answer")

    if q_type == "single":
        return evaluate_single_choice(user_response, int(answer))
    if q_type == "multiple":
        return evaluate_multiple_choice(user_response or [], list(answer or []))
    if q_type == "tf":
        return evaluate_true_false(user_response, bool(answer))
    if q_type == "input":
        return evaluate_free_input(user_response or "", str(answer))
    return False


def compute_score(questions: List[Dict[str, Any]], responses: List[Any]) -> Dict[str, Any]:
    """Calcula puntaje total y detalle por pregunta.

    Retorna un diccionario con llaves: "total", "correct" y "detail".
    """
    detail: List[Dict[str, Any]] = []
    correct_count = 0
    for q, r in zip(questions, responses):
        is_correct = evaluate_question(q, r)
        detail.append({"correct": is_correct})
        if is_correct:
            correct_count += 1
    return {"total": len(questions), "correct": correct_count, "detail": detail}


