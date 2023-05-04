"Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun."
"Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)"
kilo = float(input("Kilo değerini giriniz:"))
boy = float(input("boy değerini 'metre' cinsinden giriniz:"))
vki = kilo / (boy ** 2)
print("Kilonuz:{}\nBoyunuz:{}\nVücut Kitle Endeksiniz:{}\n".format(kilo,boy,vki))
