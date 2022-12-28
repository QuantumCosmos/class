import numpy as np
import matplotlib.pyplot as plt
N = 10
nconf = 5000
neqlm = 1000
nt = 32
T = np.linspace(1.54, 3.28, nt)
E = np.zeros(nt)
n1 = 1/(nconf*N*N)
config = np.random.choice([-1, 1], size=(N, N))
print(config)
def mcmove(config, beta):
    for i in range(N):
        for j in range(N):
            a = np.random.randint(0, N)
            b = np.random.randint(0, N)
            s = config[a, b] 
            nb = config[(a+1)%N, b] + config[(a-1)%N, b] + config[a, (b+1)%N] + config[a, (b-1)%N]
            cost = 2*s*nb
            if cost < 0:
                s = -1*s
            elif np.random.rand() < np.exp(-cost*beta):
                s = -1*s
            config[a, b] = s
    return


def Energy(config):
    e = 0
    for i in range(N):
        for j in range(N):
            s = config[i, j] 
            nb = config[(i+1)%N, j] + config[(i-1)%N, j] + config[i, (j+1)%N] + config[i, (j-1)%N]
            e += -nb*s
    return e/4


beta = 1/1.53

for i in range(neqlm):
    mcmove(config, beta)

for t in range(nt):
    E1 = 0
    beta = 1/T[t]
    print(t)
    for i in range(nconf):
        mcmove(config, beta)
        En = Energy(config)
        E1 += En

    E[t] = n1*E1

plt.scatter(T, E)
plt.show()

'''

40 38 42


'''
        
