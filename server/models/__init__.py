from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 

from .restaurant import Restaurant
from .pizza import Pizza
from .restaurant_pizza import RestaurantPizza

__all__ = ['Restaurant', 'Pizza', 'RestaurantPizza']