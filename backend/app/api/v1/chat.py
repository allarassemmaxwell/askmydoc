from fastapi import APIRouter

router = APIRouter()


@router.post("/{document_id}/ask")
async def ask_question(document_id: str):
    """Ask a question about a specific document."""
    return {"message": f"ask question about document {document_id} - coming soon"}


@router.get("/{document_id}/history")
async def get_chat_history(document_id: str):
    """Get chat history for a specific document."""
    return {"message": f"chat history for document {document_id} - coming soon"}