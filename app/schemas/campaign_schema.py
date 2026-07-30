from enum import Enum
from typing import Optional

from pydantic import BaseModel


class CampaignType(str, Enum):
    awareness = "Awareness"
    emergency = "Emergency Alert"
    notification = "Notification"
    announcement = "Announcement"


class CampaignStatus(str, Enum):
    draft = "Draft"
    review = "Review"
    scheduled = "Scheduled"
    sent = "Sent"


class CampaignCreate(BaseModel):
    title: str
    description: str
    campaign_type: CampaignType
    scheduled_time: Optional[str] = None
    created_by: str


class CampaignResponse(BaseModel):
    id: int
    title: str
    description: str
    campaign_type: CampaignType
    status: CampaignStatus
    scheduled_time: Optional[str]
    created_by: str

    class Config:
        from_attributes = True