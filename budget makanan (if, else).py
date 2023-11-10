#Rekomendasi Paket makanan Bedasarkan budget

print('=================================================================')
print('==     Selamat datang di Restoran Kami!                        ==')
print('==     Bingung mau makan apa?                                  ==')
print('==     pengen yang sesuai budget?                              ==')
print('==     tuliskan budget mu di bawah, biar kami yang beri saran! ==')
print('=================================================================')

budget = int(input('Rp :'))

if budget > 100000:    
    print('oops! Budget kamu kebesaran.. cukup seratus ribu kebawah aja ya :)')
elif budget >= 80000:
    print('1. Paket Ayam betutu')
    print('2. Paket Udang bakar')
    print('3. Paket Kepiting Racaca')
    print('Silahkan di pilih! :)')
elif budget >= 60000:
    print('1. Paket Cumi Goreng tepung')
    print('2. Paket Udang Bakar')
    print('3. Paket kerang Bale')
elif budget >= 40000:
    print('1. Paket Ayam Bakar Madu')
    print('2. Paket Lele Bakar Madura')
    print('3. Paket Kerang Asam Manis')
elif budget >= 20000:
    print('1. Paket Ca Sayuran')
    print('2. Paket Capcay seafood')
    print('3. Paket Soto')
elif budget >= 10000:
    print('1. Paket Sayur Asem')
    print('2. Paket Cah kangkung')
    print('3. Paket Sayur Sop')
else:
    print('Yah.. Budget kamu masih kurang untuk menu kita :(')