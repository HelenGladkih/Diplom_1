import pytest
from data import IngredientTestData


class TestIngredient:

    @pytest.mark.parametrize(
        "ingredient_fixture, expected_type",
        [(case, case[0]) for case in IngredientTestData.COMMON_CASES], indirect=["ingredient_fixture"]
    )
    def test_get_type_true(self, ingredient_fixture, expected_type):
        """Проверка получения типа ингредиента"""
        assert ingredient_fixture.get_type() == expected_type

    @pytest.mark.parametrize(
        "ingredient_fixture, expected_name",
        [(case, case[1]) for case in IngredientTestData.COMMON_CASES], indirect=["ingredient_fixture"]
    )
    def test_get_name_true(self, ingredient_fixture, expected_name):
        """Проверка получения названия ингредиента"""
        assert ingredient_fixture.get_name() == expected_name

    @pytest.mark.parametrize(
        "ingredient_fixture, expected_price",
        [(case, case[2]) for case in IngredientTestData.COMMON_CASES], indirect=["ingredient_fixture"]
    )
    def test_get_price_true(self, ingredient_fixture, expected_price):
        """Проверка получения цены ингредиента"""
        assert ingredient_fixture.get_price() == expected_price

    @pytest.mark.parametrize(
        "ingredient_fixture", IngredientTestData.INVALID_CASES, indirect=True
    )
    def test_init_accepts_any_parameters(self, ingredient_fixture):
        """Проверка создания ингредиента с нестандартными параметрами"""
        assert ingredient_fixture  # Просто проверяем, что объект создается
        