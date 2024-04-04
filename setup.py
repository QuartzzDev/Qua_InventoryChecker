##################
#   QuartzzDev   #
##################

import tkinter as tk
from tkinter import messagebox
import sqlite3

class SetupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kurulum Ekranı")
        
        self.store_name_label = tk.Label(root, text="Mağaza İsmi:")
        self.store_name_label.pack()
        self.store_name_entry = tk.Entry(root)
        self.store_name_entry.pack()

        self.setup_button = tk.Button(root, text="Kurulumu Tamamla", command=self.setup)
        self.setup_button.pack()

    def setup(self):
        store_name = self.store_name_entry.get()

        # Mağaza ismini SQL veritabanına kaydet
        connection = sqlite3.connect("store.db")
        cursor = connection.cursor()

        # Mağaza ismini kaydetme sorgusu
        cursor.execute("INSERT INTO store (store_name) VALUES (?)", (store_name,))
        connection.commit()
        connection.close()

        messagebox.showinfo("Başarılı", "Kurulum tamamlandı!")
        self.root.destroy()  # Kurulum tamamlandıysa pencereyi kapat

if __name__ == "__main__":
    root = tk.Tk()
    app = SetupApp(root)
    root.mainloop()
