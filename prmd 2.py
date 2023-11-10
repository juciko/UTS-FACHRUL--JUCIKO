#piramida Terbalik


piramida = int(input('tinggi Untuk Piramida :'))
print ()

for i in range(piramida):
    for j in range(i+1):
        print(' ', end='')

    for k in range(piramida-i):
        print('* ', end='')
    print ()