raw_file_object = open("raw_file.txt", "r")

# read the lines
raw_file_lines = raw_file_object.readlines()
# print raw_file_lines

# read a line
for elm in raw_file_lines:
    print elm.split("\"")[1]

# em day la manh