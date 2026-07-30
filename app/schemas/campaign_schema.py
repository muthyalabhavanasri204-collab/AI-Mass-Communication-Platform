from typing import Optional

from pydantic import BaseModel


class CampaignCreate(BaseModel):
    title: str
    description: str
    campaign_type: str
    scheduled_time: str
    created_by: str

    template_id: Optional[int] = None


class CampaignResponse(CampaignCreate):
    id: int
    status: str

    class Config:
        from_attributes = True