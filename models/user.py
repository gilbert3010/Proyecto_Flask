from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy() # crear una instancia de SQLAlchemy y pasarle la aplicación Flask

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True )
    username = db.Column(db.String(50), nullabel=False, unique=True)
    email = db.Column(db.String(120), nullabel=False, unique=True)
    password_hash = db.Column(db.String(128), nullabel=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'