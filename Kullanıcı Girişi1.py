print("""***************************
Kullanıcı Girişi
***************************
""")

sys_kullanıcı_adı = "Azizhan"
sys_parola = "12345"

kullanıcı_adı = input("Kullanıcı Adı Giriniz: ")
parola = input("Parola Giriniz: ")

if (kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
    print("Parola Hatalı...")

elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola == parola):
    print("Kullanıcı Adı Hatalı Girilmiştir...")

elif (kullanıcı_adı != sys_kullanıcı_adı and sys_parola != parola):
    print("Kullanıcı Adı Ve Parola Hatalıdır...")

else:
    print("Sisteme Başarıyla Giriş Yapıldı.")