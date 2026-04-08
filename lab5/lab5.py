import os
from collections import deque
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

class IslandAnalyzerBFS:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

        self.island_ids = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.total_islands = 0

    def count_and_mark_islands(self):
        if self.rows == 0 or self.cols == 0:
            return 0

        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] > 0 and self.island_ids[r][c] == 0:
                    self.total_islands += 1
                    self._bfs(r, c, self.total_islands)
                    
        return self.total_islands

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

                if 0 <= nr < self.rows and 0 <= nc < self.cols:
                    if self.grid[nr][nc] > 0 and self.island_ids[nr][nc] == 0:
                        self.island_ids[nr][nc] = current_id
                        queue.append((nr, nc))

    def visualize(self):
        if self.total_islands == 0:
            print("Островів не знайдено.")
            return
            
        fig, ax = plt.subplots(figsize=(8, 8))
        cmap = ListedColormap(['#1E90FF', '#FFD700'])
        
        color_mask = [[1 if self.grid[r][c] > 0 else 0 for c in range(self.cols)] for r in range(self.rows)]
        
        ax.matshow(np.array(color_mask), cmap=cmap, vmin=0, vmax=1)

        for r in range(self.rows):
            for c in range(self.cols):
                if self.island_ids[r][c] > 0:
                    ax.text(c, r, str(self.island_ids[r][c]), 
                            va='center', ha='center', 
                            color='black', fontweight='bold', fontsize=14)
                else:
                    ax.text(c, r, "0", 
                            va='center', ha='center', 
                            color='white', alpha=0.4, fontsize=10)

        ax.set_title(f"Аналіз: Знайдено {self.total_islands} островів", 
                     fontsize=16, pad=20, fontweight='bold')
        
        ax.set_xticks(np.arange(-0.5, self.cols, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, self.rows, 1), minor=True)
        ax.grid(which="minor", color="black", linestyle='-', linewidth=2)
        ax.tick_params(which="minor", bottom=False, left=False)
        ax.set_xticks([])
        ax.set_yticks([])

        plt.show()

def load_matrix_from_file(filename):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Помилка: Файл '{filename}' не знайдено!")

    grid = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, 1):
            cleaned_line = line.strip()
            if not cleaned_line:
                continue
            try:
                cleaned_line = cleaned_line.replace(',', ' ')
                row = [int(val) for val in cleaned_line.split()]
                grid.append(row)
            except ValueError:
                raise ValueError(f"Помилка формату у файлі '{filename}' на рядку {line_num}.")
                
    if grid:
        cols_count = len(grid[0])
        if any(len(row) != cols_count for row in grid):
            raise ValueError("Помилка: Матриця у файлі не є прямокутною.")

    return grid


if __name__ == "__main__":
    file_name = r"C:\Users\Legion\Documents\uni\2\alg\lab5\map.txt" 
    
    try:
        print(f"Завантаження карти з файлу '{file_name}'...")
        file_grid = load_matrix_from_file(file_name)
        
        analyzer = IslandAnalyzerBFS(file_grid)
        total = analyzer.count_and_mark_islands()
        
        print(f"Алгоритм завершив роботу. Знайдено островів: {total}")
        analyzer.visualize()
        
    except Exception as e:
        print(f"\nEXCEPTION: {e}")