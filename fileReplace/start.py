from output_lib import *

rep = replace("repl.csv") # Файл с сопоставлениями
mass = read_file("Форма6АПК.np", rep, r1=9,r2=10,r3=11,r4=12) # Имя файла, где нужно произвести замену. r номера столбцов в csv файле: r1,r2 было. r3,r4 стало соответственно.
output("output/Форма6АПК_re.np", mass) # Имя файла выгрузки