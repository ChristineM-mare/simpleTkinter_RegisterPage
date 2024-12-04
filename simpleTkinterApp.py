import tkinter as tk
from tkinter import messagebox
import sqlite3

def open_login_page():
    # Create a new login window
    login_window = tk.Toplevel()
    login_window.title("Login")
    login_window.geometry("400x300")

    tk.Label(login_window, text="Enter Username: ", font=("Arial", 11)).grid(row=0, column=0, padx=10, pady=10)
    textbox_login_username = tk.Entry(login_window, font=("Arial", 11))
    textbox_login_username.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_window, text="Enter Password: ", font=("Arial", 11)).grid(row=1, column=0, padx=10, pady=10)
    textbox_login_password = tk.Entry(login_window, show="*", font=("Arial", 11))
    textbox_login_password.grid(row=1, column=1, padx=10, pady=10)

    def login_user():
        username = textbox_login_username.get()
        password = textbox_login_password.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            conn = sqlite3.connect('users.db')
            cursor = conn.cursor()


            cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
            result = cursor.fetchone()

            if result:
                if result[0] == password:
                    messagebox.showinfo("Success", "Login successful!")
                else:
                    messagebox.showerror("Error", "Wrong password!")
            else:
                messagebox.showerror("Error", "Username not found!")

            conn.close()
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")


    tk.Button(login_window, text="Login", command=login_user, font=("Arial", 11)).grid(row=2, columnspan=2, pady=10)


root = tk.Tk()
root.title("My Simple Tkinter Register Application")
root.geometry("400x300")

# Registration UI
label_username = tk.Label(root, text="Enter Username: ", fg="black", font=("Arial", 11))
label_username.grid(row=0, column=0, padx=10, pady=10)
textbox_username = tk.Entry(root, bg="#D3D3D3", fg="black", font=("Arial", 11))
textbox_username.grid(row=0, column=1, padx=10, pady=10)

label_password = tk.Label(root, text="Enter Password: ", fg="black", font=("Arial", 11))
label_password.grid(row=1, column=0, padx=10, pady=10)
textbox_password = tk.Entry(root, show="*", bg="#D3D3D3", fg="black", font=("Arial", 11))
textbox_password.grid(row=1, column=1, padx=10, pady=10)

label_confirm = tk.Label(root, text="Confirm Password: ", fg="black", font=("Arial", 11))
label_confirm.grid(row=2, column=0)
textbox_confirm = tk.Entry(root, show="*", bg="#D3D3D3", fg="black", font=("Arial", 11))
textbox_confirm.grid(row=2, column=1, padx=10, pady=10)

def register_user():
    username = textbox_username.get()
    password = textbox_password.get()
    confirm_password = textbox_confirm.get()


    if not username or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """)

        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()

        textbox_username.delete(0, tk.END)
        textbox_password.delete(0, tk.END)
        textbox_confirm.delete(0, tk.END)

        messagebox.showinfo("Success", "Account created successfully!")

    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")
    except Exception as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")

# Register button
button = tk.Button(root, text="Register Here", command=register_user, fg="black", bg="#90EE90", font=("Arial", 11))
button.grid(row=3, columnspan=4, padx=10, pady=10)

# Login button
label = tk.Label(root, text="Already have an account?")
label.grid(padx=10, pady=10, row=4, columnspan=2)
button_login = tk.Button(root, text="Login", command=open_login_page, fg="black", bg="#ADD8E6", font=("Arial", 11))
button_login.grid(padx=10, pady=10, row=5, columnspan=3)

root.mainloop()
