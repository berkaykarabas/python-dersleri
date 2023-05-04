"Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın."

"Hipotenüs Formülü: a^2 + b^2 = c^2"
a = float(input("Birinci Kenar uzunlugunu giriniz:"))
b = float(input("İkinci Kenar uzunlugunu giriniz:"))
c = (a ** 2 + b ** 2) ** 0.5
print("Birinci Kenar:{}\nİkinci Kenar:{}\nHipotenüs{}\n".format(a,b,c))