from praktikum.ingredient import Ingredient
import pytest


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type", ["sauce", "filling"])
    def test_create_new_ingredient(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "hot sauce", 100)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("name", ["hot sauce", "sour cream", "chili sauce"])
    def test_create_new_name(self, name):
        ingredient = Ingredient("sauce", name, 100)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", [100, 200, 300])
    def test_create_new_price(self, price):
        ingredient = Ingredient("sauce", "hot sauce", price)
        assert ingredient.get_price() == price
