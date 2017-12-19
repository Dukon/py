import re

def output(file, mass):
	with open (file, "w", encoding='utf-8') as f:
		for t in mass:
			#print (t)
			f.write(t)
	print("Готово! Файл находится в папке output")

def replace(file):
	repl2 = []
	with open(file, "r", encoding='cp1251') as repl_file:
		for text in repl_file:
			repls = text.split(';')
			repl2.append(repls)
	return repl2

def generate_replace (file,par1=3,par2=5,reg1=r'стр(?P<str>\d+)_Гр(?P<nm>\d+)',reg2=r'Стр(?P<str>\d+)_Гр(?P<nm>\d+)'):
	repl2 = []
	with open(file, "r", encoding='cp1251') as repl_file:
		for text in repl_file:
			repls = text.split(';')
			print(repls)
			result1 = re.findall(reg1, repls[par1])
			result2 = re.findall(reg2, repls[par2])
			print (result1)
			#print (result2)
			if result2 != [] and result1 != []:
				a, b = result1[0]
				c, d = result2[0]
				#print (a, b)
				#print (c, d)
				#resultr = ('{}|{}|{}|{}|end').format(a, b, c, d)
				resultr = [a, b, c, d]
				#print (resultr)

				repl2.append(resultr)
	#print (repl2)
	return repl2


def read_file(file, repl2,r1=12,r2=13,r3=14,r4=15):
	mass=[]
	repl = []
	print("Подождите...")
	with open(file, "r", encoding='utf-8') as file_input:
		for text in file_input:
			repl = text.split('|')
			for r in repl2:
				
				if repl[0] == 'DATA' and repl[2] == r[r1] and repl[3] == r[r2]:
					#print (repl)
					repl[2] = r[r3]
					repl[3] = r[r4]

					#print(r[r1], r[r2],r[r3], r[r4])
					break
			repl = ("|").join(repl)
			mass.append(repl)
	return mass