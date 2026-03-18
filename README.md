# Lab 2
## Level 3
### Option 3
Farmer John has built a new long cattle pen consisting of N (2 <= N <= 100,000) sections.
The sections are arranged in a straight line at positions x1, ..., xN (0 <= x-i <= 1 000 000
000).
His C (2 <= C <= N) cows do not like the new building and become aggressive towards one another
when placed in adjacent stalls. To avoid a situation where the cows might cause
harm to one another, the farmer wants to place the aggressive cows in stalls in such a way that
the minimum distance between any two of them is as large as possible.
What is the largest possible minimum distance?
Function input:
N = 5 C = 3
free_sections = `[1, 2, 8, 4, 9]
Result 3
Explanation: The farmer has 5 cows, 3 of which are aggressive. They can be placed in stalls 1, 4 and 8
or 1, 4 and 9. Thus, the minimum value of the maximum distance is 3
Hint:
Since we have at least two cows, the best we can do is place
them in the pen in the first free stall and at the end
To verify the implementation of the algorithm, use
the unittest library and test your function using the examples given above

---

### Варіант 3
Фермер Джон побудував новий довгий загін для худоби, з N (2 <= N <= 100,000) секцій.
Секції розташовуються уздовж прямої лінії в положеннях x1, ..., xN (0 <= x-i <= 1 000 000
000).
Його C (2 <= C <= N) корів не люблять нову будівлю і стають агресивними одна до одної,
коли вони поставлені в сусідні стійла. Щоб уникнути ситуації, коли корови можуть заподіяти
шкоду одна одній, фермер хоче розташувати агресивних корів у стійлах таким чином, щоб
мінімальна відстань між будь-якими з них була настільки великою, наскільки це можливо.
Яка найбільша мінімальна відстань?
Вхідні дані функції:
N = 5 С = 3
free_sections = `[1, 2, 8, 4, 9]
Результат 3
Пояснення: У фермера є 5 корів, з яких 3 агресивні. Їх можна роташувати в стійлах 1, 4 та 8
або 1,4, 9. Таким чином мінімальне значення максимальної дистанції становить 3
Підказка:
Оскільки у нас є щонайменше дві корови, найкраще, що ми можемо зробити, це розташувати
їх у загоні у першому вільному стійлі і в кінці
Для перевірки виконання роботи реалізованого алгоритму слід використати
бібліотеку unittest та перевірити роботу вашої функції на прикладах, наведених вище
