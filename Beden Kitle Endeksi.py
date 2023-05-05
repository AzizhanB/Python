print("""************************************
Beden Kitle Endeksi Hesaplama
************************************
""")

boy = float(input("Boyunuzu Giriniz: "))

kilo = int(input("Kilonuzu Girin: "))

bki = kilo / (boy ** 2)

if (bki < 18.5):
    print("Zayıfsınız.")

elif (bki >= 18.5 and bki < 25):
    print("Normalsiniz.")

elif (bki >= 25 and bki < 30):
    print("Fazla Kilolusunuz.")

else:
    print("Obezsiniz.")
