import zlib


original_data = open('cities.csv','rb').read()
compressed_data = zlib.compress(original_data,zlib.Z_BEST_COMPRESSION)

#compress_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(len(original_data))


compress_ratio = (float(len(original_data)) - float(len(compressed_data))) / float(len(original_data))

print('Compressed: %d%%' % (100.0 * compress_ratio))


f = open('g6.csv','wb')
f.write(compressed_data)
f.close()



