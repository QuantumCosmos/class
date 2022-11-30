import numpy as np
def f(x):
    return np.exp(-x**2)


a = int(input("Enter Lower Limit: "))
b = int(input("Enter Upper Limit: "))
n = 10**6
h = (b-a)/n
if a!=b:
    xodd = np.arange(a+h, b, 2*h)
    xeven = np.arange(a+2*h, b, 2*h)

    I = (f(a)+f(b)+2*sum(f(xeven))+4*sum(f(xodd)))*h/3
    from scipy import integrate
    x = np.arange(a, b, h)
    y = f(x)
    I = integrate.simps(y, x)
    print(f"module s   = {I}")
    I = integrate.quad(f, a, b)
else:
    I = 0
print(f"numarcally = {I}")




# print(f"module q   = {I}")
# I = integrate.trapz(y, x, h)
# print(f"module t   = {I}")

# I = integrate.quad(f, 0, np.inf)
# print(f"module q i = {I}")
