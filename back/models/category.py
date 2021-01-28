import sys
sys.path.append('.')

from sqlalchemy import Column, String
from sqlalchemy.orm import validates

from back.models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column('name', String(length=255), nullable=False)
    description = Column('description', String(length=255), nullable=True)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
    
    @validates('name')
    def validate_name(self, key, name) -> None:
        if not isinstance(name, str):
            raise TypeError("Name type must be a string")
        if not name.strip():
            raise ValueError("Name can't be empty")
        if len(name) > 100:
            raise ValueError("Name must have a maximum of 100 characters")
    
    @validates('description')
    def validate_description(self, key, description) -> None:
        if not isinstance(description, str):
            raise TypeError("Description type must be a string")
        if not description.strip():
            raise ValueError("Description can't be empty")
        if len(description) > 255:
            raise ValueError("Description must have a maximum of 255 characters")
