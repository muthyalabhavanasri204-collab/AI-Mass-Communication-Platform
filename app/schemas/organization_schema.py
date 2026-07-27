from pydantic import BaseModel


class OrganizationCreate(BaseModel):
    name: str
    org_type: str
    country: str
    state: str
    city: str
    email: str
    phone: str


class OrganizationResponse(OrganizationCreate):
    id: int

    class Config:
        from_attributes = True