RED = 1
BLACK = 0

class Node:
    __slots__ = ['value', 'priority', 'color', 'parent', 'left', 'right']

    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.color = RED
        self.parent = None
        self.left = None
        self.right = None

class RedBlackPriorityQueue:
    def __init__(self):
        self.TNULL = Node(None, None)
        self.TNULL.color = BLACK
        self.root = self.TNULL

    def peek(self):
        if self.root == self.TNULL:
            return None
        
        node = self.root
        while node.left != self.TNULL:
            node = node.left
        return node.value, node.priority

    def insert(self, value, priority):
        new_node = Node(value, priority)
        new_node.parent = None
        new_node.left = self.TNULL
        new_node.right = self.TNULL

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if new_node.priority >= x.priority:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y is None:
            self.root = new_node
        elif new_node.priority >= y.priority:
            y.left = new_node
        else:
            y.right = new_node

        if new_node.parent is None:
            new_node.color = BLACK
            return
        if new_node.parent.parent is None:
            return

        self._insert_fixup(new_node)

    def pop(self):
        if self.root == self.TNULL:
            raise IndexError("Спроба вилучення з порожньої черги (Underflow)")
        
        z = self.root
        while z.left != self.TNULL:
            z = z.left
            
        result_value, result_priority = z.value, z.priority
        y_original_color = z.color
        x = z.right

        self._rb_transplant(z, z.right)

        if y_original_color == BLACK:
            self._delete_fixup(x)
            
        return result_value, result_priority

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def _insert_fixup(self, k):
        while k.parent is not None and k.parent.color == RED:
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == RED:
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self._left_rotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self._right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == RED:
                    u.color = BLACK
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self._right_rotate(k)
                    k.parent.color = BLACK
                    k.parent.parent.color = RED
                    self._left_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = BLACK

    def _rb_transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _delete_fixup(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self._right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self._right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self._left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = BLACK