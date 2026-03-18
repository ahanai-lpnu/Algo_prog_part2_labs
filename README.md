# Lab 3
## Level 3
For all tasks, you should write tests using the `unittest` library. Your
project should be organised into separate folders for the application code and tests (`src` and
`test` respectively).
When writing code, adhere to the PEP 8 standard, which defines rules
for formatting Python code, such as indentation, line length, variable naming
and so on. To improve code readability, you should format your code using
`Black`
### Option 3
For a given binary tree, implement a function that calculates and returns
the value of the maximum diameter in the binary tree — the greatest distance between
two leaves. The maximum diameter in a binary tree defines the greatest
distance between any pair of leaves (terminal nodes) in the tree. The diameter
is measured as the number of edges that must be traversed to get from one leaf
to another. The maximum diameter does not necessarily have to include the root
node
Suppose you are given a binary tree of the following form:
```
1
/ \
3 2
/ \
7 4
/ \
8 5
/ \
9 6
```

For this tree, the maximum diameter is 6: `9 -> 8 -> 7 -> 3 -> 4 -> 5
-> 6` – to go from leaf 9 to leaf 6, you must traverse 6 edges.
The function you have implemented, `binary_tree_diameter(tree: BinaryTree) -> int`, takes
the root of the binary tree as input and returns the maximum diameter of the tree.
The class describing a binary tree (and any tree node) looks like this:
```
class BinaryTree:
def __init__(self, value, left=None, right=None):
self.value = value
self.left = left
self.right = right
```
---
### Варіант 3
Для заданого бінарного дерева реалізуйте функцію, яка обчислює та повертає
значення максимального діаметра у бінарному дереві - найвіддаленішу відстань між
двома листками. Максимальний діаметр у бінарному дереві визначає найбільшу
відстань між будь-якою парою листків (кінцевих вузлів) у дереві. Діаметр
вимірюється як кількість ребер, які потрібно пройти, щоб дістатися одного листка
від іншого. Максимальний діаметр не обов'язково має включати в себе кореневий
вузол
Нехай у вас задане бінарне дерево такого вигляду:
```
1
/ \
3 2
/ \
7 4
/ \
8 5
/ \
9 6
```

Для даного дерева максимальний діаметр становить 6: `9 -> 8 -> 7 -> 3 -> 4 -> 5
-> 6` - для проходження від листка 9 до листка 6 слід пройти 6 ребер.
Реалізована вами функція `binary_tree_diameter(tree: BinaryTree) -> int` отримує
на вхід корінь бінарного дерева та повертає максимальний діаметр дерева.
Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:
```
class BinaryTree:
def __init__(self, value, left=None, right=None):
self.value = value
self.left = left
self.right = right
```
Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів
з бінарного дерева. У тесті ви можете створити достатню кількість елементів
класу `BinaryTree` наступним чином:
```
root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
```
