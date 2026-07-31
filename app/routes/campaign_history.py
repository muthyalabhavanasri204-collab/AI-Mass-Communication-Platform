from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.campaign_history import CampaignHistory

router = APIRouter(
    prefix="/campaign-history",
    tags=["Campaign History"]
)


# Get all campaign history
@router.get("/")
def get_all_history(db: Session = Depends(get_db)):
    return db.query(CampaignHistory).all()


# Get history by campaign id
@router.get("/{campaign_id}")
def get_campaign_history(
    campaign_id: int,
    db: Session = Depends(get_db)
):

    history = db.query(CampaignHistory).filter(
        CampaignHistory.campaign_id == campaign_id
    ).all()

    return history