print("Oyuncu Kaydetme Programı")

isim = input("Oyuncunun İsmi : ")
soyisim = input("Oyuncunun Soyismi : ")
takım = input("Oyuncunun Takımı : ")

bilgiler = [isim,soyisim,takım]

print("Bilgiler Kaydediliyor...")

print("Oyuncu İsmi : {}\nOyuncu Soyismi : {}\nOyuncu Takımı : {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2],))

print("Bilgiler Kaydedildi...")