from sqlalchemy.orm import Session
from typing import Optional
import uuid
import datetime

from ..models.chat import ChatSession, ChatMessage
from ..models.user import User # To link sessions to users
from ..models.chapter import Chapter # To link sessions to chapters

class ChatService:
    def __init__(self, db: Session):
        self.db = db

    def create_chat_session(self, user_id: Optional[uuid.UUID] = None, chapter_id: Optional[uuid.UUID] = None) -> ChatSession:
        """Creates a new chat session."""
        session = ChatSession(user_id=user_id, current_context_chapter_id=chapter_id)
        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)
        return session

    def get_chat_session(self, session_id: uuid.UUID) -> Optional[ChatSession]:
        """Retrieves a chat session by ID."""
        return self.db.query(ChatSession).filter(ChatSession.session_id == session_id).first()

    def end_chat_session(self, session_id: uuid.UUID) -> Optional[ChatSession]:
        """Ends an active chat session."""
        session = self.get_chat_session(session_id)
        if session:
            session.is_active = False
            session.end_time = datetime.datetime.now(datetime.timezone.utc)
            self.db.commit()
            self.db.refresh(session)
        return session

    def create_chat_message(self, session_id: uuid.UUID, sender_type: str, content: str,
                            context_selected_text: Optional[str] = None,
                            retrieved_sources: Optional[list] = None) -> ChatMessage:
        """Creates a new chat message within a session."""
        message = ChatMessage(
            session_id=session_id,
            sender_type=sender_type,
            content=content,
            context_selected_text=context_selected_text,
            retrieved_sources=retrieved_sources
        )
        self.db.add(message)
        self.db.commit()
        self.db.refresh(message)
        return message

    def get_chat_messages(self, session_id: uuid.UUID) -> list[ChatMessage]:
        """Retrieves all messages for a given chat session."""
        return self.db.query(ChatMessage).filter(ChatMessage.session_id == session_id).order_by(ChatMessage.timestamp).all()

    # Placeholder for RAG integration logic - to be implemented in US2
    async def get_rag_response(self, session_id: uuid.UUID, user_message: str, selected_text: Optional[str] = None) -> str:
        """
        Placeholder for getting a RAG-generated response.
        This will be expanded in User Story 2.
        """
        print(f"Simulating RAG response for session {session_id}: {user_message}")
        if selected_text:
            return f"Simulated RAG response based on selected text: '{selected_text}'. User asked: '{user_message}'"
        return f"Simulated RAG response for: '{user_message}'"
