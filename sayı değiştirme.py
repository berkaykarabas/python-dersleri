"Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin."
a = int(input("birinci sayı dğerini giriniz:"))
b = int(input("ikinci sayı dğerini giriniz:"))
print("Birinci Sayınız:{}\nİkinci Sayınız{}\n".format(a,b))
a , b = b , a
print("güncel durum")
print("Birinci Sayınız:{}\nİkinci Sayınız{}\nSayılarınızın yerleri değişmiştir.\n".format(a,b))
