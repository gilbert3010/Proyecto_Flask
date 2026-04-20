from werkzeug.security import generate_password_hash, check_password_hash
from models import db

class User(db.Model): # Definir el modelo de usuario con los campos id, username, email y password_hash
    id = db.Column(db.Integer, primary_key=True )
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return f'<User {self.username}>'