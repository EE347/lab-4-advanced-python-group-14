import csv
import matplotlib.pyplot as plt
from datetime import datetime

stock_data = "task9.csv"

dates = []
meta = []
aapl = []
amzn = []
nflx = []
nvda = []
googl = []

with open(stock_data, mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    for row in csv_reader:
        dates.append(datetime.strptime(row[0], '%d/%m/%Y'))

        meta.append(float(row[1]))
        aapl.append(float(row[2]))
        amzn.append(float(row[3]))
        nflx.append(float(row[4]))
        nvda.append(float(row[5]))
        googl.append(float(row[6]))

def calculate_change(prices):
    return (((prices[-1] - prices[0]) / prices[0]) * 100) + 100

meta_pc = calculate_change(meta)
aapl_pc = calculate_change(aapl)
amzn_pc = calculate_change(amzn)
nflx_pc = calculate_change(nflx)
nvda_pc = calculate_change(nvda)
googl_pc = calculate_change(googl)

plt.figure(figsize=(12,6))

plt.plot(dates, meta, label=f'META: +{meta_pc:.2f}%')
plt.plot(dates, aapl, label=f'AAPL: +{aapl_pc:.2f}%')
plt.plot(dates, amzn, label=f'AMZN: +{amzn_pc:.2f}%')
plt.plot(dates, nflx, label=f'NFLX: +{nflx_pc:.2f}%')
plt.plot(dates, nvda, label=f'NVDA: +{nvda_pc:.2f}%')
plt.plot(dates, googl, label=f'GOOGL: +{googl_pc:.2f}%')


plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.title('FAANNG Performance')
plt.legend()

plt.tight_layout()
plt.show()