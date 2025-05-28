import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock) 

window = tk.Tk()
window.title("Digital Clock")
window.geometry("300x100")
window.configure(bg="black")
clock_label = tk.Label(window, font=('Arial', 40, 'bold'), fg='white', bg='black')
clock_label.pack(expand=True)
update_clock()
window.mainloop()
