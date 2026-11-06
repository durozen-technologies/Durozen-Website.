from typing import List, Optional
from pydantic import BaseModel, Field

class ProjectBase(BaseModel):
    name: str = Field(..., example="Makeover Studio")
    category: str = Field(..., example="Beauty")
    tagline: Optional[str] = Field(default="", example="Luxury makeup & beauty styling")
    description: Optional[str] = Field(default="", example="Chic beauty consultation platform")
    url: str = Field(..., example="https://makeeeover.netlify.app")
    accent_color: Optional[str] = Field(default="#E52521", alias="accentColor")
    accent_badge: Optional[str] = Field(default=None, alias="accentBadge")
    year: Optional[str] = Field(default="2026")
    client: Optional[str] = Field(default="")
    domain: Optional[str] = Field(default="")
    image_url: Optional[str] = Field(default="", alias="imageUrl")
    tags: Optional[List[str]] = Field(default_factory=list)
    highlights: Optional[List[str]] = Field(default_factory=list)
    is_active: Optional[bool] = Field(default=True, alias="isActive")

    class Config:
        populate_by_name = True

class ProjectCreate(ProjectBase):
    id: Optional[str] = Field(default=None, description="Unique slug or ID, generated if omitted")

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    tagline: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
    accent_color: Optional[str] = Field(default=None, alias="accentColor")
    accent_badge: Optional[str] = Field(default=None, alias="accentBadge")
    year: Optional[str] = None
    client: Optional[str] = None
    domain: Optional[str] = None
    image_url: Optional[str] = Field(default=None, alias="imageUrl")
    tags: Optional[List[str]] = None
    highlights: Optional[List[str]] = None
    is_active: Optional[bool] = Field(default=None, alias="isActive")

    class Config:
        populate_by_name = True

class ProjectResponse(BaseModel):
    id: str
    name: str
    category: str
    tagline: str
    description: str
    url: str
    accentColor: str
    accentBadge: str
    year: str
    client: str
    domain: str
    imageUrl: Optional[str] = ""
    tags: List[str]
    highlights: List[str]
    isActive: bool
    createdAt: Optional[str] = None
    updatedAt: Optional[str] = None

    class Config:
        from_attributes = True

class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    username: str

class CreateAdminRequest(BaseModel):
    username: str
    password: str

class CreateAdminResponse(BaseModel):
    success: bool
    message: str
    username: str

