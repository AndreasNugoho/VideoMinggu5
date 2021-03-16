#Andreas Nugroho
#71200646
#endi sedang kesulitan mengerjakan tugas, tugas yang 
#endi kerjakan adalah tentang membuat program pola 
#trapesium dan persegi. bantulah endi agar bisa 
#menyelesaikan tugas tersebut

#input
#trapesium(tinggi, panjang)
#persegi(sisi)

#proses
#perulangan

#output
#pola dari pilihan user

print("Selamat Datang Di Program Pola")
print("1. Trapesium\n2. Persegi")

while True:
    pilih = input("Masukkan Pilihan Anda : ")
    if pilih in ('1','2'):
        if pilih == '1':
            tinggi = int(input("Masukkan Tinggi Trapesium : "))
            panjang = int(input("Masukan panjang Trapesium : "))
            for i in range(tinggi):
                for j in range(tinggi-i-1):
                    print(" ",end="")
                for k in range(panjang+i*2):
                    print("*",end="")
                print()
        elif pilih =='2':
            sisi = int(input("Masukan Sisi Persegi : "))
            for i in range(sisi):
                for j in range(sisi):
                    print("*",end=" ")
                print()
        break
    else:
        print("Inputan salah")


