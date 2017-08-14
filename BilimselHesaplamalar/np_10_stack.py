import numpy as np
a=np.array([[1,2],[3,4]])
#repeat each element 3 times
print(np.repeat(a,3))
#tile the matrix 3 times
print(np.tile(a,3)) #her grubu 3er defa tekrar ediyor
b=np.array([[5,6]]) #yeni bir array oluşturduk
print(np.concatenate((a,b),axis=0)) #axis=0!! #sonra da a ile byi birleştirmek istedik.
print(np.vstack((a,b))) #vertical stack
print(np.hstack((a,b.T))) #horizontal stack
#aynı boyutta olsunlar diye b'nin transpozunu aldık
