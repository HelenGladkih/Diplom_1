import pytest
from data import DatabaseData


class TestDatabase:

    @pytest.mark.parametrize('index, name, price', DatabaseData.DATABASE_BUNS)
    def test_buns_values_true(self, database_fixture, index, name, price):
        """Проверка данных булочек в базе"""
        buns = database_fixture.available_buns()
        assert (buns[index].name == name and buns[index].price == price), (
            f"Булка с индексом {index} не соответствует ожиданиям. "
            f"Ожидалось: name='{name}', price={price}. "
            f"Фактически: name='{buns[index].name}', price={buns[index].price}"
    )
        
    @pytest.mark.parametrize('index, type, name, price', DatabaseData.DATABASE_INGREDS)
    def test_ingredients_values_true(self, database_fixture, index, type, name, price):
        """Проверка данных ингредиентов в базе"""
        ingredient = database_fixture.available_ingredients()
        assert (ingredient[index].type == type and ingredient[index].name == name and ingredient[index].price == price), (
            f"Ингредиент с индексом {index} не соответствует ожиданиям. "
            f"Ожидалось: type='{type}', name='{name}', price={price}. "
            f"Фактически: type='{ingredient[index].type}', name='{ingredient[index].name}', price={ingredient[index].price}"
    )       

    def test_available_buns_returns_list(self, database_fixture):
        """Проверка формата возвращаемых булочек"""
        buns = database_fixture.available_buns()
        assert isinstance(buns, list) and len(buns) > 0, "Метод available_ingredients должен возвращать заполненный список"

    def test_available_ingredients_returns_list(self, database_fixture):
        """Проверка формата возвращаемых ингредиентов"""
        ingredients = database_fixture.available_ingredients()
        assert isinstance(ingredients, list) and len(ingredients) > 0, "Метод available_ingredients должен возвращать заполненный список"
        