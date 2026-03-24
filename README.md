# Lab 4
## Level 3
### Variant 1
Implement a ‘priority queue’ data structure based on a red-black
tree, in which a parent element has a higher priority than its right child,
or a lower or equal priority than its left child.
Operations supported by your queue:
1. Inserting an element with a given value and priority into the queue.
2. Removing and returning the element with the highest priority from the queue.
3. Iterating through the queue without modifying it.
To implement such a priority queue, you should use a separate Node class,
where each element will have two fields: value and priority. When inserting
an element into the queue, it must be placed in the correct order,
taking priority into account.
The name of the implementation file is red_black_priority_queue.py
---
## Рівень 3
### Варіант 1
Реалізуйте структуру даних "черга з пріоритетами" на основі червоно-чорного
дерева, в якому батьківський елемент має вищий пріоритет, ніж елемент справа,
або нижчий або рівний пріоритет, ніж пріоритет його лівої дитини.
Операції, які підтримує ваша черга:
1. Вставка елемента з заданим значенням та пріоритетом до черги.
2. Видалення та повернення елемента з найвищим пріоритетом з черги.
3. Перегляд черги без її зміни.
Для реалізації такої черги з пріоритетами слід використати окремий клас Node,
де кожен елемент буде мати два поля: значення та пріоритет. При вставці
елемента до черги, його потрібно розмістити у відповідному порядку з
урахуванням пріоритету.
Назва файлу реалізації - red_black_priority_queue.py
