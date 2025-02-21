import tkinter as tk

# Function to handle button clicks
def button_click(event):
    current = entry.get()
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("400x500")
root.config(bg="lightblue")  # Set the background color to light blue

# Create the entry widget for displaying calculations
entry = tk.Entry(root, font=("Arial", 24), bd=10, relief="sunken", justify="right", bg="white", fg="black")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# Define buttons and their configurations (text, background color)
buttons = [
    ("7", "lightgreen"), ("8", "lightgreen"), ("9", "lightgreen"), ("/", "orange"),
    ("4", "lightgreen"), ("5", "lightgreen"), ("6", "lightgreen"), ("*", "orange"),
    ("1", "lightgreen"), ("2", "lightgreen"), ("3", "lightgreen"), ("-", "yellow"),
    ("0", "lightgreen"), ("C", "red"), ("=", "lightblue"), ("+", "yellow")
]

# Create and place the buttons
for i, (text, color) in enumerate(buttons):
    row = i // 4 + 1
    col = i % 4
    button = tk.Button(root, text=text, font=("Arial", 20), bg=color, fg="black", height=2, width=5)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", button_click)

# Run the application
root.mainloop()
