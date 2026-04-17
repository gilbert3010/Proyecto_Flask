from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola, Flask!'

from flask import Flask, request  # ← IMPORTANTE: importar request

@app.route('/create-article', methods=['GET', 'POST'])
def create_article():
    if request.method == 'POST':
        title = request.form['title']      
        content = request.form.get('content')  
        return f'Artículo creado: {title} - {content}'
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