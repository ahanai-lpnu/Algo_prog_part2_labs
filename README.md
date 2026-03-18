# Lab 1
### Option 3
Write a function that takes an unordered array of integers and returns the length
of the longest peak subsequence. To form a peak subsequence,
at least 3 numbers are required. A peak subsequence is defined as a sequence
of numbers that starts with a smaller number, followed by a number strictly greater
than the previous one, until they reach the peak (the maximum value in
the subsequence). All values after reaching the peak must always be smaller
than their predecessor. For example, a peak sequence might look like this:
1 7 2
Where 7 is the peak of the sequence
1 2 3 is not a peak sequence (no left part)
3 2 1 – is also not a peak sequence (no right part)
-1 -5 -1 – is also not a peak sequence (we need to find the peak, not a trough)
There may be several peak subsequences in the array; it is necessary to find the length
of the longest one
Example
For the input array: 1, 3, 5, 4, 2, 8, 3, 7, the longest peak
subsequence found has a length of 5 - 1, 3, 5, 4, 2
To verify the correctness of the implemented algorithm, use the
`unittest` library and test the following scenarios:
all elements of the array are sorted in ascending order,
sorted in descending order,
an array with 2 elements,
contains no peak sequences,
contains 3 peak sequences

---

### Варіант 3
Напишіть функцію, яка приймає невпорядкований масив цілих чисел і повертає довжину
найдовшої пікової підпослідовностію Для формування пікової підпослідовності
необхідно мінімум 3 числа. Пікова підпослідовність визначається як послідовність
чисел, яка починається з меншого числа, після чого наступне число строго більше
попереднього, поки вони не досягнуть вершини (максимального значення у
підпослідовності). Всі значення після досягнення вершини мають бути завжди меншими
від попередника. Наприклад, пікова послідовність може мати вигляд:
1 7 2
Де 7 - є вершиною послідовності
1 2 3 - не є піковою послідовністю (немає лівої частки)
3 2 1 - також не є піковою полідовністю (немає правої частки)
-1 -5 -1 - теж не є піковою послідовністю (необхідно знайти вершину, а не впадину)
У масиві може бути декілька пікових підпослідовностей, необхідно знайти довжину
максимальної
Приклад
Для вхідного масиву: 1, 3, 5, 4, 2, 8, 3, 7, знайдена найдовша пікова
підпослідовність має довжину 5 - 1, 3, 5, 4, 2
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку
`unittest` та перевірити сценарії коли:
всі елементи масиву посортовані за зростанням,
посортовані за спаданням,
масив з 2х елементів,
не містять пікових підпослідовностей,
містять 3 пікові послідовності
