import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("bun_name, price", [["Bun", 10], ["Bun2", 20]])
    def test_create_new_bun(self, bun_name, price):
        bun = Bun(bun_name, price)
        assert bun.get_name() == bun_name
        assert bun.get_price() == price