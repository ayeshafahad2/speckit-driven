from sqlalchemy import Column, String, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid

from ..database import Base
from .user import User # Import User model
from .chapter import Chapter # Import Chapter model

class ChatSession(Base):
    __tablename__ = "chat_sessions"

    session_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"), nullable=True)
    start_time = Column(DateTime(timezone=True), server_default=func.now())
    end_time = Column(DateTime(timezone=True), nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)
    current_context_chapter_id = Column(UUID(as_uuid=True), ForeignKey("chapters.chapter_id"), nullable=True)

    user = relationship("User", backref="chat_sessions")
    chapter = relationship("Chapter", backref="chat_sessions") # Assuming Chapter model exists
    messages = relationship("ChatMessage", backref="chat_session", lazy="joined") # Add relationship to ChatMessage

    def __repr__(self):
        return f"<ChatSession(session_id='{self.session_id}', user_id='{self.user_id}', is_active={self.is_active})>"

class ChatMessage(Base):
    __tablename__ = "chat_messages"

    message_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    session_id = Column(UUID(as_uuid=True), ForeignKey("chat_sessions.session_id"), nullable=False)
    sender_type = Column(String(50), nullable=False) # 'user', 'chatbot', 'agent'
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    context_selected_text = Column(Text, nullable=True)
    retrieved_sources = Column(JSONB, nullable=True)

    def __repr__(self):
        return f"<ChatMessage(message_id='{self.message_id}', sender='{self.sender_type}')>"