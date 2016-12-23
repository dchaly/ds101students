import requests
import csv
import json
import webbrowser

my_new_list={}
majora=set()
count=0
with open('data-01-structure-01.csv', 'r', encoding='cp1251') as myface:
    rdr=csv.reader(myface)
    for line in rdr:
        line=str(line)
        line=line.replace(' ', '')
        line=line.replace("['", '')
        line = line.replace("']", '')
        line=line.split(';')

        try:
            if int(line[18])-int(line[18])==0:
                majora.add(line[18])
        except:
            count=count
##Считываем CSV файл и отбираем нужные данные
for i in majora:
    req = requests.get('http://openapi.clearspending.ru/restapi/v3/suppliers/get/?inn=' + i)
    if req.text != 'Data not found.':
        req.encoding='UTF-8'
        pars=json.loads(req.text)
        spy=[]
        try:
            spy.append(pars['suppliers']['data'][0]['contractsSum'])
            spy.append(pars['suppliers']['data'][0]['contractsCount'])

        except:
            spy.append(pars['suppliers']['data'][0]['contracts223Sum'])
            spy.append(pars['suppliers']['data'][0]['contracts223Count'])

        my_new_list[pars['suppliers']['data'][0]["organizationName"]]=spy
##Забираем данные по суммам и контрактам с гос закупок . ру


me=open("new_site.html", 'w')

i='<html>'\
    '<head>' \
    '<title>' \
   'COUNTERNINGOTASIA' \
   '</title>' \
   '</head>' \
  '<body>'\
   ' <center>'\
   '<b>'\
    'Отчёт о Компаниях и их сумках'\
    '</b>'\
    '</center>' \
  '<table border ="1"' \
  '<tr>' \
  '<td>' \
  'ИМЯ КОМПАНИИ' \
  '</td>' \
  '<td>' \
  'Сумма со всех контрактов' \
  '</td>' \
  '<td>' \
  'Количество контрактов' \
  '</td>'
me.write(i)
for m in list(my_new_list.items()):
        me.write('<tr>'\
                 '<td>'\
                 +str(m[0])+
                 '</td>'\
                 '<td>'
                 +str(m[1][0])+
                 '</td>'
                 '<td>'
                 +str(m[1][1])+
                 '</td>'\
                 '</tr>')
end='</table>' \
    '</body>' \
    '</html>'
me.write(end)
me.close()
#Составляем отчёт

webbrowser.open('new_site.html')