# 1- 3 ürün bilgisini (id,ad,fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.

urunler = {
    '1': {
        'ad': 'ad 1', 
        'fiyat': 'fiayt 1'
    }, 
    '2': {
        'ad': 'ad 2',
        'fiyat': 'fiyat 2'
    }, 
    '3': {
        'ad': 'ad 3',
        'fiyat': 'fiyat 3'
     }
}

# id = input("id: ")
# ad = input("ad: ")
# fiyat = input("fiyat: ")

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat,
# }

# id = input("id: ")
# ad = input("ad: ")
# fiyat = input("fiyat: ")

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat,
# }


# id = input("id: ")
# ad = input("ad: ")
# fiyat = input("fiyat: ")

# urunler[id] = {
#     "ad": ad,
#     "fiyat": fiyat,
# }

id = input("Aramak istediğiniz ürün Id: ")
urun = urunler[id]


print(f"id: {id} ürün adı: {urun['ad']} ürün fiyatı: {urun['fiyat']}")