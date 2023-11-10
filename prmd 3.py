#Piramida setangah

piramida = int(input('Tinggi untuk Piramida :'))
print ()

for i in range(piramida):
    for j in range(piramida-6):
      print(' ', end='')

    for k in range(i+1):
      print('* ',end='')
    print()

