def tambolenleribulma(sayı):
    tambolenler=[]
    for i in range (2,sayı+1):
        if (sayı%i==0):
            tambolenler.append(i)
    return tambolenler
while True:
    sayı= input("sayı:")
    if (sayı=="q"):
        print("programdan çıkılıyor")
        break
    else:
        sayı=int(sayı)
        print("tambolenler",tambolenleribulma(sayı))