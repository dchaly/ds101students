#Функция для создания нового файла без лишней информации
def create_uranium(tnved_book):
    try:
        f1 = open('TCBT.csv', 'r', encoding='ibm866')
    except:
        print('Error')
        exit()

    uranium_book = []

    for line in f1:
        snip = line.find(',', 10, -1)
        if((line[0:2] == 'ИМ') and (line[snip+1:snip+5] in tnved_book)):
            uranium_book.append(line)

    f1.close()

    try:
        f2 = open('uranium.csv', 'w')
    except:
        print('Error')
        exit()

    for i in uranium_book:
        f2.write(i)

    f2.close()

#-----------------------------------------------------

try:
    file1 = open('tnved.csv', 'r', encoding='cp1251')
except:
    print('Error')
    exit()

tnved_book = []

#Нахождение кодов продукции с ураном в справочнике
for line in file1:
    if((line.find('УРАН') != -1) and (line.find('ФУРАН') == -1)):
        i = line[0:4]
        if(i not in tnved_book):
            tnved_book.append(line[0:4])

file1.close()

create_uranium(tnved_book)

#-----------------------------------------------------

try:
    file2 = open('uranium.csv', 'r')
except:
    print('Error')
    exit()

uranium_list = []
i = 0

for line in file2:
    list = line.split(',')
    uranium_list.append([])
    for j in range(len(list)):
        uranium_list[i].append(list[j].strip())
    i += 1

file2.close()

stat = {}

#Создание словарей, где ключ - код страны, а значение - количество продукции
for i in range(len(uranium_list)):
    if(float(uranium_list[i][6]) != 0):
        if(uranium_list[i][2] not in stat):
            stat[uranium_list[i][2]] = 0
        stat[uranium_list[i][2]] += float(uranium_list[i][6])

#-----------------------------------------------------

#Замена кодов государств на их обычные названия
try:
    file5 = open('country.csv', 'r', encoding='cp1251')
except:
    print('Error')
    exit()

country = {}

for line in file5:
    list = line.split(',')
    if(list[1][0] == '"'):
        list[1] = list[1][1:]
    country[list[0]] = list[1].strip()

file5.close()

stat_book_csv = []
stat_book_html = []

#Создание списков, состоящих из строк, на основе словарей (для записи в файлы)
for key, value in stat.items():
    stat_book_csv.append(str(country[key]) + ';' + str("%.2f" % value) + '\n')
    stat_book_html.append('<tr><td>' + str(country[key]) + '</td><td>' + str("%.2f" % value) + '</td></tr>')

#-----------------------------------------------------

#Запись в CSV-файл
try:
    file3 = open('stat.csv', 'w')
except:
    print('Error')
    exit()

file3.write('COUNTRY;URANIUM\n')

for i in stat_book_csv:
    file3.write(i)

file3.close()

#-----------------------------------------------------

#Запись в HTML-файл
begin = '<html><head><title>Uranium</title></head>' \
    '<body><center><b>Страны, поставляющие уран в Россию</b><br><br>' \
    '<table border width="40%" cellspacing="0" cellpadding="5">' \
    '<tr><th>Страна</th><th>Количество урана (кг)</th>'

end = '</table><br>' \
    '<img src="https://pp.vk.me/c604518/v604518184/4453d/YmjE_YzB8Ww.jpg"; width="150">' \
    '</center></body></html>'

try:
    file4 = open('stat.html', 'w')
except:
    print('Error')
    exit()

file4.write(begin)

for i in stat_book_html:
    file4.write(i)

file4.write(end)
file4.close()

#-----------------------------------------------------

#Функция для визуализации результатов
def visualization():
    import matplotlib.pyplot as plt
    import numpy as np

    from matplotlib import rc
    font = {'family': 'Verdana', 'weight': 'normal'}
    rc('font', **font)

    file = open('stat.csv', 'r')

    book = []
    i = 0

    for line in file:
        if(i == 1):
            list = line.split(';')
            book.append(list)
        i = 1

    file.close()

    objects = []
    performance = []

    for i in range(len(book)):
        pos = np.arange(len(book))
        objects.append(book[i][0])
        performance.append(float(book[i][1]))

    plt.barh(pos, performance, align='center', alpha=0.5)
    plt.yticks(pos, objects)
    plt.ylabel('Страны')
    plt.xlabel('Количество урана (кг * 10^(-7))')
    plt.title('Страны, поставляющие уран в Россию')
    plt.savefig('uranium.pdf')

    plt.show()

visualization()