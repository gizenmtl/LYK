def kayit():
    i="E"
    ogrenci=[]
    while i=="E" :
        a=[]
        name=input("Öğrenci ismi girin:")
        note1=int(input("Öğrenci notu girin:"))
        note2=int(input("Öğrenci notu girin:"))
        note3=int(input("Öğrenci notu girin:"))
        a.append(name)
        a.append(note1)
        a.append(note2)
        a.append(note3)
        ogrenci.append(a)
        i=input("Devam etmek istiyor musunuz? E/H")
    return ogrenci
ogrenci=kayit()
f=open("/home/gizen/Masaüstü/kayit2.txt", "w")
f.write(str(ogrenci))
print('ogr', ogrenci)

def ort(ogrenci):
    b=[]
    for x in ogrenci:
        L=x[1:4]
        ortalama=float(sum(L))/len(L)
        enbuyuk=max(L)
        enkucuk=min(L)
        liste=(x[0], ortalama, enbuyuk, enkucuk)
        b.append(liste)
    return(b)
from operator import itemgetter
b=ort(ogrenci)
c=sorted(b, key=itemgetter(1), reverse=True)
print("{}   {}         {}         {}".format('Name', 'Ortalama', 'En büyük', 'En düşük'))
for i in c:
    print("{}   {}   {}   {}".format(i[0], i[1], i[2], i[3]))
