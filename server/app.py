from flask import Flask, jsonify
from models import db
from controllers.restaurant_controller import restaurant_bp
from controllers.pizza_controller import pizza_bp
from controllers.restaurant_pizza_controller import restaurant_pizza_bp


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12e45@localhost/pizza_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
         db.create_all()
         
    
    app.register_blueprint(restaurant_bp, url_prefix='/api/restaurants')
    app.register_blueprint(pizza_bp, url_prefix='/api/pizzas')
    app.register_blueprint(restaurant_pizza_bp, url_prefix='/api/restaurant_pizzas')
    app.url_map.strict_slashes = False
    

    @app.route('/')
    def home():
        return "Pizza API is running. Try /api/restaurants or /api/pizzas"
     
    @app.route('/routes')
    def list_routes():
        return jsonify({
            'routes': [str(rule) for rule in app.url_map.iter_rules()
                    if str(rule) != '/static/<path:filename>' ]
        }) 
    return app
 
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)