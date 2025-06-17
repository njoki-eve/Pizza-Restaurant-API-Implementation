from models import db 
from app import create_app
from models import db, Restaurant, Pizza, RestaurantPizza

def seed_data():
    app = create_app()
    
    with app.app_context():
        # Clear existing data - handle case where tables don't exist
        try:
            db.session.query(RestaurantPizza).delete()
            db.session.query(Restaurant).delete()
            db.session.query(Pizza).delete()
            db.session.commit()
        except:
            db.session.rollback()
            print("Tables may not exist yet - continuing with seeding")

    
        restaurant1 = Restaurant(name='Pizza Hut', address='123 Main St')
        restaurant2 = Restaurant(name='Dominos', address='456 Oak Ave')
        
        
        pizza1 = Pizza(name='Cheese', ingredients='Dough, Tomato Sauce, Cheese')
        pizza2 = Pizza(name='Pepperoni', ingredients='Dough, Tomato Sauce, Cheese, Pepperoni')
        
        db.session.add_all([restaurant1, restaurant2, pizza1, pizza2])
        db.session.commit()
        
        
        rp1 = RestaurantPizza(restaurant=restaurant1, pizza=pizza1, price=10)
        rp2 = RestaurantPizza(restaurant=restaurant1, pizza=pizza2, price=12)
        rp3 = RestaurantPizza(restaurant=restaurant2, pizza=pizza2, price=11)
        
        db.session.add_all([rp1, rp2, rp3])
        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()