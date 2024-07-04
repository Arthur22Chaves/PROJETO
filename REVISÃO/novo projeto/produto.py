from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Configuração do banco de dados
DATABASE = 'products.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_product_data(query, limit=10):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE name LIKE ? LIMIT ?", (f"%{query}%", limit))
    products = cursor.fetchall()
    conn.close()
    return products

def get_product_data_by_id(product_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product

@app.route('/', methods=['GET', 'POST'])
def search_products():
    if request.method == 'POST':
        query = request.form['query']
        search_results = get_product_data(query, limit=10)
        return render_template('search_results.html', search_results=search_results)
    return render_template('index.html')

@app.route('/product/<int:product_id>')
def product_details(product_id):
    product_data = get_product_data_by_id(product_id)
    return render_template('product_details.html', product=product_data)

if __name__ == '__main__':
    app.run(debug=True)