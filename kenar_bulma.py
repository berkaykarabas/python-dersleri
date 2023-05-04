"""Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;"""



a = int(input("Girmek istediğiniz kenar sayısını giriniz"))
if (a == 3):
    birinci_kenar = abs(int(input("birinci kenar uzunluğunu giriniz:")))
    ikinci_kenar = abs(int(input("ikinci kenar uzunluğunu giriniz:")))
    ucuncu_kenar = abs(int(input("üçüncü kenar uzunluğunu giriniz:")))
    if (birinci_kenar + ikinci_kenar > ucuncu_kenar and birinci_kenar + ucuncu_kenar > ikinci_kenar and ikinci_kenar + ucuncu_kenar > birinci_kenar):
        if (birinci_kenar == ikinci_kenar or ikinci_kenar == ucuncu_kenar or birinci_kenar == ucuncu_kenar):
            print("ikizkenar üçgen")
        elif (birinci_kenar == ikinci_kenar and birinci_kenar == ucuncu_kenar):
            print("eşkenar üçgen")
        elif (birinci_kenar != ikinci_kenar and ikinci_kenar != ucuncu_kenar and birinci_kenar != ucuncu_kenar):
            print("çeşitkenar üçgen")
    else:
        print("üçgen olma şartı karşılanamadı")

elif (a == 4):
    birinci_kenar = abs(int(input("birinci kenar uzunluğunu giriniz:")))
    ikinci_kenar = abs(int(input("ikinci kenar uzunluğunu giriniz:")))
    ucuncu_kenar = abs(int(input("üçüncü kenar uzunluğunu giriniz:")))
    dorduncu_kenar = abs(int(input("dördüncü kenar uzunluğunu giriniz:")))
    if (birinci_kenar == ikinci_kenar and ikinci_kenar == ucuncu_kenar and ucuncu_kenar == dorduncu_kenar):
        print("Bu geometrik şekil karedir. Alanı {} dır".format(birinci_kenar ** 2))
    elif (birinci_kenar == ikinci_kenar and ucuncu_kenar == dorduncu_kenar or birinci_kenar == dorduncu_kenar and ikinci_kenar == ucuncu_kenar or birinci_kenar == ucuncu_kenar and ikinci_kenar == dorduncu_kenar):
        print("Bu geometrik şekil Dikdörtgendir.")
    else:
        print("Bu geometrik şekil bir dörtgendir.")