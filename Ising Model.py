import numpy as np
dim = 10 #int(input())
S = np.full((dim, dim), 1)
N = 10
K = 1
T = 100


def total(S):
    J = 1
    E = E_p = 0

    def b(i, j):
        if i in range(dim) and j in range(dim):
            return S[i][j]
        else:
            return 0

    def p(i, j):
        if i in range(-1, dim) and j in range(-1, dim):
            return S[i][j]
        elif i==dim:
            return S[0][j]
        elif j==dim:
            return S[i][0]
        else:
            return 0

    for i in range(dim):
        for j in range(dim):
            E -= J*S[i][j]*(b(i+1,j)+b(i-1,j)+b(i,j+1)+b(i,j-1))
            E_p -= J*S[i][j]*(p(i+1,j)+p(i-1,j)+p(i,j+1)+p(i,j-1))

    return E_p

total_prob = 0
dist = 0
print(S)
print(total(S))

for i in range(N):
    r_x = np.random.randint(dim)
    r_y = np.random.randint(dim)
    E_prev = total(S)
    S[r_x][r_y] = -S[r_x][r_y]
    E_next = total(S)
    delta = E_next-E_prev
    prob = np.exp(-delta/(K*T))
    r_p = np.random.rand(1)[0]
    if (r_p < prob) or E_prev>E_next:
        total_prob += np.exp(-E_next/(K*T))
        dist += np.exp(-E_next/(K*T))*E_next
        E_prev = E_next
        # print(total_prob)
    else:
        S[r_x][r_y] = -S[r_x][r_y]
    
print("Last ACCEPTED config")
print(S)
print(E_prev)
# E_avg = float(dist/total_prob)
# print(f"Average Energy = {E_avg}")

