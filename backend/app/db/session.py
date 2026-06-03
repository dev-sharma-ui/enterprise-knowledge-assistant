from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


engine = create_engine(
    settings.database_url,
    echo=settings.DEBUG
)

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
)