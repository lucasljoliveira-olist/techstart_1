from back.resources.base_resource import BaseResource
from back.models.category import Category
from back.dao.category_dao import CategoryDao

from flask_restful import marshal_with, fields


class CategoryResource(BaseResource):
    fields = {
        "id": fields.Integer,
        "name": fields.String,
        "description": fields.String
    }

    def __init__(self):
        self.__dao = CategoryDao()
        self.__model_type = Category
        super().__init__(self.__dao, self.__model_type)
    

    @marshal_with(fields)
    def get(self, id: int = None):
        return super().get(id)
    

    @marshal_with(fields)
    def post(self):
        return super().post()
    

    @marshal_with(fields)
    def put(self, id: int):
        return super().put(id)
