import matplotlib.pyplot as plt 
import csv
import random

def visual():
	data_orig = [random.randint(0,100) for i in range(1000)]
	data_trans = [3*random.randint(0,100)+6 for i in range(1000)]
	fig, ax = plt.subplots()
	ax.plot(data_orig,label="original")
	ax.plot(data_trans,label="transformed")
	plt.legend()
	fig.savefig("linear_trans_vs_random.jpg",bbox_inches = "tight", dpi = 150)


visual()