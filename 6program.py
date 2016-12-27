import random

def readlist(filename):
    f=open(filename, 'r', encoding = 'utf-8')
    word=f.read()
    f.close()
    words=word.split()
    return words

def adjtoadv():
    adjs=readlist(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\предложения\adj.txt')
    advs=[]
    i=0
    while i<len(adjs)+1:
        for adj in adjs:
            adv=adj[:-2]+'о'
            advs.append(adv)
            i+=1
    return advs

def f1(advs, nouns, verbs, conjs, adjs):
    i=0
    s=''
    while i<6:
        noun1=random.choice(nouns)
        adv=random.choice(advs)
        verb1=random.choice(verbs)[:-2]
        conj=random.choice(conjs)
        noun2=random.choice(nouns)
        adj=random.choice(adjs)
        verb2=random.choice(verbs)[:-2]
        if noun1.endswith('а') or noun1.endswith('я') or noun1.endswith('ь'):
            s1=adv[0].upper()+adv[1:]+' '+noun1+' '+verb1+'ла, '+conj+' '
        elif noun1.endswith('о') or noun1.endswith('е'):
            s1=adv[0].upper()+adv[1:]+' '+noun1+' '+verb1+'ло, '+conj+' '
        else:
            s1=adv[0].upper()+adv[1:]+' '+noun1+' '+verb1+'л, '+conj+' '
        if noun2.endswith('а') or noun2.endswith('я') or noun2.endswith('ь'):
            s2=adj[:-2]+'ая '+noun2+' '+verb2+'ла. '
        elif noun2.endswith('о') or noun2.endswith('е'):
            s2=adj[:-2]+'ое '+noun2+' '+verb2+'ло. '
        else:
            s2=adj+' '+noun2+' '+verb2+'л. '
        ss=s1+s2
        s=s+ss
        i+=1
    return s

def main():
    nouns=readlist(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\предложения\noun.txt')
    adjs=readlist(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\предложения\adj.txt')
    conjs=readlist(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\предложения\conj.txt')
    verbs=readlist(r'C:\Users\M_Nastya\Desktop\Учеба\Программирование\предложения\verb.txt')
    advs=adjtoadv()
    text=f1(advs, nouns, verbs, conjs, adjs)
    print(text)

if __name__=='__main__':
    main()
