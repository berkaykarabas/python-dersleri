import time
import random
print("""
***********************************
sayı tahmini oyunu
1 ile 40 arasında sayıyı tahmin edin-
***********************************
""")
rastgele_sayı = random.randint(1,40)
tahmin_hakkı=7
while True:
    tahmin=int(input("Tahmininiz:"))
    if (tahmin<rastgele_sayı):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("Daha yüksek bir sayı söyleyin.")
        tahmin_hakkı-=1
        print("Kalan tahmin hakkınız", tahmin_hakkı)
    elif (tahmin>rastgele_sayı):
        print("Bilgiler Sorgulanıyor...")
        time.sleep(1)
        print("daha düşük bir sayı söyleyin")
        tahmin_hakkı-=1
        print("Kalan tahmin hakkınız",tahmin_hakkı)
    else:
        print("Bilgiler Sorgulanıyor.")
        time.sleep(1)
        print("Tebrikler! tahmininiz doğru sayınız:",rastgele_sayı)
        break
    if (tahmin_hakkı==0):
        print("Tahmin hakkınız bitti")
        print("sayınız:",rastgele_sayı)
        break

