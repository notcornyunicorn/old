import os
import re

def function():
    a = []
    b = []
    c = []
    for root, dirs, files in os.walk('C:\\Users\\M_Nastya\\Desktop\\Учеба\\Программирование'):
        for fl in files:
            a.append(fl)
    regex = '(.+)[.].+'
    for i in a:
        name = re.search(regex, i)
        if name:
            res = name.group(1)
            b.append(res)
    for i in b:
        if i not in c:
            c.append(i)
    print('Найдено ' + str(len(c)) + ' разных названий файлов.')
    os.mkdir('Test')
    os.mk
    
def main():
    result = function()

if __name__=='__main__':
    main()

