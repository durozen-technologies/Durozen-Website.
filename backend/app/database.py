import logging
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

logger = logging.getLogger("durozen.database")
logging.basicConfig(level=logging.INFO)

DATABASE_URL = settings.DATABASE_URL
engine = None
SessionLocal = None
Base = declarative_base()

def init_engine():
    global engine, SessionLocal
    
    # Try connecting to configured database (PostgreSQL by default)
    try:
        logger.info(f"Connecting to database: {DATABASE_URL.split('@')[-1] if '@' in DATABASE_URL else DATABASE_URL}")
        test_engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True,
            connect_args={"connect_timeout": 3} if "postgresql" in DATABASE_URL else {}
        )
        # Test connection
        with test_engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        
        logger.info("Successfully connected to PostgreSQL database!")
        engine = test_engine
    except Exception as e:
        if settings.USE_SQLITE_FALLBACK:
            logger.warning(
                f"Could not connect to PostgreSQL ({e}). "
                "USE_SQLITE_FALLBACK is enabled, falling back to local SQLite database (durozen_local.db)."
            )
            engine = create_engine(
                "sqlite:///./durozen_local.db",
                connect_args={"check_same_thread": False}
            )
        else:
            logger.error(f"PostgreSQL connection failed and fallback is disabled: {e}")
            raise e

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    try:
        # Create tables immediately on engine initialization
        from . import models
        Base.metadata.create_all(bind=engine)
        logger.info("Database schema verified and tables created.")

        # Ensure image_url column exists in existing database tables
        with engine.connect() as conn:
            try:
                conn.execute(text("ALTER TABLE projects ADD COLUMN image_url TEXT"))
                conn.commit()
                logger.info("Verified/Added 'image_url' column in projects table.")
            except Exception:
                pass
    except Exception as e:
        logger.warning(f"Note on table creation: {e}")

init_engine()

def get_db():
    if SessionLocal is None:
        init_engine()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
