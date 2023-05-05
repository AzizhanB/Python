print("""
*********************************
Faktöriyel Bulma

Çıkmak İçin q'ya Basın
*********************************
""")

while True:
    sayı = input("Sayı: ")
    if (sayı == "q"):
        print("Program Sonlandırılıyor...")
        break

    else:
        sayı = int(sayı)

        faktöriyel = 1

        for i in range(2,sayı+1):
            faktöriyel *= i
        print("Faktöriyel",faktöriyel)