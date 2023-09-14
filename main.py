nm = 100
contador_pares = 0
while nm <= 200:
    if nm % 2 == 0:
        contador_pares = contador_pares + 1
    nm = nm + 1
print(contador_pares)

for time1 in ('Fla', 'Flu', 'Bot', 'Vas', 'Ame'):
    for time2 in ('Fla', 'Flu', 'Bot', 'Vas', 'Ame'):
        if time1 != time2:
            print(time1, 'x', time2)

