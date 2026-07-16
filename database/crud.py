from sqlalchemy.orm import Session
from database.models import Conversation


def save_conversation(
    db: Session,
    session_id: str,
    human_message: str,
    ai_message: str,
):
    conversation = Conversation(
        session_id=session_id,
        Human_message=human_message,
        AI_message=ai_message,
    )
    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation


def get_conversation_by_session(
    db: Session,
    session_id: str,
):
    return (
        db.query(Conversation)
        .filter(Conversation.session_id == session_id)
        .order_by(Conversation.created_at.asc())
        .all()
    )