# Задача

Реализация алгоритма бинарного поиска. Найти индекс искомого числа за O(logN).

# Решение
Создано три метода:
+ метод ввода целочисленных значений
+ метод формирования списка из неповторяющихся чисел в порядке возрастания
+ собственно метод бинарного поиска

# Тесты на время выполнения программы

Тест проводился на поиск элемента, который стоит последним в списке.

_Количество элементов:_ ______________10___100__1000____10 000___100 000___1 000 000___10 000 000___100 000 000

_Время выполнения бинарного поиска:_ _0.0__0.0__0.0_____0.0______0.0_______0.0_________0.0__________0.0
_Время выполнения обычного поиска:_ __0.0__0.0__0.0_____0.0______3.09______34.01_______253.06_______2658.94