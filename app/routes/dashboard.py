from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.audience import Audience
from app.models.campaign import Campaign
from app.models.template import Template

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/")
def dashboard(db: Session = Depends(get_db)):

    total_audience = db.query(Audience).count()
    total_campaigns = db.query(Campaign).count()
    total_templates = db.query(Template).count()

    draft = db.query(Campaign).filter(Campaign.status == "Draft").count()
    review = db.query(Campaign).filter(Campaign.status == "Review").count()
    scheduled = db.query(Campaign).filter(Campaign.status == "Scheduled").count()
    sent = db.query(Campaign).filter(Campaign.status == "Sent").count()

    return {
        "total_audience": total_audience,
        "total_campaigns": total_campaigns,
        "total_templates": total_templates,
        "campaign_status": {
            "Draft": draft,
            "Review": review,
            "Scheduled": scheduled,
            "Sent": sent
        }
    }