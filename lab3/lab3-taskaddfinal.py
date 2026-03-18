import os

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @classmethod
    def build_regular_from_postorder(cls, postorder: list):
        if not postorder:
            return None
        
        root_val = postorder[-1]
        if root_val in ('N', 'None', 'null'):
            return None
            
        root = cls(root_val)
        remaining = postorder[:-1]
        
        if remaining:
            mid = len(remaining) // 2
            root.left = cls.build_regular_from_postorder(remaining[:mid])
            root.right = cls.build_regular_from_postorder(remaining[mid:])
            
        return root

    def _get_height(self) -> int:
        left_height = self.left._get_height() if self.left else 0
        if left_height == -1:
            return -1
        right_height = self.right._get_height() if self.right else 0
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    def is_tree_balanced(self) -> bool:
        return self._get_height() != -1

    def print_tree(self):
        def display_aux(n):
            if n is None:
                return [], 0, 0, 0
                
            s = str(n.value)
            u = len(s)
            
            if n.right is None and n.left is None:
                return [s], u, 1, u // 2

            if n.right is None:
                left, n_w, n_h, n_m = display_aux(n.left)
                first_line = (n_m + 1) * " " + (n_w - n_m - 1) * "_" + s
                second_line = n_m * " " + "/" + (n_w - n_m - 1 + u) * " "
                shifted = [line + u * " " for line in left]
                return [first_line, second_line] + shifted, n_w + u, n_h + 2, n_m + 1 + u // 2

            if n.left is None:
                right, m_w, m_h, m_m = display_aux(n.right)
                first_line = s + m_m * "_" + (m_w - m_m) * " "
                second_line = (u + m_m) * " " + "\\" + (m_w - m_m - 1) * " "
                shifted = [u * " " + line for line in right]
                return [first_line, second_line] + shifted, m_w + u, m_h + 2, u // 2

            left, n_w, n_h, n_m = display_aux(n.left)
            right, m_w, m_h, m_m = display_aux(n.right)
            
            first_line = (n_m + 1) * " " + (n_w - n_m - 1) * "_" + s + m_m * "_" + (m_w - m_m) * " "
            second_line = n_m * " " + "/" + (n_w - n_m - 1 + u + m_m) * " " + "\\" + (m_w - m_m - 1) * " "

            if n_h < m_h:
                left += [n_w * " "] * (m_h - n_h)
            elif m_h < n_h:
                right += [m_w * " "] * (n_h - m_h)

            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
            return lines, n_w + m_w + u, max(n_h, m_h) + 2, n_w + u // 2

        lines, *_ = display_aux(self)
        for line in lines:
            print(line)

    def print_top_view(self):
        canvas = {}

        def get_depth(node):
            if not node: return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1

        depth = get_depth(self)
        initial_dy = 2 ** max(1, depth - 1)
        dx = 6 

        def draw(node, x, y, dy, is_left_side, is_root=False):
            if not node:
                return
            
            canvas[(x, y)] = str(node.value)

            if is_root:
                if node.left:
                    for i in range(2, dx): canvas[(x - i, y)] = "-"
                    draw(node.left, x - dx, y, dy, True, False)
                if node.right:
                    for i in range(2, dx): canvas[(x + i, y)] = "-"
                    draw(node.right, x + dx, y, dy, False, False)
            else:
                next_dy = max(1, dy // 2)
                if is_left_side:
                    if node.left:
                        canvas[(x - dx // 2, y - dy // 2)] = "\\"
                        draw(node.left, x - dx, y - dy, next_dy, True, False)
                    if node.right:
                        canvas[(x - dx // 2, y + dy // 2)] = "/"
                        draw(node.right, x - dx, y + dy, next_dy, True, False)
                else:
                    if node.left:
                        canvas[(x + dx // 2, y - dy // 2)] = "/"
                        draw(node.left, x + dx, y - dy, next_dy, False, False)
                    if node.right:
                        canvas[(x + dx // 2, y + dy // 2)] = "\\"
                        draw(node.right, x + dx, y + dy, next_dy, False, False)

        draw(self, 0, 0, initial_dy, True, True)

        if not canvas:
            return

        min_x = min(x for x, y in canvas.keys())
        max_x = max(x + len(val) for (x, y), val in canvas.items())
        min_y = min(y for x, y in canvas.keys())
        max_y = max(y for x, y in canvas.keys())

        grid = [[' ' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]

        for (x, y), val in canvas.items():
            for i, char in enumerate(val):
                grid[y - min_y][x - min_x + i] = char

        for row in grid:
            line = "".join(row).rstrip()
            if line:
                print(line)

if __name__ == "__main__":
    filename = r'C:\Users\Legion\Documents\uni\2\alg\lab3\postik.txt'
    
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = f.read().split()
            
        root = BinaryTree.build_regular_from_postorder(data)
        
        if root:
            root.print_tree()
            print()
            root.print_top_view()