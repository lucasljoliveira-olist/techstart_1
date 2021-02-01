import sys
sys.path.append('.')
from back.models.category import Category
import pytest

class Category:

    def test_category_type(self):
        category = Category('nome', 'descricao')
        assert isinstance(category, Category)

    def test_category_name_characterexcess():
        with pytest.raises(ValueError):
            category = Category('nome'*100, 'descrição')

    @pytest.mark.parametrize("name, description", [
        ('qualquer coisa', 'Blablabla')])
    def test_category_instance(name, description):
        category = Category(name, description)
        assert isinstance(category, Category)

    @pytest.mark.parametrize("name, description", [
        ('qualquer nome', 'Blablabla')])
    def test_category_name(name, description):
        category = Category(name, description)
        assert category.name

    @pytest.mark.parametrize("name, description", [
        (None, 'descrição'),
        ('', 'descrição'),
        (123, 'descrição'),
        (' ', 'descrição')])
    def test_category_name_none_empty_int_space(
        name, description):
        category = Category(name, description)
        assert category.name
            
    def test_category_description_characters_excess():
        with pytest.raises(ValueError):
            category = Category('nome', 'descrição'*100)

    @pytest.mark.parametrize("name, description", [
        ('teste', 'Vacina pronta'),
        ('teste', None),
        ('teste', ''),
        ('teste', 123),
        ('teste', ' ')])
    def test_description_none_empty_int_space(
        name,description):
        category = Category(name, description)
        assert category.description