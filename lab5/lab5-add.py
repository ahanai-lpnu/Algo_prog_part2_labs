import tkinter as tk
from tkinter import filedialog, messagebox
from collections import deque
import copy

class IslandGame:
    def __init__(self, root, initial_grid):
        self.root = root
        self.root.title("Іграшка (зате з BFS!!!)")
        self.root.configure(bg="#DDDDDD")

        self.initial_grid = copy.deepcopy(initial_grid)
        self.grid = copy.deepcopy(initial_grid)
        
        self.rows = len(self.grid)
        self.cols = len(self.grid[0]) if self.rows > 0 else 0
        self.island_ids = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.total_islands = 0

        self._setup_ui()
        self.recalculate_and_draw()

    def _setup_ui(self):
        self.status_label = tk.Label(
            self.root, text="Знайдено островів: ?", 
            font=("Helvetica", 18, 'bold'), bg="#DDDDDD", fg="#8C720A"
        )
        self.status_label.pack(pady=(20, 10))

        self.grid_frame = tk.Frame(self.root, bg="black", bd=2)
        self.grid_frame.pack(padx=20, pady=10)

        self._build_grid_buttons()

        self.control_frame = tk.Frame(self.root, bg="#DDDDDD")
        self.control_frame.pack(pady=15)

        load_btn = tk.Button(
            self.control_frame, text="Завантажити карту з файлу", 
            font=("Helvetica", 12, "bold"), bg="#338FCD", fg="white",
            activebackground="#1984CB", activeforeground="white",
            command=self.load_from_file
        )
        load_btn.grid(row=0, column=0, padx=10)

        reset_btn = tk.Button(
            self.control_frame, text="Скинути (рісет)", 
            font=("Helvetica", 12, "bold"), bg="#E74C3C", fg="white",
            activebackground="#C0392B", activeforeground="white",
            command=self.reset_grid
        )
        reset_btn.grid(row=0, column=1, padx=10)

    def _build_grid_buttons(self):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        self.buttons = []
        for r in range(self.rows):
            row_buttons = []
            for c in range(self.cols):
                btn = tk.Button(
                    self.grid_frame, width=4, height=2, 
                    font=("Helvetica", 12, "bold"), relief=tk.FLAT,
                    command=lambda r=r, c=c: self.toggle_cell(r, c)
                )
                btn.grid(row=r, column=c, padx=1, pady=1)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def load_from_file(self):
        file_path = filedialog.askopenfilename(
            title="Оберіть текстовий файл з матрицею",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        
        if not file_path:
            return

        try:
            new_grid = []
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    cleaned_line = line.strip()
                    if not cleaned_line:
                        continue
                    cleaned_line = cleaned_line.replace(',', ' ')
                    row = [1 if int(val) > 0 else 0 for val in cleaned_line.split()]
                    new_grid.append(row)

            if not new_grid:
                raise ValueError("Файл порожній або не містить чисел.")

            cols_count = len(new_grid[0])
            if any(len(row) != cols_count for row in new_grid):
                raise ValueError("Матриця не є прямокутною (різна довжина рядків).")

            self.initial_grid = copy.deepcopy(new_grid)
            self.grid = copy.deepcopy(new_grid)
            self.rows = len(self.grid)
            self.cols = len(self.grid[0])
            
            self._build_grid_buttons()
            self.recalculate_and_draw()

        except Exception as e:
            messagebox.showerror("Помилка завантаження", f"Не вдалося прочитати файл:\n{str(e)}")

    def toggle_cell(self, r, c): # самий сок допки
        self.grid[r][c] = 1 if self.grid[r][c] == 0 else 0
        self.recalculate_and_draw()

    def reset_grid(self):
        self.grid = copy.deepcopy(self.initial_grid)
        self.recalculate_and_draw()

    def recalculate_and_draw(self):
        self.island_ids = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.total_islands = 0

        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 1 and self.island_ids[r][c] == 0:
                    self.total_islands += 1
                    self._bfs(r, c, self.total_islands)

        self.status_label.config(text=f"Знайдено островів: {self.total_islands}")
        
        for r in range(self.rows):
            for c in range(self.cols):
                btn = self.buttons[r][c]
                if self.grid[r][c] == 1:
                    btn.config(
                        text=str(self.island_ids[r][c]), 
                        bg="#FFD700", fg="black", activebackground="#F39C12"
                    )
                else:
                    btn.config(
                        text="0", 
                        bg="#1E90FF", fg="#87CEFA", activebackground="#2980B9"
                    )

    def _bfs(self, start_r, start_c, current_id):
        queue = deque([(start_r, start_c)])
        self.island_ids[start_r][start_c] = current_id

        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

        while queue:
            curr_r, curr_c = queue.popleft()
            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc
                if (0 <= nr < self.rows and 0 <= nc < self.cols and 
                    self.grid[nr][nc] == 1 and self.island_ids[nr][nc] == 0):
                    self.island_ids[nr][nc] = current_id
                    queue.append((nr, nc))

if __name__ == "__main__":
    default_matrix = [
        [1, 1, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0],
        [1, 0, 0, 1, 0, 1, 0],
        [1, 0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1]
    ]

    root = tk.Tk()
    app = IslandGame(root, default_matrix)
    root.mainloop()