from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB # Assuming JSONB for metadata
from sqlalchemy.orm import relationship
import uuid

from ..database import Base
from .book import Book
from .chapter import Chapter

class ContentEmbedding(Base):
    __tablename__ = "content_embeddings" # This model is primarily for metadata linking, actual vectors in Qdrant

    embedding_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    chapter_id = Column(UUID(as_uuid=True), ForeignKey("chapters.chapter_id"), nullable=False)
    book_id = Column(UUID(as_uuid=True), ForeignKey("books.book_id"), nullable=False)
    text_segment = Column(Text, nullable=False)
    segment_order = Column(Integer, nullable=False)
    # The actual embedding_vector will be stored in Qdrant, not Postgres directly.
    # This JSONB column can store any additional metadata needed for Qdrant payload.
    metadata_ = Column("metadata", JSONB, nullable=True) # Renamed to metadata_ to avoid conflict with Python keyword

    chapter = relationship("Chapter", backref="content_embeddings")
    book = relationship("Book", backref="content_embeddings")

    def __repr__(self):
        return f"<ContentEmbedding(embedding_id='{self.embedding_id}', chapter_id='{self.chapter_id}', segment_order={self.segment_order})>"
