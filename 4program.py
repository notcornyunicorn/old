print('Пиши латинские глаголы в пассиве настоящего времени. Когда устанешь, нажми enter.')
stop=''
verb=1
verblist=[]
while verb!=stop:
    verb=input()
    if verb!=stop:
        verblist.append(verb)
#Если глагол заканчивается -tur, то он стоит в Praesens Indicativi Passivi или в Praesens Conjuctivi Passivi
#Если глагол заканчивается на -bitur, то глагол в Futurum I Indicativi Passivi
#Если глагол заканчивается на -batur, то глагол в Imperfectum Indicativi Passivi
#Если глагол заканчивается на -retur, то глагол в Imperfectum Conjuctivi Passivi
#Если глагол заканчивается на -ntur, то глагол в 3PL, а не 3SG
print('А вот это глаголы из введенных тобою, которые точно будут стоять в пассиве настоящего времени:')
for word in verblist:
    if word.endswith('bitur') or word.endswith('batur') or word.endswith('ntur') or word.endswith('retur'):
        continue
    if word.endswith('tur'):
        print(word)

