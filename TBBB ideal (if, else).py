#Penghitung Tinggi dan Berat yang ideal
print('==========================')
print('||maksimal tinggi 200cm!||')
print('==========================')
tinggi = int(input('Masukan tinggi badan :'))
berat = int(input('Masukan berat badan : '))

#Jika tinggi >=190cm

if tinggi > 200:
    print('tidak dapat menghitung melebihi 200cm.')

elif tinggi >=190:
    if (berat <65):
        print('Berat Badan kekurang!')
        print('Kami sarankan untuk memperbanyak Kalori dan banyak berolahraga angkat Beban.')
    elif (berat <90):
        print('Berat Badan Kamu Normal!')
        print('kami sarankan untuk menjaganya dan tetap olahraga seperti angkat beban, sedikit kardio dan memperbanyak protein.')
    elif (berat <110):
        print('Berat Badan Kamu kelebihan!')
        print('kami sarankan untuk diet dengan defisi kalor dan memperbanyak olahraga kardio dan angkat beban.')
    else:
        print('Kamu Obesitas!')
        print('Kami sarankan untuk konsultasi terlebih dahulu ke dokter kesehatan')

#Jika Tinggi  >=180cm

elif tinggi >=180:
    if (berat <60):
        print('Berat Badan kekurang!')
        print('Kami sarankan untuk memperbanyak Kalori dan banyak berolahraga angkat Beban.')
    elif (berat <80):
        print('Berat Badan Kamu Normal!')
        print('kami sarankan untuk menjaganya dan tetap olahraga seperti angkat beban, sedikit kardio dan memperbanyak protein.')
    elif (berat <98):
        print('Berat Badan Kamu kelebihan!')
        print('kami sarankan untuk diet dengan defisi kalor dan memperbanyak olahraga kardio dan angkat beban.')
    else:
        print('Kamu Obesitas!')
        print('Kami sarankan untuk konsultasi terlebih dahulu ke dokter kesehatan')

#Jika tinggi >=170cm

elif tinggi >=170:
    if (berat <54):
        print('Berat Badan kekurang!')
        print('Kami sarankan untuk memperbanyak Kalori dan banyak berolahraga angkat Beban.')
    elif (berat <72):
        print('Berat Badan Kamu Normal!')
        print('kami sarankan untuk menjaganya dan tetap olahraga seperti angkat beban, sedikit kardio dan memperbanyak protein.')
    elif (berat <87):
        print('Berat Badan Kamu kelebihan!')
        print('kami sarankan untuk diet dengan defisi kalor dan memperbanyak olahraga kardio dan angkat beban.')
    else:
        print('Kamu Obesitas!')
        print('Kami sarankan untuk konsultasi terlebih dahulu ke dokter kesehatan')

#Jika Tinggi >=160

elif tinggi >=160:
    if (berat <48):
        print('Berat Badan kekurang!')
        print('Kami sarankan untuk memperbanyak Kalori dan banyak berolahraga angkat Beban.')
    elif (berat <64):
        print('Berat Badan Kamu Normal!')
        print('kami sarankan untuk menjaganya dan tetap olahraga seperti angkat beban, sedikit kardio dan memperbanyak protein.')
    elif (berat <77):
        print('Berat Badan Kamu kelebihan!')
        print('kami sarankan untuk diet dengan defisi kalor dan memperbanyak olahraga kardio dan angkat beban.')
    else:
        print('Kamu Obesitas!')
        print('Kami sarankan untuk konsultasi terlebih dahulu ke dokter kesehatan')

#jika tinggi >=150

elif tinggi >=150:
    if (berat <42):
        print('Berat Badan kekurang!')
        print('Kami sarankan untuk memperbanyak Kalori dan banyak berolahraga angkat Beban.')
    elif (berat <56):
        print('Berat Badan Kamu Normal!')
        print('kami sarankan untuk menjaganya dan tetap olahraga seperti angkat beban, sedikit kardio dan memperbanyak protein.')
    elif (berat <68):
        print('Berat Badan Kamu kelebihan!')
        print('kami sarankan untuk diet dengan defisi kalor dan memperbanyak olahraga kardio dan angkat beban.')
    else:
        print('Kamu Obesitas!')
        print('Kami sarankan untuk konsultasi terlebih dahulu ke dokter kesehatan')

#jika tinggi >=140

elif tinggi >=140:
    if (berat <37):
        print('Berat Badan kekurang!')
        print('Kami sarankan untuk memperbanyak Kalori dan banyak berolahraga angkat Beban.')
    elif (berat <49):
        print('Berat Badan Kamu Normal!')
        print('kami sarankan untuk menjaganya dan tetap olahraga seperti angkat beban, sedikit kardio dan memperbanyak protein.')
    elif (berat <59):
        print('Berat Badan Kamu kelebihan!')
        print('kami sarankan untuk diet dengan defisi kalor dan memperbanyak olahraga kardio dan angkat beban.')
    else:
        print('Kamu Obesitas!')
        print('Kami sarankan untuk konsultasi terlebih dahulu ke dokter kesehatan')

#Jika tinggi >=130

elif tinggi >=130:
    if (berat <37):
        print('Berat Badan kekurang!')
        print('Kami sarankan untuk memperbanyak Kalori dan banyak berolahraga angkat Beban.')
    elif (berat <49):
        print('Berat Badan Kamu Normal!')
        print('kami sarankan untuk menjaganya dan tetap olahraga seperti angkat beban, sedikit kardio dan memperbanyak protein.')
    elif (berat <59):
        print('Berat Badan Kamu kelebihan!')
        print('kami sarankan untuk diet dengan defisi kalor dan memperbanyak olahraga kardio dan angkat beban.')
    else:
        print('Kamu Obesitas!')
        print('Kami sarankan untuk konsultasi terlebih dahulu ke dokter kesehatan')

#Kalkulator ini baru di buat untuk remaja sampai dewasa saja
#maka

else:
    print('maaf, kami belum bisa menghitung tinggi dan berat badan yang ideal buat kamu.')