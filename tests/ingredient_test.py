from praktikum.ingredient import Ingredient
import pytest


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        ["sauce", "hot sauce", 100],
        ["sauce", "sour cream", 200],
        ["sauce", "chili sauce", 300],
        ["filling", "cutlet", 100],
        ["filling", "dinosaur", 200],
        ["filling", "sausage", 300]
    ])
    def test_create_new_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

