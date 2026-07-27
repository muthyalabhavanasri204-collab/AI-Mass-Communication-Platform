from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.organization import Organization
from app.schemas.organization_schema import OrganizationCreate

router = APIRouter(
    prefix="/organization",
    tags=["Organization"]
)


@router.post("/")
def create_organization(
    organization: OrganizationCreate,
    db: Session = Depends(get_db)
):

    new_org = Organization(
        name=organization.name,
        org_type=organization.org_type,
        country=organization.country,
        state=organization.state,
        city=organization.city,
        email=organization.email,
        phone=organization.phone
    )

    db.add(new_org)
    db.commit()
    db.refresh(new_org)

    return {
        "message": "Organization created successfully",
        "data": new_org
    }


@router.get("/")
def get_all_organizations(
    db: Session = Depends(get_db)
):
    return db.query(Organization).all()


@router.get("/{organization_id}")
def get_organization(
    organization_id: int,
    db: Session = Depends(get_db)
):

    org = db.query(Organization).filter(
        Organization.id == organization_id
    ).first()

    if org is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found"
        )

    return org


@router.put("/{organization_id}")
def update_organization(
    organization_id: int,
    updated_org: OrganizationCreate,
    db: Session = Depends(get_db)
):

    org = db.query(Organization).filter(
        Organization.id == organization_id
    ).first()

    if org is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found"
        )

    org.name = updated_org.name
    org.org_type = updated_org.org_type
    org.country = updated_org.country
    org.state = updated_org.state
    org.city = updated_org.city
    org.email = updated_org.email
    org.phone = updated_org.phone

    db.commit()
    db.refresh(org)

    return {
        "message": "Organization updated successfully",
        "data": org
    }


@router.delete("/{organization_id}")
def delete_organization(
    organization_id: int,
    db: Session = Depends(get_db)
):

    org = db.query(Organization).filter(
        Organization.id == organization_id
    ).first()

    if org is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found"
        )

    db.delete(org)
    db.commit()

    return {
        "message": "Organization deleted successfully"
    }