import sys
sys.path.append('.')

import pytest
from back.dao.category_dao import CategoryDao
from back.models.category import Category
from sqlalchemy.orm.exc import UnmappedInstanceError


class TestCategoryDao:
    @pytest.fixture
    def create_category(self):
        category = Category('Category', 'Category description')
        return category

    def test_instance(self):
        category_dao = CategoryDao()
        assert isinstance(category_dao, CategoryDao)

    def test_save(self, create_category):
        category = CategoryDao().save(create_category)
        assert category.id is not None
        CategoryDao().delete(category)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            CategoryDao().save('invalid-id')

    def test_read_by_id(self, create_category):
        category = CategoryDao().save(create_category)
        category_read = CategoryDao().read_by_id(category.id)
        assert isinstance(category_read, Category)
        CategoryDao().delete(category_read)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            CategoryDao().read_by_id('invalid-id')

    def test_read_all(self):
        categories = CategoryDao().read_all()
        assert isinstance(categories, list)
        for category in categories:
            assert isinstance(category, Category)

    def test_delete(self, create_category):
        category = CategoryDao().save(create_category)
        category_read = CategoryDao().read_by_id(category.id)
        CategoryDao().delete(category_read)
        category_read = CategoryDao().read_by_id(category_read.id)
        assert category_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            CategoryDao().delete('invalid-id')
