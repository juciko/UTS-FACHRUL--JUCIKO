list = ["udin", "samsul", "dadang", "juki", "nana", "sumanto"]

print("Nama Siswa: ", list)
print("Banyak Siswa: ", len(list))

print("----------------------------------------------------------")
print("Sisa siswa setelah udin pindah")

del list[0]
print(list)
print("Sisa Siswa: ", len(list))

print("===================================")
nomer = [n**2 for n in range(1, 6)]

print(nomer)
