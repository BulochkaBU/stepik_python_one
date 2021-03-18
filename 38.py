'''
Условие задачи:
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".
Попробуем написать подобную систему.
На вход программе первой строкой передаётся количество dd известных нам слов, после чего на dd строках указываются эти слова. Затем передаётся количество ll строк текста для проверки, после чего ll строк текста.
Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
Sample Output:
stepic
champignons
the
'''

#Code
a=int(input())
w=[]
for x in range(a):
    a=input().lower()
    s=a
    w.append(s)
ss=set()
a=int(input())
for x in range(a):
    a=input().lower().split()
    for y in a:
        if y not in w:
            ss.add(y)
for x in ss:
    print(x)

