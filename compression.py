import zlib
import binascii

data = "Hello world"

compressed_data = zlib.compress(data,2)

print("Original data: " + data)
print("Compressed data: " + binascii.hexlify(compressed_data))