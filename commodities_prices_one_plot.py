
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

data_brent = pd.read_csv('price_brent.csv', sep=';')
data_gold = pd.read_csv('price_gold.csv', sep=';')
data_copper = pd.read_csv('price_copper.csv', sep=';')

#coord for brent's plot
x_values_brent = data_brent.YEAR_MONTH.to_list()
x_values_brent = [dt.datetime.strptime(str(i), '%Y%m%d') for i in x_values_brent]
y_values_brent = data_brent.PRICE.to_list()
y_values_brent = [i * 100 for i in y_values_brent] #magic number (coefficient) used for same scale

#coord for gold's plot
x_values_gold = data_gold.YEAR_MONTH.to_list()
x_values_gold = [dt.datetime.strptime(str(i), '%Y%m%d') for i in x_values_gold]
y_values_gold = data_gold.PRICE.to_list()
y_values_gold = [i * 5 for i in y_values_gold] #magic number (coefficient) used for same scale

#coord for copper's plot
x_values_copper = data_copper.YEAR_MONTH.to_list()
x_values_copper = [dt.datetime.strptime(str(i), '%Y%m%d') for i in x_values_copper]
y_values_copper = data_copper.PRICE.to_list()

fig, ax = plt.subplots(figsize=(12, 8))
ax.set_title('Brent (price per barrel x 100),\n Gold (price per oz x 5),\n Copper (price per ton)', fontsize = 14)
ax.set_xlabel('Date', fontsize=12)
ax.set_ylabel('Price, USD', fontsize=12)
plt.plot(x_values_brent, y_values_brent, linewidth=1, c='brown')
plt.plot(x_values_gold, y_values_gold, linewidth=1, c='yellow')
plt.plot(x_values_copper, y_values_copper, linewidth=1, c='red')
plt.show()
