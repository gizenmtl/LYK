from numpy import random #specific olarak kütüphanenin içindeki bir paketi kullanmak istiyorsan böyle yaz
r1=random.rand(5) #uniform in [0,1]. 0-1 arasındaki decimal değerler üretir.içine 5 yazdığımız için 5 tane yazdırdı
r2=random.rand(4,5)#Gaussian 0-1 aralığında 4e 5lik matrisler şeklinde değerler üretir.
r3=random.random_integers(0,10) #random bir integer değer üretti.
r4=random.randn(8)#pythonun kendi numpy fonksiyonu ile numpynin kendi random fonksiyonu arasında bir fark yoktur.ama
print(r1)
print(r2)
print(r3)
#pseudo random:math fonksiyonun karşılığını çıkartır.tahmin edilebilen bir fonksiyon denir.mesela tarih saat bilgisininin cevabı tahmin edilebilir.
#real random:tahmin edilemeyen bir fonksiyondur.
