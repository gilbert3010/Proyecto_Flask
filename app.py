from flask import Flask, request, jsonify
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

with app.app_context(): # Crear el contexto de la aplicación para ejecutar operaciones relacionadas con la base de datos
    db.create_all() # Crear las tablas en la base de datos según los modelos definidos (en este caso, la tabla 'Article')






@app.route('/')# Decorador para definir la ruta de la página de inicio
def home():
    return 'Hola, Flask!'

@app.route('/articles', methos=['GET'])
def get_articles():
    articles = Article.query.all() # Obtener todos los artículos de la base de datos
    return jsonify([{
        'id': article.id,
        'title': article.title,
        'content': article.content
    } for article in articles]) # Devolver una respuesta JSON con la lista de artículos

# Decorador para definir la ruta y el método HTTP para crear un nuevo artículo
@app.route('/create-article', methods=['POST'])
def create_article():
    data = request.get_json()
    new_article = Article(title=data['title'], content=data['content'])
    db.session.add(new_article)
    db.session.commit()
    
    return jsonify({
        'id': new_article.id,
        'title': new_article.title,
        'content': new_article.content
    }), 201 # Devolver una respuesta JSON con los detalles del nuevo artículo y un código de estado 201 (Creado)

# Decorador para definir la ruta y el método HTTP para actualizar un artículo existente
@app.route('/article/<int:id>', methods=['PUT'])
def update_article(id):
    article = Article.query.get_or_404(id)
    data = request.get_json()
    article.title = data['title']
    article.content = data['content']
    db.session.commit()
    
    return jsonify({
        'id': article.id,
        'title': article.title,
        'content': article.content
    })

@app.route('/article/<int:id>', methods=['DELETE'])# Decorador para definir la ruta y el método HTTP para eliminar un artículo
def delete_article(id):
    article = Article.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    
    return jsonify({
        'message': f'Articulo {id} eliminado con exito'
    })



# Decorador para definir la ruta y el método HTTP para obtener los detalles de un artículo específico
@app.route('/article/<int:article_id>')
def view_article(article_id):
    article = Article.query.get_or_404(article_id)
    return jsonify({
        'id': article.id,
        'title': article.title,
        'content': article.content
    })












if __name__ == '__main__':
    app.run(debug=True)