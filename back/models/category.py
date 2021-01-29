import sys
sys.path.append('.')
from sqlalchemy import Column, String
from sqlalchemy.orm import validates
from back.models.base_model import BaseModel


class Category(BaseModel):
    __tablename__ = 'category'
    name = Column('name', String(length=255), nullable=False)
    description = Column('description', String(length=255), nullable=True)

    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
    
    @validates('name')
    def validate_name(self, key, name) -> None:
        print('a')
        if not isinstance(name, str):
            raise TypeError("Name type must be a string")
        if not name.strip():
            raise ValueError("Name can't be empty")
        if len(name) > 100:
            raise ValueError("Name must have a maximum of 100 characters")
        return name
    
    @validates('description')
    def validate_description(self, key, description) -> None:
        if not isinstance(description, str):
            raise TypeError("Description type must be a string")
        if len(description) > 0 and not description.strip():
            raise ValueError("Description can't be only spaces")
        if len(description) > 255:
            raise ValueError("Description must have a maximum of 255 characters")
        return description
