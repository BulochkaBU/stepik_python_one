'''
Условие задачи:
Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.
Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

Sample Input:
7
Sample Output:
1 2 2 3 3 3 4
'''

#Code
a = int(input())
c = 0
if a == 1:
    print(a)

for h in range(a):
    if a == 2:
        print(1, '', a, end='')
        break
    for j in range(h):
        if c == a:
            break
        print(h, '', end='')
        c += 1









