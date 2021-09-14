import sys

def help():
	print("    This tool needs proper parameters to run correctly")
	print("    The first is the original CRAM file")
	print("    It shouldn't be a very large file")
	print("    The second is the output file")
	print("    The output file will be an act file,")
	print("    It's intended for use with RSDK, but it'll work with anything")
	print("    that has act file support")
	exit()

if len(sys.argv) < 2:
	help()

ramFile = open(sys.argv[1], 'rb')
actFile = open(sys.argv[2], 'wb')

while True:
	byteOne = ramFile.read(1)

	# End of file? Break
	if byteOne == b'':
		break

	byteTwo = ramFile.read(1)
	Red = 0; Green = 0; Blue = 0
	Blue = byteOne
	Blue = int.from_bytes(Blue, "big")
	Blue &= 0x0F
	Blue <<= 4
	Green = byteOne
	Green = int.from_bytes(Green, "big")
	Green &= 0xF0
	Red = byteTwo
	Red = int.from_bytes(Red, "big")
	Red &= 0x0F
	Red <<= 4
	Red = Red.to_bytes(1, 'big')
	Green = Green.to_bytes(1, 'big')
	Blue = Blue.to_bytes(1, 'big')
	actFile.write(Blue)
	actFile.write(Green)
	actFile.write(Red)

print("Finished!")
print("Output can be found at " + sys.argv[2])
