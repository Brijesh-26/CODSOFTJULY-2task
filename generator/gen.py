import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    name = name_entry.get()
    password_length = len_entry.get()

    if not name or not password_length:
        messagebox.showwarning("Error", "Please enter your name and password length.")
        return

    password = generate_random_password(name, int(password_length))
    password_label.config(text=f"Generated Password: {password}")

def generate_random_password(name, length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random.seed(name)  # Seed the random number generator with the name for consistent results
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def accept_password():
    password = password_label.cget("text").split(": ")[1]
    messagebox.showinfo("Accepted Password", f"Accepted password: {password}")

def reset_fields():
    name_entry.delete(0, tk.END)
    len_entry.delete(0, tk.END)
    password_label.config(text="Generated Password: ")

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("400x250")

# Create labels and entry fields
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

len_label = tk.Label(window, text="Password Length:")
len_label.pack()
len_entry = tk.Entry(window)
len_entry.pack()

# Create the generate button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Create label to display generated password
password_label = tk.Label(window, text="Generated Password: ", font=("Arial", 12, "bold"))
password_label.pack()

# Create the accept and reset buttons
accept_button = tk.Button(window, text="Accept", command=accept_password)
accept_button.pack()

reset_button = tk.Button(window, text="Reset", command=reset_fields)
reset_button.pack()

# Run the main loop
window.mainloop()
