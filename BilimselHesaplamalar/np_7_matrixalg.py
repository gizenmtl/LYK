import numpy as np
A=np.array([[n+m*10 for n in range(5)] for m in range(5)])
v1=np.arange(0,5)
print(np.dot(A,A)) #array üzerinden matris carpimi (matris çarpımı yapmak istediğinde dot fonksiyonu)
print(np.dot(A,v1)) #alignmenti kendisi yaparak matris carpimi
M=np.matrix(A) #change the behaviour of A
v=np.matrix(v1).T #make it a column vector
print(A*A)
print(M*v) #transpozuyla çarpması için yaptık. Eğer T'yi oradan kaldırırsak hata verecektir.
#dot fonksiyonu matrislerin satır ve sütun sayısı eşit olmasa bile onu otomatikman ayarlıyor
