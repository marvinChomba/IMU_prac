import zlib
import sys

compressed_data = open(sys.argv[1],'rb').read()
decom = zlib.decompress(compressed_data)

#print(sys.argv[1][:-25])

f = open(sys.argv[1][:-25]+"-v2.csv", 'wb')
f.write(decom)
f.close()