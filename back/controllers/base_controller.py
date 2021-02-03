from back.models.base_model import BaseModel


class BaseController:
    def __init__(self, dao):
        self.__dao = dao

    def save(self, model: BaseModel) -> None:
        model = self.__dao.save(model)
        return model

    def read_by_id(self, id: int) -> object:
        model = self.__dao.read_by_id(id)
        return model

    def read_all(self) -> list:
        models = self.__dao.read_all()
        return models

    def delete(self, model: BaseModel) -> None:
        self.__dao.delete(model)

    def update(self, model: BaseModel) -> None:
        model = self.__dao.save(model)
        return model
