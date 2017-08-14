import numpy as np
m=np.random.rand(3,3) #3e 3lük bir matriste 0-1 arasında random değerler atıyor.
print(m)
print(m,max())
print(m.max(axis=0)) #column, her sütunun en yüksek değerini buldurur.
print(m.max(axis=1)) #row, her satırın en yüksek değerini alır.

A=np.array([[n+m*10 for n in range(5)] for m in range(5)])
n,m = A.shape #boyut değerlerini aldık.
B=A.reshape((1,n*m)) #tek bir arraye dönüştü.görüntü işlemede reshape çok kullanılır.
#print(B)
#B[0,0:5]=5 #modify the array
print(B) #b değiştiği an anında içeriği değişiyor.
print(A)
C=A.flatten() #ama burada c'de yaptığımız değişiklikler A'yı etkilemiyor.
print(C)
