import numpy as np
import matplotlib.pyplot as plt

data=np.genfromtxt('stockholm_td_adj.dat')#generate from txt'nin kısaltması
#print(data.shape)
fig, ax=plt.subplots(figsize=(14,4))
ax.plot(data[:,0]+data[:,1]/12.0+data[:,2]/365,data[:,5])
ax.axis('tight') #grafikteki çizgileri sıkılaştırmak için. bir parametredir.
ax.set_title('tempeatures in Stockholm')
ax.set_xlabel('year')
ax.set_ylabel('temperature (C)')
plt.show(fig)

m=np.random.rand(3,4)
np.savetxt("deneme.csv",m) #bu dosyanın türü txt de olabilirdi.bize bağlı.csv'nin avantajlarından biri excel formatına göre datayı küçültüyor, virgülle ayırdığımızda arrayin her birinin indeksiymiş gibi görüyor.

print(m)
print(m.itemsize) #bytes per element (her bir byte için)
print(m.nbytes) #number of bytes
print(m.ndim) #number of dimensions (her bir boyut için)
