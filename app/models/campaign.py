from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Campaign(Base):
    __tablename__ = "campaign"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(Text)

    campaign_type = Column(String)

    status = Column(String, default="Draft")

    scheduled_time = Column(String)

    created_by = Column(String)