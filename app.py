from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # Crear una instancia de Flask


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db' # Configurar la URI de la base de datos (en este caso, SQLite)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desactivar el seguimiento de modificaciones de objetos para mejorar el rendimiento



db = SQLAlchemy(app) # crear una instancia de SQLAlchemy y pasarle la aplicación Flask
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f'<Article {self.title}>'

with app.app_context():
    db.create_all()






@app.route('/')# Decorador para definir la ruta de la página de inicio
def home():
    return 'Hola, Flask!'



@app.route('/create-article', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        
        title = request.form['title']
        content = request.form.get('content')
        
        new_article = Article(title=title, content=content)
        db.session.add(new_article)
        db.session.commit()
        
        return f'Articulo creado {new_article.title}, contenido: {new_article.content}'
        
        
    return '''

        <form method = "POST" action="create-article">
            <label form='title'> Título del artículo: </label><br>
            <input type='text' id='title' name='title'><br>
            
            <label form='content'> Contenido del artículo: </label><br>
            <textarea id='content' name='content'></textarea><br>
            
            <input type='submit' value='Crear Artículo'>
        </form>

'''

@app.route('/article/<int:article_id>')
def view_article(article_id):
    return f'Estas viendo el articulo con ID: {article_id}'












if __name__ == '__main__':
    app.run(debug=True)