# 1- Girilen 2 sayıdan hangisi büyüktür ?

""" 
sayi1, sayi2 = int(input("x: ")), int(input("y: "))
sonuc = sayi1 > sayi2
print(f"{sayi1} {sayi2}'den büyüktür: {sonuc}")
 """

# 2- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

""" sayi1 = int(input("x: "))
sonuc = (sayi1 % 2 == 0)

print(f"{sayi1} çift sayıdır: {sonuc}")
 """

# 3- Girilen bir sayının negatif pozitif durumunu yazdırın.

""" sayi1 = int(input("x: "))
sonuc = sayi1 > 0

print(f"Girilen sayı pozitif: {sonuc}")
 """

# 4- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.

""" vize1, vize2, final = (
    int(input("Vize 1: ")),
    int(input("Vize 2: ")),
    int(input("Final : ")),
)
genelOrt = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)

sonuc = genelOrt > 50  # Boolean

print(f"Öğrenci geçiş durumu: {sonuc} , Ortalamanız: {genelOrt}")

 """
# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: info@sadikturan.com parola:12345)

""" _email = "info@sadikturan.com"
_password = "12345"

email, password = input("Email: "), input("Password: ")
isEmail = email.lower().strip() == _email
isPassword = password.lower().strip() == _password

print(f"Email doğrulugu : {isEmail} , ve parola Doğrulugu {isPassword}")
 """