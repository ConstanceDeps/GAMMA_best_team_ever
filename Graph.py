import matplotlib.pylab as plt
import pandas as pd
import numpy as np

data = pd.read_csv('IONIZATION_case_daily_production_data.csv')
#print(data.head())
#print(data.info())
data2 = data[data.slab_production > 0]
data3 = data2.groupby(['year', 'month'], as_index=False)['slab_production'].sum()
print(data3.head())


def myplot(data, avg):
    averageline = avg*np.ones((len(data)+6))
    plt.plot(data.slab_production, color='b')
    plt.plot(averageline, color='r')
    plt.savefig('plotslab.png')
    plt.show()
    pass

myplot(data3, 237.5)



