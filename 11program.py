import re

def reading(filename):
    f = open(filename, 'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    return text

def catation(text):
    regex = 'Диноза́?вр'
    subst = 'Кот'
    preresult = re.sub(regex, subst, text)
    regex = 'динозавр'
    subst = 'кот'
    result = re.sub(regex, subst, preresult)
    f = open('кот.txt', 'w', encoding = 'utf-8')
    f.write(result)
    f.close()
    
            
def main():
    text = reading(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\динозавр.txt')
    dinocat = catation(text)
       
if __name__=='__main__':
    main()
