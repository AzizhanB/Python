print("""Karşılaştırma""")

sayı1 = int(input("Birinci Sayıyı Giriniz: "))

sayı2 = int(input("İkinci Sayıyı Giriniz: "))

sayı3 = int(input("Üçüncü Sayıyı Giriniz: "))

if (sayı1 >= sayı2 and sayı1 >= sayı3):
    print("En Büyük Sayı: ",sayı1)

elif (sayı2 >= sayı1 and sayı2 >= sayı3):
    print("En Büyük Sayı: ",sayı2)

elif(sayı3 >= sayı1 and sayı3 >= sayı2):
    print("En Büyük Sayı: ",sayı3)