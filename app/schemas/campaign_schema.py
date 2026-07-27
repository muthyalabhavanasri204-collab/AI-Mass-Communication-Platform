from pydantic import BaseModel


class CampaignCreate(BaseModel):
    title: str
    message: str
    target_language: str
    created_by: str


class CampaignResponse(CampaignCreate):
    id: int
    status: str

    class Config:
        from_attributes = True