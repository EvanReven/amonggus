print ('=KALKULATOR=')
print ("1. perkalian")
print ("2. pembagian")
print ("3. penambahan")
print ("4. pengurangan")
angka = float (input("masukkan nomor pilihan anda: "))

if (angka == 1):
  print("")
  a = input ("masukkan angka pertama : ")
  b = input ("masukkan angka kedua : ")
  print ("hasil dari",a,"x",b,"=",(int(a)*int(b)))

elif (angka == 2):
  print("")
  a = input ("masukkan angka pertama : ")
  b = input ("masukkan angka kedua : ")
  print ("hasil dari",a,":",b,"=",(int(a)/int(b)))

elif (angka == 3):
  print("")
  a = input ("masukkan angka pertama : ")
  b = input ("masukkan angka kedua : ")
  print ("hasil dari",a,"+",b,"=",(int(a)+int(b)))

elif (angka == 4):
  print("")
  a = input ("masukkan angka pertama : ")
  b = input ("masukkan angka kedua : ")
  print ("hasil dari",a,"-",b,"=",(int(a)-int(b)))

else:
  print("angka yang anda masukkan salah silahkan coba lagi")