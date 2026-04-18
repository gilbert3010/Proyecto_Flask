from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy() # crear una instancia de SQLAlchemy y pasarle la aplicación Flask

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<Article {self.title}>'