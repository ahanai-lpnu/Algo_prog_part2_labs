class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def _my_max(a, b):
        return a if a > b else b

    def _dfs(self, node: 'BinaryTree'):
        if node is None:
            return 0, 0

        left_height, left_diam = self._dfs(node.left)
        right_height, right_diam = self._dfs(node.right)

        current_diam = left_height + right_height

        max_child_diam = self._my_max(left_diam, right_diam)
        max_diam = self._my_max(max_child_diam, current_diam)
        
        current_height = self._my_max(left_height, right_height) + 1
        
        return current_height, max_diam

    def get_diameter(self):
        _, final_diameter = self._dfs(self)
        return final_diameter