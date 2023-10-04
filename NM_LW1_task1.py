import math
import sympy as sp
import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('macosx')

def sin(x):
    return math.sin(x)

def exp(x):
    return math.exp(x)

def cos(x):
    return math.cos(x)

pi = math.pi

x = sp.Symbol('x')
m_T = 10
xs = np.array([i/m_T for i in range(int(-3*m_T), m_T+2)])
ys = np.array([exp((x**2)/5+0.3)*sin(3*x) for x in xs])

xf = np.array([(-2.5+(3.5/m_T)*k) for k in range(m_T+1)])
yf = np.array([exp((x**2)/5+0.3)*sin(3*x) for x in xf])


Q = 0

for i in range(m_T):
    l = 1
    for j in range(m_T):
        if i != j: 
            l *= (x-xf[j])/(xf[i]-xf[j])
    Q += l*yf[i]

Q_s = sp.simplify(Q)
print(Q_s)

X1 = np.linspace(xs.min(), xs.max(), 1000)
spline1 = make_interp_spline(xs, ys)
Y1 = spline1(X1)

X2 = np.linspace(xf.min(), xf.max(), 500)
spline2 = make_interp_spline(xf, yf)
Y2 = spline2(X2)


plt.plot(X1, Y1, color='blue', label='Функция')
plt.plot(X2, Y2, color='red', label='Аппроксимация')
plt.legend()
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title('Интерполяционный полином в форме Лагранжа')
plt.grid(True)
plt.show()
