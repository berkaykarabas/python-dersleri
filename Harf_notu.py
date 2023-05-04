"""Öğrencilerin harf notunu hesaplayan program"""
vize1 = int(input("İlk vize notunuzu giriniz:"))
vize2 = int(input("İkinci vize notunuzu giriniz:"))
final = int(input("Final notunuzu giriniz:"))
sonuc = vize1 * 0.3 + vize2 * 0.3 + final * 0.4
if (sonuc >= 90):
    print("Aldığınız not:{} Harf notunuz AA".format(sonuc))
elif (sonuc >= 80):
    print("Aldığınız not:{} Harf notunuz BA".format(sonuc))
elif (sonuc >= 70):
    print("Aldığınız not:{} Harf notunuz BB".format(sonuc))
elif (sonuc >= 60):
    print("Aldığınız not:{} Harf notunuz CB".format(sonuc))
elif (sonuc >= 50):
    print("Aldığınız not:{} Harf notunuz CC".format(sonuc))
elif (sonuc >= 40):
    print("Aldığınız not:{} Harf notunuz DC".format(sonuc))
elif (sonuc >= 30):
    print("Aldığınız not:{} Harf notunuz DD".format(sonuc))
else:
    print("Aldığınız not:{} FF aldınız".format(sonuc))