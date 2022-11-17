import numpy as np
import pygame
from pygame.locals import *

# Loop Params
dim = 10
S = np.full((dim, dim), 1)
N = 1000
K = 1
T = 10
total_prob = 0
dist = 0

# Visualization Params
RED = (255, 0, 0)
WHITE = (255, 255, 255)
s_size = 500
border = 5
width = s_size/dim
display = s_size + border*(dim+1)
pygame.init()
screen = pygame.display.set_mode((display, display))
screen.fill((0, 0, 0))

# Draw colored rectangles
def draw_update(S):
    for i in range(dim):
        for j in range(dim):
            if S[i][j]+1:
                Color = RED
            else:
                Color = WHITE
            pygame.draw.rect(screen, Color, pygame.Rect(border+i*(border+width), border+j*(border+width), width, width))
    pygame.display.update()

# Calculate Total Energy
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

print("\u2022 Visuals:\n\tRED: +1\n\tWHITE: -1\n")

print(f"Model Dimension = {dim}x{dim}")
print(f"Temperature = {T}K")
print("Initial Configuration:")
print(S)
print(f"Total Energy of Initial config = {total(S)}")

# Evolve the Configuration
def config(i):
    global dist, total_prob
    # for i in range(N):
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
        draw_update(S)
    else:
        S[r_x][r_y] = -S[r_x][r_y]
    return S, E_prev


run = True
i = 0
while run:
    if i<N:
        S, E_prev = config(i)
    elif i==N:
        print("Process Compleated!")
        print("Final Configuration:")
        print(S)
        print(f"Total Energy of Final config: {E_prev}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            if i<N:
                print("Final Configuration:")
                print(S)
                print(f"Total Energy of Final config: {E_prev}")
                print(f"Process Interrupted!\n{i} iteations done of total {N}")
            run = False
    i+=1





# E_avg = float(dist/total_prob)
# print(f"Average Energy = {E_avg}")

