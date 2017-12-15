def output(file):
			
	output_file = open(file, "w", encoding='utf-8')

	for t in mass:
		#print (t)
		output_file.write(t)
	print("Готово! Файл находится в папке output")

def replace(file):
	repl2 = []
	with open(file, "r", encoding='cp1251') as repl_file:
		for text in repl_file:
			repls = text.split(';')
			repl2.append(repls)

def read_file(file):
	mass=[]
	repl = []
	print("Подождите...")
	with open(file, "r", encoding='utf-8') as file_input:
		for text in file_input:
			repl = text.split('|')
			for r in repl2:
				if repl[0] == 'DATA' and repl[2] == r[12] and repl[3] == r[13]:
				repl[2] = r[14]
				repl[3] = r[15]
			repl = ("|").join(repl)
			mass.append(repl)