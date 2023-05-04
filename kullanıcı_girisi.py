print("""
Kullanıcı girişi
""")

sys_kullanıcı = "Berkay"
sys_parola = "12345"

kullanıcı_adı = input("Kullanıcı adı:")
parola = input("Parola:")

if (kullanıcı_adı == sys_kullanıcı and sys_parola != parola):
    print("Parola Hatalı")
elif (kullanıcı_adı!= sys_kullanıcı and sys_parola == parola):
    print("Kullanıcı adı hatalı girildi.")
elif (kullanıcı_adı!= sys_kullanıcı and sys_parola != parola):
    print("Kullanıcı adı ve parola hatalı girildi.")
else:
    print("sisteme başarılı bir şekilde giriş yapıldı")
