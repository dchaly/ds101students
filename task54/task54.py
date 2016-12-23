import pandas as pd
import numpy as np
import matplotlib.pylab as pb
import matplotlib.pyplot as plt
from matplotlib import rc
#Устанавливаем параметры отображения шрифта
font = {'family': 'Tahoma', 'weight': 'bold', 'size': 10}
rc('font', **font)
#Устанавливаем стиль отображения графиков
plt.style.use('fivethirtyeight')
#Считываем файл
data_csv = pd.read_csv('https://raw.githubusercontent.com/infoculture/opencustoms/master/data/countries/turkey.csv', delimiter=',')
#Очищаем данные
data_next = data_csv.drop(data_csv.columns[[2,4,7]], axis=1)
data_next.columns = ['NAPR', 'PERIOD', 'TNVED', 'STOIM', 'NETTO', 'REGION', 'REGION_S']
data = data_next[ data_next.STOIM > 2000 ]

#1график
data_graph1 = data[data.columns[[0, 1, 6, 3, 4]]]
final_data = data_graph1.groupby('PERIOD').size()
final_data = data_graph1.pivot_table(index=['REGION_S','NAPR'], columns = ['PERIOD'] , values='STOIM', aggfunc=sum, fill_value=0)
final_data.plot(subplots = True, layout=(2, 5), figsize=(20, 10), fontsize = 10, kind = 'bar',  stacked = True, legend = False )

#2график
year = ['2013', '2014', '2015', '2016']
pb.subplot(4, 6, 12)
data_graph2 = data_csv[data_csv.columns[[1, 3]]]
P_S_pie = data_graph2.groupby('PERIOD').size()
pd.set_option('precision',3)
plt.pie(P_S_pie, labels=year)

#3 график
pb.subplot(4, 6, 18)
data_graph3 = data_csv[data_csv.columns[[1, 4]]]
P_N_pie = data_graph3.groupby('PERIOD').size()
pd.set_option('precision',3)
plt.pie(P_N_pie, labels=year)
plt.title('Масса товарооборота, находящаяся в импорте и экспорте', fontsize = 9, weight = 'bold')
plt.suptitle('Деньги, затраченные на импорт и экспорт')

#Сохраняем график в файл
plt.savefig('task54.pdf')

#Показываем график
plt.show()
