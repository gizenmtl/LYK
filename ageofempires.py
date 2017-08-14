class Birim:
    def __init__(self,can=100,x=0,y=0):
        self.can=can
        self.x=x
        self.y=y
    def hareketEt(self,x,y):
        self.x=x
        self=y
        #hareket etme bir davranıştır.
    def solaGit(self):
        self.x-=1 #sola gitmesi için x'i azalttık herhangi bir parametre atamadık
    def sagGit(self):
        self.x+=1
    def yukariGit(self):
        self.y-=1
    def asagiGit(self):
        self.y+=1

class Isci(Birim):
    def __init__(self, ismi, can0100, x=0,y=0):
        super.()__init__(can,x,y)
        self.ismi=ismi
    def calis(self):
        print(self.ismi+" çalışıyor..")

class Asker(Birim):
    def __init__(self,saldiriGucu=7,ismi="Basit Asker",can=100,x=0,y=0):
        super().__init__(can,x,y)
        self.saldiriGucu=saldiriGucu
        self.ismi=ismi
    def saldir(self, hedef):
        hedef.can-=self.saldiriGucu
        print(self.ismi+" "+hedef.ismi+" birimine "+self.saldiriGucu+"hasar verdi")
    def savun(self):
        self.can+=5
        print(self.ismi+" birimi 5 can arttırdı ")
class Bina:
    def __init__(self,can=5000):
        self.can=can
        self.olustuMu=False #o bina daha oluşmadı demek için.
    def olustur(self):
        self.olustuMu=True #o binayı olustura geçsin ve oluştursun diye.

class Ambar(Bina):
    def __init__(self, can=700): #atama olarak yapıyoruz. fonksiyon içinde kullanmak için parametre atıyoruz.aksi taktirde değiştiremiyoruz.
        super.()__init__(can)
        self.yemek=0
    def yemekTopla(self):
        if self.olustuMu:
            self.yemek+=10
            print("Ambar'daki yeni yemek sayısı: "+str(self.yemek))
        else:
            print("Henüz ambar oluşturulmadı, kullanamazsınız. ")

class Kisla(Bina):
    def __init__(self,can=1500,maksimum=5): #maxı parametre olarak almamızın sbebi bazı kışlalar daha fazla asker alsın diye.
        super().__init__(can)
        self.askerler=[]
        self.maksimum=maksimum
    def askerUret(self):
        yeniAsker=Asker()
        if len(self.askerler)<maksimum:
            yeniAsker=Asker()
            self.askerler.append(yeniAsker)
            print("Kışladaki asker sayısı: "+str(len(self.askerler)))
        else:
            print("Kışlada yer yok asker üretilemiyor!")
class Merkez(Bina):
    def __init__(self,can=10000,maksimum=20):
        super().__init__(can)
        self.isciler=[]
        self.maksimum=maksimum
    def isciUret(self,adet=1):
        bostakiAlan=self.maksimum-len(self.isciler)
        if adet<=bostakiAlan:
            for i in range(0,adet):
                yeniIsci=Isci()
                self.isciler.append(yeniIsci)
            print(str(adet)+"adet işçi üretildi. Yeni işçi sayısı: "+str(len(self.isciler)))
        else:
            print("İşçi üretebilmek için merkezinizi geliştirmelisiniz!")
merkez=Merkez() #varsayılan değerleri zaten elimizde olduğu için bir değer vermek zorunda kalmadık.
kisla=Kisla()
ambar=Ambar()



isci_listesi=[]
for i in range(10):
    isci=isci("hareket")
    isci_listesi.append(isci)
