import numpy as np
d1=np.diag([1,2,3]) #a diagonal(kare) matrix.köşegenlerinde değer bulunup diğerleri 0 olan matristir. diagonal matris üretmek istediğimzde diag fonksyionunu kullanıyoruz.
d2=np.diag([1,2,3], k=2) #diagonal with offset from the main diagonal
m1=np.zeros((5,4))
m2=np.ones((2,3))

print(d1)
#offset matris üretmek istedğimizde yani köşesine ya da herhangi bir yerne değerler eklemek istediğimizde kullanılıyor.
print(d2)
print(m1)
print(m2)
