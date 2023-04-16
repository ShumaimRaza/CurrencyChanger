#Code By Shumaim Raza, done as an assignment and submitted to Sir Owais
import tkinter as tk
import requests

#matplotlib to  display the graph chart of currency rates over 30 day span
#import matplotlib.pyplot as plt
# API endpoint and app ID from openexchangerates
url = "https://openexchangerates.org/api/latest.json"
app_id = "64dc40bfab24463281eabe170861d89c"

# Fetch the latest exchange rates using the API
response = requests.get(url, params={"app_id": app_id})
data = response.json()

# Define the conversion function that will be called when the button is clicked
def convert_currency():
    # Get the input values from the entry fields and dropdown menus
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    amount = float(amount_entry.get())

    # Convert the amount from one currency to another using the exchange rates
    exchange_rate = data["rates"][to_currency] / data["rates"][from_currency]
    converted_amount = round(amount * exchange_rate, 2)

    # Update the result label with the converted amount
    result_label.config(text=f"{converted_amount} {to_currency}")

# Create the main window of the GUI
window = tk.Tk()
window.title("Shumaim's Currency Converter")
window.configure(background='light green')

# Create the input fields and dropdown menus for amount, from currency, and to currency
amount_label = tk.Label(window, text="Amount:")
amount_label.grid(row=0, column=0, pady=10)

amount_entry = tk.Entry(window)
amount_entry.grid(row=0, column=1, pady=10)

from_currency_label = tk.Label(window, text="From Currency:")
from_currency_label.grid(row=1, column=0, pady=10)

# Create a variable to store the selected value for the from currency dropdown menu
from_currency_var = tk.StringVar(window)
from_currency_var.set("USD") # Set the default value to USD

# Create the from currency dropdown menu with the options from the API response
from_currency_option = tk.OptionMenu(window, from_currency_var, *data["rates"].keys())
from_currency_option.grid(row=1, column=1, sticky="w", pady=10)

to_currency_label = tk.Label(window, text="To Currency:")
to_currency_label.grid(row=2, column=0, pady=10)

# Create a variable to store the selected value for the to currency dropdown menu
to_currency_var = tk.StringVar(window)
to_currency_var.set("EUR") # Set the default value to EUR

# Create the to currency dropdown menu with the options from the API response
to_currency_option = tk.OptionMenu(window, to_currency_var, *data["rates"].keys())
to_currency_option.grid(row=2, column=1, sticky="w", pady=10)

# Create the Convert button that will call the convert_currency function when clicked
convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create the label that will display the converted result
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main event loop for the GUI
window.mainloop()
