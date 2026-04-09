import tkinter
import random

ROWS = 25
COLS = 25
TITLE_SIZE = 25

WINDOW_WIDTH = TITLE_SIZE * COLS
WINDOW_HEIGHT = TITLE_SIZE * ROWS

#game window
window = tkinter.Tk()
window.title("Snake")
window.resizable(False, False)

window.mainloop()