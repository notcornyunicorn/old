import re

def reading(filename):
    f = open(filename, 'r', encoding = 'utf-8')
    word = f.read()
    word = word.lower()
    f.close()
    arr = word.split()
    words = []
    for word in arr:
        word = word.strip('()={}[]:;.,/-!?')
        words.append(word)
    return words

def eat(words):
    i = 0
    RESULT = []
    regex = 'съе(м|шь(те)?|сть?|л(а|о|и)?|в(ш(ая|ую|е(е|й|го|му?)|и(й|х|е|ми?)))?|д(ят|и(м|те)|ен(а|о|ы)?(н(ая|ую|о(й|е|го|му?)|ы(е|й|х|ми?)))?))'
    while i < len(words):
        m = re.search(regex, words[i])
        if m != None:
            print(m.group())
        i += 1
            
def main():
    words = reading(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\В и М.txt')
    verb = eat(words)

if __name__=='__main__':
    main()
