import matplotlib.pyplot as plt
import numpy as np
dim = n = 10  # int(input())
S = np.random.choice([1, -1], size=(n, n))  # np.full((dim, dim), 1)
# S = np.full((dim, dim), 1)
N = 1000
K = 1


def total(S):
    J = 1
    E_p = 0
    for i in range(dim):
        for j in range(dim):
            E_p -= J*S[i, j]*(S[(i+1) % n, j]+S[(i-1) %
                              n, j]+S[i, (j-1) % n]+S[i, (j+1) % n])

    return E_p/4


def change(T, S):
    # total_E = []
    # inst_avg_E = []
    # dist = 0
    # print(S)
    # print(total(S))
    for _ in range(n):
        for _ in range(n):
            i = np.random.randint(dim)
            j = np.random.randint(dim)
            # E_prev = total(S)
            s = S[i][j]
            # E_next = total(S)
            delta = 2*s*(S[(i+1) % n, j]+S[(i-1) % n, j] +
                         S[i, (j-1) % n]+S[i, (j+1) % n])
            prob = np.exp(-delta/(K*T))
            r_p = np.random.rand(1)[0]
            # print(prob)
            # print(type(E_next), type(E_prev), type(r_p), type(prob))
            if (r_p < prob) or (delta < 0):
                S[i][j] = -s
                # total_E.append(E_prev)
                # E_prev = E_next
            # else:
            #     S[i][j] = -S[i][j]


    # total_E.append(E_next)
    # avg_E = np.average(total_E)100*N*N)
    # return avg_E
# iter = range(1, len(total_E)+1)
# avg_E_list = np.cumsum(total_E)/iter
# print("Last ACCEPTED config")
# print(S)
# print(E_prev)
Ti = 1.54
Tf = 3.28
x = 5000*100
x2 = x*5000
for _ in range(1000):
    change(Ti, S)
nt = 32
avg_E_list = np.zeros(nt)
avg_M_list = np.zeros(nt)
avg_E2_list = np.zeros(nt)
avg_M2_list = np.zeros(nt)
T = np.linspace(Ti, Tf, nt)

# E = 0
for t in range(nt):
    print(t)
    E = M = E2 = M2 = 0
    for _ in range(1000):
        change(T[t], S)
    for i in range(5000):
        change(T[t], S)
        e = total(S)
        m = np.sum(S)
        E += e
        M += m
        E2 += e*e
        M2 += m*m
    # print(S)
    # print(e, t)
    avg_E_list[t] = E/x
    avg_M_list[t] = M/(x2)
    avg_E2_list[t] = (E2/x - E*E/x2)/(T[t]*T[t])
    avg_M2_list[t] = (M2/x - M*M/x2)/T[t]

# iter = range(1, len(avg_E_list)+1)
# a = np.cumsum(avg_E_list)/iter
# print(avg_E_list)
# print(a)
# print(f"Average Energy = {avg_E}")
# # for i in range(N):
# for t in T:
#     S_T = S.copy()
#     avg_E_list.append(change(S_T, t))
fig, ax = plt.subplots(2, 2)

ax[0, 0].plot(T, avg_E_list, 'o')  # row=0, col=0
ax[1, 0].plot(T, avg_M_list, 'o')  # row=1, col=0
ax[0, 1].plot(T, avg_E2_list, 'o')  # row=0, col=1
ax[1, 1].plot(T, avg_M2_list, 'o')  # row=1, col=1
# plt.plot(T, avg_E_list, 'o')
ax[0, 0].set_xlabel("Energy")
ax[1, 0].set_xlabel("Magnetization")
ax[0, 1].set_xlabel("Specific Heat")
ax[1, 1].set_xlabel("Susceptibility")
# plt.plot(T, avg_M2_list)
# plt.show()
