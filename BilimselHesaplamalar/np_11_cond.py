import numpy as np
A=np.array([[n+m*10 for n in range(5)] for m in range(5)])
M=np.matrix(A)
print(M)
if (M>20).any(): #cevaplamaz true ya da false olarak döndürür
    print("at least one element in M is larger than 20")
else:
    print("None")
if (M>5).all(): #M içerisindeki bütün elemanlar 5ten büyük mü diye bakıyor.
    print("all elements in M are larger than 5")
else:
    print("all elements in M are not larger than 5")
