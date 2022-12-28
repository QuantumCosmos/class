import matplotlib.pyplot as plt
import numpy as np
n  = 10 #int(input())
S = np.random.choice([1, -1],size=(n,n)) # np.full((n, n), 1)
# S = np.full((n, n), 1)
N = 1000
K = 1



def tot_engr(S):
    J = 1
    E_p = 0
    for i in range(n):
        for j in range(n):
            E_p -= J*S[i, j]*(S[(i+1)%n,j]+S[(i-1)%n,j]+S[i,(j-1)%n]+S[i,(j+1)%n])

    return E_p/4

E_avg_0 = []
def chng_config(N, T, S):
    E_tot = []
    Ez = 0
    for _ in range(N):
        r_x = np.random.randint(n)
        r_y = np.random.randint(n)
        E_prev = tot_engr(S) # total energy of the system before
        S[r_x][r_y] = -S[r_x][r_y]
        E_next = tot_engr(S) # total energy of the system after
        delta = E_next-E_prev
        prob = np.exp(-delta/(K*T))
        r_p = np.random.rand(1)[0]
        if (r_p < prob) or (E_prev>E_next): # Metropolice Algorithm
            E_tot.append(E_prev) # collecting total energies of every confis
            E_prev = E_next 
        else:
            S[r_x][r_y] = -S[r_x][r_y]
        
    E_tot.append(E_prev) # getting the missed last energy
    E_avg_0.append(np.average(E_tot)) # average energy of through process of config change

T = 1.54
avg_E_list = []

T = np.linspace(T,4.28,32+10)

E = 0
for t in T:
    chng_config(5000*100, t, S) # changing the config with temp
    # Ez = tot_engr(S)
    Ex = np.average(E_avg_0) # average energy of every config done yet
    avg_E_list.append(Ex) # cumulative average while increasing the temp

plt.plot(T, avg_E_list, 'o')
plt.show()

