from back.models.base_model import BaseModel
from back.dao.session import Session


class BaseDao:
    def __init__(self, type_model):
        self.__type_model = type_model

    def save(self, model: BaseModel) -> None:
        with Session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            return model

    def read_by_id(self, id: int) -> BaseModel:
        if isinstance(id, int):
            with Session() as session:
                result = session.query(
                    self.__type_model).filter_by(id=id).first()
            return result
        else:
            raise TypeError('Id must be integer.')

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.__type_model).order_by('id').all()
        return result

    def delete(self, model: BaseModel) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()