from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.template import Template
from app.schemas.template_schema import TemplateCreate

router = APIRouter(
    prefix="/template",
    tags=["Template"]
)


# ==========================================
# Create Template
# ==========================================
@router.post("/")
def create_template(template: TemplateCreate, db: Session = Depends(get_db)):

    new_template = Template(**template.model_dump())

    db.add(new_template)
    db.commit()
    db.refresh(new_template)

    return new_template


# ==========================================
# Get All Templates
# ==========================================
@router.get("/")
def get_templates(db: Session = Depends(get_db)):
    return db.query(Template).all()


# ==========================================
# Get All Categories
# ==========================================
@router.get("/categories/")
def get_categories(db: Session = Depends(get_db)):

    categories = db.query(
        Template.category
    ).distinct().all()

    return {
        "categories": [category[0] for category in categories]
    }


# ==========================================
# Get All Languages
# ==========================================
@router.get("/languages/")
def get_languages(db: Session = Depends(get_db)):

    languages = db.query(
        Template.language
    ).distinct().all()

    return {
        "languages": [language[0] for language in languages]
    }


# ==========================================
# Search Templates
# ==========================================
@router.get("/search/")
def search_templates(
    category: Optional[str] = None,
    language: Optional[str] = None,
    db: Session = Depends(get_db)
):

    query = db.query(Template)

    if category:
        query = query.filter(Template.category == category)

    if language:
        query = query.filter(Template.language == language)

    return query.all()


# ==========================================
# Get Template By ID
# ==========================================
@router.get("/{template_id}")
def get_template(template_id: int, db: Session = Depends(get_db)):

    template = db.query(Template).filter(
        Template.id == template_id
    ).first()

    if template is None:
        raise HTTPException(
            status_code=404,
            detail="Template not found"
        )

    return template


# ==========================================
# Update Template
# ==========================================
@router.put("/{template_id}")
def update_template(
    template_id: int,
    updated: TemplateCreate,
    db: Session = Depends(get_db)
):

    template = db.query(Template).filter(
        Template.id == template_id
    ).first()

    if template is None:
        raise HTTPException(
            status_code=404,
            detail="Template not found"
        )

    for key, value in updated.model_dump().items():
        setattr(template, key, value)

    db.commit()
    db.refresh(template)

    return template


# ==========================================
# Delete Template
# ==========================================
@router.delete("/{template_id}")
def delete_template(
    template_id: int,
    db: Session = Depends(get_db)
):

    template = db.query(Template).filter(
        Template.id == template_id
    ).first()

    if template is None:
        raise HTTPException(
            status_code=404,
            detail="Template not found"
        )

    db.delete(template)
    db.commit()

    return {
        "message": "Template deleted successfully"
    }