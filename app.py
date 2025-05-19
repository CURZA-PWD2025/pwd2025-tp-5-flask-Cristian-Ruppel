from flask import Flask
from data.data_productos import categorias, productos

app = Flask(__name__)

@app.route('/')
def home():
    mensaje = '<h1>¡Hola desde Flask!</h1>'
    mensaje += '<p>Soy Cristian Virtual, estudiante de Web Dinámica.</p>'
    mensaje += '<p>Estoy aprendiendo a usar Flask para crear aplicaciones web.</p>'
    return mensaje

@app.route('/productos')
def listar_productos():
    mensaje = '<h1>Listado de Productos</h1><ul>'
    
    for producto in productos:
        mensaje += f'<li>ID: {producto["id"]} - Descripción: {producto["descripcion"]} - Categoría ID: {producto["categoria_id"]}</li>'
    
    mensaje += '</ul>'
    return mensaje

@app.route('/categorias')
def listar_categorias():
    mensaje = '<h1>Listado de Categorías</h1><ul>'
    
    for categoria in categorias:
        mensaje += f'<li>ID: {categoria["id"]} - Descripción: {categoria["descripcion"]}</li>'
    
    mensaje += '</ul>'
    return mensaje

if __name__ == '__main__':
    app.run(debug=True)