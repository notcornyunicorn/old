import re

def reading(filename):
    f = open(filename, 'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    return text

def findall(text):
    regex = '(не .[^ |-]+?(?:у|ю|гъ|лъ))(?: |,|[.])'
#когда я искала просто слова, заканчивающиеся на ъ, в выдачу попало очень много мусора
    result = re.findall(regex, text)
    a = ''
    if result:
        for word in result:
            a = a + word + '\n'
        f = open('результат.txt', 'w', encoding = 'utf-8')
        f.write(a)
        f.close()
            
def main():
    text = reading(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\rur.txt')
    negverb = findall(text)
       
if __name__=='__main__':
    main()
