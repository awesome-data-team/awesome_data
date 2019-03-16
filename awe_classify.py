#coding:utf-8
import os,math
from PIL import Image

def circle():
	s = 100# size of image
	r = 40# radius of circle
	im = Image.new('RGB',(s,s))
	pim = im.load()
	c = s/2 # center of circle

	for i in range(s):
		for j in range(s):
			lx = abs(i-c)
			ly = abs(j-c)
			l = ((lx*lx+ly*ly))**0.5
			if l < r:
				pim[i,j] = (249,205,173)
			else:
				pim[i,j] = (255,255,255)
	im.save('test.png')

if __name__ == '__main__':
	circle()

