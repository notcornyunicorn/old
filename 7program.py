import random

def reading(filename):
    f = open(filename, 'r', encoding = 'utf-8')
    word = f.read()
    f.close()
    words = word.split(',')
    return words

def game(bread, water, cheese, chocolate, meat, secretwords):
    hints = {'хлеб':random.choice(bread), 'вода':random.choice(water), 'сыр':random.choice(cheese), 'шоколад':random.choice(chocolate), 'мясо':random.choice(meat)}
    secretword = random.choice(secretwords)
    hint = hints[secretword]
    print('Давай сыграем! Я загадаю слово и дам тебе подсказку. Твоя задача - угадать слово.')
    print(str(hint)+' ...')
    tries = 0
    guess = input('Как ты думаешь, что это за слово?\n')
    while guess != secretword:
        tries += 1
        guess = input('Попробуй еще раз!\n')
    print('Ты выиграл, поздравляю! Количество попыток, которое тебе потребовалось: ' + str(tries))

    

def main():
    bread = reading(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\загадки\bread.csv')
    water = reading(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\загадки\water.csv')
    cheese = reading(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\загадки\cheese.csv')
    chocolate = reading(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\загадки\chocolate.csv')
    meat = reading(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\загадки\meat.csv')
    secretwords = reading(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\загадки\secretwords.csv')   
    result = game(bread, water, cheese, chocolate, meat, secretwords)
       
if __name__=='__main__':
    main()
