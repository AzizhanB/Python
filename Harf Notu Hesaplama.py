print("""***********************************
Harf Notu Hesaplama
***********************************
""")

vize1 = int(input("Vize1: "))
vize2 = int(input("Vize2: "))
final = int(input("Final: "))

Genel_Not = vize1 * 3/10 + vize2 * 3/10 + final * 4/10

if (Genel_Not >= 90):
    print("AA")

elif (Genel_Not >= 85):
    print("BA")

elif (Genel_Not >= 80):
    print("BB")

elif (Genel_Not >= 75):
    print("CB")

elif (Genel_Not >= 70):
    print("CC")

elif (Genel_Not >= 65):
    print("DC")

elif (Genel_Not >= 60):
    print("DD")

elif (Genel_Not >= 55):
    print("FD")

else:
    print("FF")