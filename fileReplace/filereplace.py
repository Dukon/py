# -*- coding: utf-8 -*-



mass=[]
repl = []
repl2 = []

with open("1.csv", "r", encoding='cp1251') as repl_file:
	for text in repl_file:
		repls = text.split(';')
		repl2.append(repls)
	#print (repl2)
print("Подождите...")
with open("Форма6АПК.np", "r", encoding='utf-8') as file_input:
	for text in file_input:
		repl = text.split('|')
		for r in repl2:
			if repl[0] == 'DATA' and repl[2] == r[12] and repl[3] == r[13]:
				repl[2] = r[14]
				repl[3] = r[15]
		repl = ("|").join(repl)
		mass.append(repl)

output_file = open("output/Форма6АПК_re.np", "w", encoding='utf-8')

for t in mass:
	#print (t)
	output_file.write(t)
print("Готово! Файл находится в папке output")


