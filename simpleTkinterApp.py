import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("My simple Tkinter Register Application")
root.geometry("400x300")
root.configure(bg="#013220")


label_username = tk.Label(root, text="Enter Username: ", fg="black", font=("Arial", 12))
label_username.grid(row=0, column=0, padx=10, pady=10)
textbox_username = tk.Entry(root, bg="#D3D3D3", fg="black", font=("Arial", 12))
textbox_username.grid(row=0, column=1, padx=10, pady=10)
label_password = tk.Label(root, text="Enter Password: ", fg="black", font=("Arial", 12))
label_password.grid(row=1, column=0, padx=10, pady=10)
textbox_password = tk.Entry(root, show="*", bg="#D3D3D3", fg="black", font=("Arial", 12))
textbox_password.grid(row=1, column=1, padx=10, pady=10)
label_confirm = tk.Label(root, text="Confirm Password: ", fg="black", font=("Arial", 12))
label_confirm.grid(row=2, column=0)
textbox_confirm = tk.Entry(root, show="*", bg="#D3D3D3", fg="black", font=("Arial", 12))
textbox_confirm.grid(row=2, column=1, padx=10, pady=10)


def show_info():
    username = textbox_username.get()
    password = textbox_password.get()
    label_username.config(text="You entered username as: "+username)
    label_password.config(text="You entered password as: "+password)
    messagebox.showinfo("Account Created Successfully!")


button = tk.Button(root, text="Register Here", command=show_info,fg="black", bg="#90EE90", font=("Arial", 12), relief='solid', borderwidth=2,)
button.grid(row=3, columnspan=3)
root.mainloop()
