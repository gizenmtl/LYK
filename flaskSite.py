from flask import Flask, render_template, request, redirect #template dosyasını burada render ettik.Flask'ın içindeki request'i import ettik burada.
import json
app=Flask(__name__) #name burada flaskSite olarak çalıştırdığımız dosyanın ismi anlamındadır ama tavsiye olarak name kullanmak iyidir.
kullanicilar={"ahmet":"aksoy","selim":"koc","ayse":"donmez"}
json_file="kisiler.json"

@app.route("/") #alttaki fonksiyonum /'da çalışıyor demek.'
def hello():
    isimler=["Ahmet","Burak","Ayse","Ali"]
    return render_template("index.html",isimlistesi=isimler) #return hello world yerine render ettiğimiz template'i yazdırdık
@app.route("/kullanicilar") #alttaki fonksiyonum /'da çalışıyor demek.'
def kullanicilar():
    try:
        kisilistesi=json.load(open(json_file,"r")) #kullanıcıya göstermek yerine ekleme yapmak için. yoksa önceki kullanıcıları siler bunu eklerdi
    except:
        kisilistesi=[] #eğer bir hata çıkarsa kişi listesini boş bir array olarak tanımladık.kişi oluşturulmamış olarak gözüksün diye.
    return render_template("kullanici_kaydi.html",kisilistesi=kisilistesi)

@app.route("/kullanici_kaydet", methods=("POST", "GET"))
def kullanici_kaydet():
    try:
        kisilistesi=json.load(open(json_file,"r"))
    except:
        kisilistesi=[]
    if request.method=="POST":
        if request.form.get('isim',None) and request.form.get('telefon',None):
            if len(kisilistesi)>0:
                uid=kisilistesi[-1].get("id")+1
            else:
                uid=1
            kisilistesi.append({"isim":request.form.get('isim'),"telefon":request.form.get('telefon'),"id":uid, "bio":request.form.get('bio')})
            open(json_file,"w").write(json.dumps(kisilistesi)) #dosya yaazma işlemi. json dumps komutuyla elimizde olan dict objelerini stringe çeviriyor.
    return redirect("/kullanicilar") #post işlemini yaptıktan sonra kullanıcılar sayfasına geri dönecek.
@app.route("/kisi/<int:uid>")
def kisi_goruntuleme(uid):
    try:
        kisilistesi=json.load(open(json_file,"r"))
    except:
        kisilistesi=[]
    bulunan_kisi=None
    for kisi in kisilistesi:
        if kisi.get("id")==uid:
            bulunan_kisi=kisi
    return render_template("kisi.html",kisi=bulunan_kisi)

@app.route("/kullanici/<kullanici>")
def kullanicilar_goruntuleme(kullanici):
    if kullanicilar.get(kullanici,None):
        bulunan_kullanici=kullanicilar.get(kullanici)
    else:
        bulunan_kullanici=None
    return render_template("kullanici.html",bulunan=bulunan_kullanici,kullanici_url=kullanici) #fonksiyonumuza gelen kullanıcıyı da atadık. kullanıcı da route'dan geliyor.

@app.route("/secondpage")
def second_page():
    return "second page"
@app.route("/x")
def x():
    return "Gizen MUTLU"
app.run(debug=True, host="0.0.0.0", port=5000) #bu da kodları çalıştırması için. debug true ise her defasında değişiklik yaptığımızda terminalden yenilememek için.
#0.0.0.0 bizim tüm requestlerimizi dinle anlamına gelir.
#port ise her zaman integer değeri almak zorunda, host ise her zaman string olmak zorunda. port bizim localhost uzantımızdaki 5000 değeri olur.
