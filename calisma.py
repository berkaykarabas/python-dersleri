"""Her bir while döngüsünde kullanıcıdan bir sayı alın ve
kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin.
 Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve ekrana "toplam değişkenini" bastırın."""
print("""
Çıkmak için q'ya basınız...
""")
sayı=0
toplam=0
while True:
    sayı=input("sayı giriniz")
    if (sayı=='q'):
        print("programdan çıkılıyor..")
        break
    else:
        sayı=int(sayı)
        toplam+=sayı
        print("toplam",toplam)