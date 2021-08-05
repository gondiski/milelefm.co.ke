from PIL import Image
import os, sys

path = "img/"
dirs = os.listdir( path )

def resize():
	for item in dirs:
		if os.path.isfile(path+item):
			im = Image.open(path+item)
			f, e = os.path.splitext(path+item)
			# imResize = im.resize((200,200), Image.ANTIALIAS)
			# imFinal = imResize.convert('RGB')
			imFinal = im.convert('RGB')
			imFinal.save(f + '_resized.jpg', 'JPEG', quality=90, dpi=(100,100))

resize()