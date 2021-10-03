import os
 
file_size = os.path.getsize('./outfile.csv')
print("File Size is :", file_size, "bytes")

#2018-09-19-03_57_11_VN100.csv

file_size2 = os.path.getsize('./2018-09-19-03_57_11_VN100.csv')
print("Main File Size is :", file_size2, "bytes")


if(file_size2 > file_size):
    print("Yessirski compress")
    
    
file_size3 = os.path.getsize('./decomfile.csv')
print("File Size is :", file_size3, "bytes")


if(file_size3 == file_size):
   print("Yessirski lossless compression")
elif(file_size3 < file_size2):
   print("Lossy compression.Smaller by {} bytes".format(file_size2 - file_size3))