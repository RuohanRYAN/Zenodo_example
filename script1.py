import random 
import csv
import sys
def get_random():

	return [[i,random.randint(0,100)] for i in range(1000)]

def save_file(content,file_name):
	with open(file_name,"w") as f:
		write = csv.writer(f)
		write.writerow(["index","value"])
		write.writerows(content)


args = sys.argv
result = get_random()
# print(result)
print("The program runs")

save_file(result,args[1])