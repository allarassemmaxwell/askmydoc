from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.security import verify_token
from app.db.session import get_db
from sqlalchemy.ext.asyncio import AsyncSession

# ========================
# Token Extractor
# ========================

bearer_scheme = HTTPBearer()


async def get_current_user_id(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> str:
    """
    Extracts and verifies the JWT token from the
    Authorization header of every protected request.

    Header format: Authorization: Bearer <token>

    Returns the user ID if valid.
    Raises 401 if token is missing, invalid, or expired.
    """
    token = credentials.credentials

    user_id = verify_token(token, token_type="access")

    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token. Please login again.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user_id


# ========================
# Database Session
# ========================

async def get_db_session(
    db: AsyncSession = Depends(get_db),
) -> AsyncSession:
    """
    Provides a database session for each request.
    Automatically closes it when the request is done.
    """
    return db


# ========================
# Combined — Current User + DB
# ========================

async def get_current_user_and_db(
    user_id: str = Depends(get_current_user_id),
    db: AsyncSession = Depends(get_db_session),
) -> tuple[str, AsyncSession]:
    """
    Convenience dependency that returns both
    the current user ID and a database session.
    Used in routes that need both.
    """
    return user_id, db