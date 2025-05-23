import tkinter as tk

# Main window
root = tk.Tk()
root.title("Calculator")

# Entry field
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Functions
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Number Buttons
buttons = []
for i in range(10):
    buttons.append(tk.Button(root, text=str(i), padx=40, pady=20, command=lambda x=i: button_click(x)))

# Operator Buttons
button_add = tk.Button(root, text="+", padx=39, pady=20, command=lambda: button_click('+'))
button_sub = tk.Button(root, text="-", padx=41, pady=20, command=lambda: button_click('-'))
button_mul = tk.Button(root, text="*", padx=41, pady=20, command=lambda: button_click('*'))
button_div = tk.Button(root, text="/", padx=41, pady=20, command=lambda: button_click('/'))

button_equal = tk.Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = tk.Button(root, text="C", padx=91, pady=20, command=button_clear)

# Place Number Buttons (1–9)
buttons[1].grid(row=3, column=0)
buttons[2].grid(row=3, column=1)
buttons[3].grid(row=3, column=2)

buttons[4].grid(row=2, column=0)
buttons[5].grid(row=2, column=1)
buttons[6].grid(row=2, column=2)

buttons[7].grid(row=1, column=0)
buttons[8].grid(row=1, column=1)
buttons[9].grid(row=1, column=2)

# Button 0
buttons[0].grid(row=4, column=0)

# Operator Buttons
button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)

# Equal and Clear Buttons
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)

# Run
root.mainloop()
