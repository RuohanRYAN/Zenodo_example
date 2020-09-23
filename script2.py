import random 
import csv
import pandas as pd
import sys
def get_random(data):
	return [[i,3*data[i]+6] for i in range(1000)]

def save_file(content,file_name):
	with open(file_name,"w") as f:
		write = csv.writer(f)
		write.writerow(["index","value"])
		write.writerows(content)
def read_file(file_name):
	df = pd.read_csv(file_name)
	return df.values[:,1]

argv = sys.argv
path_read = argv[1]
path_save = argv[2]

data = read_file(path_read)
save_file(get_random(data),path_save)
# save_file(result)

