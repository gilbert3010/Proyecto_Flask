from flask import Flask, request, jsonify
from models.article import Article
from models.user import User
from models import db


app = Flask(__name__) # Crear una instancia de Flask


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db' # Configurar la URI de la base de datos (en este caso, SQLite)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desactivar el seguimiento de modificaciones de objetos para mejorar el rendimiento


db.init_app(app)# Inicializar la extensión SQLAlchemy con la aplicación Flask

with app.app_context(): # Crear el contexto de la aplicación para ejecutar operaciones relacionadas con la base de datos
    db.create_all() # Crear las tablas en la base de datos según los modelos definidos (en este caso, la tabla 'Article')


@app.route('/')# Decorador para definir la ruta de la página de inicio
def home():
    return 'Hola, Flask!'

@app.route('/register', methods=['POST']) # Decorador para definir la ruta y el método HTTP para registrar un nuevo usuario
def register():
    data = request.get_json() # Obtener los datos JSON enviados en la solicitud
    if User.query.filter_by(email=data['email']).first() is not None:
        return jsonify({'message': 'El correo electrónico ya está registrado'}), 400 # Devolver un mensaje de error si el correo electrónico ya está registrado

    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])# Establecer la contraseña del nuevo usuario utilizando el método set_password
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({
        'message': f'Usuario {new_user.username}registrado correctamente',
        "id": new_user.id,
        "username": new_user.username,
        "email": new_user.email
    })
    
@app.route('/login', methods=['POST']) # Decorador para definir la ruta y el método HTTP para iniciar sesión
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    
    if user is None or not user.check_password(data['password']):
        return jsonify({'message': 'Correo electrónico o contraseña incorrectos'}), 401
    
    return jsonify({
        'message': f'Bienvenido {user.username}',
        'id': user.id,
        'username': user.username,
        'email': user.email
    }), 200



@app.route('/articles', methods=['GET'])
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

@app.route('/delete-article/<int:id>', methods=['DELETE'])# Decorador para definir la ruta y el método HTTP para eliminar un artículo
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