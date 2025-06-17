from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from models import db


class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    
    id =db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')
 
    def to_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'restaurant_id': self.restaurant_id,
            'pizza_id': self.pizza_id,
            'restaurant': {'id': self.restaurant.id, 'name': self.restaurant.name, 'address': self.restaurant.address},
            'pizza': {'id': self.pizza.id, 'name': self.pizza.name, 'ingredients': self.pizza.ingredients}
        }

@validates('price')
def validate_price(self, key, price):
    if price < 1 or price > 30:
        raise ValueError("Price must be between 1 and 30")
    return price