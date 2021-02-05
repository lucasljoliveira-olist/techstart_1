from flask import request
from flask_restful import Resource

from back.dao.base_dao import BaseDao
from back.models.base_model import BaseModel


class BaseResource(Resource):
    def __init__(self, dao: BaseDao, model_type: BaseModel) -> None:
        self.__dao = dao
        self.__model_type = model_type
    
    
    def get(self, id: int = None) -> BaseModel:
        if id:
            return self.__dao.read_by_id(id), 200
        return self.__dao.read_all(), 200
    
    
    def post(self) -> BaseModel:
        data = request.json
        item = self.__model_type(**data)
        return self.__dao.save(item), 201
    
    
    def put(self, id: int) -> BaseModel:
        data = request.json

        if data['id'] == id:
            item = self.__dao.read_by_id(id)
            # updated_item = item(**data)
            # item.update(updated_item)
            
            for key, value in data.items():
                setattr(item, key, value)
            item = self.__dao.save(item)
            return item, 201
        return None, 404
    
    
    def delete(self, id: int) -> None:
        item = self.__dao.read_by_id(id)
        self.__dao.delete(item)
        return None, 204
