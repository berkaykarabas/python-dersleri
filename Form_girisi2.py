print("""********************************
Kullanıcı giriş programı
""")

sys_kullanıcı = "Berkay"
sys_parola = "12345"
giris_hakkı = 3
while True:
    kullanıcı_adı = input("Kullanıcı adı:")
    parola = input("Parola:")
    if (kullanıcı_adı!= sys_kullanıcı and sys_parola == parola):
      print("Kullanıcı adı hatalı girildi.")
      giris_hakkı -= 1
    elif (kullanıcı_adı == sys_kullanıcı and sys_parola != parola):
      print("Parola Hatalı")
      giris_hakkı -= 1
    elif (kullanıcı_adı!= sys_kullanıcı and sys_parola != parola):
      print("Kullanıcı adı ve parola hatalı girildi.")
      giris_hakkı -= 1
    else:
        print("sisteme başarılı bir şekilde giriş yapıldı")
        break
    if (giris_hakkı==0):
        print("giriş hakkınız bitti...")
        break