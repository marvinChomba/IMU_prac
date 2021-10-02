import zlib


original_data = open('2018-09-19-04_22_21_VN100.csv','rb').read()
compressed_data = zlib.compress(original_data,zlib.Z_BEST_COMPRESSION)

#compress_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(len(original_data))


compress_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(len(original_data))

print('Compressed: %d%%' % (100.0 * compress_ratio))


f = open('outfile.txt','wb')
f.write(compressed_data)
f.close()



