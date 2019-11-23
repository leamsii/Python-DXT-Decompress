"""
This small scripts decompresses Don't Starve .TEX Texture files
using DXTDecompress.py
"""

import sys
import struct
from time import sleep
from PIL import Image
from pathlib import Path

sys.path.append('../')
from DXTDecompress import DXTBuffer


def _exit(msg):
	print(msg)
	print("Exiting in 5 seconds..")
	sleep(5)
	sys.exit(-1)

def unpack(_bytes):
	STRUCT_SIGNS = {
	1 : 'B',
	2 : 'H',
	4 : 'I',
	8 : 'Q'
	}
	return struct.unpack('<' + STRUCT_SIGNS[len(_bytes)], _bytes)[0]

class KTEX:
	def __init__(self, file_name):
		PIXEL_FORMAT = {
			0 : 'DXT1',
			1 : 'DXT3',
			2 : 'DXT5',
			4 : 'ARGB',
			8 : 'Unknown'
		}
		PLATFORM = {
			12 : 'PC',
			11 : 'XBOX360',
			10 : 'PS3',
			0 : 'Unknown'
		}
		TEXTURE_TYPE = {
			1 : '1D',
			2 : '2D',
			3 : '3D',
			4 : 'Cube Mapped'
		}

		# Open the file and check the magic number
		with open(file_name, 'rb') as file:
			assert file.read(4).decode() == 'KTEX'

			# Now get the image properties
			header = unpack(file.read(4))

			self.pixel_format = PIXEL_FORMAT[(header >> 4) & 31]
			self.texture_type = TEXTURE_TYPE[(header >> 9) & 15]
			self.flags = (header >> 18) & 3
			self.remainder = (header >> 20) & 4095
			self.mipmaps = (header >> 13) & 31

			self.width = unpack(file.read(2))
			self.height = unpack(file.read(2))
			self.pitch = unpack(file.read(2))
			self.data_size = unpack(file.read(4))

			# Jump to the DXT compressed data
			file.seek(8 + (self.mipmaps * 10)) # 8 is for the magic and the header
			
			_buffer = DXTBuffer(self.width, self.height) # Width and height of the image

			# Detect the compression type
			if self.pixel_format == 'DXT1' or self.pixel_format == 'DXT2':
				_buffer = _buffer.DXT1Decompress(file)
			elif self.pixel_format == 'DXT3' or self.pixel_format == 'DXT5':
				_buffer = _buffer.DXT5Decompress(file)

			new_image = Image.frombuffer('RGBA', (self.width, self.height), _buffer, 'raw', 'RGBA', 0 ,1)
			new_image.save("sample.png")

			print("Log: Finished.")


# Check the sys arguements
args = sys.argv
if len(args) <= 1:
	_exit("Error: Please specify a .TEX file! ie, convert.py sample.tex")

if not Path(args[1]).exists():
	_exit(f"Error: The image file {args[1]} was not found!")

ktex = KTEX(args[1])