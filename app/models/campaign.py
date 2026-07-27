from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.database import Base


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    message = Column(String, nullable=False)
    target_language = Column(String, nullable=False)

    created_by = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

    status = Column(String, default="Draft")