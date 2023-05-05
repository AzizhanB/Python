import math

print("""
****************************
1.Toplama İşlemi

2.Çıkarma İşlemi

3.Çarpma İşlemi

4.Bölme İşlemi

5.Faktöriyel

6.Kalan Bulma

7.EBOB Bulma

8.Karekök Bulma

9.Üs Bulma
****************************
""")

işlem = input("İşlemi Seçiniz: ")
while True:
    if (işlem == "q"):
        print("Program Sonlandırılıyor...")
        break


    elif işlem == "1" :
        a = int(input("Birinci Sayı: "))
        b = int(input("İkinci Sayı: "))
        print("{} ile {} in toplamından çıkan sonuç {} dır".format(a,b,a+b))

    elif işlem == "2" :
        a = int(input("Birinci Sayı: "))
        b = int(input("İkinci Sayı: "))
        print("{} ile {} in çıkarılmasından kalan sonuç {} dır".format(a,b,a-b))

    elif işlem == "3" :
        a = int(input("Birinci Sayı: "))
        b = int(input("İkinci Sayı: "))
        print("{} ile {} çarpılmasından çıkan sonuç {} dır".format(a, b, a * b))

    elif işlem == "4" :
        a = int(input("Birinci Sayı: "))
        b = int(input("İkinci Sayı: "))
        print("{} ile {} bölünmesinden kalan sonuç {} dır".format(a, b, a / b))

    elif işlem == "5" :
        a = int(input("Sayı Giriniz: "))
        print("{} sayısının faktöriyeli {} dir".format(a,math.factorial(a)))

    elif işlem == "6" :
        a = int(input("Birinci Sayı: "))
        b = int(input("İkinci Sayı: "))
        print("{} sayısının {} sayısına bölümünden kalan {} dır".format(a,b,math.fmod(a,b)))

    elif işlem == "7" :
        a = int(input("Birinci Sayı: "))
        b = int(input("İkinci Sayı: "))
        print("{} sayısı ile {} sayısının en büyük ortak böleni {} dır".format(a,b,math.gcd(a,b)))

    elif işlem == "8" :
        a = int(input("Sayınızı Giriniz: "))
        print("{} sayısının karekökü {} dir".format(a,math.sqrt(a)))

    elif işlem == "9" :
        a = int(input("Sayıyı Giriniz: "))
        b = int(input("Üssü Giriniz: "))
        print("{} sayısının {}. üssü {} dır".format(a,b,math.pow(a,b)))

    else:
        print("Geçersiz İşlem.")
#Birini seçtiğinde whiledan dolayı başkasına geçemiyorsun onu çözmeye çalış