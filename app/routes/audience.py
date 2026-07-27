from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.audience import Audience
from app.schemas.audience_schema import AudienceCreate

# ... keep your existing code ...
router = APIRouter(
    prefix="/audience",
    tags=["Audience"]
)

@router.put("/{audience_id}")
def update_audience(
    audience_id: int,
    updated_data: AudienceCreate,
    db: Session = Depends(get_db)
):

    audience = db.query(Audience).filter(
        Audience.id == audience_id
    ).first()

    if audience is None:
        raise HTTPException(
            status_code=404,
            detail="Audience not found"
        )

    audience.full_name = updated_data.full_name
    audience.age = updated_data.age
    audience.gender = updated_data.gender
    audience.email = updated_data.email
    audience.phone = updated_data.phone
    audience.language = updated_data.language
    audience.country = updated_data.country
    audience.state = updated_data.state
    audience.city = updated_data.city
    audience.occupation = updated_data.occupation
    audience.organization = updated_data.organization
    audience.department = updated_data.department

    db.commit()
    db.refresh(audience)

    return {
        "message": "Audience updated successfully",
        "data": audience
    }