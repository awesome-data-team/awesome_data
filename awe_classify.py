#coding:utf-8
import os,math
from PIL import Image

def circle():
	s = 50
	r = 30
	ima = Image.new('RGBA',(r*2,r*2),(135,135,0,0))
	imb = Image.new('RGBA',(r*2,r*2),(255,255,255,0))
	pima = ima.load()
	pimb = imb.load()
	c = 25

	for i in range(s):
		for j in range(s):
			lx = abs(i-r)
			ly = abs(j-r)
			l = ((lx*lx+ly*ly))**0.5
		if l < r:
			pimb[i-(s-r),j-(s-r)] = pima[i,j]
	imb.save('test.png')

if __name__ == '__main__':
	circle()

