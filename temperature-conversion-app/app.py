import tkinter as tk
from tkinter import ttk

# Define conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        input_unit = combo_input_unit.get().lower()

        if input_unit == 'celsius':
            fahrenheit = celsius_to_fahrenheit(temp)
            kelvin = celsius_to_kelvin(temp)
            result_text = f"{temp:.2f}°C = {fahrenheit:.2f}°F, {kelvin:.2f}K"
        elif input_unit == 'fahrenheit':
            celsius = fahrenheit_to_celsius(temp)
            kelvin = fahrenheit_to_kelvin(temp)
            result_text = f"{temp:.2f}°F = {celsius:.2f}°C, {kelvin:.2f}K"
        elif input_unit == 'kelvin':
            celsius = kelvin_to_celsius(temp)
            fahrenheit = kelvin_to_fahrenheit(temp)
            result_text = f"{temp:.2f}K = {celsius:.2f}°C, {fahrenheit:.2f}°F"
        else:
            result_text = "Invalid input unit."

        label_result.config(text=result_text)
    except ValueError:
        label_result.config(text="Invalid input. Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Temperature Conversion🌡️")
root.geometry("400x350")

# Set a uniform background color
background_color = "#f8f8f8"
root.configure(bg=background_color)

# Style configuration
style = ttk.Style(root)
style.theme_use('clam')
style.configure("TFrame", background=background_color)
style.configure("TLabel", background=background_color, foreground="#333333", font=("Arial", 12))
style.configure("TButton", background="#007acc", foreground="#ffffff", font=("Arial", 12, "bold"), padding=10)
style.configure("TEntry", font=("Arial", 12))
style.map("TButton", background=[('active', '#005f99')])

# Create and place widgets within a frame
frame = ttk.Frame(root, padding="10 10 10 10", style="TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

label_temp = ttk.Label(frame, text="Enter Temperature:")
label_temp.grid(column=0, row=0, padx=10, pady=10, sticky="W")

entry_temp = ttk.Entry(frame, width=15)
entry_temp.grid(column=1, row=0, padx=10, pady=10)

label_input_unit = ttk.Label(frame, text="Select Input Unit:")
label_input_unit.grid(column=0, row=1, padx=10, pady=10, sticky="W")

combo_input_unit = ttk.Combobox(frame, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Arial", 12))
combo_input_unit.grid(column=1, row=1, padx=10, pady=10)
combo_input_unit.current(0)

button_convert = ttk.Button(frame, text="Convert", command=convert_temperature)
button_convert.grid(column=0, row=3, columnspan=2, pady=20, ipadx=10, ipady=5)

label_result = ttk.Label(frame, text="Result will be shown here.")
label_result.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Add padding to all children of the frame
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Run the application
root.mainloop()
