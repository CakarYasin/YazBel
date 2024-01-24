#%%                                                        SÖZLÜKLER
çeviri_tablosu = {"Ö": "O",
                  "ç": "c",
                  "Ü": "U",
                  "Ç": "C",
                  "İ": "I", 
                  "ı": "i",
                  "Ğ": "G",
                  "ö": "o",
                  "ş": "s",
                  "ü": "u",
                  "Ş": "S",
                  "ğ": "g"}
for i in çeviri_tablosu:
    print(i, " : ", çeviri_tablosu[i])

#%%

telefon_defteri = {"ahmet" : "0532 532 32 32",
                   "mehmet": "0543 543 42 42",
                   "seda" : "0533 533 33 33",
                   "eda" : "0212 212 12 12"}

kişi = input("Telefon numarasını öğrenmek için bir kişi adı girin: ")

if kişi in telefon_defteri:
    cevap = "{} adlı kişinin telefon numarası: {} "
    print(cevap.format(kişi, telefon_defteri[kişi]))
else:
    print("Aradığınız kişi telefon rehberinde yok!")

#%% 
# değerler (values), herhangi bir veri türü olabilir.
kişiler = {"Ahmet Özkoparan": ["İstanbul", "Öğretmen", 34],

           "Mehmet Yağız" : {"Memleket": "Adana",
                             "Meslek" : "Mühendis",
                             "Yaş" : 40},
           "Seda Bayrak" : 30,
           
           "Gizem Ay" : "Eskişehir",
           
           "Yunus" : True,
           
           "Azad" : (25,20)}

print(kişiler["Ahmet Özkoparan"][1])
print(kişiler["Mehmet Yağız"]["Memleket"])
print(kişiler["Seda Bayrak"])
print(kişiler["Gizem Ay"])
print(kişiler["Yunus"])
print(kişiler["Azad"])

#%% Sözlüğe eklenen sırada ekrana yazılır
sözlük = {'a': '1'}
print(sözlük)
sözlük['b'] = '2'
print(sözlük)
sözlük['e'] = '5'
print(sözlük)
sözlük['d'] = '4'
print(sözlük)
sözlük['c'] = '3'
print(sözlük)

#%%
#Sözlüğe eklenen sırada ekrana yazılır
notlar = {}

notlar["Ahmet"] = 45
notlar["Mehmet"] = 77
notlar["Seda"] = 98
notlar["Deniz"] = 95
notlar["Ege"] = 95
notlar["Zeynep"] = 100

print(notlar)

#%%
"""Bir değerin ‘anahtar’ olabilmesi için, o öğenin değiştirilemeyen (immutable) bir veri tipi olması
gerekir. Python’da şimdiye kadar öğrendiğimiz şu veri tipleri değiştirilemeyen veri tipleridir:
1. Demetler
2. Sayılar
3. Karakter Dizileri"""

sözlük = {}
l = (1,2,3)
sözlük[l] = 'falanca'
l2 = 45
sözlük[l2] = 55
l3 = 'kardiz'
sözlük[l3] = (20,45)

print(sözlük)

#%%
#Sözlük üreteçleri
isimler = ["ahmet", "mehmet", "fırat", "zeynep", "selma", "abdullah", "cem"]
sözlük = {i: len(i) for i in isimler}
print(sözlük)


#%%                                                SÖZLÜKLERİN METODLARI
sözlük = {"a": 0,
          "b": 1,
          "c": 2,
          "d": 3}
print(sözlük.keys())

listt = list(sözlük.keys())
print("list : ", listt)
tuplee = tuple(sözlük.keys())
print("tuple : ", tuplee)
strr = ",".join(sözlük.keys())
print("strr : ", strr)

for i in sözlük.keys():
    print(i)
    
#%%
#values, items
sözlük = {"a": 0,
          "b": 1,
          "c": 2,
          "d": 3}
print(sözlük.values())

listt = list(sözlük.values())
print("list : ", listt)
tuplee = tuple(sözlük.values())
print("tuple : ", tuplee)
strr = ",".join([str(i) for i in sözlük.values()])
print("strr : ", strr)

