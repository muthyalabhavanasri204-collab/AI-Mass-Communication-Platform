from sqlalchemy import Column, Integer, String

from app.database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    org_type = Column(String, nullable=False)

    country = Column(String)
    state = Column(String)
    city = Column(String)

    email = Column(String, unique=True)
    phone = Column(String)