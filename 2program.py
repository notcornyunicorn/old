slovo=input('Напиши слово, и я выведу первую половину его букв, не считая средней буквы\n')
slovo=str(slovo)
i=len(slovo)
i=int(i)
i=i-1
for sym in slovo:
    print(sym)
    i=i-1
    if i<len(slovo)/2:
            break
