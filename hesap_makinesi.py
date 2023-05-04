print("""Hesap makinesi programı * * * *
1. toplama işlemi
2. çıkarma işlemi
3. çarpma işlemi
4. bölme işlemi
* * * * 
   """)
a = int(input("birinci sayı"))
b = int(input("ikinci sayı"))
islem = int(input("Lütfen işlemi giriniz"))
if islem == 1 :
    print("{} ile {} in toplamı {} dir.".format(a,b,a+b))
elif islem == 2 :
    print("{} ile {} in farkı {} dir.".format(a, b, a - b))
elif islem == 3 :
    print("{} ile {} in çarpımı {} dir.".format(a, b, a * b))
elif islem == 4 :
    print("{} ile {} in bölümü {} dir.".format(a, b, a / b))
else:
    print("Geçersiz işlem girdiniz")
