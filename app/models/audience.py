from sqlalchemy import Column, Integer, String, Boolean

from app.database import Base


class Audience(Base):
    __tablename__ = "audience"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    email = Column(String, unique=True)
    phone = Column(String)

    language = Column(String)

    country = Column(String)
    state = Column(String)
    city = Column(String)

    occupation = Column(String)

    organization = Column(String)
    department = Column(String)

    is_active = Column(Boolean, default=True)