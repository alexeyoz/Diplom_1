from unittest.mock import Mock

from praktikum.burger import Burger


class TestBurger:
    def test_set_buns(self):
        bun = Mock()
        burger = Burger()
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients

    def test_remove_ingredient(self):
        ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert ingredient not in burger.ingredients

    def test_move_ingredientX(self):
        ingredient1 = Mock()
        ingredient2 = Mock()
        burger = Burger()
        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients[0] == ingredient2 and burger.ingredients[1] == ingredient1

    def test_get_price(self):
        price = 10
        bun = Mock()
        bun.get_price.return_value = price
        burger = Burger()
        burger.set_buns(bun)
        assert burger.get_price() == price * 2

    def test_get_receipt(self):
        mock = Mock()
        burger = Burger()
        mock.get_name.return_value = "bun_test"
        mock.get_price.return_value = 100
        mock.get_type.return_value = "sauce"
        burger.set_buns(mock)
        burger.add_ingredient(mock)
        expected_result = "(==== bun_test ====)\n= sauce bun_test =\n(==== bun_test ====)\n\nPrice: 300"
        assert burger.get_receipt() == expected_result
