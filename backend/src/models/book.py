from sqlalchemy import Column, String, Text, Integer, Date, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
import uuid

from ..database import Base

class Book(Base):
    __tablename__ = "books"

    book_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    cover_image_url = Column(String(255), nullable=True)
    total_modules = Column(Integer, nullable=True)
    total_chapters = Column(Integer, nullable=True)
    published_date = Column(Date, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    def __repr__(self):
        return f"<Book(book_id='{self.book_id}', title='{self.title}')>"
