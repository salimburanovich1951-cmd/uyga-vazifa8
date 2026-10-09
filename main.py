son = int(input("Juft son kiriting: "))
if son % 2 == 0:
    print("Rahmat!")
else:
    print("Bu son juft emas.")


yosh = int(input("Yoshingizni kiriting: "))
if yosh < 4 or yosh > 60:
    print("Bepul")
elif yosh < 18:
    print("Chipta narxi: 10000 so'm")
else:
    print("Chipta narxi: 20000 so'm")


a=int(input("Birinchi soni kiriting:"))
b=int(input("Ikkinchi soni kiriting:"))
if a > b:
   print(a)
   if a <b:
       print(b)
   else:
       print("Ikkala son teng")


mahsulotlar = ["anor", "uzum", "olma", "tarvuz", "qovun","un", "non", "sut", "shakar", "guruch"]
savat = []
for i in range(5):
    mahsulot = input(f"Savatga {i+1}-mahsulotni qo'shing: ")
    savat.append(mahsulot)
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(mahsulot, "- Mahsulot do'konimizda bor")
    else:
        print(mahsulot, "- Mahsulot do'konimizda yo'q")
son = int(input("Istalgan butun son kiriting: "))
for i in range(2, 11):
    if son % i == 0:
        print(son, "soni", i, "ga qoldiqsiz bo'linadi")


bor_mahsulotlar = []
mavjud_emas = []
mahsulotlar = ["un", "non", "sut", "olma", "qovun","guruch", "shakar", "tuz", "yog'", "tuxum"]
for i in range(5):
    mahsulot = input(f"Savatga {i+1}-mahsulotni qo'shing: ")
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if len(mavjud_emas) == 0:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
else:
    print("Quyidagi mahsulotlar do'konimizda yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
foydalanuvchilar = ["anvar", "ali", "vali", "hasan", "husan"]
login = input("Yangi login tanlang: ")
if login in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print("Xush kelibsiz, foydalanuvchi!")