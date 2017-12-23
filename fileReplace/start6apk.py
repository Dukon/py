import re
from output_lib import *


#rep = replace("repl_7apk.csv") # Файл с сопоставлениями
#mass = read_file("Форма7АПК.np", rep, r1=10,r2=11,r3=12,r4=13) # Имя файла, где нужно произвести замену. r номера столбцов в csv файле: r1,r2 было. r3,r4 стало соответственно.
#output("output/Форма7АПК_re.np", mass) # Имя файла выгрузки

rep = generate_replace("6apk.csv", par1=10,par2=11,reg1=r'стр(?P<str>\d+)_Гр(?P<nm>\d+)',reg2=r'стр(?P<str>\d+)_Гр(?P<nm>\d+)')    #Параметры ячеек в файле(расдоложение) было/надо
mass = read_file("Форма6АПК.np", rep, r1=0,r2=1,r3=2,r4=3)
output("output/Форма7.np", mass) # Имя файла выгрузки
