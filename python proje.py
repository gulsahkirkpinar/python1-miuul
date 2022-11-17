# -*- coding: utf-8 -*-

# -- Sheet --

            #####alıştırmalar####

###soru1####
Verilen değerlerin veri yapılarını inceleyiniz.Type() metodunu kullanınız.

x = 8
type(x)

y = 3.2
type(y)

z =8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 <22
type(c)

l = [1, 2, 3, 4]
type(l)

d = {"Name": "Jake",
     "Age":27,
     "Adress": "Downtown"}
type(d)

t = ("Machine Learning", "Data Science")
type(t)

s = {"Python", "Machine Learning","Data Science"}
type(s)

#####soru2####      
Verilen string ifadenintümharflerinibüyükharfeçeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız

text = "The goal is to turn data into information, and information into insight."
a = text.upper().replace("."," ").replace(","," ").split()

a

#####SORU3#####
Adım1:Verilenlisteninelemansayısınabakınız
Adım2: Sıfırıncıveonuncuindekstekielemanlarıçağırınız.
Adım3: Verilenlisteüzerinden["D", "A", "T", "A"] listesioluşturunuz.
Adım4: Sekizinciindekstekielemanısiliniz.
Adım5: Yeni birelemanekleyiniz.
Adım6: Sekizinciindekse"N" elemanınıtekrarekleyiniz.



lst = ["D","A","T","A","S","C","I","E","N","C","E"]
len(lst)

lst[0:4]

lst.pop(8)

lst

lst.append("G")

lst

lst.insert(8,"N")

lst

#######soru 4####
Adım1: Key değerlerine erişiniz.
Adım2: Value'laraerişiniz
Adım3: Daisy key'ineait 12 değerini 13 olarak güncelleyiniz.
Adım4: Key değeriAhmet value değeri[Turkey,24] olanyeni bir değer ekleyiniz.
Adım5: Antonio'yu dictionary'den siliniz.

dict = {'Cristian':["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}

dict.keys()

dict.values()

dict['Daisy'][1] = 13

dict

dict.update({'Ahmet': ["Turkey",24]})

dict

dict.pop('Antonio')

dict

#####soru 5####
Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
return eden fonksiyon yazınız.

l = [2,13,18,93,22]

def func(liste):

   even_list = []

   odd_list = []

   for i in l:
      if i%2 == 0:
        even_list.append(i)
      else:
        odd_list.append(i)
   print(odd_list)
   print(even_list)
   return odd_list, even_list
func(l)

###soru 6####
#Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrencide tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.Beklenen çıktı:.

ogrenciler = ["Ali","Veli", "Ayşe","Talat","Zeynep","Ece"]

for index, student in enumerate(ogrenciler,1):
    if int(index)<4:

      print("Mühendislik Fakültesi", index ,".öğrenci:" + student)

    else:
      print("Tıp Fakültesi",index-int((len(ogrenciler)/2)),".öğrenci:" + student)



###soru 7#####
#Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. 
#Zip kullanarakdersbilgilerinibastırınız.BeklenenÇıktı:

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

for dk,kr,kn in zip(ders_kodu,kredi,kontenjan):
    print(f"Kredisi {kr} olan {dk} kodlu dersin kontenjanı {kn} kişidir")

#####soru 8$#####
#Aşağıda 2 adet set verilmiştir. Sizden istenil eneğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını 
#eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedi

kume1 = set(["data","python"])
kume2 = set(["data","function","qcut","lambda","python","miuul"])

def new_fnk(arg1,arg2):
  if arg1.issuperset(arg2):
      print(arg1.intersection(arg2))
  else:
      print(arg2.difference(arg1))
new_fnk(kume1,kume2)





