

isimler = ['Ada','Yiğit','Hasan','Beril']
yaslar = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
isimler.append("Cenk")

# 2-  "Sena" değerini listenin başına ekleyiniz.
isimler.insert(0,"Sena")

# 3-  "Yiğit" ismini listeden siliniz.
isimler.remove("Yiğit")

# 4-  "Yiğit" isminin indeksi nedir ?
index = isimler.index("Beril")
# print(index)

# 5-  "Beril" listenin bir elemanı mıdır ?
result = "Beril" in isimler
print(result)

# 6-  Liste elemanlarını ters çevirin.
isimler.reverse()

# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
isimler.sort()

# 8-  yaslar listesini rakamsal büyüklüğe göre sıralayınız.
yaslar.sort()

# 9-  s = "IPhone X,IPhone XR" karakter dizisini listeye çeviriniz.
s = "IPhone X,IPhone XR"
newList = s.split(",")
# print(newList)

# 10- yaslar dizisinin en büyük ve en küçük elemanı nedir ?
# print(2022 - min(yaslar))
# print(2022 - max(yaslar))


# 11- yaslar dizisinde kaç tane 1998 değeri vardır ?
print(yaslar.count(1998))

# 12- yaslar dizisinin tüm elemanlarını siliniz.
yaslar.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar = []

marka = input("Marka Adı: ")
markalar.append(marka)

marka = input("Marka Adı: ")
markalar.append(marka)

marka = input("Marka Adı: ")
markalar.append(marka)

print(markalar)
print(isimler)
print(yaslar)
