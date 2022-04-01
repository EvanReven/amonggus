"""user_input = float (input("masukkan angka yang kurang dari 3 dan lebih dari 10\n:"))
kurang_dari = (user_input < 3)
print(kurang_dari)

lebih_dari = (user_input > 10)
print(lebih_dari)

jika_bujur =kurang_dari or lebih_dari

print("angka yang di masukkan bersifat : ",jika_bujur)"""

user_input = float (input("masukkan angka yang lebih dari 3 dan kurang 10\n:"))

lebih_dari = (user_input > 3)
print(lebih_dari)

kurang_dari = (user_input < 10)
print(kurang_dari)

jika_bujur = lebih_dari and kurang_dari
print(jika_bujur)



