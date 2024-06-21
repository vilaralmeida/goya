str = 'Rodrigo; Almeida; Santos.'
data = str.split(';')
print(data)

for r in data:
    file1=open(r".\db\\2.txt","a", encoding="utf-8")
    file1.writelines(r + '\n')