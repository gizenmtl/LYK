import numpy as np #buradaki np yerine herhangi birşey yazsan da olur. np olarak yazılmasının sebebi kısaltması gibi oldığu için

###################ARANGE####################################
#create a range
x1=np.arange(0,10,1) #0 başlangıç, 10 bitiş ama dahil değil, 1'de artış miktarı. arguments:start,stop,step
x2=np.arange(-1,1,0.1)
print(x1)
print(x2)


###########LINSPACE-LOGSPACE############################
l1=np.linspace(0,10,10)#0-10 arasındaki değerleri 10 parçaya bölüp lineer olarak yazdırıyor.
l2=np.logspace(0,10,10,base=2)#0-10 arasındaki değerleri 2 tabanında logaritmik olarak yazdırıyor.
print(l1)
print(l2)

#############MGRID#############################
#MESH GRID
x,y=np.mgrid[0:5,0:5]
print(x)
print(y)
