import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from ai.classify import classify_ticket  # noqa: E402
from ai.priority_basic import calculate_priority  # noqa: E402
from ai.routing import route_department  # noqa: E402


def analyze_ticket(description: str) -> dict:
    classification = classify_ticket(description)
    routing = route_department(classification["category"])
    priority = calculate_priority(description, classification["category"])

    return {
        "category": classification["category"],
        "sub_category": classification.get("sub_category"),
        "confidence_score": classification.get("confidence_score"),
        "department": routing["department"],
        "priority_level": priority["priority_level"],
        "ai_reason": " ".join(
            part
            for part in [
                classification.get("reason"),
                routing.get("reason"),
                priority.get("reason"),
            ]
            if part
        ),
    }
