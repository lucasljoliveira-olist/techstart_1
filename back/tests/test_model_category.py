import sys
sys.path.append('.')
from back.models.category import Category
import pytest

@pytest.mark.parametrize("name, description", [
    ('qualquer coisa', 'Blablabla'),
    ('open bar', 'Tananan'),
    ('teste', 'Vacina pronta')])
def test_category_instance(name, description):
    category = Category(name, description)
    assert isinstance(category, Category)

@pytest.mark.parametrize("name, description", [
    ('qualquer coisa', 'Blablabla'),
    ('open bar', 'Tananan'),
    ('teste', 'Vacina pronta')])
def test_category_name(name, description):
    category = Category(name, description)
    assert category.name, name

def test_category_name_none():
    with pytest.raises(TypeError):
        category = Category(None, 'descrição')
    
def test_category_name_int():
    with pytest.raises(TypeError):
        category = Category(123, 'descrição')

def test_category_name_emptystring():
    with pytest.raises(ValueError):
        category = Category('', 'descrição')
        
def test_category_name_space():
    with pytest.raises(ValueError):
        category = Category(' ', 'descrição')
        
def test_category_name_characterexcess():
    with pytest.raises(ValueError):
        category = Category('nome'*100, 'descrição')

@pytest.mark.parametrize("name, description", [
    ('qualquer coisa', 'Blablabla'),
    ('open bar', 'Tananan'),
    ('teste', 'Vacina pronta')])
def test_category_description(name, description):
    category = Category(name, description)
    assert category.description, description

def test_category_description_none():
    with pytest.raises(TypeError):
        category = Category(None, 'descrição')

    
def test_category_description_int():
    with pytest.raises(TypeError):
        category = Category('nome', 123)

    
def test_category_description_space():
    with pytest.raises(ValueError):
        category = Category('nome', ' ')

        
def test_category_description_characters_excess():
    with pytest.raises(ValueError):
        category = Category('nome', 'descrição'*100)

            