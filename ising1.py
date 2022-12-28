import numpy as np

#dim=int(input("dimension="))
dim=10
s=np.empty((dim,dim))
s.fill(1)
J,K=1,1
#s=np.random.choice([-1,1],size=(dim,dim))
#T=int(input("temperature="))
T=np.arange(1,80,2)
T3=[10,20,30,40,50]
T1=np.arange(1,801,10)
T2=np.linspace(1.54,3.28,32)
print(s)

#iter=int(input("no. of iterations="))
iter=10

def energy(s):
    Ep=0
    for i in range(dim):
        for j in range(dim):
            Ep=Ep-J*s[i,j]*(s[(i+1)%dim,j]+s[(i-1)%dim,j]+s[i,(j+1)%dim]+s[i,(j-1)%dim])
    return Ep/4

Eprev=energy(s)
E1=energy(s)
steplen=[1]
Eaverage=[]
Eavga=[]
Eavgb=[]
Eavgc=[]
for j in T2:
    
    for i in range(iter):
        Etotal=[]
        for k in range(dim):
            for l in range(dim):
                rx=np.random.randint(dim)
                ry=np.random.randint(dim)
                s[rx,ry]=-s[rx,ry]
                Enext=energy(s)
                delta=Enext-Eprev
                prob=np.exp(-delta/(K*j))
                rp=np.random.random(1)[0]
                #print(rp,prob)
                if( (delta<0)or (delta>0 and rp<prob)):
                    Eprev=Enext
                    Etotal.append(Eprev)
       
            #steplen.append(len(Etotal))
                else:
                    s[rx,ry]=-s[rx,ry]
                #print(s)
  #      print(Etotal)
        Eavg2=np.average(Etotal)
        Eavga.append(Eavg2)
    Eavg3=np.average(Eavga)
    Eavgb.append(Eavg3)

print(Eavgb)   
	
	
import matplotlib.pyplot as p
p.scatter(T2,Eavgb)
p.show()

