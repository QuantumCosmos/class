import matplotlib.pyplot as plt
import numpy as np
dim = n = 10 #int(input())
S = np.random.choice([1, -1],size=(n,n)) # np.full((dim, dim), 1)
# S = np.full((dim, dim), 1)
N = 1000
K = 1



def total(S):
    J = 1
    E_p = 0
    for i in range(dim):
        for j in range(dim):
            E_p -= J*S[i, j]*(S[(i+1)%n,j]+S[(i-1)%n,j]+S[i,(j-1)%n]+S[i,(j+1)%n])

    return E_p/4
def change(N, T, S):
    # total_E = []
    # inst_avg_E = []
    # dist = 0
    # print(S)
    # print(total(S))

    for _ in range(N):
        r_x = np.random.randint(dim)
        r_y = np.random.randint(dim)
        E_prev = total(S)
        S[r_x][r_y] = -S[r_x][r_y]
        E_next = total(S)
        delta = E_next-E_prev
        prob = np.exp(-delta/(K*T))
        r_p = np.random.rand(1)[0]
        # print(prob)
        # print(type(E_next), type(E_prev), type(r_p), type(prob))
        if (r_p < prob) or (E_prev>E_next):
            # total_E.append(E_prev)
            E_prev = E_next
        else:
            S[r_x][r_y] = -S[r_x][r_y]
        
    # total_E.append(E_next)
    # avg_E = np.average(total_E)100*N*N)
    # return avg_E
# iter = range(1, len(total_E)+1)
# avg_E_list = np.cumsum(total_E)/iter
# print("Last ACCEPTED config")
# print(S)
# print(E_prev)
T = 1
change(1000, T, S)
avg_E_list = []
T = np.linspace(T,T+1,20)

E = 0
for t in T:
    change(5000, t, S)
    e = total(S)
    E +=  e
    # print(S)
    # print(e, t)
    avg_E_list.append(E/(5000*N*N))

# iter = range(1, len(avg_E_list)+1)
# a = np.cumsum(avg_E_list)/iter
# print(avg_E_list)
# print(a)
# print(f"Average Energy = {avg_E}")
# # for i in range(N):
# for t in T:
#     S_T = S.copy()
#     avg_E_list.append(change(S_T, t))

plt.plot(T, avg_E_list, 'o')
plt.show()
