numb = input('Напиши натуральное число, и я сделаю из него магический треугольник!\n')
lim = int(numb) + 1
for sec in range(1, lim):
    res = ''
    for rep in range(sec, lim):
        res = res + str(rep) + ' '
    print(res)
