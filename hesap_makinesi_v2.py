from math import *

print("""
1-topla
2-çıkar
3-böl
4-çarp
5-üs al
6-cos
7-sin
8-faktöriyel
""")
sayı1 = int(input("Birinci sayıyı giriniz:"))
sayı2 = int(input("ikinci sayıyı giriniz:"))
islem = input("işlemi giriniz:")
while True:
    if (islem == '1'):
        toplam = sayı1 + sayı2
        print("Toplam:", toplam)
        break
    elif (islem == '2'):
        fark = abs(sayı1 - sayı2)
        print("Fark:", fark)
        break
    elif (islem == '3'):
        sayı1=float(sayı1)
        sayı2=float(sayı2)
        bolum = sayı1 / sayı2
        print("Bölüm:", bolum)
        break
    elif (islem == '4'):
        carp = sayı1 * sayı2
        print("Çarpım", carp)
        break
    elif (islem == '5'):
        usal = pow(sayı1, sayı2)
        print("üssü", usal)
        break
    elif (islem == '6'):
        cosunual1 = cos(sayı1)
        cosunual2 = cos(sayı2)
        print("1. sayının cosinüsü {}\n2.Sayının cosinüsü{}".format(cosunual1, cosunual2))
        break
    elif (islem == '7'):
        sinal1 = sin(sayı1)
        sinal2 = sin(sayı2)
        print("1. sayının sinüsü {}\n2.Sayının sinüsü{}".format(sinal1, sinal2))
        break
    elif (islem == '8'):
        fakt1 = factorial(sayı1)
        fakt2 = factorial(sayı2)
        print("1. sayının faktöriyeli:{}\n2.Sayının faktöriyeli:{}".format(fakt1, fakt2))
        break
    elif (islem == 'q'):
        print("programdan çıkılıyor..")
        break
    else:
        print("geçersiz işlem girildi.")
