import sys
sys.path.append('.')

import pytest
from back.controllers.base_controller import BaseController
from back.controllers.category_controller import CategoryController
from back.models.category import Category


class TestCategoryController:
    @pytest.fixture
    def create_controller(self):
        controller = CategoryController()
        return controller

    @pytest.fixture
    def create_category(self):
        category = Category('Category', 'Category description')
        return category

    def test_instance(self, create_controller):
        assert isinstance(create_controller, CategoryController)

    def test_read_all(self, create_controller):
        result = create_controller.read_all()
        assert isinstance(result, list)

    def test_create(self, create_controller, create_category):
        category = create_controller.save(create_category)
        assert category.id is not None
        create_controller.delete(category)

    def test_update(self, create_controller, create_category):
        category = create_controller.save(create_category)
        category.name = 'New category'
        category.description = 'New description'
        category_updated = create_controller.update(category)

        assert category_updated.id is not None
        assert category_updated.name == 'New category'
        assert category_updated.description == 'New description'

        create_controller.delete(category)

    def test_delete(self, create_controller, create_category):
        category = create_controller.save(create_category)
        create_controller.delete(category)

        with pytest.raises(Exception) as exc:
            create_controller.read_by_id(category.id)
            assert exc.value == 'Object not found in the database.'

    def test_read_by_id(self, create_controller, create_category):
        category = create_controller.save(create_category)
        category_read = create_controller.read_by_id(category.id)

        assert isinstance(category_read, Category)
        create_controller.delete(category_read)

    def test_not_read_by_id(self, create_controller):
        with pytest.raises(Exception) as exc:
            create_controller.read_by_id('invalid-id')
            assert exc.value == 'Object not found in the database.'
