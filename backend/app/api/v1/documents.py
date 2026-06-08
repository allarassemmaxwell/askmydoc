from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_documents():
    """Get all documents for the current user."""
    return {"message": "get documents - coming soon"}


@router.post("/upload")
async def upload_document():
    """Upload a PDF, Excel, or Word document."""
    return {"message": "upload endpoint - coming soon"}


@router.get("/{document_id}")
async def get_document(document_id: str):
    """Get a single document by ID."""
    return {"message": f"get document {document_id} - coming soon"}


@router.delete("/{document_id}")
async def delete_document(document_id: str):
    """Delete a document and its embeddings."""
    return {"message": f"delete document {document_id} - coming soon"}