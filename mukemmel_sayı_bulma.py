
def mukemmelsayi(sayı):
    i = 1
    toplam = 0
    while (i < sayı):
        if  (sayı % i == 0):
            toplam+=i
        i+=1
    if (toplam==sayı):
        print("bu bir mükemmel sayıdır.")
    else:
        print("bu bir mükemmel sayı değildir.")
while True:
    sayı= input("sayı:")
    if (sayı=="q"):
        print("programdan çıkılıyor")
        break
    else:
        sayı=int(sayı)
        print(mukemmelsayi(sayı))