import sys
sys.path.append('.')

from back.models.category import Category

class TestCategory():
    def test_category_name_none(self):
        try:
            category = Category(None, 'Descrição')
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, TypeError)
    
    def test_category_name_int(self):
        try:
            category = Category(123, 'Descrição')
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, TypeError)
    
    def test_category_name_emptystring(self):
        try:
            category = Category('', 'Descrição')
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, ValueError)
        
    def test_category_name_space(self):
        try:
            category = Category(' ', 'Descrição')
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, ValueError)
        
    def test_category_name_characterexcess(self):
        try:
            category = Category('nome'*100, 'Descrição')
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, ValueError)

    def test_category_description_none(self):
        try:
            category = Category(None, 'Descrição')
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, TypeError)
    
    def test_category_description_int(self):
        try:
            category = Category('nome', 123)
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, TypeError)
    
    def test_category_description_emptystring(self):
        try:
            category = Category('nome', '')
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, ValueError)
        
    def test_category_description_space(self):
        try:
            category = Category('nome', ' ')
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, ValueError)
        
    def test_category_description_charactersexcess(self):
        try:
            category = Category('nome', 'Descrição'*100)
            raise NotImplementedError("Error not raised")
        except Exception as error:
            assert isinstance(error, ValueError)
            