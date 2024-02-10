import tkinter as tk
from tkinter.font import Font

def btns(num):  # This function handles the function when the button is clicked
    text = num.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    
    elif text == "del":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text[:-1])  # Delete the last character
    
    elif text == "←":  # Backspace button
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text[:-1])  # Delete the last character
    
    elif text == "%":  # Percentage button
        current_text = entry.get()
        try:
            result = eval(current_text) / 100
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
            
    else:
        entry.insert(tk.END, text)


# Setting the window size
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("350x400")
window.configure(bg="seashell")

# Create an input field (Entry widget) for displaying and inputting numbers and expressions
entry = tk.Entry(window, font=("typewriter", 20))
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=10) 

# Buttons with text color and background color settings
button_settings = (
    ("del", "black", "lightcoral"),
    ("%", "black", "lightblue"),
    ("←", "black", "plum"),
    ("/", "black", "lightyellow"),
    ("7", "black", "lightgray"),
    ("8", "black", "lightgray"),
    ("9", "black", "lightgray"),
    ("*", "black", "lightyellow"),
    ("4", "black", "lightgray"),
    ("5", "black", "lightgray"),
    ("6", "black", "lightgray"),
    ("-", "black", "lightyellow"),
    ("1", "black", "lightgray"),
    ("2", "black", "lightgray"),
    ("3", "black", "lightgray"),
    ("+", "black", "lightyellow"),
    ("00", "black", "lightgray"),
    ("0", "black", "lightgray"),
    (".", "black", "lightgray"),
    ("=", "black", "palegreen")
)

c = 0  # column
r = 1  # row

for button_text, text_color, bg_color in button_settings:
    btn = tk.Button(window, text=button_text, font=("typewriter", 15),
                    padx=10, pady=10, width=5, height=2, fg=text_color, bg=bg_color)
    btn.grid(row=r, column=c, padx=5, pady=5)
    c += 1
    if c > 3:
        c = 0
        r += 1

# Configure row and column weights for resizing
for row_index in range(1, 6):
    window.grid_rowconfigure(row_index, weight=1)

for column_index in range(4):
    window.grid_columnconfigure(column_index, weight=1)

# Bind the buttons to the click event
for btn in window.winfo_children():
    btn.bind("<Button-1>", btns)

window.mainloop()
