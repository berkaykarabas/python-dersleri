"Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre"
"yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın."

yakıt = float(input("Aracınız kilometrede ne kadar yakıyor"))
yol = float(input("Kaç km yol yaptınız"))
para = yakıt * yol
print("Toplam km başına ne  kadar yaktığınız değer:{}\nToplam gitmiş olduğunuz yol{}\nToplam ödemeniz gereken tutar{}\n".format(yakıt,yol,para))
