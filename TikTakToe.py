import tkinter as tk
from tkinter import ttk

class TikTakToe:  
    def __init__(self):
        self.player = 'X'
        self.root = tk.Tk()
        self.style =ttk.Style()
        self.configure_style()
        self.build_board()
        self.build_buttons()
        self.build_labels()
        self.build_menu()
        self.root.mainloop()
        
    def configure_style(self):
        self.style.configure('GameButton.TButton', font='normal 20 bold', padding=5)
        self.style.configure('PlayerLabel.TLabel', font='normal 20', padding=5, anchor='center')
        self.style.configure('GameRunsLabel.TLabel', font='normal 20', padding=5, foreground='green', anchor='center')
        self.style.configure('GameOverLabel.TLabel', font='normal 20 bold', padding=5, foreground='red', anchor='center')
        
    def build_board(self):
        self.root.title("Tik Tak Toe")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

    def build_buttons(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            self.root.grid_columnconfigure(i, weight=1)
            for j in range(3):
                button = ttk.Button(self.root, text='', style='GameButton.TButton',
                                   command=lambda i=i, j=j: self.on_gamebutton_click(i, j))
                button.grid(row=i, column=j, sticky='nsew')
                self.buttons[i][j] = button

    def on_gamebutton_click(self, i, j):
        self.buttons[i][j].config(text=self.player, state='disabled')
        if self.check_winner(): 
            return
        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'
        self.update_Playerlabel()
        
    def build_labels(self):
        self.playerlabel = ttk.Label(self.root, text="Spieler "+self.player+" ist dran", style='PlayerLabel.TLabel')
        self.playerlabel.grid(row=3, column=0, columnspan=3, sticky='nsew')
        self.statuslabel = ttk.Label(self.root, text="Das Spiel läuft!", style='GameRunsLabel.TLabel')
        self.statuslabel.grid(row=4, column=0, columnspan=3, sticky='nsew') 
    
    def update_Playerlabel(self):
        self.playerlabel.config(text="Spieler "+self.player+" ist dran")

    def update_SiegStatuslabel(self):
        self.statuslabel.config(text=self.player+" hat gewonnen!", style='GameOverLabel.TLabel')
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != '':
                self.update_SiegStatuslabel()
                return True
            if self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != '':
                self.update_SiegStatuslabel()
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != '':
            self.update_SiegStatuslabel()
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != '':
            self.update_SiegStatuslabel()
            return True
        if all(self.buttons[i][j]['text'] != '' for i in range(3) for j in range(3)):
            self.statuslabel.config(text="Unentschieden!", style='GameOverLabel.TLabel')
            return True

    def build_menu(self):
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.menu.add_command(label='Neues Spiel', command=self.on_newgame_click)
        self.menu.add_separator()
        self.menu.add_command(label="Verlassen", command=self.exit_game)

    def on_newgame_click(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state='normal')
        self.player = 'X'
        self.update_Playerlabel()
        self.statuslabel.config(text="Das Spiel läuft!", style='GameRunsLabel.TLabel')

    def exit_game(self):
        self.root.quit()

if __name__ == "__main__":
    TikTakToe()