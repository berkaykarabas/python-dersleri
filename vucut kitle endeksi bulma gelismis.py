"Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun."
"Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)"
kilo = float(input("Kilo değerini giriniz:"))
boy = float(input("boy değerini 'metre' cinsinden giriniz:"))
vki = kilo / (boy ** 2)
print("Kilonuz:{}\nBoyunuz:{}\nVücut Kitle Endeksiniz:{}\n".format(kilo,boy,vki))
if (vki < 18.5) :
    print("zayıfsınız")
elif (vki >= 18.5 and vki< 25):
    print("Normalsiniz")
elif (vki >= 25 and vki < 30):
    print("kilolusunuz")
else:
    print("aşırı kilolusunuz")