import zlib
import sys

compressed_data = open(sys.argv[1],'rb').read()
decom = zlib.decompress(compressed_data)


f = open(sys.argv[2], 'wb')
f.write(decom)
f.close()