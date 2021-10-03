import zlib

def compress_file(file_name1,file_name2):

    original_data = open(file_name1,'rb').read()
    compressed_data = zlib.compress(original_data,zlib.Z_BEST_COMPRESSION)

    #compress_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(len(original_data))


    compress_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(len(original_data))

    print('Compressed: %d%%' % (100.0 * compress_ratio))


    f = open(file_name2,'wb')
    f.write(compressed_data)
    f.close()



