piramid = int(input("Tinggi Piramid yang di inginkan: "))

for i in range(piramid, 0, -1):
    for j in range(1, i+1):
        print(j, end="  ")
    print("")
