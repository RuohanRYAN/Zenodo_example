import random 
import csv
def get_random():

	return [[i,random.randint(0,100)] for i in range(1000)]

def save_file(content):
	with open("script1_output.csv","w") as f:
		write = csv.writer(f)
		write.writerow(["index","value"])
		write.writerows(content)

result = get_random()
print(result)
save_file(result)