############
# imports
############

import csv
import os
import sys
import inspect
import pandas as pd
import numpy as np

# 1. File IO

file = open('file.txt','r')
with open('newfile.txt','w') as newfile:
	for line in file:
		newfile.write(file)
		newfile.write('\n')


# 2. Read and write a CSV file

# Write

with open('eggs.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

# Read

with open('csvfile.csv', 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
	print ', '.join(row)

# 3. Using OS

# Find current_working_directory
print os.getcwd()

# Go to a directory
path = '/home/priyansh/Hobbies'
os.chroot(path)

# Get names of everything present in a particular directory
path = '/home/priyansh/Hobbies'
allfiles = os.listdir(path)

# Set an environment variable
# Should be strings
os.environ["ME"] = "STAR"
os.environ["CGPA"] = "10"

# 4. Get system parameters

# command-line arguments 
print sys.argv[0] # prints filename
print sys.argv[1] # prints first argument
print len(sys.argv) # prints (the number of arguments passed + 1)

# get system parameters
print sys.maxint # max-limit of integers

# 5. Using inspect library for debugging

# Return the name of the (text or binary) file in which an object was defined.
print inspect.getfile(some_object)

# Return the name of the Python source file in which an object was defined.
print inspect.getsourcefile(some_object)

# find the caller of the current function
print inspect.stack()[1][3]

# 6 . Using Pandas

# Using Series
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print s

# Using dataframes
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print df

# Adding a new column to an existing DataFrame object with column label by passing new series

print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']

print df
