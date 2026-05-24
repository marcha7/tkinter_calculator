import tkinter as tk

class Calculator:
    def __init__(self, result_text):
        self.result_text = result_text
        self.operands = []
        self.operation = ""

    def show_equation(self):
        match len(self.operands):
            case 0:
                self.result_text.set('0')
            case 1:
                if self.operation == "":
                    self.result_text.set(f"{self.operands[0]}")
                else : 
                    self.result_text.set(f"{self.operands[0]} {self.operation}")
            case 2:
                self.result_text.set(f"{self.operands[0]} {self.operation} {self.operands[1]}")

    def add_operand(self, number):
        match len(self.operands):
            case 0:
                self.operands.append(number)
            case 1:
                if self.operation == "":
                    self.operands[0] = number
                else : 
                    self.operands.append(number)
            case 2:
                self.operands[1] = number
        self.show_equation()

    def set_operation(self, operation):
        if len(self.operands) != 0:
            self.operation = operation
            self.show_equation()

    def clear(self):
        self.operands.clear()
        self.operation = ""
        self.result_text.set('0')

    def calculate_result(self):
        if len(self.operands) == 2:
            match self.operation:
                case '+':
                    result = self.operands[0] + self.operands[1]
                case '-':
                    result = self.operands[0] - self.operands[1]
                case '*':
                    result = self.operands[0] * self.operands[1]
                case '/':
                    if self.operands[1] == 0:
                        self.clear()
                        result = "Zero Division Err"
                        self.result_text.set(result)
                        return
                    else:
                        result = self.operands[0] / self.operands[1]
                case _:
                    return
            self.clear()
            self.operands.append(result)
            self.result_text.set(result)


root = tk.Tk()
root.title('Calculatrice')
root.iconbitmap('Puck.ico')
root.config(background='#333333')
root.geometry("400x600")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)


main_frame = tk.Frame(root, bg='#333333')
main_frame.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)


main_frame.rowconfigure(0, weight=2)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)
main_frame.rowconfigure(3, weight=1)
main_frame.rowconfigure(4, weight=1)
main_frame.rowconfigure(5, weight=1)
main_frame.columnconfigure(0, weight=1, uniform="same_group")
main_frame.columnconfigure(1, weight=1, uniform="same_group")
main_frame.columnconfigure(2, weight=1, uniform="same_group")
main_frame.columnconfigure(3, weight=1, uniform="same_group")

pad_y = 10
pad_x = 10
calculator_font = ('Courrier', 20)
button_bg = '#595959'

result_text = tk.StringVar()
result_text.set('0')
result = tk.Label(main_frame, textvariable=result_text, bg='#A2AF77', fg='white', font=calculator_font, anchor='e', padx=10)
result.grid(row=0, rowspan=2, column=0, columnspan=4, sticky='nsew', padx=pad_x, pady=pad_y)


calculator = Calculator(result_text)


mc_button = tk.Button(main_frame, text='MC', bg=button_bg, fg='white', font=calculator_font)
mc_button.grid(row=2, column=0, sticky='nsew', padx=pad_x, pady=pad_y)

m_plus_button = tk.Button(main_frame, text='M+', bg=button_bg, fg='white', font=calculator_font)
m_plus_button.grid(row=2, column=1, sticky='nsew', padx=pad_x, pady=pad_y)


digit_buttons = [
    (7, 3, 0, 1, 1), (8, 3, 1, 1, 1), (9, 3, 2, 1, 1),
    (4, 4, 0, 1, 1), (5, 4, 1, 1, 1), (6, 4, 2, 1, 1),
    (1, 5, 0, 1, 1), (2, 5, 1, 1, 1), (3, 5, 2, 1, 1),
    (0, 6, 0, 1, 2),
]

for number, row, column, rowspan, columnspan in digit_buttons:
    button = tk.Button(
        main_frame,
        text=str(number),
        bg=button_bg,
        fg='white',
        font=calculator_font,
        command=lambda n=number: calculator.add_operand(n)
    )

    button.grid(
        row=row,
        column=column,
        rowspan=rowspan,
        columnspan=columnspan,
        sticky='nsew',
        padx=pad_x,
        pady=pad_y
    )


operation_buttons = [
    ("/", 2, 2),
    ("*", 2, 3),
    ("-", 3, 3),
    ("+", 4, 3),
]

for text, row, column in operation_buttons:
    button = tk.Button(
        main_frame,
        text=text,
        bg=button_bg,
        fg='white',
        font=calculator_font,
        command=lambda operation=text: calculator.set_operation(operation)
    )
    button.grid(row=row, column=column, sticky='nsew', padx=pad_x, pady=pad_y)


clear_button = tk.Button(main_frame, text='C', bg='black', fg='white', font=calculator_font, command=lambda: calculator.clear())
clear_button.grid(row=6, column=2, sticky='nsew', padx=pad_x, pady=pad_y)

equal_button = tk.Button(main_frame, text='=', bg='#F05A2D', fg='white', font=calculator_font, command=lambda: calculator.calculate_result())
equal_button.grid(row=5, rowspan=2, column=3, sticky='nsew', padx=pad_x, pady=pad_y)

main_frame.mainloop()