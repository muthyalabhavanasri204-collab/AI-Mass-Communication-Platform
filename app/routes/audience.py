from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.audience import Audience
from app.schemas.audience_schema import AudienceCreate

router = APIRouter(
    prefix="/audience",
    tags=["Audience"]
)


# Create Audience
@router.post("/")
def create_audience(audience: AudienceCreate, db: Session = Depends(get_db)):

    new_audience = Audience(**audience.model_dump())

    db.add(new_audience)
    db.commit()
    db.refresh(new_audience)

    return new_audience


# Get All Audience
@router.get("/")
def get_all_audience(db: Session = Depends(get_db)):
    return db.query(Audience).all()


# Filter Audience (PUT THIS BEFORE /{audience_id})
@router.get("/filter/")
def filter_audience(
    age: Optional[int] = None,
    gender: Optional[str] = None,
    language: Optional[str] = None,
    country: Optional[str] = None,
    state: Optional[str] = None,
    city: Optional[str] = None,
    occupation: Optional[str] = None,
    organization: Optional[str] = None,
    department: Optional[str] = None,
    db: Session = Depends(get_db),
):

    query = db.query(Audience)

    if age is not None:
        query = query.filter(Audience.age == age)

    if gender:
        query = query.filter(Audience.gender == gender)

    if language:
        query = query.filter(Audience.language == language)

    if country:
        query = query.filter(Audience.country == country)

    if state:
        query = query.filter(Audience.state == state)

    if city:
        query = query.filter(Audience.city == city)

    if occupation:
        query = query.filter(Audience.occupation == occupation)

    if organization:
        query = query.filter(Audience.organization == organization)

    if department:
        query = query.filter(Audience.department == department)

    return query.all()


# Get Audience by ID
@router.get("/{audience_id}")
def get_audience(audience_id: int, db: Session = Depends(get_db)):

    audience = db.query(Audience).filter(
        Audience.id == audience_id
    ).first()

    if audience is None:
        raise HTTPException(status_code=404, detail="Audience not found")

    return audience


# Update Audience
@router.put("/{audience_id}")
def update_audience(
    audience_id: int,
    updated: AudienceCreate,
    db: Session = Depends(get_db)
):

    audience = db.query(Audience).filter(
        Audience.id == audience_id
    ).first()

    if audience is None:
        raise HTTPException(status_code=404, detail="Audience not found")

    for key, value in updated.model_dump().items():
        setattr(audience, key, value)

    db.commit()
    db.refresh(audience)

    return audience


# Delete Audience
@router.delete("/{audience_id}")
def delete_audience(
    audience_id: int,
    db: Session = Depends(get_db)
):

    audience = db.query(Audience).filter(
        Audience.id == audience_id
    ).first()

    if audience is None:
        raise HTTPException(status_code=404, detail="Audience not found")

    db.delete(audience)
    db.commit()

    return {"message": "Audience deleted successfully"}