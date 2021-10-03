import zlib
import sys

def compress_file(file_name1,file_name2):

    original_data = open(file_name1,'rb').read()
    compressed_data = zlib.compress(original_data,zlib.Z_BEST_COMPRESSION)

    #compress_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(len(original_data))


    #compress_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(len(original_data))

#    print('Compressed: %d%%' % (100.0 * compress_ratio))

    #print(sys.argv[2])
    f = open(file_name2+".txt",'wb')
    f.write(compressed_data)
    f.close()
    
    f = open(file_name2+".csv",'wb')
    f.write(compressed_data)
    f.close()


if __name__ == "__main__":
    compress_file(sys.argv[1],sys.argv[2])

