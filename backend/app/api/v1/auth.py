from fastapi import APIRouter

router = APIRouter()


@router.post("/register")
async def register():
    """Register a new user with email and password."""
    return {"message": "register endpoint - coming soon"}


@router.post("/login")
async def login():
    """Login with email and password."""
    return {"message": "login endpoint - coming soon"}


@router.post("/refresh")
async def refresh_token():
    """Get a new access token using refresh token."""
    return {"message": "refresh endpoint - coming soon"}


@router.post("/logout")
async def logout():
    """Logout and invalidate tokens."""
    return {"message": "logout endpoint - coming soon"}


@router.get("/google")
async def google_login():
    """Redirect to Google OAuth login page."""
    return {"message": "google oauth - coming soon"}


@router.get("/github")
async def github_login():
    """Redirect to GitHub OAuth login page."""
    return {"message": "github oauth - coming soon"}


@router.get("/facebook")
async def facebook_login():
    """Redirect to Facebook OAuth login page."""
    return {"message": "facebook oauth - coming soon"}