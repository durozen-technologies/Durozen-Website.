import datetime
from sqlalchemy import Column, String, Text, Boolean, DateTime, JSON
from .database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(String(100), primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    category = Column(String(100), nullable=False, default="Lifestyle")
    tagline = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    url = Column(String(500), nullable=False)
    accent_color = Column(String(20), default="#E52521") # DUROZEN Red default
    accent_badge = Column(String(50), nullable=True)
    year = Column(String(10), default="2026")
    client = Column(String(255), nullable=True)
    domain = Column(String(255), nullable=True)
    image_url = Column(Text, nullable=True) # Website Front Look Picture / Thumbnail
    tags = Column(JSON, default=list)
    highlights = Column(JSON, default=list)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "tagline": self.tagline or "",
            "description": self.description or "",
            "url": self.url,
            "accentColor": self.accent_color or "#E52521",
            "accentBadge": self.accent_badge or self.category,
            "year": self.year or "2026",
            "client": self.client or "",
            "domain": self.domain or "",
            "imageUrl": self.image_url or "",
            "tags": self.tags or [],
            "highlights": self.highlights or [],
            "isActive": self.is_active,
            "createdAt": self.created_at.isoformat() if self.created_at else None,
            "updatedAt": self.updated_at.isoformat() if self.updated_at else None,
        }

class AdminUser(Base):
    __tablename__ = "admin_users"

    id = Column(String(100), primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(50), default="admin")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role,
            "createdAt": self.created_at.isoformat() if self.created_at else None,
        }

