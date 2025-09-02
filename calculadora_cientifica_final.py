import tkinter as tk
import math
import re

BG_COLOR = "black"
BTN_BG_COLOR = "gray30"
BTN_FG_COLOR = "white"
BTN_ACTIVE_BG = "gray35"
DISPLAY_BG = "white"
DISPLAY_FG_COLOR = "black"
FONT_DISPLAY = ("Arial", 25)
FONT_BUTTON = ("Arial", 15)
WINDOW_SIZE = "425x350"
BTN_CELL_SIZE = 55

BUTTON_LAYOUT = [
    ['sin', 'cos', 'tan', 'log', 'ln', 'sqrt'],
    ['7', '8', '9', '/', '(', ')'],
    ['4', '5', '6', '*', 'π', 'e'],
    ['1', '2', '3', '-', 'C', '←'],
    ['.', '0', '+', '=', 'x²', '^']]

def agregar(valor):
    actual = display_var.get()
    display_var.set(valor if actual == '0' else actual + valor)

def limpiar():
    display_var.set('0')

def borrar():
    actual = display_var.get()
    display_var.set(actual[:-1] if len(actual) > 1 else '0')

def es_expresion_segura(expr):
    patron = r'^[0-9+\-*/().πe^ ]*(sin|cos|tan|log|ln|sqrt)*[0-9+\-*/().πe^ ]*$'
    return bool(re.fullmatch(patron, expr.replace(' ', '')))

def calcular():
    expr = display_var.get()
    expr_eval = expr.replace('π', str(math.pi)) \
                    .replace('e', str(math.e)) \
                    .replace('^', '**') \
                    .replace('ln', 'log')
    
    if not es_expresion_segura(expr):
        display_var.set("Error")
        return
    try:
        resultado = eval(expr_eval, {"__builtins__": None}, vars(math))
        display_var.set(str(resultado))
    except Exception:
        display_var.set("Error")

def crear_interfaz(root):
    root.title('Calculadora científica')
    root.configure(bg = BG_COLOR)
    root.geometry(WINDOW_SIZE)
    root.resizable(False, False)

    root.grid_rowconfigure(0, 
                           weight=0, 
                           minsize=70
                           )
    
    root.grid_columnconfigure(0, 
                              weight=1
                              )

    display = tk.Entry(
        root,
        fon = FONT_DISPLAY,
        justify = 'right',
        textvariable = display_var,
        bd = 0,
        relief = 'flat',
        state = 'readonly',
        readonlybackground = DISPLAY_BG,
        fg = DISPLAY_FG_COLOR,
        highlightthickness = 0
    )

    display.grid(row = 0, 
                 column = 0, 
                 sticky = tk.NSEW, 
                 padx = 6, 
                 pady = 6
                 )

    frame_botones = tk.Frame(root, bg = BG_COLOR)
    
    frame_botones.grid(row = 1, 
                       column = 0, 
                       sticky = tk.NSEW
                       )

    for r in range(len(BUTTON_LAYOUT)):
        frame_botones.grid_rowconfigure(r, 
                                        weight = 1, 
                                        minsize = BTN_CELL_SIZE
                                        )
    for c in range(6):
        frame_botones.grid_columnconfigure(c, 
                                           weight = 1, 
                                           minsize = BTN_CELL_SIZE
                                           )

    for row_num, fila in enumerate(BUTTON_LAYOUT):
        for col_num, texto in enumerate(fila):
            boton = tk.Button(
                frame_botones,
                text = texto,
                font = FONT_BUTTON,
                bg = BTN_BG_COLOR,
                fg = BTN_FG_COLOR,
                activebackground = BTN_ACTIVE_BG,
                activeforeground = BTN_FG_COLOR,
                relief = "ridge",
                bd = 1,
                highlightthickness = 0,
                command=lambda x=texto: manejar_click(x)
            )
            
            boton.grid(row = row_num, 
                       column = col_num, 
                       sticky = tk.NSEW, 
                       padx = 3, 
                       pady = 3
                       )

def manejar_click(valor):
    if valor == 'C':
        limpiar()
    elif valor == '←':
        borrar()
    elif valor == '=':
        calcular()
    elif valor == 'π':
        agregar('π')
    elif valor == 'e':
        agregar('e')
    elif valor == '^':
        agregar('^')
    elif valor in ('sin', 'cos', 'tan', 'log', 'sqrt', 'ln'):
        agregar(f'{valor}(')
    elif valor == 'x²':
        agregar('^2')
    else:
        agregar(valor)

if __name__ == "__main__":
    root = tk.Tk()
    display_var = tk.StringVar(value='0')
    crear_interfaz(root)
    root.mainloop()
