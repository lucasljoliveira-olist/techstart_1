import sys
sys.path.append('.')
from back.models.category import Category
import pytest

def test_category_instance():
    category = Category('Produto', 'muito bom')
    assert isinstance(category, Category)
    
@pytest.mark.parametrize("name, description", [
    (None, 'descrição'),
    (123, 'descrição')])
def test_category_name_none_int_space(name, description):
    with pytest.raises(TypeError):
        category = Category(name, description)

def test_category_name_empty():
    with pytest.raises(ValueError):
        category = Category('', 'descricao')

def test_category_name_space():
    with pytest.raises(ValueError):
        category = Category(' ', 'descricao')

def test_category_name_excess():
    with pytest.raises(ValueError):
        category = Category('nome'*100, 'descricao')

@pytest.mark.parametrize("name, description", [
    ('teste', None),
    ('teste', 123)])
def test_description_none_int(name, description):
    with pytest.raises(TypeError):
        category = Category(name, description) 

def test_category_description_space():  
    with pytest.raises(ValueError):
        category = Category('teste', ' ')

def test_category_name_excess():
    with pytest.raises(ValueError):
        category = Category('nome', 'descricao'*100)