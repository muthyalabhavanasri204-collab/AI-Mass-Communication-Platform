from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from app.models.campaign_history import CampaignHistory
from app.database import get_db
from app.models.campaign import Campaign
from app.models.template import Template
from app.schemas.campaign_schema import CampaignCreate

router = APIRouter(
    prefix="/campaign",
    tags=["Campaign"]
)


# Create Campaign
@router.post("/")
def create_campaign(campaign: CampaignCreate, db: Session = Depends(get_db)):

    data = campaign.model_dump()

    data["status"] = "Draft"

    if campaign.template_id is not None:

        template = db.query(Template).filter(
            Template.id == campaign.template_id
        ).first()

        if template is None:
            raise HTTPException(
                status_code=404,
                detail="Template not found"
            )

        data["description"] = template.message

    new_campaign = Campaign(**data)

    db.add(new_campaign)
    db.commit()
    db.refresh(new_campaign)

    return new_campaign


# Get All Campaigns
@router.get("/")
def get_all_campaigns(db: Session = Depends(get_db)):
    return db.query(Campaign).all()


# Get Campaign by ID
@router.get("/{campaign_id}")
def get_campaign(campaign_id: int, db: Session = Depends(get_db)):

    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if campaign is None:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    return campaign


# Update Campaign
@router.put("/{campaign_id}")
def update_campaign(
    campaign_id: int,
    updated: CampaignCreate,
    db: Session = Depends(get_db)
):

    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if campaign is None:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    for key, value in updated.model_dump().items():
        setattr(campaign, key, value)

    db.commit()
    db.refresh(campaign)

    return campaign


# Delete Campaign
@router.delete("/{campaign_id}")
def delete_campaign(campaign_id: int, db: Session = Depends(get_db)):

    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if campaign is None:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    db.delete(campaign)
    db.commit()

    return {
        "message": "Campaign deleted successfully"
    }


# Update Campaign Status
@router.put("/{campaign_id}/status")
def update_campaign_status(
    campaign_id: int,
    status: str,
    db: Session = Depends(get_db)
):

    campaign = db.query(Campaign).filter(
        Campaign.id == campaign_id
    ).first()

    if campaign is None:
        raise HTTPException(
            status_code=404,
            detail="Campaign not found"
        )

    allowed_status = [
        "Draft",
        "Review",
        "Scheduled",
        "Sent"
    ]

    if status not in allowed_status:
        raise HTTPException(
            status_code=400,
            detail=f"Status must be one of {allowed_status}"
        )

    campaign.status = status

    db.commit()
    db.refresh(campaign)

    return campaign