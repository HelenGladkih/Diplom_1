import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from unittest.mock import Mock
from data import *


@pytest.fixture
def bun_fixture(request):
    """Фикстура для создания экземпляра Bun с параметрами из теста"""
    name, price = request.param
    return Bun(name, price)

@pytest.fixture
def ingredient_fixture(request):
    """Фикстура для создания экземпляра Ingredient с параметрами из теста"""
    ingredient_type, name, price = request.param
    return Ingredient(ingredient_type, name, price)

@pytest.fixture
def burger_fixture():
    """Фикстура для создания экземпляра Burger"""
    burger = Burger()
    return burger

@pytest.fixture
def burger_with_ingredient(burger_fixture, mock_ingredient_filling):
    """Фикстура бургера с одним добавленным ингредиентом"""
    burger_fixture.add_ingredient(mock_ingredient_filling)
    return burger_fixture

@pytest.fixture
def database_fixture():
    """Фикстура для создания экземпляра Database"""
    database = Database()
    return database


@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.name = 'White'
    mock.price = 200
    mock.get_name.return_value = 'White'
    mock.get_price.return_value = 200
    return mock

@pytest.fixture
def mock_ingredient_filling():
    mock = Mock()
    mock.type = 'FILLING'
    mock.name = 'dinosaur'
    mock.price = 200
    mock.get_type.return_value = 'FILLING'
    mock.get_name.return_value = 'dinosaur'
    mock.get_price.return_value = 200
    return mock

@pytest.fixture
def mock_ingredient_sauce():
    mock = Mock()
    mock.type = 'SAUCE'
    mock.name = 'hot sauce'
    mock.price = 100
    mock.get_type.return_value = 'SAUCE'
    mock.get_name.return_value = 'hot sauce'
    mock.get_price.return_value = 100
    return mock