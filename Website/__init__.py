from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"



def create_app():
        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'SecretKey'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(DB_NAME)

        db.init_app(app)

      

        from .views import views
        from .auth import auth
        from .payment import payment
        from .stockpage import stockpage

        app.register_blueprint(views, url_prefix= '/')
        app.register_blueprint(auth, url_prefix= '/auth') #registering blueprints
        app.register_blueprint(payment, url_prefix='/payment')
        app.register_blueprint(stockpage, url_prefix='/items')


        from .models import User, Basket, Items

        

        login_manager = LoginManager()
        login_manager.login_view='auth.login'
        login_manager.init_app(app)

        @login_manager.user_loader
        def load_user(id):
                return User.query.get(int(id))

        with app.app_context():
                db.create_all()
                create_items()
        #create_database(app)


        return app

def create_items():
        from .models import Items

        item1 = Items(name = 'Red Flowers',
                      description = 'Indulge in the captivating allure of our red flowers. Their passionate and fiery hue exudes a sense of vitality and intensity, commanding attention wherever they bloom. With their rich and deep tones, these blossoms ignite a feeling of love and romance, evoking emotions that stir the heart. Symbolizing strength and desire, red flowers captivate the senses and leave a lasting impression. Whether used as a bold statement in a bouquet or as an accent in floral arrangements, these red flowers are a captivating addition that adds a touch of drama and elegance. Immerse yourself in their passionate beauty and let their enchanting presence ignite your imagination.', 
                      picture = 'redflowers.png', 
                      price = 10.99, 
                      enviroment_impact = 7)
        
 
        item2 = Items(name = 'Pink Flowers',
                      description = 'Experience the delicate charm and grace of our pink flowers. With their soft and gentle hues, these blossoms exude a sense of femininity and tenderness, creating a captivating and romantic atmosphere. Symbolizing love, joy, and sweetness, pink flowers evoke feelings of affection and appreciation. Their elegant petals and subtle fragrance add a touch of elegance and sophistication to any setting. Whether used in bouquets, floral arrangements, or as decorative accents, pink flowers bring a sense of warmth and serenity to any space. Let their ethereal beauty enchant you and create a blissful ambiance that celebrates beauty and love.', 
                      picture = 'pinkflowers.png', 
                      price = 13.99, 
                      enviroment_impact = 7)


        item3 = Items(name = 'Yellow Flowers',
                      description = 'Embrace the radiant beauty of our yellow flowers. Bask in the warm glow of their vibrant petals, radiating joy and positivity. These blossoms embody the essence of sunshine and happiness, instantly brightening any space they adorn. Their cheerful allure brings a sense of optimism and optimism, infusing your surroundings with a burst of energy. Whether used to create a sunny bouquet or to add a pop of color to your home, these yellow flowers are a delightful symbol of warmth and optimism. Embrace their golden charm and let their sunny disposition uplift your spirits.', 
                      picture = 'yellowflowers.png', 
                      price = 15.99, 
                      enviroment_impact = 6)
        
    
        item4 = Items(name = 'Blue Flowers',
                      description = 'Experience the enchantment of our exquisite blue flowers. Delicate petals in shades of blue dance with grace, radiating a sense of tranquility and serenity. Embrace their captivating allure and let their stunning hues captivate your senses. Elevate any setting with their timeless beauty, evoking a sense of calm and harmony. Perfect for adding a touch of elegance to any occasion, these blue flowers are sure to leave a lasting impression.', 
                      picture = 'blueflowers.png', 
                      price = 20.99, 
                      enviroment_impact = 4)
        
        db.session.add(item1)
        db.session.add(item2)
        db.session.add(item3)
        db.session.add(item4)


        db.session.commit()
        