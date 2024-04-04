##################
#   QuartzzDev   #
##################

import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Giriş Ekranı")
        
        self.username_label = tk.Label(root, text="Kullanıcı Adı:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Şifre:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="Giriş Yap", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Kullanıcı adı ve şifreyi doğrula
        if self.authenticate(username, password):
            messagebox.showinfo("Başarılı", "Giriş başarılı!")
            self.root.destroy()  # Giriş başarılıysa pencereyi kapat
            # Ana uygulama ekranını burada açabilirsiniz.
        else:
            messagebox.showerror("Hata", "Kullanıcı adı veya şifre yanlış!")

    def authenticate(self, username, password):
        # Kullanıcı adı ve şifreyi SQL veritabanında kontrol et
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Kullanıcı doğrulama sorgusu
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
        user = cursor.fetchone()

        connection.close()

        if user:
            return True
        else:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
