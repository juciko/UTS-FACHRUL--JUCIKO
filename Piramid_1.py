
piramid = int(input("Tinggi Piramid yang diinginkan: "))

for i in range(piramid):
    for j in range(i+1):
        print( j+1, end=" ")
    print()
