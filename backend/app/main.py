from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1 import auth, documents, chat


# ========================
# Startup & Shutdown
# ========================

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs on startup and shutdown.
    Good place to connect to DB, warm up AI models, etc.
    """
    # Startup
    print(f"🚀 {settings.APP_NAME} v{settings.APP_VERSION} starting...")
    print(f"📦 Environment: {settings.APP_ENV}")
    print(f"📖 API docs: http://localhost:8000/docs")

    yield  # app runs here

    # Shutdown
    print(f"👋 {settings.APP_NAME} shutting down...")


# ========================
# Create App
# ========================

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="""
    AskMyDoc API — Upload documents and ask questions using AI.

    ## Features
    - 🔐 Auth: Email, Google, GitHub, Facebook
    - 📄 Upload PDF, Excel, Word documents
    - 💬 Ask questions about your documents
    - ⚡ Streaming AI responses
    """,
    docs_url="/docs",        # Swagger UI at /docs
    redoc_url="/redoc",      # ReDoc UI at /redoc
    lifespan=lifespan,
)


# ========================
# CORS Middleware
# ========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ========================
# Routes
# ========================

app.include_router(
    auth.router,
    prefix="/api/v1/auth",
    tags=["Auth"],
)

app.include_router(
    documents.router,
    prefix="/api/v1/documents",
    tags=["Documents"],
)

app.include_router(
    chat.router,
    prefix="/api/v1/chat",
    tags=["Chat"],
)


# ========================
# Health Check
# ========================

@app.get("/health", tags=["Health"])
async def health_check():
    """
    Simple endpoint to check if the API is running.
    Used by Docker and Kubernetes to monitor the app.
    """
    return {
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.APP_ENV,
    }


@app.get("/", tags=["Health"])
async def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "docs": "http://localhost:8000/docs",
    }