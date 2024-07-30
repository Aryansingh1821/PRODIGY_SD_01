import tkinter as tk
from tkinter import ttk, messagebox

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

def convert_temperature(value, unit):
    if unit == 'C':
        celsius = value
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif unit == 'F':
        fahrenheit = value
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif unit == 'K':
        kelvin = value
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        return None

    return celsius, fahrenheit, kelvin

def convert():
    try:
        value = float(entry_value.get())
        unit = unit_combobox.get()
        result = convert_temperature(value, unit)
        
        if result:
            celsius, fahrenheit, kelvin = result
            result_label.config(text=f"{value}°{unit} is equivalent to:\n"
                                     f"{celsius:.2f}°C\n"
                                     f"{fahrenheit:.2f}°F\n"
                                     f"{kelvin:.2f}K")
        else:
            messagebox.showerror("Error", "Invalid unit of temperature entered. Please enter C, F, or K.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric temperature value.")

# Set up the main application window
root = tk.Tk()
root.title("Temperature Converter")

# Create and place the widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Enter the temperature value:").grid(row=0, column=0, sticky=tk.W, pady=5)
entry_value = ttk.Entry(frame, width=20)
entry_value.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)

ttk.Label(frame, text="Select the unit of the temperature:").grid(row=1, column=0, sticky=tk.W, pady=5)
unit_combobox = ttk.Combobox(frame, values=["C", "F", "K"], state="readonly")
unit_combobox.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
unit_combobox.current(0)

convert_button = ttk.Button(frame, text="Convert", command=convert)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="", justify="left")
result_label.grid(row=3, column=0, columnspan=2, pady=5)

# Configure resizing behavior
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Start the application
root.mainloop()
