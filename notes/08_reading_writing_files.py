#### Reading files
f = open('08_text.txt', 'r') # path, "r" = read only
f_data_args = f.read(3) # .read() can take arg that reads up to the number of characters
f_data = f.read()
# f.readline() reads a single line from the file
f.close() # always close files
print("Reading up to 3 characters =", f_data_args)
print("Reading full file =", f_data) # can only read remaining


"""
Reading up to 3 characters = Hel
Reading full file = lo World!
Goodbye New Line...
"""

# #### Writing files
# f2 = open('08_write.txt', 'w') # path, "w" = write to file (will overwrite existing or create new if it doesn't exist)
# f2.write("Goodnight Moon!")
# f2.close()


#### Using 'with' to auto-close files
with open('08_text.txt', 'r') as f3: 
  f3_data = f3.read() ## is another kind of scope, when done, it closes and you can no longer interact with it
  
print("Using with =", f3_data) ## since you called the data, it is now available to be used

######################################################## Exercise

def create_cast_list(filename):
    cast_list = []

    with open(filename, 'r') as f:
        for line in f:
            cast_list.append(line.split(",")[0])

    return cast_list

cast_list = create_cast_list('08_cast.txt')
for actor in cast_list:
    print(actor)



#### Documentation https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files