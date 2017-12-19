import re
from output_lib import *


#rep = replace("repl_7apk.csv") # Файл с сопоставлениями
#mass = read_file("Форма7АПК.np", rep, r1=10,r2=11,r3=12,r4=13) # Имя файла, где нужно произвести замену. r номера столбцов в csv файле: r1,r2 было. r3,r4 стало соответственно.
#output("output/Форма7АПК_re.np", mass) # Имя файла выгрузки

rep = generate_replace("7apk-xyz.csv")
mass = read_file("Форма7АПК.np", rep, r1=0,r2=1,r3=2,r4=3)
output("output/Форма7АПК_re.np", mass) # Имя файла выгрузки
