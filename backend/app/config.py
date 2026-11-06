import os
from dotenv import load_dotenv

# Load .env from backend directory and/or workspace root
_backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_root_dir = os.path.dirname(_backend_dir)
load_dotenv(os.path.join(_root_dir, ".env"))
load_dotenv(os.path.join(_backend_dir, ".env"))
load_dotenv()

class Settings:
    _raw_db_url: str = os.getenv(
        "DATABASE_URL", 
        "postgresql://postgres:postgres@localhost:5432/durozen_db"
    )

    @property
    def DATABASE_URL(self) -> str:
        url = self._raw_db_url
        if url.startswith("postgresql://"):
            # Ensure psycopg2 driver is used if generic postgresql:// is provided
            return url.replace("postgresql://", "postgresql+psycopg2://", 1)
        return url
    
    SECRET_KEY: str = os.getenv("SECRET_KEY", "durozen-creative-portfolio-secret-key-change-in-production")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "1440"))
    
    ADMIN_USERNAME: str = os.getenv("ADMIN_USERNAME", "admin")
    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD", "durozenAdmin2026!")
    
    CORS_ORIGINS_RAW: str = os.getenv(
        "CORS_ORIGINS", 
        "http://localhost:3000,http://127.0.0.1:3000,http://localhost:5173"
    )
    
    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS_RAW.split(",") if origin.strip()]

settings = Settings()
