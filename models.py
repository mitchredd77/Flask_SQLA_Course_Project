from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
db = SQLAlchemy(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    name = db.Column('Name', db.String())
    age = db.Column('Age', db.String())
    breed = db.Column('Breed', db.String())
    color = db.Column('Color', db.String())
    size = db.Column('size', db.String())
    weight = db.Column('Weight', db.String())
    url = db.Column('URL', db.String())
    url_tag = db.Column('ALT Tag', db.String())
    pet_type = db.Column('Pet Type', db.String())
    gender = db.Column('Gender', db.String())
    spay = db.Column('Spay', db.String())
    house_trained = db.Column('House Trained', db.String())
    description = db.Column('Description', db.Text)

    def __repr__(self):
        return f'''<Pet Name: {self.name} Age: {self.age} 
                    Breed: {self.breed} Color: {self.color}
                    Size: {self.size} Weight: {self.weight}
                    URL: {self.url} Type: {self.pet_type}
                    Gender: {self.gender} Spay: {self.spay}
                    House Trained: {self.house_trained}
                    Description: {self.description}>'''

pet1 = Pet(name="Kitty", age="4 months", breed="Tabby", color="Grey", size="Small", weight="7lbs", url="https://cdn.pixabay.com/photo/2017/07/25/01/22/cat-2536662_960_720.jpg", url_tag="Cute Kitty Kat", pet_type="Cat", spay="No", house_trained="No", description="Adopt the Kitty today")  
pet1.name     
pet2 = Pet(name="Jabby", age="2 years", breed="Tabby", color="White", size="Medium", weight="7lbs", url="https://cdn.pixabay.com/photo/2016/01/20/13/05/cat-1151519_960_720.jpg", url_tag="Cute Kitty Kat", pet_type="Cat", spay="Yes", house_trained="Yes", description="Adopt the Kitty today")
pet2.name





