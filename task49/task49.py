
import pandas as pd
import matplotlib.pyplot as plt

datafile = pd.read_csv('TCBT.csv', encoding='ISO-8859-1', delimiter=',')
data_3_8 = datafile[datafile.TNVED < u'2209'][datafile.TNVED > u'2202']

data_3_8 = data_3_8.drop(data_3_8.columns[[0,3,4,7,8,9]], axis=1)
data_3_8 = data_3_8[ data_3_8.STOIM > 3250000 ]

Str_Per_Stoim = data_3_8.groupby('PERIOD').size()
Str_Per_Stoim = data_3_8.pivot_table(index='STRANA', columns = 'PERIOD' , values='STOIM', aggfunc=sum, fill_value=0)
Str_Per_Stoim.plot(kind = 'bar', stacked = False, legend = True)

print(Str_Per_Stoim)
plt.savefig('task49.pdf')
plt.show()