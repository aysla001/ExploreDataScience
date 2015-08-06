# intro to exporting to a file
# csv.reader to read file
import csv
# open up connection to file
outfile = open("newfile.csv", 'w')
# writer connection
out = csv.writer(outfile, lineterminator ='\n')
# output first row
out.writerow(['this', 'is', 'your', 'header'])
# output to file
for i in range(10):
	out.writerow([i,i+1,i+2,i+3])
outfile.close()


# read from a file
reader = csv.reader(infile)
infile = open('sample.data', 'r')
reader = csv.reader(infile)
for line in reader:
	print line