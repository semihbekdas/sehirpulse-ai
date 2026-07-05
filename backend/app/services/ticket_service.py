from sqlalchemy.orm import Session

from app.ai_adapter import analyze_ticket
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate


def create_ticket(db: Session, payload: TicketCreate) -> Ticket:
    ai_result = analyze_ticket(payload.description)
    ticket = Ticket(
        citizen_name=payload.citizen_name or "Anonim",
        description=payload.description,
        district=payload.district,
        neighborhood=payload.neighborhood,
        address=payload.address,
        request_type=payload.request_type,
        category=ai_result["category"],
        sub_category=ai_result.get("sub_category"),
        department=ai_result["department"],
        confidence_score=ai_result.get("confidence_score"),
        priority_level=ai_result["priority_level"],
        ai_reason=ai_result.get("ai_reason"),
        status="Yeni",
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def list_tickets(db: Session) -> list[Ticket]:
    return db.query(Ticket).order_by(Ticket.created_at.desc()).all()


def get_ticket(db: Session, ticket_id: int) -> Ticket | None:
    return db.get(Ticket, ticket_id)
