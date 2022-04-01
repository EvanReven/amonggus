print("**** KALKULATOR PENJUMLAHAN*****")
pilihan =int (input("masukkan pilihan anda:"))

if (pilihan > 3):
    print("ini adalah penjumlahan")
    a = (int(input("masukkan angka pertama: ")))
    b = (int(input("masukkan angka kedua: ")))
    print("hasilnya adalah: ",a+b)

elif (pilihan < 3):
    print("ini adalah penngurangan")
    a = (int(input("masukkan angka pertama: ")))
    b = (int(input("masukkan angka kedua: ")))
    print("hasilnya adalah: ",a-b)

else :
    print("angka lu salah njirrr")
