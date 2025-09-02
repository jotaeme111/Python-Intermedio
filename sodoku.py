import tkinter as tk
from  tkinter import messagebox
import random

class SodokuGame:
    #Inicicializando la ventana principal
    def __init__(self,master):
        self.master = master
        master.title("Sodoku")
        master.geometry("600x700")

    #definir la cantidad de espacios vacios para regular el nivel de dificultad

        self.boards = {
            "Basico": 40,
            "Intermedio": 50,
            "Avanzado": 60
        }

    #Definir los estados de cada uno de los tableros

        self.original_board = None
        self.current_board = None
        self.solution_board = None

        self.errors = 0
        self.max_errors = 4
        self.selected_cell = (None,None) #Celda que seleccionamos a la hora de jugar

        self.level_frame = tk.Frame(master)
        self.level_frame.pack(pady=10)

        tk.Button(self.level_frame, text="Basico", command=lambda:self.start_game("Basico"),width=10, height=2).pack(side=tk.LEFT, padx=5)
        tk.Button(self.level_frame, text="Intermedio", command= lambda:self.start_game("Intermedio"),width=10, height=2).pack(side=tk.LEFT, padx=5)
        tk.Button(self.level_frame, text="Avanzado", command= lambda:self.start_game("Avanzado"),width=10, height=2).pack(side=tk.LEFT, padx=5)

        #Etiqueta para mostrar los errores

        self.error_label = tk.Label(master, text=f'{self.errors}/{self.max_errors}', font=("Arial,14"))
        self.error_label.pack(pady=10)

        # Marco principal para el tablero de SODOKU
        self.sodoku_frame = tk.Frame(master, bd=5, relief="ridge")
        self.sodoku_frame.pack(padx=20,pady=20)

        self.cells = {}  #Se crea un diccionario para almacenar cada una de las entradas de TKINTER

        # Crear una cuadricula de 9 x 9

        for r in range(9):
            for c in range(9):
                entry = tk.Entry(self.sodoku_frame, width=3, font=('Arial',24),justify="center",relief="solid",bd=1)

                entry.grid(row=r, column=c, ipadx=5, ipady=5)

                #Haciendo un marco para las subcuadriculasd de 3 x 3 
                if( r + 1) % 3 == 0 and r !=8:
                    entry.grid(pady=(0,5))
                if (c + 1) % 3 == 0 and c != 8:
                    entry.grid(padx=(0,5))
                self.cells[(r,c)] = entry

                # Vincalacion del evento con el click de cada celda
                entry.bind("<Button-1>",lambda event, r=r,c=c: self.on_cell_click(r,c))

        #Frame para los botones de juego
        self.control_frame = tk.Frame(master)
        self.control_frame.pack(pady=10)

        #Botones para ingresar numero y borrar
        self.number_buttons = []
        for i in range(1,10):
            button = tk.Button(self.control_frame, text=str(i), width=4,height=2, command=lambda num=i: self.enter_number(num))
            button.pack(side=tk.LEFT,padx=2)
            self.number_buttons.append(button)

        self.clear_button = tk.Button(self.control_frame, text="Borrar",width=6, height=2, command=self.clear_cell)
        self.clear_button.pack(pady=10)

        self.restart_button = tk.Button(master, text="Jugar de nuevo", command=self.reset_game, state=tk.DISABLED, width=15, height=2)
        self.restart_button.pack(pady=10)


    def start_game(self, level):

        self.errors = 0
        self.error_label.config(text=f'Errores: {self.errors}/{self.max_errors}')

        #Generar un nuevo tablero de SODOKU segun el nivel seleccionado

        self.generate_sudoku_puzzle(self.boards[level])

        self.populate_board()
        self.restart_button.config(state=tk.NORMAL)
        self.enable_input_buttons()

    def populate_board(self):
        # Rellena el tablero segun el nivel de juego


        for r in range(9):
            for c in range(9):
                value = self.current_board[r][c]
                entry = self.cells[(r,c)]
                entry.config(state=tk.NORMAL)
                entry.delete(0, tk.END)
                if value != 0:
                    entry.insert(0, str(value))
                    entry.config(state='readonly',fg='blue')
                else:
                    entry.config(fg='black')
                entry.config(bg='white')

    def on_cell_click(self,r,c):
        if self.original_board is None:
            return
        if self.selected_cell[0] is not None:
            prev_r , prev_c = self.selected_cell

            if(prev_r,prev_c) != (r,c):
                self.cells[(prev_r,prev_c)].config(bg='white')
        self.selected_cell = (r,c)
        self.cells[(r,c)].config(bg="lightblue")


    def enter_number(self,num):
        if self.selected_cell[0] is not None:
            r, c = self.selected_cell
            if self.original_board[r][c] == 0:
                entry = self.cells[(r,c)]
                entry.delete(0, tk.END)
                entry.insert(0, str(num))
                self.check_number(r,c,num)# Falta hacer este metodo
            else:
                messagebox.showwarning("Sodoku", "No puedes cambiar los numeros iniciales del SODOKU")

    def clear_cell(self):
        if self.selected_cell[0] is not None:
            r, c = self.selected_cell
            if self.original_board[r][c] == 0:
                entry = self.cells[(r,c)]
                entry.delete(0, tk.END)
                self.current_board[r][c] = 0
                entry.config(fg="black")

    def check_number(self, r,c,num):
        # Verificar si el numero ingresado es correcto

        if self.solution_board[r][c] == num:
            self.current_board[r][c] = num
            self.cells[(r,c)].config(fg="green")
            if self.is_game_over():
                self.game_won()
            else:
                self.errors += 1
                self.error_label.config(text=f'Errores: {self.errors}/{self.max_errors}')
                self.cells[(r,c)].config(fg="red")
                if self.errors >= self.max_errors:
                    self.game_lost()

    def is_game_over(self):
        for r in range(9):
            for c in range(9):
                if self.current_board[r][c] == 0:
                    return False
        return True

    def game_won(self):
        messagebox.showinfo("Sodoku","!Felicidades, gano el juego!")
        self.disable_input_buttons()
        self.restart_button.config(state=tk.NORMAL)

    def game_lost(self):
        messagebox.showinfo("Sodoku",f'Haz superado los {self.max_errors} errores.... :..(')
        self.disable_input_buttons()
        self.show_solution()
        self.restart_button.config(state=tk.NORMAL)

    def show_solution(self):

        for r in range(9):
            for c in range(9):
                entry = self.cells[(r,c)]
                entry.config(state=tk.NORMAL)
                entry.delete(0, tk.END)
                entry.insert(0, str(self.solution_board[r][c]))
                entry.config(fg='purple', state="readonly")

    def disable_input_buttons(self):
        for button in self.number_buttons:
            button.config(state=tk.DISABLED)
        self.clear_button.config(state=tk.DISABLED)

        for r in range(9):
            for c in range(9):
                self.cells[(r,c)].config(state="readonly")

    def enable_input_buttons(self):
        for button in self.number_buttons:
            button.config(state=tk.NORMAL)
        self.clear_button.config(state=tk.NORMAL)
        for r in range(9):
            for c in range(9):
                if self.original_board[r][c] == 0:
                    self.cells[(r,c)].config(state=tk.NORMAL)

    def reset_game(self):
        self.errors = 0
        self.error_label.config(text=f'Errores: {self.errors}/{self.max_errors}')
        self.original_board = None
        self.current_board = None
        self.solution_board = None
        self.selected_cell = (None,None)
        self.disiable_input_buttons()
        self.restart_button.config(state=tk.DISABLED)

        for r in range(9):
            for c in range(9):
                entry = self.cells[(r,c)]
                entry.config(state=tk.NORMAL)
                entry.delete(0,tk.END)
                entry.config(bg="white", fg="black")

    def find_empty(self,board):
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0 :
                    return (r,c)
                
        return None
    

    #Metodo de verificacion si el numero ingresado es correcto
    def is_valid(self,board,num,pos):
        row, col = pos

         #revisar cada fila
        for c in range(9):
            if board[row][c] == num and col != c:
                return False
        for r in range(9):
            if board[r][col] == num and row != r:
                return False
            
        box_x = col // 3
        box_y = row // 3

        for r in range(box_y * 3, box_y * 3 + 3):
            for c in range (box_x * 3, box_x * 3 + 3):
                if board[r][c] == num and (r,c) != pos:
                    return False
        return True
        
     
         
    # Esto es un BACK-TRACKING       
    def solve_sudoku(self,board):
        find = self.find_empty(board)

        if not find:
            return True
        else:
            row,col = find

        for i in range(1,10):
            if self.is_valid(board,i,(row,col)):
                board[row][col] = i

                if self.solve_sudoku(board):
                    return True  
                board[row][col] = 0
        
        return False

    def generate_sudoku_puzzle(self,num_cells_to_remove):

        full_board = [[0 for _ in range(9)] for _ in range(9)]  #Crea un tablero completamente vacio

        #Necesito llenar el tablero de forma aleatoria respetando las reglas

        self._fill_board_randomly(full_board)

        self.solution_board = [row[:] for row in full_board] #Guardo una copia del tablero resuelto
        
        puzzle_board = [row[:] for row in self.solution_board]

        all_cells = [(r,c) for r in range(9) for c in range(9)]
        random.shuffle(all_cells)

        removed_count = 0

        for r,c in all_cells:
            if removed_count < num_cells_to_remove:
                puzzle_board[r][c] = 0
                removed_count += 1

            else:
                break

        self.original_board = [row[:] for row in puzzle_board]
        self.current_board = [row[:] for row in puzzle_board]

    def _fill_board_randomly(self,board):

        find = self.find_empty(board)
        if not find:
            return True # Existe un tablero lleno  y valido
        
        else:
            row, col = find #Otro uso del backtracking

        numbers = list(range(1,10))
        random.shuffle(numbers)

        for num in numbers:
            if self.is_valid(board,num,(row,col)):
                board[row][col] = num

                if self._fill_board_randomly(board):
                    return True
                
                board[row][col] = 0
        return False
    
if __name__ == "__main__":
    root = tk.Tk()
    game = SodokuGame(root)
    root.mainloop()
        