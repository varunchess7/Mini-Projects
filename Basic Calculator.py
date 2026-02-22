import tkinter as tk

# Function to perform the calculation
def perform_calculation(operator):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error (Divide by 0)"
        # Update the result field
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Error (Invalid Input)")

# Create the main window
root = tk.Tk()
root.title("Arithmetic Calculator")
root.geometry("400x400")  # Increase window size

# Create two input fields with larger font and size
entry1 = tk.Entry(root, width=15, font=("Arial", 24), bd=5, relief="solid")
entry1.grid(row=0, column=0, padx=20, pady=20)

entry2 = tk.Entry(root, width=15, font=("Arial", 24), bd=5, relief="solid")
entry2.grid(row=0, column=1, padx=20, pady=20)

# Create buttons for basic arithmetic operations with larger size
add_button = tk.Button(root, text="+", width=5, height=2, font=("Arial", 20), command=lambda: perform_calculation("+"))
add_button.grid(row=1, column=0, padx=20, pady=20)

subtract_button = tk.Button(root, text="-", width=5, height=2, font=("Arial", 20), command=lambda: perform_calculation("-"))
subtract_button.grid(row=1, column=1, padx=20, pady=20)

multiply_button = tk.Button(root, text="*", width=5, height=2, font=("Arial", 20), command=lambda: perform_calculation("*"))
multiply_button.grid(row=2, column=0, padx=20, pady=20)

divide_button = tk.Button(root, text="/", width=5, height=2, font=("Arial", 20), command=lambda: perform_calculation("/"))
divide_button.grid(row=2, column=1, padx=20, pady=20)

# Label to display the result with larger font
result_label = tk.Label(root, text="Result: ", font=("Arial", 20))
result_label.grid(row=3, column=0, columnspan=2, pady=20)

# Start the Tkinter main loop
root.mainloop()


