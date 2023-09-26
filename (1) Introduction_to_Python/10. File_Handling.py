'''
---------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                    File Handling 
---------------------------------------------------------------------------------------------------------------------------------------------------------------


Opening a File
___________________
'''
# Syntax: 
# file = open ( filename, mode, buffersize)
# The mode can be read, write, or append (r, w, and a, respectively). If none are specified, read mode is assumed.
# If you're working with a binary file, replace the mode indicator with the letter b (for example, rb or wb). The letter b denotes binary mode (text translation mode).
# The buffersize clause is the syntax's final argument, which means:
# -> 0 = no buffering
# > 1 = line buffering
# > If buffersize is larger than one, its value is the buffer size in bytes.
# > If the value is negative, the buffer size is set to the system default (default behaviour). 

# Example:
file = open("pyfile.txt", "r") 
line = file.readline()
line = line[:-1] #chop off the newline character
while line: 
    print (line)
    line = file.readline()
    line = line[:-1] 
file.close()


'''
Supported Methods
___________________
'''

# All file objects implement the methods listed below:

# read()
# ________
# It can read up to n bytes. However, if no arguments are provided, read() reads all accessible data from the file.
# Syntax: file.read( [nbytes] )
# Example: 
file = open("pyfile.txt").read()
# If you use the command file = open("pyfile.txt"), Python will read the first 200 bytes of the file using read(200).


# readline()
# ____________
# It only reads one line at a time (until the newline character). 
# Syntax: file.readline()
# Example: 
file=open("test.txt","r") 
while 1: 
    line = file.readline()
    if not line: 
        break 


# readlines()
# ______________
# It reads the full file and converts it to a string list. 
# Syntax: file.readlines()
# Example: 
file=open("test.txt","r") 
for line in file.readlines():
    print (line)


# write()
# _____________
# It writes the string to a file.
# Syntax: file.write(string)
# Example: 
file.write('Topic: File Handling')


# writelines()
# ______________
# It writes list of strings to a file.
# Syntax: file.writelines(list)
# Example: 
file.writelines(["int","string","float"])


# Fileno()
#____________
# It returns a file descriptor that is an integer. 
# Syntax: file.fileno()


# seek()
#____________
# It moves to a different file place. If how=0, the position is relative to the current position; if how=1, the position is relative to the end of the file; and if how=2, the position is relative to the beginning of the file. The number 0 is the default for how.
# Syntax: file.seek(position[, how])


# tell()
#_________
# It provides the current file pointer as a response. 
# Syntax: file.tell()


# truncate()
#_____________
# It trims down a file.
# Syntax: file.truncate([size])


# flush()
#____________
# It clears the internal buffer. 
# Syntax: file.flush()


# close()
#____________
# It closes a file.
# Syntax: file.close()


# File Object Attributes
#_________________________

# Here are some file-specific attributes:
# file.name # returns the name of the file
# file.mode # returns the I/O mode for the file 
# file.closed # returns 0 if the file is closed; 1 otherwise 
