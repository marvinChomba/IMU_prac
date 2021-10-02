import zlib

compressed_data = open('outfile.txt','rb').read()
decom = zlib.decompress(compressed_data)


f = open('decomfile.txt', 'wb')
f.write(decom)
f.close()