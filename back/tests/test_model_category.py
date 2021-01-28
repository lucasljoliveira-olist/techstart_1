import sys
sys.path.append('.')

from back.models.category import Category

class TestCategory():
    def test_category_type(self):
        category = Category('nome', 'descrição')
        assert isinstance(category, Category)
        
    def test_category_name(self):
        name = 'name'
        description = 'description'
        category = Category(name, description)
        assert category.name, name

    def test_category_name_none(self):
        try:
            category = Category(None, 'descrição')
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, TypeError)
    
    def test_category_name_int(self):
        try:
            category = Category(123, 'descrição')
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, TypeError)
    
    def test_category_name_emptystring(self):
        try:
            category = Category('', 'descrição')
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, ValueError)
        
    def test_category_name_space(self):
        try:
            category = Category(' ', 'descrição')
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, ValueError)
        
    def test_category_name_characterexcess(self):
        try:
            category = Category('nome'*100, 'descrição')
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, ValueError)

    def test_category_description(self):
        name = 'name'
        description = 'description'
        category = Category(name, description)
        assert category.description, description

    def test_category_description_none(self):
        try:
            category = Category(None, 'descrição')
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, TypeError)
    
    def test_category_description_int(self):
        try:
            category = Category('nome', 123)
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, TypeError)
    
    def test_category_description_space(self):
        try:
            category = Category('nome', ' ')
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, ValueError)
        
    def test_category_description_charactersexcess(self):
        try:
            category = Category('nome', 'descrição'*100)
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, ValueError)
            