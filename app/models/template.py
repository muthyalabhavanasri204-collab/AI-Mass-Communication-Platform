from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Template(Base):
    __tablename__ = "template"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)
    language = Column(String, nullable=False)
    message = Column(Text, nullable=False)