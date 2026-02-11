import tkinter as tk

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

expression = ""

# Function to update expression
def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

# Function to evaluate expression
def equalpress():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Function to clear
def clear():
    global expression
    expression = ""
    input_text.set("")

# Entry field
input_text = tk.StringVar()
entry = tk.Entry(root, textvariable=input_text, font=('Arial', 20),
                 bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, height=2,
                  font=('Arial', 14), command=equalpress)\
            .grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=button, width=5, height=2,
                  font=('Arial', 14),
                  command=lambda b=button: press(b))\
            .grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root, text="C", width=22, height=2,
          font=('Arial', 14), command=clear)\
    .grid(row=row, column=0, columnspan=4, padx=5, pady=5)

# Run app
root.mainloop()
