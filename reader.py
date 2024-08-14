import PyPDF2
import re

pdf_file = open('.\db\\rc_cadm_006_2020.pdf', 'rb')  # Open the PDF in binary mode
pdfreader = PyPDF2.PdfReader(pdf_file)

file = ['.\db\\politicas\\rc_cadm_001_2018_2.pdf', # nao
        '.\db\\politicas\\rc_cadm_001_2022.pdf', # sim
        '.\db\\politicas\\rc_cadm_003_2018_0.pdf',
        '.\db\\politicas\\rc_cadm_003_2022.pdf',
        '.\db\\politicas\\rc_cadm_004_2022.pdf',
        '.\db\\politicas\\rc_cadm_006_2020.pdf',
        '.\db\\politicas\\rc_cadm_006_2021.pdf',
        '.\db\\politicas\\rc_cadm_006_2022.pdf',
        '.\db\\politicas\\rc_cadm_007_2022.pdf',
        '.\db\\politicas\\rc_cadm_008_2022.pdf',
        '.\db\\politicas\\rc_cadm_009_2020.pdf',
        '.\db\\politicas\\rc_cadm_009_2021.pdf',
        '.\db\\politicas\\rc_cadm_009_2022.pdf',
        '.\db\\politicas\\rc_cadm_010_2021.pdf',
        '.\db\\politicas\\rc_cadm_012_2022.pdf',
        '.\db\\politicas\\rc_cadm_013_2021.pdf',
        '.\db\\politicas\\rc_cadm_013_2022.pdf',
        '.\db\\politicas\\rs_cadm_010_2022.pdf',
        '.\db\\politicas\\rs_pr_3198_2012.pdf',
        '.\db\\politicas\\rs_pr_3222_2013.pdf',
        '.\db\\politicas\\rs_pr_3402_2014.pdf',
        '.\db\\politicas\\rs_pr_3425_2014.pdf']



x=len(pdfreader.pages)


text = "" 
for page in range(1,x): 
   pageobj=pdfreader.pages[page]
   text+=pageobj.extract_text()


# text = re.split(';',text)
data = text.split(';')
# text = "".join(text.splitlines())
# print(text.split('\n\n'))

for var in data:
    file1=open(r".\db\\3.txt","a", encoding="utf-8")
    file1.writelines(var + '\n')

# file1=open(r".\db\\1.txt","a", encoding="utf-8")
# file1.writelines(text.split(' • '))

