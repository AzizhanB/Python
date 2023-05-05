şekil = input("Hangi Şeklin Tipini Öğrenmek İstiyosunuz ?")

if (şekil == "Dörtgen"):
    print("Lütfen Kenarları Sırayla Giriniz: ")
    a = int(input("Kenar1: "))
    b = int(input("Kenar2: "))
    c = int(input("Kenar3: "))
    d = int(input("Kenar4: "))

    if (a == b and a == c and a == d):
        print("Kare")
    elif (a == c and b == d):
        print("Dikdörtgen")
    else:
        print("Dörtgen")


elif (şekil == "Üçgen"):
    a = int(input("Kenar1: "))
    b = int(input("Kenar2: "))
    c = int(input("Kenar3: "))


    if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a): #abs = mutlak değer
        if (a == b and a == c):
            print("Eşkenar Üçgen")
        elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
            print("İkizkenar Üçgen")
        else:
            print("Çeşitkenar Üçgen")
    else:
        print("Üçgen Belirtmiyor")

else:
    print("Geçersiz Şekil.")
