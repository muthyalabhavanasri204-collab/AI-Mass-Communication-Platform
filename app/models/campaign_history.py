from sqlalchemy import Column, Integer, String
from app.database import Base


class CampaignHistory(Base):
    __tablename__ = "campaign_history"

    id = Column(Integer, primary_key=True, index=True)

    campaign_id = Column(Integer)

    old_status = Column(String)

    new_status = Column(String)

    changed_at = Column(String)