for i in sözlük.values():
    print(i)
    
for anahtar, değer in sözlük.items():
    print("{} = {} ".format(anahtar, değer))
    
#%%
sözlük = {"a": 0,
          "b": 1,
          "c": 2,
          "d": 3}
print(sözlük.get('b', "Bu kelime veritabanımızda yoktur!"))

#%%
# clear()
lig = {"şampiyon": "Adana Demirspor", 
       "ikinci": "Mersin İdman Yurdu",
       "üçüncü": "Adana Gençlerbirliği"}
print(lig)
lig.clear()
print(lig)
del lig
print(lig)

#%%
#pop
sepet = {"meyveler": ("elma", "armut"), 
         "sebzeler": ("pırasa", "fasulye"),
         "içecekler": ("su", "kola", "ayran")}

oge = sepet.pop("tatlılar", "Silinecek öğe yok!")
print(oge)
oge = sepet.pop("sebzeler", "Silinecek öğe yok!")
print(oge)
print(sepet)

#%%
#popitem() : son eklenen öğeyi siler
sepet = {}
sepet["meyveler"] = ("elma", "armut")
sepet["sebzeler"] = ("pırasa", "fasulye")
sepet["içecekler"] = ("su", "kola", "ayran")

print(sepet, '\n')
sepet.popitem()
print(sepet)

#%%
#setdefault
sepet = {"meyveler": ("elma", "armut"), "sebzeler": ("pırasa", "fasulye")}
sepet.setdefault("içecekler", ("su", "kola"))
print(sepet, '\n')
sepet.setdefault("meyveler", ("erik", "çilek"))
print(sepet, '\n')

#%%
#update()

stok = {"elma": 5, "armut": 10, "peynir": 6, "sosis": 15}
yeni_stok = {"elma": 3, "armut": 20, "peynir": 8, "sosis": 4, "sucuk": 6}
stok.update(yeni_stok)
print(stok)



#%%

harfler = "abcçdefgğhıijklmnoöprsştuüvyz"
çevrim = {i: harfler.index(i) for i in harfler}
isimler = ["ahmet", "ışık", "ismail", "çiğdem",
"can", "şule", "iskender"]
key=lambda x: çevrim.get(x[0])
# print(key("ışık"))
print(sorted(isimler, key=lambda x: çevrim.get(x[0])))

#%%

l = [2, 5, 10, 23, 3, 6]
print(map(lambda sayı: sayı ** 2, l))
print(*map(lambda sayı: sayı ** 2, l))
print([*map(lambda sayı: sayı ** 2, l)])

#%%
import sys
print(sys.getrecursionlimit())

#%%
s = [0,1,2]
print(s[3:])

#%%
def azalt(s):
    if len(s) < 1:
        return s
    else:
        print(s)
        return azalt(s[1:])
print(azalt('istihza'))

#%%
def azalt(s):
    if len(s) < 1:
        return s
    else:
        print(list(s))
        return azalt(s[1:])
print(azalt('istihza'))
#%%
def azalt(s):
    if len(s) < 1:
        return s
    else:
        print('özyineleme sürecine girerken:', s)
        azalt(s[1:])
        print('özyineleme sürecinden çıkarken:', s)
azalt('istihza')
#%%

def ters_çevir(s):
    if len(s) < 1:
        return s
    else:
        ters_çevir(s[1:])
        print(s[0])
ters_çevir("istihza")
#%%

def ters_çevir(s):
    if len(s) < 1:
        return s
    else:
        return ters_çevir(s[1:]) + s[0]
print(ters_çevir("istihza"))
#%%
def sayaç(sayı, sınır):
    print(sayı)
    if sayı == sınır:
        return 'bitti!'
    else:
        return sayaç(sayı+1, sınır)
# print(sayaç(0, 100))
sayaç(0, 100)
#%%
def sayaç(sayı, sınır):
    if sayı == sınır:
        return 'bitti!'
    else:
        sayaç(sayı+1, sınır)
        print(sayı)
