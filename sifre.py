import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Şifre uzunluğunu girin: "))
sifre = ""
for i in range(uzunluk):
    sifre += random.choice(karakterler)

print("Şifren:",sifre)

while True:
    begenmemek = int(input("Şifreyi beğenmediysen ve yenisini istiyorsan 1 yaz: "))
    if begenmemek == 1:
        uzunluk = int(input("Şifre uzunluğunu girin: "))
        sifre = ""
        for i in range(uzunluk):
            sifre += random.choice(karakterler)

        print("Yeni Şifren:",sifre)

    else:
        print("Yeni Şifren Hayırlı olsun")
        break
