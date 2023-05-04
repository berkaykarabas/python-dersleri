print("""
-*-*-*-*-*-*-*-*-
Faktoriyel bulma programı

çıkmak için f'ye basınız
-*-*-*-*-*-*-*-*-
""")
while True:
    sayı = input("sayı:")
    if (sayı == 'q'):
        print("programdan çıkılıyor...")
        break
    else:
        sayı=int(sayı)
        faktoriyel = 1

        for i in range(2,sayı+1):
            faktoriyel*=i
        print("faktöriyel:",faktoriyel)