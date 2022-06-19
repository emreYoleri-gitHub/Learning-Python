from csv import DictReader

# delimiter="/"
with open("products.csv") as file:
    csv_reader = DictReader(file , delimiter="|")
    for p in csv_reader:
        if (p["Category"] == "Bilgisayar"):
            print(p['ProductName'],p['Price'])