import random 
import csv
def get_random():

	return [[i,3*random.randint(0,100)+6] for i in range(1000)]

def save_file(content):
	with open("script2_output.csv","w") as f:
		write = csv.writer(f)
		write.writerow(["index","value"])
		write.writerows(content)

result = get_random()
print(result)
save_file(result)