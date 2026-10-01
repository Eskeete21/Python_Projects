"""Snake - a classic snake game using only Python's standard library (tkinter).

Controls:
    Arrow keys / WASD  - steer
    Space              - pause / resume
    R                  - restart
    Esc                - quit
"""

import random
import tkinter as tk

CELL = 20            # pixel size of one grid cell
COLS, ROWS = 30, 20  # grid size
BASE_DELAY = 110     # ms per tick (gets faster as you score)
MIN_DELAY = 55

BG = "#14181d"
GRID = "#1b2027"
SNAKE_HEAD = "#7ee787"
SNAKE_BODY = "#3fb950"
FOOD = "#ff6b6b"
TEXT = "#e6edf3"

DIRECTIONS = {
    "Up": (0, -1), "w": (0, -1),
    "Down": (0, 1), "s": (0, 1),
    "Left": (-1, 0), "a": (-1, 0),
    "Right": (1, 0), "d": (1, 0),
}


class SnakeGame:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Snake")
        root.resizable(False, False)
        root.configure(bg=BG)

        self.score_label = tk.Label(root, text="", bg=BG, fg=TEXT,
                                    font=("Helvetica", 14, "bold"))
        self.score_label.pack(pady=(8, 4))

        self.canvas = tk.Canvas(root, width=COLS * CELL, height=ROWS * CELL,
                                bg=BG, highlightthickness=0)
        self.canvas.pack(padx=10, pady=(0, 10))

        root.bind("<Key>", self.on_key)
        self.high_score = 0
        self.reset()
        self.tick()

    def reset(self):
        cx, cy = COLS // 2, ROWS // 2
        self.snake = [(cx, cy), (cx - 1, cy), (cx - 2, cy)]  # head first
        self.direction = (1, 0)
        self.queue = []  # buffered turns so quick key presses aren't lost
        self.score = 0
        self.paused = False
        self.game_over = False
        self.food = self.place_food()
        self.draw()

    def place_food(self):
        free = [(x, y) for x in range(COLS) for y in range(ROWS)
                if (x, y) not in self.snake]
        return random.choice(free) if free else None

    def on_key(self, event):
        key = event.keysym
        key = key.lower() if len(key) == 1 else key

        if key == "Escape":
            self.root.destroy()
        elif key == "r":
            self.reset()
        elif key == "space" and not self.game_over:
            self.paused = not self.paused
            self.draw()
        elif key in DIRECTIONS and len(self.queue) < 3:
            new = DIRECTIONS[key]
            last = self.queue[-1] if self.queue else self.direction
            # ignore reversing into yourself or repeating the same direction
            if new != last and new != (-last[0], -last[1]):
                self.queue.append(new)

    def tick(self):
        if not self.game_over and not self.paused:
            self.step()
            self.draw()
        delay = max(MIN_DELAY, BASE_DELAY - self.score * 3)
        self.root.after(delay, self.tick)

    def step(self):
        if self.queue:
            self.direction = self.queue.pop(0)

        dx, dy = self.direction
        hx, hy = self.snake[0]
        head = (hx + dx, hy + dy)

        eating = head == self.food
        # the tail moves out of the way unless we're growing
        body = self.snake if eating else self.snake[:-1]

        if not (0 <= head[0] < COLS and 0 <= head[1] < ROWS) or head in body:
            self.game_over = True
            self.high_score = max(self.high_score, self.score)
            return

        self.snake.insert(0, head)
        if eating:
            self.score += 1
            self.food = self.place_food()
            if self.food is None:  # board full - you win
                self.game_over = True
                self.high_score = max(self.high_score, self.score)
        else:
            self.snake.pop()

    def draw_cell(self, x, y, color, inset=1):
        self.canvas.create_rectangle(
            x * CELL + inset, y * CELL + inset,
            (x + 1) * CELL - inset, (y + 1) * CELL - inset,
            fill=color, outline="")

    def draw(self):
        c = self.canvas
        c.delete("all")

        for x in range(1, COLS):
            c.create_line(x * CELL, 0, x * CELL, ROWS * CELL, fill=GRID)
        for y in range(1, ROWS):
            c.create_line(0, y * CELL, COLS * CELL, y * CELL, fill=GRID)

        if self.food:
            fx, fy = self.food
            c.create_oval(fx * CELL + 3, fy * CELL + 3,
                          (fx + 1) * CELL - 3, (fy + 1) * CELL - 3,
                          fill=FOOD, outline="")

        for i, (x, y) in enumerate(self.snake):
            self.draw_cell(x, y, SNAKE_HEAD if i == 0 else SNAKE_BODY)

        self.score_label.config(
            text=f"Score: {self.score}     Best: {self.high_score}")

        if self.game_over:
            self.overlay("Game Over", "Press R to play again")
        elif self.paused:
            self.overlay("Paused", "Press Space to resume")

    def overlay(self, title, subtitle):
        w, h = COLS * CELL, ROWS * CELL
        self.canvas.create_text(w // 2, h // 2 - 16, text=title, fill=TEXT,
                                font=("Helvetica", 28, "bold"))
        self.canvas.create_text(w // 2, h // 2 + 20, text=subtitle, fill=TEXT,
                                font=("Helvetica", 13))


if __name__ == "__main__":
    root = tk.Tk()
    SnakeGame(root)
    root.mainloop()