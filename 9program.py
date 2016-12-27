import re

def reading(filename):
    f = open(filename, 'r', encoding = 'utf-8')
    ananas = f.readlines()
    f.close()
    return ananas

def family(ananas):
    regex = '<td align="left"><a href=".+" title=".+">(.+)</a></td>\n'
    i = 0
    while i < len(ananas):
        if '<td align="right">Семейство:</td>' in ananas[i]:
            res = re.search(regex, ananas[i+1])
            if res:
                fam = res.group(1)
                print("Семейство", " ", fam)
                f = open('результат.txt', 'w', encoding = 'utf-8')
                f.write(fam)
                f.close
        i += 1
            
def main():
    ananas = reading(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\ананас.html')
    sem = family(ananas)
       
if __name__=='__main__':
    main()
