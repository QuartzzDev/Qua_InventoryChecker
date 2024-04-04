##################
#   QuartzzDev   #
##################

import sqlite3

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        # Mağaza tablosu oluşturma
        self.cursor.execute("CREATE TABLE IF NOT EXISTS store (id INTEGER PRIMARY KEY, store_name TEXT)")
        # Ürünler tablosu oluşturma
        self.cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price REAL)")
        # Çalışanlar tablosu oluşturma
        self.cursor.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, position_id INTEGER)")
        # Pozisyonlar tablosu oluşturma
        self.cursor.execute("CREATE TABLE IF NOT EXISTS positions (id INTEGER PRIMARY KEY, name TEXT)")

        self.connection.commit()

    def add_product(self, name, price):
        self.cursor.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
        self.connection.commit()

    def delete_product(self, product_id):
        self.cursor.execute("DELETE FROM products WHERE id=?", (product_id,))
        self.connection.commit()

    def update_product_price(self, product_id, new_price):
        self.cursor.execute("UPDATE products SET price=? WHERE id=?", (new_price, product_id))
        self.connection.commit()

    def get_all_products(self):
        self.cursor.execute("SELECT * FROM products")
        return self.cursor.fetchall()

    def add_employee(self, name, age, position_id):
        self.cursor.execute("INSERT INTO employees (name, age, position_id) VALUES (?, ?, ?)", (name, age, position_id))
        self.connection.commit()

    def get_all_employees(self):
        self.cursor.execute("SELECT * FROM employees")
        return self.cursor.fetchall()

    def add_position(self, name):
        self.cursor.execute("INSERT INTO positions (name) VALUES (?)", (name,))
        self.connection.commit()

    def delete_position(self, position_id):
        self.cursor.execute("DELETE FROM positions WHERE id=?", (position_id,))
        self.connection.commit()

    def get_all_positions(self):
        self.cursor.execute("SELECT * FROM positions")
        return self.cursor.fetchall()


if __name__ == "__main__":
    db = Database("inventory.db")
    db.create_tables()
