import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("bun_name", ["Bun", "Bun2"])
    def test_create_new_bun(self, bun_name):
        bun = Bun(bun_name, 10)
        assert bun.get_name() == bun_name

    @pytest.mark.parametrize("price", [10, 20])
    def test_create_new_price(self, price):
        bun = Bun("Bun", price)
        assert bun.get_price() == price