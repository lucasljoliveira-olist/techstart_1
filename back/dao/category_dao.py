from back.dao.base_dao import BaseDao
from back.models.category import Category


class CategoryDao(BaseDao):
    def __init__(self):
        super().__init__(Category)
