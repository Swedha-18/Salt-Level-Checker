
import tkinter as tk

def check_salt_level():
    try:
        # Get value entered by user
        salt_level = float(entry.get())
        
        # Show the entered salt level
        label_value.config(text=f"{salt_level} ppm")
        
        # Check threshold and update status
        if salt_level <= 1000:
            label_status.config(text="Safe", fg="green")
        else:
            label_status.config(text="Too Salty", fg="red")
    
    except ValueError:
        # If the user enters invalid input
        label_status.config(text="Please enter a number", fg="orange")

# Main window
app = tk.Tk()
app.title("Salt Level Checker")
app.geometry("300x200")

# Title
label_title = tk.Label(app, text="Salt Level Checker", font=("Arial", 16))
label_title.pack(pady=10)

# Entry field for user input
entry = tk.Entry(app, font=("Arial", 12))
entry.pack(pady=5)

# Salt value display
label_value = tk.Label(app, text="--- ppm", font=("Arial", 14))
label_value.pack(pady=5)

# Status label
label_status = tk.Label(app, text="Enter value and click 'Check'", font=("Arial", 12))
label_status.pack(pady=5)

# Button
btn_check = tk.Button(app, text="Check", font=("Arial", 12), command=check_salt_level)
btn_check.pack(pady=10)

app.mainloop()

