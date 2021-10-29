num = int(input()) #количество показателей
first = [int(input()) for i in range(num)] #брат1
second = first[:] #брат2 (изначально одинаковые показатели с братом 1)
training = int(input())#количество тренировок
for i in range(training):# задаем показатели, зависящий от кол-ва тренировок.
    brother = int(input())# определяем кто из братьев тренировался
    if brother == 1:# если 1 брат
        first[int(input())] += int(input())# прибавляем это
    elif brother == 2: #если 2 брат
        second[int(input())] += int(input())#прибавляем это
print(*first)# вывод первого брата
print(*second)# вывод второго
dd = 0 # вводим переменную для подсчета одинаковых показателей
for i in range(len(first)): # сравниваем показатели первого и второго брата
    if first[i] == second[i]: # если они одинаковые
        dd = dd + 1 # прибавляем 1, каждый раз, когда показтели совпадают
print(dd) # выводим