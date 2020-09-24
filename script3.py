import matplotlib.pyplot as plt 
import csv
import random
import sys
import pandas as pd 
def visual(data1,data2):

	fig, ax = plt.subplots()
	ax.plot(data1,data2)
	ax.set_title("visualization of linear transformation")
	ax.set_xlabel("script1_output")
	ax.set_ylabel("script2_output")
	fig.savefig("linear_trans_vs_random.jpg",bbox_inches = "tight", dpi = 150)

def read_file(file_name):
	df = pd.read_csv(file_name)
	return df.values[:,1]

argv = sys.argv
path_read = argv[1]
path_save = argv[2]

data1 = read_file(path_read)
data2 = read_file(path_save)

visual(data1,data2)