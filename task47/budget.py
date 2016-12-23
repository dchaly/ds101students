from lxml import html
import requests
#import time
#from io import StringIO, BytesIO
import csv
import random
import os #для создания папки

budget1912 = 0
budget1913 = 0
budget1914 = 0
budget1915 = 0
count = 0
year=0

print('В результате работы программы создаются файлы budget191*.html в подкаталоге Budget')
print('Данную папку необходимо скопировать подкаталог demos библиотеки bubbletree-master(например в Х:\\bubbletree-master\demos)')

random.seed() #для разных цветов

htmlreq = requests.get('http://minfin.ru/OpenData/7710168360-agencies_budget_1912_1915/data-20141230-structure-20141230.csv')

tree = html.fromstring(htmlreq.text)
tree.text=tree.text.replace(',',';')
tree.text=tree.text.replace('\r',' ') #убираем перенос строки
tree.text=tree.text.replace('; ',', ')

f=open("budget.csv", 'w') #создаем файл
f.write(tree.text)
f.close()
f=open("budget.csv", 'r')
rdr = csv.reader((f), delimiter=';') #разделает на столбцы

for rec in rdr:
    count=count+1
    if count > 1: #пропускаем заголовок
        budget1912=budget1912+int(rec[4])
        budget1913=budget1913+int(rec[5])
        budget1914=budget1914+int(rec[6])
        budget1915=budget1915+int(rec[7])

f.close()

if not os.path.exists('Budget'): #если не существует папки Budget, мы ее создаем
    os.mkdir('Budget')

h=open("header.txt", 'r')
header=h.read()
h.close()

f1=open("Budget/budget1912.html", 'w')
f1.write(header)
f2=open("Budget/budget1913.html", 'w')
f2.write(header)
f3=open("Budget/budget1914.html", 'w')
f3.write(header)
f4=open("Budget/budget1915.html", 'w')
f4.write(header)

header="				label: 'Бюджет России за 1912',\n" +"				amount:" + str(budget1912) + ",\n" + "				color: '#"  + str(hex(random.randint(0,16777216)))[2:] + "',\n" + "				children: [\n"
f1.write(header)
header="				label: 'Бюджет России за 1913',\n" +"				amount:" + str(budget1913) + ",\n" + "				color: '#"  + str(hex(random.randint(0,16777216)))[2:] + "',\n" + "				children: [\n"
f2.write(header)
header="				label: 'Бюджет России за 1914',\n" +"				amount:" + str(budget1914) + ",\n" + "				color: '#"  + str(hex(random.randint(0,16777216)))[2:] + "',\n" + "				children: [\n"
f3.write(header)
header="				label: 'Бюджет России за 1915',\n" +"				amount:" + str(budget1915) + ",\n" + "				color: '#"  + str(hex(random.randint(0,16777216)))[2:] + "',\n" + "				children: [\n"
f4.write(header)

h.close()

body1=""
body2=""
body3=""
body4=""
count=0

f=open("budget.csv", 'r')
rdr = csv.reader((f), delimiter=';')

for rec in rdr:
    count+=1
    if count > 1:
        body1 = body1 + "					{ label: '" + rec[3] + "', amount: " + str(rec[4]) + ", color: '#"  + str(hex(random.randint(0,16777216)))[2:] + "' },\n" #+ str(hex(random.randint(0,255)))
        body2 = body2 + "					{ label: '" + rec[3] + "', amount: " + str(rec[5]) + ", color: '#"  + str(hex(random.randint(0,16777216)))[2:] + "' },\n" #+ str(hex(random.randint(0,255)))
        body3 = body3 + "					{ label: '" + rec[3] + "', amount: " + str(rec[6]) + ", color: '#"  + str(hex(random.randint(0,16777216)))[2:] + "' },\n" #+ str(hex(random.randint(0,255)))
        body4 = body4 + "					{ label: '" + rec[3] + "', amount: " + str(rec[7]) + ", color: '#"  + str(hex(random.randint(0,16777216)))[2:] + "' },\n" #+ str(hex(random.randint(0,255)))

f1.write(body1)
f2.write(body2)
f3.write(body3)
f4.write(body4)
        
f=open("footer.txt", 'r')
footer=f.read()
f.close()

f1.write(footer)
f2.write(footer)
f3.write(footer)
f4.write(footer)

f1.close()
f2.close()
f3.close()
f4.close()

print('......................')
print('Готово')
