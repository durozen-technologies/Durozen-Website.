import uuid
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from ..schemas import LoginRequest, TokenResponse, CreateAdminRequest, CreateAdminResponse
from ..auth import verify_admin_credentials, create_access_token, get_current_admin, hash_password
from ..database import get_db
from ..models import AdminUser
from ..config import settings

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    if not verify_admin_credentials(data.username, data.password, db):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": data.username, "role": "admin"})
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        username=data.username
    )

@router.post("/register-admin", response_model=CreateAdminResponse)
def register_admin(
    data: CreateAdminRequest, 
    db: Session = Depends(get_db),
    current_admin: str = Depends(get_current_admin)
):
    clean_user = data.username.strip()
    clean_pass = data.password.strip()

    if len(clean_user) < 3:
        raise HTTPException(status_code=400, detail="Username must be at least 3 characters long")
    if len(clean_pass) < 6:
        raise HTTPException(status_code=400, detail="Password must be at least 6 characters long")

    # Check if username clashes with default admin
    if clean_user.lower() == settings.ADMIN_USERNAME.lower():
        raise HTTPException(status_code=400, detail="An administrator with this username already exists")

    # Check if already in database
    existing = db.query(AdminUser).filter(AdminUser.username == clean_user).first()
    if existing:
        raise HTTPException(status_code=400, detail="An administrator with this username already exists")

    new_admin = AdminUser(
        id=f"admin_{uuid.uuid4().hex[:12]}",
        username=clean_user,
        password_hash=hash_password(clean_pass),
        role="admin"
    )
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)

    return CreateAdminResponse(
        success=True,
        message=f"Administrator '{clean_user}' created successfully",
        username=clean_user
    )

@router.get("/me")
def get_me(username: str = Depends(get_current_admin)):
    return {
        "authenticated": True,
        "username": username,
        "role": "admin"
    }

