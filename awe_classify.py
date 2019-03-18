#coding:utf-8
import os,math
from PIL import Image
import random

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
	return im

def triangle():
	s = 100
	im = Image.new('RGB',(s,s))
	pim = im.load()
	
	for i in range(s):
		for j in range(s):
			if (j<80) and (i+j>80) and (i-j<20):
				pim[i,j] = (249,205,173)
			else:
				pim[i,j] = (255,255,255)
	return im
	
def square():
	s = 100 # size of image
	im = Image.new('RGB',(s,s))
	pim = im.load()

	for i in range(s):
		for j in range(s):
			if (i>30) and (i<70) and (j>30) and (j<70):
				pim[i,j] = (249,205,173)
			else:
				pim[i,j] = (255,255,255)
	return im
	
def 3_classify():
	img_size = 224
	# total 1000 fake images
	# 1/3 circle, 1/3 square , 1/3  triangle
	for i in range(1,1001):
		x = random.randint(0,2)
		label = x
		if (1==x):
			im = square()
		elif (2==x):
			im = triangle()
		else:
			im = circle
		rand_temp = random.randint(50,100)
		size = rand_temp(50,100)/100
		img = Image.new('RGB',(img_size,img_size))
		pim = im.load()
		pimg = img.load()
		# we define left top point as anchor
		anchor_x = random.randint(rand_temp,img_size-rand_temp)
		anchor_y = random.randint(rand_temp,img_size-rand_temp)
		for j in range(0,img_size):
			for k in range(0,img_size):
				x = int((j-anchor_x)/size)
				y = int((k-anchor_y)/size)
				z = (random.gauss(0,3),random.gauss(0,3),random.gauss(0,3))
				if (x<100) and (x>0) and (y<100) and (y>0):
					pimg[i,j] = pim[x,y]+z
				else:
					pimg[i,j] = z
		img_name = os.path.join(save_path , str(i)+'.jpg')
		img.save(img_name)
		with open(txt_name,'a') as f:
			f.writelines([img_name,' ',label])
	print('ok')
			
				
					

if __name__ == '__main__':
	3_classify()
