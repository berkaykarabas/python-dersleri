print("""
**********
Atm makinesine hoşgeldiniz..

1. Bakiye Sorgulama
2. Para yatırma
3. Para Çekme
Programdan çıkmak için 'q' ya basınız..
**********
""")
bakiye = 1000
while True:
    islem = input("Yapacağınız işlemi seçiniz:")
    if (islem == 'q'):
        print("Tüm işlemler sona erdi.")
        break
    elif (islem=="1"):
        print("Bakiyeniz {} tldir.".format(bakiye))
    elif (islem == "2"):
        miktar=int(input("yatırmak istediğiniz tutar nedir?"))
        bakiye +=miktar
    elif (islem == "3"):
        miktar = int(input("çekmek istediğiniz tutar nedir?"))
        if (bakiye-miktar<0):
            print("böyle bir miktar çekemezsiniz")
            continue
        bakiye-=miktar
    else:
        print("geçersiz işlem")