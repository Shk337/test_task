def main(): # создаем функцию мейн
    input_file = open("input.txt", "r") # отсюда считываем число(пишем руками)
    output_file = open("output.txt", "w") # сюда выводится
    line = input_file.readline().split()# считываем число из input на 1 строке.
    n = int(line[0]) # считываем первое число на этой строке
    if n == 0:# если это число =0, 
        otv = 1 # то мы вводим 1 по условию
    else:
        otv = n * (n - 1) + 2 # в ином случае по формуле n(n-1)+2 деления плоскостей окружностями. вот тута http://nature.web.ru/db/msg.html?mid=1158715&mode=2
    print(otv) # выводим ответ
    output_file.write(str(otv) + '\n') #пишет в оутпут ответ на новой строке
main() # выводим функцию мэйн