import tkinter as tk

#Este codigo se va a usar despues.

def click_boton(caracter):
    current_text = display.get()

    if caracter == '=':
        try:
            result = eval(current_text)
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")

    elif caracter == 'C':
            display.delete(0, tk.END)
    else:
        display.insert(tk.END, caracter)
        
root = tk.Tk()
root.title("Calculadora")
root.geometry("750x500")

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1) 
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)  
root.grid_columnconfigure(2, weight=1)  
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)

display = tk.Entry(root, font=("Arial", 24), justify="right")
display.grid(row=0, column=0, columnspan=5, sticky=tk.NSEW, padx=5, pady=5)

botones = ['7', '8', '9', '/',
           '4', '5', '6', '*',
           '1', '2', '3', '-',
           '0', '.', '=', '+'
           'C']

row_num = 1
col_num = 0
for boton_texto in botones:
    
    if boton_texto == '=':
         button = tk.Button(root, text=boton_texto, font=("Arial", 18), command=lambda: click_boton('='))
    elif boton_texto == 'C':
         button = tk.Button(root, text=boton_texto, font=("Arial", 18), command=lambda: click_boton('C'))
    else:
         button = tk.Button(root, text=boton_texto, font=("Arial", 18), command=lambda b=boton_texto: click_boton(b))
         
    button = tk.Button(root, text=boton_texto, font=("Arial", 18))
    button.grid(row=row_num, column=col_num, sticky=tk.NSEW, padx=5, pady=5)
   
    col_num += 1    
    if col_num > 3:
        col_num = 0
        row_num += 1

root.mainloop()