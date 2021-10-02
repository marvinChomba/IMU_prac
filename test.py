import os
 
file_size = os.path.getsize('./outfile.txt')
print("File Size is :", file_size, "bytes")

#2018-09-19-03_57_11_VN100.csv

file_size2 = os.path.getsize('./2018-09-19-03_57_11_VN100.csv')
print("Main File Size is :", file_size2, "bytes")


if(file_size2 > file_size):
    print("Yessirski")