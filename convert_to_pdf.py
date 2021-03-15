# METODO 1  
from PIL import Image
import os

def listpath(path):
    pasta = path
    scanner = os.scandir(path)
    list_path = list(scanner)
    return list_path

path_img = listpath('img')
for n in path_img:
    if n.is_file():
        nome_fto = n.name.strip('.jpg')
        pdf = Image.open('img/'+n.name)
        pdf.save(f'pdf/{nome_fto}.pdf')
        print(nome_fto)




