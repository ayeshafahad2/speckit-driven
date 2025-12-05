from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from typing import Optional
import uuid

from ..database import get_db
from ..services.chat_service import ChatService
from ..models.chat import ChatSession # For response model
from pydantic import BaseModel, Field

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

class CreateChatSessionRequest(BaseModel):
    initial_message: Optional[str] = Field(None, description="Initial message from the user")
    chapter_id: Optional[uuid.UUID] = Field(None, description="Optional chapter ID to set initial context")

@router.post("/session", response_model=ChatSession)
async def create_chat_session_endpoint(
    request: Request,
    session_request: CreateChatSessionRequest,
    db: Session = Depends(get_db)
):
    user_id = getattr(request.state, "user_id", None) # Get user_id from auth middleware if present
    chat_service = ChatService(db)
    
    session = chat_service.create_chat_session(user_id=user_id, chapter_id=session_request.chapter_id)
    
    if session_request.initial_message:
        chat_service.create_chat_message(
            session_id=session.session_id,
            sender_type="user",
            content=session_request.initial_message
        )
        # Simulate initial RAG response here if needed, or handle in next message
    
    return session

@router.get("/session/{session_id}", response_model=ChatSession)
async def get_chat_session_endpoint(
    session_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    chat_service = ChatService(db)
    session = chat_service.get_chat_session(session_id)
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat session not found")
    return session

@router.post("/session/{session_id}/end", response_model=ChatSession)
async def end_chat_session_endpoint(
    session_id: uuid.UUID,
    db: Session = Depends(get_db)
):
    chat_service = ChatService(db)
    session = chat_service.end_chat_session(session_id)
    if not session:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chat session not found or already ended")
    return session
