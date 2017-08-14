x=int(input("Bir deger giriniz:"))
def f(x):
    a=[x]
    while x!=1:
        if x%2==0:
            x=x/2
            a.append(x)
            print(a)
        else:
            x=(3*x+1)
            a.append(x)
            print(a)
        return(a)
sonuc=f(x)
#print(sonuc)
