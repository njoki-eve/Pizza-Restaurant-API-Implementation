from flask import Blueprint, jsonify, request
from models.restaurant_pizza import RestaurantPizza, db

restaurant_pizza_bp = Blueprint('restaurant_pizza', __name__)

@restaurant_pizza_bp.route('/', methods=['GET'])
def get_restaurant_pizzas():
    restaurant_pizzas = RestaurantPizza.query.all()
    return jsonify([rp.to_dict() for rp in restaurant_pizzas])

@restaurant_pizza_bp.route('/restaurant_pizza', methods=['POST'])
def create_restaurant_pizzas():
    data = request.get_json()
    try:
        restaurant_pizza = RestaurantPizza(price=data['price'], pizza_id=data['pizza_id'], restaurant_id=data['restaurant_id'])
        db.session.add(restaurant_pizza)
        db.session.commit()
        return jsonify({
            'id': restaurant_pizza.id,
            'price': restaurant_pizza.price,
            'pizza_id': restaurant_pizza.pizza_id,
            'restaurant_id': restaurant_pizza.restaurant_id,
            'pizza': {'id': restaurant_pizza.pizza.id, 'name': restaurant_pizza.pizza.name, 'ingredients': restaurant_pizza.pizza.ingredients},
            'restaurant': {'id': restaurant_pizza.restaurant.id, 'name': restaurant_pizza.restaurant.name, 'address': restaurant_pizza.restaurant.address}
            
        }), 201
    except ValueError as e:
        return jsonify({'errors': [str(e)]}), 400