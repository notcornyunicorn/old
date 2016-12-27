print('Я найду, сколько процентов файла занимают слова длиной больше 10 символов!')
f=open(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\Николай 2.txt', 'r', encoding='utf-8')
res=[]
for line in f:
    a=line.split()
    for word in a:
        word=word.strip('./,()!?»«—')
        if len(word)>10:
            res.append(word)
x=str(len(res)/len(a))+'%'
print(x)
f.close()
