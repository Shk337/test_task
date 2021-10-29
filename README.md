# test_task
тестовое задание

# Задача 1: Языки – 0

Ограничение времени 1 секунда

Ограничение памяти 64Mb

:black_square_button: Ввод стандартный ввод или input.txt

:black_square_button: Вывод стандартный вывод или output.txt

Каждый ученик в классе изучает либо английский, либо немецкий, либо оба этих языка. У классного руководителя есть списки учеников, изучающих каждый из языков. Напишите программу, которая позволит классному руководителю быстро выяснить, сколько учеников изучает только один язык.

Формат ввода

В первых двух строках указывается количество учеников, изучающих английский и немецкий языки (M и N). Затем идут M строк — фамилии учеников, которые изучают английский язык; и N строк с фамилиями учеников, изучающих немецкий. Гарантируется, что среди учеников нет однофамильцев.

Формат вывода

Количество учеников, которые изучают только один язык. Если таких не окажется, в строке вывода нужно написать NO.

Пример 1

Ввод Вывод

3

2

Иванов

Петров

Васечкин

Иванов

Михайлов 3

Пример 2

Ввод Вывод

3

3

Иванов

Петров

Васечкин

Иванов

Петров

Васечкин NO

# Задача 2: Именно та буква

Ограничение времени 1 секунда

Ограничение памяти 64Mb

:black_square_button: Ввод стандартный ввод или input.txt

:black_square_button: Вывод стандартный вывод или output.txt

У Аркадия есть любимая буква и любимое число. Каждый раз, когда Аркадий видит какую-то строку, он проверяет, правда ли, что на позиции, номер которой совпадает с его любимым числом, стоит его любимая буква.

Напишите программу, которая поможет Аркадию произвести такую проверку. Если буква совпадает с его любимой, программа должна напечатать «ДА», если не совпадает — «НЕТ». Если в сообщении нет буквы с нужным номером или введённое число в принципе не может быть номером буквы, нужно вывести «ОШИБКА». Если в качестве любимой предъявлена не одна буква, а несколько, тоже нужно вывести «ОШИБКА».

Формат ввода

В первой строке записано некоторое сообщение. Вторая строка содержит любимое число Аркадия. Третья — его любимую букву либо, возможно, несколько букв.

Формат вывода

Одно из сообщений «ДА», «НЕТ» или «ОШИБКА».

Пример 1

Ввод Вывод

привет

2

р ДА

Пример 2

Ввод Вывод

синхрофазотрон

4

хроф ОШИБКА

Пример 3

Ввод Вывод

привет

1

"п" ОШИБКА

Примечания

К сожалению, Аркадий не умеет программировать на Python, поэтому нумерует элементы строки с единицы и только от начала.

# Задача 3(Егор): Маяковский

Ограничение времени 1 секунда

Ограничение памяти 64Mb

:black_square_button: Ввод стандартный ввод или input.txt

:black_square_button: Вывод стандартный вывод или output.txt

Напишите программу, которая выводит слова введённой строки (части, разделённые символами пустого пространства) в столбик. Нужно обойтись без явного использования циклов и списочных выражений, в программе должен быть всего один вызов print.

Формат ввода

Одна строка.

Формат вывода

Слова, каждое на отдельной строке.

Пример

Ввод Вывод

И волны клянутся всеводному Цику оружие бурь до победы не класть. И волны клянутся всеводному Цику оружие бурь до победы не класть.

# Задача 4: Два Пути

Ограничение времени 1 секунда

Ограничение памяти 64Mb

:black_square_button: Ввод стандартный ввод или input.txt

:black_square_button: Вывод стандартный вывод или output.txt

Однажды в далёкой восточной стране двое братьев-близнецов решили изучить искусство Кун-Фу. Каждый нашёл себе Учителя, и у каждого был свой Путь обучения. Долгими тренировками они повышали своё мастерство, оттачивая показатели — Силу, Ловкость, Харизму, Интеллект и так далее.

Но, как говорят Мудрые, «по какому бы Пути ни следовал благородный муж, он придёт к одному и тому же совершенному мастерству владения Кун-Фу».

Оцените, насколько правы Мудрые.

Формат ввода

На первой строке вводится натуральное число S — количество показателей.

На следующих S строках следуют целые числа — уровень соответствующего показателя у каждого из братьев в начале обучения (поскольку они близнецы, то и показатели у них изначально одинаковые).

На следующей после этого строке указано натуральное число N — количество тренировок.

Затем следует N блоков по три строки, характеризующие тренировку: на первой строке блока указывается число 1 или 2 — какой из братьев тренировался; на второй строке блока указывается номер показателя, над которым шла работа в эту тренировку (нумерация с нуля);

на третьей строке блока указывается, на какую величину увеличился данный показатель у данного брата.

Формат вывода

Выводятся: значения всех показателей у первого брата, значения всех показателей у второго брата и количество совпадений между ними.

Пример

Ввод Вывод

3

10

10

10

3

1

0

3

2

2

7

2

0

3 13 10 10 13 10 17 2

# Задача 5:

Многочлен с переменной x записывают, соблюдая такие правила: многочлен состоит из слагаемых со знаками "+" или "-" между ними; каждое слагаемое представляет собой или произведение натурального коэффициента на степень x (например, 5∗x2), или только степень x (например, x3), или только коэффициент (например, 7); степень записывается в виде x, знак ^, показатель степени (натуральное число); в выражении нет пробелов, после него в конце строки записан один пробел. Вычислите значение многочлена при заданном действительном значении x.
