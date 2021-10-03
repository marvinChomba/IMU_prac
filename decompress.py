import zlib

compressed_data = open('g6.txt','rb').read()
decom = zlib.decompress(compressed_data)


f = open('g8.csv', 'wb')
f.write(decom)
f.close()