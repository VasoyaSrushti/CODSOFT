import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(entry_length.get())
    if length > 0:
        password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(length))
        result.set(password)
    else:
        messagebox.showwarning("Error", "Please enter a valid password length.")

# Create main window
root_password = tk.Tk()
root_password.title("Password Generator")
root_password.configure(bg="teal")

# Create UI elements
entry_length = tk.Entry(root_password, width=30, font=("Arial", 14), bg="lightcyan")
result = tk.StringVar()

# Place UI elements in the window
tk.Label(root_password, text="Password Length:", font=("Arial", 14), bg="lightcyan").pack(pady=(20,5))
entry_length.pack(pady=5)
generate_button = tk.Button(root_password, text="Generate Password", command=generate_password, font=("Arial", 14), bg="darkblue", fg="white")
generate_button.pack(pady=(5, 5))  # Added extra space below the button
tk.Label(root_password, text="Generated Password:", font=("Arial", 14), bg="lightcyan").pack()
password_label = tk.Label(root_password, textvariable=result, font=("Courier", 14), bg="seashell")
password_label.pack(pady=(5, 5))  # Added extra space below the generated password label

# Run the password generator application
root_password.mainloop()