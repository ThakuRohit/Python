#!/usr/bin/env python
# coding: utf-8

# ## File Handling
# in python we can create, read, update, delete file
## for file handling we use open() function

# In[2]:
## open(filename, mode)


# there are 4 methods

# 1. "r" methods (It is use to read to file, throw error if file doesn't exist)
# 2. "w" methods (it is use to write data on the file, creates the file if it doesn't exist)
# 3. "a" methods (it is use to append data, creates the file if it doesn't exist)
# 4. "x" methods(it creates the specific file, throw error if file already exist)

# we can specify the file handling by binary or text mode
# "t" text mode 
# "b" binary mode

file = open("file_name") or 
file = open("file_name","rt")
#### "r" and "t" are the by default file value

# to read "n" number of  character from the file 
file.read(n)# to read single line of file
file.readline()# to add text at the end of the file

## we can use "a"
file_2 = open(file_name,"a")
file_2.write("Adding text in the file")

## NOTE:
if file do not exist, system create new file# If we use "w" file method, it will overwrite the complete text with new text

file_3 = open(file_name,"w")
file_3.write("Creating the new text in the file")

## NOTE:
Already present text will be replace by new text

# # to close the file file_name.close()
file.close()
## NOTE :
While writing the file it is important to close the file before we want to read it.


## To delete the file from the system
## import operating system into the environment and use .remove() function
import os
os.remove("file_name")


## we can also remove folder from the environment by using .rmdir() function
import os
os.rmdir("folder_name")




