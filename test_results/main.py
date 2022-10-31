import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import csv
import os


def importData(file_name):
    fileContent= []
    with open(file_name, "r", encoding="UTF-8") as file:
        file_reader = csv.reader(file, delimiter = ",")
        for i in file_reader:
            fileContent.append(i)
        return fileContent

def plotRes(file_name):
    resData = importData(file_name)
    x_axis_name, y_axis_name, size_var_name = resData[0]
    resData = resData[1:]
    x_axis = []
    y_axis = [] 
    size_var = []
    for i in resData:
        x_axis.append(np.float64(i[0]))
        y_axis.append(np.float64(i[1]))
        size_var.append(np.float64(i[2]))
    
    x_array = np.asarray(x_axis)
    y_array = np.asarray(y_axis)
    size_array = np.asarray(size_var)

    plt.scatter(x_array, y_array, size_array, alpha=0.5)
    plt.title("Image size testing")
    plt.xlabel(x_axis_name)
    plt.ylabel(y_axis_name)
    plt.grid()
    plt.show()

plotRes("test_results/RPS/image_resolution_data.csv")


# # Load a numpy record array from yahoo csv data with fields date, open, high,
# # low, close, volume, adj_close from the mpl-data/sample_data directory. The
# # record array stores the date as an np.datetime64 with a day unit ('D') in
# # the date column.
# price_data = (cbook.get_sample_data('goog.npz', np_load=True)['price_data']
#               .view(np.recarray))
# price_data = price_data[-250:]  # get the most recent 250 trading days

# delta1 = np.diff(price_data.adj_close) / price_data.adj_close[:-1]

# # Marker size in units of points^2
# volume = (15 * price_data.volume[:-2] / price_data.volume[0])**2
# close = 0.003 * price_data.close[:-2] / 0.003 * price_data.open[:-2]

# fig, ax = plt.subplots()
# ax.scatter(delta1[:-1], delta1[1:], c=close, s=volume, alpha=0.5)

# ax.set_xlabel(r'$\Delta_i$', fontsize=15)
# ax.set_ylabel(r'$\Delta_{i+1}$', fontsize=15)
# ax.set_title('Volume and percent change')

# ax.grid(True)
# fig.tight_layout()

# plt.show()