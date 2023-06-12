from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(Nike)

# connect to SQLite database
conn = sqlite3.connect('clothing.db')
c = conn.cursor()

# create a table for the products
c.execute('''CREATE TABLE IF NOT EXISTS products 
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             description TEXT,
             price REAL,
             image TEXT)''')
conn.commit()

@app.route('/')
def home():
    # display all products in the home page
    c.execute("SELECT * FROM products")
    products = c.fetchall()
    return render_template('home.html', products=products)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        # get the form data and insert into the database
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        image = request.form['image']
        c.execute("INSERT INTO products (name, description, price, image) VALUES (?, ?, ?, ?)", 
                  (name, description, price, image))
        conn.commit()
        return redirect(url_for('home'))
    else:
        return render_template('add_product.html')

@app.route('/product/<int:id>')
def view_product(id):
    # display details of a specific product
    c.execute("SELECT * FROM products WHERE id=?", (id,))
    product = c.fetchone()
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
