from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.campaign import Campaign
from app.schemas.campaign_schema import CampaignCreate

router = APIRouter(
    prefix="/campaign",
    tags=["Campaign"]
)


@router.post("/")
def create_campaign(
    campaign: CampaignCreate,
    db: Session = Depends(get_db)
):

    new_campaign = Campaign(
        title=campaign.title,
        message=campaign.message,
        target_language=campaign.target_language,
        created_by=campaign.created_by
    )

    db.add(new_campaign)
    db.commit()
    db.refresh(new_campaign)

    return {
        "message": "Campaign created successfully",
        "data": new_campaign
    }


@router.get("/")
def get_all_campaigns(db: Session = Depends(get_db)):
    return db.query(Campaign).all()


@router.get("/{campaign_id}")
def get_campaign(
    campaign_id: int,
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

    return campaign


@router.put("/{campaign_id}")
def update_campaign(
    campaign_id: int,
    updated_campaign: CampaignCreate,
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

    campaign.title = updated_campaign.title
    campaign.message = updated_campaign.message
    campaign.target_language = updated_campaign.target_language
    campaign.created_by = updated_campaign.created_by

    db.commit()
    db.refresh(campaign)

    return {
        "message": "Campaign updated successfully",
        "data": campaign
    }


@router.delete("/{campaign_id}")
def delete_campaign(
    campaign_id: int,
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

    db.delete(campaign)
    db.commit()

    return {
        "message": "Campaign deleted successfully"
    }