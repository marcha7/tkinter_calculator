import tkinter as tk





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


mc_button = tk.Button(main_frame, text='MC', bg=button_bg, fg='white', font=calculator_font)
mc_button.grid(row=2, column=0, sticky='nsew', padx=pad_x, pady=pad_y)

m_plus_button = tk.Button(main_frame, text='M+', bg=button_bg, fg='white', font=calculator_font)
m_plus_button.grid(row=2, column=1, sticky='nsew', padx=pad_x, pady=pad_y)

div_button = tk.Button(main_frame, text='/', bg=button_bg, fg='white', font=calculator_font)
div_button.grid(row=2, column=2, sticky='nsew', padx=pad_x, pady=pad_y)

mult_button = tk.Button(main_frame, text='*', bg=button_bg, fg='white', font=calculator_font)
mult_button.grid(row=2, column=3, sticky='nsew', padx=pad_x, pady=pad_y)

button7 = tk.Button(main_frame, text='7', bg=button_bg, fg='white', font=calculator_font)
button7.grid(row=3, column=0, sticky='nsew', padx=pad_x, pady=pad_y)

button8 = tk.Button(main_frame, text='8', bg=button_bg, fg='white', font=calculator_font)
button8.grid(row=3, column=1, sticky='nsew', padx=pad_x, pady=pad_y)

button9 = tk.Button(main_frame, text='9', bg=button_bg, fg='white', font=calculator_font)
button9.grid(row=3, column=2, sticky='nsew', padx=pad_x, pady=pad_y)

minus_button = tk.Button(main_frame, text='-', bg=button_bg, fg='white', font=calculator_font)
minus_button.grid(row=3, column=3, sticky='nsew', padx=pad_x, pady=pad_y)

button4 = tk.Button(main_frame, text='4', bg=button_bg, fg='white', font=calculator_font)
button4.grid(row=4, column=0, sticky='nsew', padx=pad_x, pady=pad_y)

button5 = tk.Button(main_frame, text='5', bg=button_bg, fg='white', font=calculator_font)
button5.grid(row=4, column=1, sticky='nsew', padx=pad_x, pady=pad_y)

button6 = tk.Button(main_frame, text='6', bg=button_bg, fg='white', font=calculator_font)
button6.grid(row=4, column=2, sticky='nsew', padx=pad_x, pady=pad_y)

plus_button = tk.Button(main_frame, text='+', bg=button_bg, fg='white', font=calculator_font)
plus_button.grid(row=4, column=3, sticky='nsew', padx=pad_x, pady=pad_y)

button1 = tk.Button(main_frame, text='1', bg=button_bg, fg='white', font=calculator_font)
button1.grid(row=5, column=0, sticky='nsew', padx=pad_x, pady=pad_y)

button2 = tk.Button(main_frame, text='2', bg=button_bg, fg='white', font=calculator_font)
button2.grid(row=5, column=1, sticky='nsew', padx=pad_x, pady=pad_y)

button3 = tk.Button(main_frame, text='3', bg=button_bg, fg='white', font=calculator_font)
button3.grid(row=5, column=2, sticky='nsew', padx=pad_x, pady=pad_y)

equal_button = tk.Button(main_frame, text='=', bg='#F05A2D', fg='white', font=calculator_font)
equal_button.grid(row=5, rowspan=2, column=3, sticky='nsew', padx=pad_x, pady=pad_y)

button = tk.Button(main_frame, text='0', bg=button_bg, fg='white', font=calculator_font)
button.grid(row=6, column=0, columnspan=2, sticky='nsew', padx=pad_x, pady=pad_y)

point_button = tk.Button(main_frame, text='.', bg=button_bg, fg='white', font=calculator_font)
point_button.grid(row=6, column=2, sticky='nsew', padx=pad_x, pady=pad_y)


main_frame.mainloop()