print(sayaç(0, 10))
#%%
# l = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, 14]
l = 5
print(isinstance(l, list))
#%%

def düz_liste_yap(liste):
    if not isinstance(liste, list):
        return [liste]
    elif not liste:
        return []
    else:
        return düz_liste_yap(liste[0]) + düz_liste_yap(liste[1:])
l = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, 14]
print(düz_liste_yap(l))

#%%                                                         NESTED Fonksiyonlar
#                               
def yazıcı():
    def yaz(mesaj):
        print(mesaj)
    return yaz

y = yazıcı()
y("Merhaba")
print(type(y))
print(y)

#%%
#kapsayıcı olan yazıcı fonksiyonu sadece bir tane iken döndürdüğü yaz fonksiyonu birden fazla ve farklı oluyor
def yazıcı():
    def yaz(mesaj):
        print(mesaj)
    return yaz
y = yazıcı()
print(y)
b = yazıcı()
print(b)
print(yazıcı)
print(yazıcı)
#%%
#iç_fonk’un içinde kapsayıcı_fonk’a ait olan non_local_değişken değişkenini değiştirmek istenirse bu nonlocal tanımlanmalı

# def kapsayıcı_fonk():                                   #HATA
#     non_local_değişken = 1

#     def iç_fonk():

#         non_local_değişken += 1
#         print(non_local_değişken)

#     return iç_fonk


def kapsayıcı_fonk():
    non_local_değişken = 1
    
    def iç_fonk():
        nonlocal non_local_değişken
        non_local_değişken += 1
        print(non_local_değişken)
        
    return iç_fonk

y = kapsayıcı_fonk()
y()
y()
y()
y2 = kapsayıcı_fonk()
y2()
y2()

#%%
def işlem_yap(sayı, bölen, *eklenenler):
    sonuç = sayı / bölen
    for i in eklenenler:
        sonuç += i
    return sonuç

print(işlem_yap(10, 2, 5, 7))


def işlem_yapıcı(*eklenenler):
    ekle = 0
    for i in eklenenler:
        ekle += i
        
    def işlem(sayı, bölen):
        return sayı/bölen + ekle
    
    return işlem

işlemci = işlem_yapıcı(1, 4, 5)
print(işlemci(4, 2))

#%%
#return deyiminin fonksiyonu sonlandırırken yield deyimi üretecin çalışmasına ara verir ve sağındaki değişkeni geriye döndürür.
def fonksiyon_sayıcı():
    sayı = 0
    def say():
        nonlocal sayı
        sayı += 1
        return sayı
    return say

def üreteç_sayıcı():
    sayı = 0
    while True:
        sayı += 1
        yield sayı
        
print(type(fonksiyon_sayıcı))
print(type(üreteç_sayıcı))

fonk = fonksiyon_sayıcı()
üreteç = üreteç_sayıcı()

print(type(fonk))
print(type(üreteç))

print(fonk())
print(fonk())
print(fonk())

print(next(üreteç))
print(next(üreteç))
print(next(üreteç))

#%%
def üreteç():
    yield "Merhaba"
    yield "Dünya"
    
g = üreteç()
print(next(üreteç()))
print(next(üreteç()))
print(next(g))
print(next(g))
# print(next(g))

#%%
#yield from deyimi bir üretecin içinde, başka bir üretecin yield ile döndüreceği değerleri tekrar yield etmek istediğimizde kullanılabilir.
def üreteç1():
    yield "üreteç1 başladı"
    yield "üreteç1 bitti"
def üreteç2():
    yield "üreteç2 başladı"
    yield from üreteç1()
    yield "üreteç2 bitti"
    
for i in üreteç2():
    print(i)
    
#%%
listem = (i for i in range(10))
print(type(listem))

print(next(listem))
print(next(listem))
print(next(listem))

print(list(listem))

#%%

üreteç = ((str(i),i) for i in range(3))

print(dict(üreteç))
#%%
if __name__ == "__main__":
    print(2+4)
    print(__name__)