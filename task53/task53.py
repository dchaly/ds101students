import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family = 'Verdana')
plt.style.use('ggplot')  # Красивые графики

data = pd.read_csv("bermudi.csv", encoding = 'Windows-1251') #Чтение файла
data = data.drop(data.columns[[0, 1, 2, 4, 6, 7, 8, 9]], axis=1) #Выбираем нужные столбцы
data_counts = data.groupby('TNVED').sum()#Группируем данные TNVED и суммируем стоимость
data_counts.index = ['Cпиртные напитки', 'Нефть и нефтепродукты',
                     'Смолы и полиуретаны\nв первичных формах',
                     'Изделия для транспортировки\nили упаковки товаров',
                     'Сланец и изделия из сланца',
                     'Бижутерия','Инструменты ручные','Сменные рабочие инструменты\nдля ручных инструментов',
                     'Тали подъемные\nи подъемники','Схемы электронные\nи интегральные',
                     'Контейнеры для перевозки',
                     'Части, принадлежности\nмоторных транспортных средств'] #Переименовываем код товара на название
print(data_counts)
#график 1
data_counts.plot(kind = 'barh', figsize=(12, 5))
plt.xlabel('Завтраты,$',color='k', fontsize=14)
plt.title('Затраты на импорт и экспорт разного вида товаров' , fontweight='normal',color='k', fontsize=16)
plt.subplots_adjust(left=0.21, bottom=0.05, right = 0.98, top = 0.90)
plt.xticks(fontsize= 12)
plt.yticks(fontsize= 12)
plt.legend(['Стоимость'])
plt.savefig('task53-1.pdf')

#график 2
data_counts.plot(figsize=(10, 6),linewidth=8)
plt.title('Затраты на импорт и экспорт разного вида товаров' , fontweight='normal',color='k', fontsize=16)
plt.subplots_adjust(bottom=0.44, top = 0.94,left=0.12, right = 0.95)
plt.legend(['Стоимость'])
plt.xticks(range(len(data_counts)),
           map(lambda x: str(x), data_counts.index),
           rotation=90, fontsize = 12)
plt.yticks(fontsize= 12)

plt.savefig('task53-2.pdf')
plt.show()
