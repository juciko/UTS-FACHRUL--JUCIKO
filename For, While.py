piramid = int(input("Tinggi Piramid yang diinginkan: "))

k = 0

for i in range(1, piramid+1):
    for space in range(1, (piramid-i)+1):
        print(end="  ")

    while k!=(2*i-1):
        print("Z ", end="")
        k += 1

    k = 0
    print()
