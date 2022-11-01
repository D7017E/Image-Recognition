import numpy as np
import matplotlib.pyplot as plt
import csv
import platform


# Import the csv file and extract the data, which is returned as a list.
def importData(file_name):
    fileContent= []
    with open(file_name, "r", encoding="UTF-8") as file:
        file_reader = csv.reader(file, delimiter = ",")
        for i in file_reader:
            fileContent.append(i)
        return fileContent


# Format the test data to be plotable, np.asarray will try to typecast
# but does a bad job of it.
def extractData(resData):
    x_axis = []
    y_axis = []
    size_var = []
    for i in resData:
        x_axis.append(np.float64(i[0]))
        y_axis.append(np.float64(i[1]))
        size_var.append(np.float64(i[2]))
    return (x_axis, y_axis, size_var)

# Given a filename plot the contained data.
def plotRes(file_name):
    resData = importData(file_name)
    x_axis_name, y_axis_name, size_var_name = resData[0]
    resData = resData[1:]
    
    x_axis, y_axis, size_var = extractData(resData)
    # Convert the datalists to numpy arrays.
    x_array = np.asarray(x_axis)
    y_array = np.asarray(y_axis)
    size_array = np.asarray(size_var)

    plt.scatter(x_array, y_array, size_array, alpha=0.5)
    plt.title("Image size testing")
    plt.xlabel(x_axis_name)
    plt.ylabel(y_axis_name)
    plt.xlim([0,1])
    plt.ylim([0,1])
    plt.grid()
    plt.show()

def osBranch():
    if platform.system() == "Linux":
        return "test_results/RPS/resolution_test/image_resolution_data.csv"
    else:
        return "image_resolution_data.csv"

plotRes(osBranch())