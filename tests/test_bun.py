import pytest
from data import BunTestData


class TestBun:
      
    @pytest.mark.parametrize("bun_fixture, expected_name", BunTestData.NAME_CASES, indirect=["bun_fixture"])
    def test_get_name_true(self, bun_fixture, expected_name):
        """Проверка получения названия булочки"""
        assert bun_fixture.get_name() == expected_name
     
    @pytest.mark.parametrize("bun_fixture, expected_price", BunTestData.PRICE_CASES, indirect=["bun_fixture"])
    def test_get_price_true(self, bun_fixture, expected_price):
        """Проверка получения цены булочки"""
        assert bun_fixture.get_price() == expected_price

    @pytest.mark.parametrize("bun_fixture", BunTestData.INVALID_CASES, indirect=True)
    def test_init_accepts_any_parameters(self, bun_fixture):
        """Проверка создания булочки с нестандартными параметрами"""
        assert bun_fixture  # Просто проверяем, что объект создан
        