import sys,time
import os

class ShowBar():
	"show the rate of progress"
	def __init__(self,max_num=50,infoDone='ok'):
		self.max_num = max_num
		self.i = 0
		self.infoDone = infoDone

	def show_process(self,perc):
		self.i = int(self.max_num*perc)
		process_bar = '['+'>'*self.i+'-'*(self.max_num-self.i)+']'+'\r'
		sys.stdout.write(process_bar)
		sys.stdout.flush()
	
	def close(self):
		print('')
		print(self.infoDone)
		self.i = 0

class NameError(RuntimeError):
	def __init__(self,*arg):
		self.args = arg

def mkdir(name):
	if os.path.exists(name):
		raise NameError(name+' already exist!')
	else:	os.mkdir(name)
