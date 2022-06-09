sayilar = [1, 5, 16, 35, 57, 72, 75, 10]
urunler = ["iphone 8", "iphone 7", "iphone X", "iphone XR", "samsung S10"]

# 1- sayilar listesindeki her bir elemanı yazdırın.
# for sayi in sayilar:
#     print(sayi)

# 2- Sayilar listesindeki hangi sayılar 5'in katıdır ?

# for sayi in sayilar:
#     if(sayi % 5 == 0):
#         print(f"{sayi}, 5'in Katıdır.")
#     else:
#         print(f"{sayi}, 5'in Katı Değildir.")

# 3- Sayilar listesinde sayıların toplamı kaçtır ?

# toplam = 0
# for sayi in sayilar:
#     toplam += sayi
# print(toplam)

# 4- Sayilar listesindeki çift sayıların karesini alınız.
# for sayi in sayilar:
#     if sayi % 2 == 0:
#         print(f"{sayi} Sayısının Karesi: {sayi ** 2}")


# 5- urunler listesindeki tüm ürünlerin 2.karakterlerini ekrana yazdırın.

# for urun in urunler:
#     print(f"{urun} Ürününn 2. Karakteri: {urun[1]}")

# 6- urunler listesinde içinde 'iphone' geçen kaç ürün vardır? (index,find)
# count = 0
# for urun in urunler:
#     if urun.find("a"):
#         count += 1
# print(f"iphone kelimesi geçen {count} ürün vardır.")
