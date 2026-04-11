import tkinter
import random

ROWS = 25
COLS = 25
TITLE_SIZE = 25

WINDOW_WIDTH = TITLE_SIZE * COLS
WINDOW_HEIGHT = TITLE_SIZE * ROWS


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y



#game window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()


#center window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#initalize game
snake = Tile(5*TITLE_SIZE, 5*TITLE_SIZE) #single tile, snake's head

window.mainloop()