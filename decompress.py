import zlib

compressed_data = open('g6.csv','rb').read()
decom = zlib.decompress(compressed_data)


f = open('g7.csv', 'wb')
f.write(decom)
f.close()