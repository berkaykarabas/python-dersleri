"""üç sayı değeri giriniz ve bu girdiğiniz sayılardan en büyüklerini ekrana yazdırılacaktır."""
a = int(input("birinci sayı değerini giriniz:"))
b = int(input("ikinci sayı değerini giriniz:"))
c = int(input("üçüncü sayı değerini giriniz:"))
if (a > b and a > c):
    print("En büyük sayı değeriniz:{}".format(a))
elif (b > a and b > c):
    print("En büyük sayı değeriniz {}".format(b))
else:
    print("En büyük sayı değeriniz:{}".format(c))