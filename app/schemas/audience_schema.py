from pydantic import BaseModel, EmailStr


class AudienceCreate(BaseModel):
    full_name: str
    age: int
    gender: str
    email: EmailStr
    phone: str
    language: str
    country: str
    state: str
    city: str
    occupation: str
    organization: str
    department: str


class AudienceResponse(AudienceCreate):
    id: int
    is_active: bool

    class Config:
        from_attributes = True