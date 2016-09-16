import random
import io
import csv
f=open('occupations.csv', 'r')
file=f.read();
lines=file.splitlines()
del lines[0]
#deletes first line
prob={}
for n in  csv.reader(lines, quotechar='"', delimiter=',',
	quoting=csv.QUOTE_ALL, skipinitialspace=True):
 	a=n[0]
	b=float(n[1])
	prob[a]=b
	#ignores comma in quotations and creates the dictionary
sorted(prob.values())
#sorts dict by value in ascending order

def randOcc():
	rand=random.randrange(0,998)
	counter=0
	for key, value in prob.iteritems():
		counter+=value*10
		#add by ascending numbers for ranges of probability
		if (rand<counter):
			return key
	return "None"

print randOcc()