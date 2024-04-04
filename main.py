##################
#   QuartzzDev   #
##################

import tkinter as tk
from tkinter import messagebox
from database import Database

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ana Uygulama Ekranı")

        self.db = Database("inventory.db")
        self.db.create_tables()

        
        self.product_menu_button = tk.Button(root, text="Ürün İşlemleri", command=self.product_menu)
        self.product_menu_button.pack()

        self.employee_menu_button = tk.Button(root, text="Çalışan İşlemleri", command=self.employee_menu)
        self.employee_menu_button.pack()

    def product_menu(self):
        product_window = tk.Toplevel(self.root)
        product_window.title("Ürün İşlemleri")

        add_product_button = tk.Button(product_window, text="Ürün Ekle", command=self.add_product_window)
        add_product_button.pack()

        delete_product_button = tk.Button(product_window, text="Ürün Sil", command=self.delete_product_window)
        delete_product_button.pack()

        update_price_button = tk.Button(product_window, text="Fiyat Güncelle", command=self.update_price_window)
        update_price_button.pack()

        list_products_button = tk.Button(product_window, text="Ürünleri Listele", command=self.list_products)
        list_products_button.pack()

    def add_product_window(self):
        add_product_window = tk.Toplevel(self.root)
        add_product_window.title("Ürün Ekle")

        name_label = tk.Label(add_product_window, text="Ürün Adı:")
        name_label.pack()
        self.name_entry = tk.Entry(add_product_window)
        self.name_entry.pack()

        price_label = tk.Label(add_product_window, text="Ürün Fiyatı:")
        price_label.pack()
        self.price_entry = tk.Entry(add_product_window)
        self.price_entry.pack()

        add_button = tk.Button(add_product_window, text="Ekle", command=self.add_product)
        add_button.pack()

    def add_product(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        self.db.add_product(name, price)
        messagebox.showinfo("Başarılı", "Ürün eklendi.")
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)

    def delete_product_window(self):
        delete_product_window = tk.Toplevel(self.root)
        delete_product_window.title("Ürün Sil")

        product_list = tk.Listbox(delete_product_window)
        products = self.db.get_all_products()
        for product in products:
            product_list.insert(tk.END, f"{product[0]} - {product[1]} - {product[2]}")
        product_list.pack()

        delete_button = tk.Button(delete_product_window, text="Seçileni Sil", command=lambda: self.delete_product(product_list))
        delete_button.pack()

    def delete_product(self, product_list):
        selected_product = product_list.get(product_list.curselection())
        product_id = selected_product.split("-")[0].strip()
        self.db.delete_product(product_id)
        messagebox.showinfo("Başarılı", "Ürün silindi.")

    def update_price_window(self):
        update_price_window = tk.Toplevel(self.root)
        update_price_window.title("Fiyat Güncelle")

        product_list = tk.Listbox(update_price_window)
        products = self.db.get_all_products()
        for product in products:
            product_list.insert(tk.END, f"{product[0]} - {product[1]} - {product[2]}")
        product_list.pack()

        price_label = tk.Label(update_price_window, text="Yeni Fiyat:")
        price_label.pack()
        self.new_price_entry = tk.Entry(update_price_window)
        self.new_price_entry.pack()

        update_button = tk.Button(update_price_window, text="Güncelle", command=lambda: self.update_price(product_list))
        update_button.pack()

    def update_price(self, product_list):
        selected_product = product_list.get(product_list.curselection())
        product_id = selected_product.split("-")[0].strip()
        new_price = self.new_price_entry.get()
        self.db.update_product_price(product_id, new_price)
        messagebox.showinfo("Başarılı", "Ürün fiyatı güncellendi.")
        self.new_price_entry.delete(0, tk.END)

    def list_products(self):
        list_products_window = tk.Toplevel(self.root)
        list_products_window.title("Ürünleri Listele")

        product_list = tk.Listbox(list_products_window)
        products = self.db.get_all_products()
        for product in products:
            product_list.insert(tk.END, f"{product[0]} - {product[1]} - {product[2]}")
        product_list.pack()

    def add_employee_window(self):
        add_employee_window = tk.Toplevel(self.root)
        add_employee_window.title("Çalışan Ekle")

        name_label = tk.Label(add_employee_window, text="Çalışan Adı:")
        name_label.pack()
        self.employee_name_entry = tk.Entry(add_employee_window)
        self.employee_name_entry.pack()

        age_label = tk.Label(add_employee_window, text="Çalışan Yaşı:")
        age_label.pack()
        self.employee_age_entry = tk.Entry(add_employee_window)
        self.employee_age_entry.pack()

        position_label = tk.Label(add_employee_window, text="Pozisyon ID:")
        position_label.pack()
        self.position_entry = tk.Entry(add_employee_window)
        self.position_entry.pack()

        add_button = tk.Button(add_employee_window, text="Ekle", command=self.add_employee)
        add_button.pack()

    def add_employee(self):
        name = self.employee_name_entry.get()
        age = self.employee_age_entry.get()
        position_id = self.position_entry.get()
        self.db.add_employee(name, age, position_id)
        messagebox.showinfo("Başarılı", "Çalışan eklendi.")
        self.employee_name_entry.delete(0, tk.END)
        self.employee_age_entry.delete(0, tk.END)
        self.position_entry.delete(0, tk.END)

    def list_employees(self):
        list_employees_window = tk.Toplevel(self.root)
        list_employees_window.title("Çalışanları Listele")

        employee_list = tk.Listbox(list_employees_window)
        employees = self.db.get_all_employees()
        for employee in employees:
            employee_list.insert(tk.END, f"{employee[0]} - {employee[1]} - {employee[2]} - {employee[3]}")
        employee_list.pack()

    def employee_menu(self):
        employee_window = tk.Toplevel(self.root)
        employee_window.title("Çalışan İşlemleri")

        add_employee_button = tk.Button(employee_window, text="Çalışan Ekle", command=self.add_employee_window)
        add_employee_button.pack()

        list_employees_button = tk.Button(employee_window, text="Çalışanları Listele", command=self.list_employees)
        list_employees_button.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
