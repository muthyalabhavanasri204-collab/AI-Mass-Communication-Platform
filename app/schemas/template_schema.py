from pydantic import BaseModel


class TemplateCreate(BaseModel):
    title: str
    category: str
    language: str
    message: str


class TemplateResponse(TemplateCreate):
    id: int

    class Config:
        from_attributes = True