from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola, Flask!'

@app.route('/create-article')
def create_article():
    return 'Aqui podemos crear un articulo'

@app.route('/article/<int:article_id>')
def view_article(article_id):
    return f'Estas viendo el articulo con ID: {article_id}'












if __name__ == '__main__':
    app.run(debug=True)