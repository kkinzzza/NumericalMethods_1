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
m_T = 20
xs = np.array([i/m_T for i in range(-1*m_T, m_T+1)])
ys = np.array([1/(1+25*(x**2)) for x in xs])

xch = np.array([-cos((pi*(2*k-1))/(2*m_T)) for k in range(1, m_T+1)])
ych = np.array([1/(1+25*(x**2)) for x in xch])

Q = 0

for i in range(1, m_T):
    l = 1
    for j in range(1, m_T):
        if i != j: 
            l *= (x-xch[j])/(xch[i]-xch[j])
    Q += l*ych[i]

Q_s = sp.simplify(Q)
print(Q_s)

X1 = np.linspace(xs.min(), xs.max(), 1000)
spline1 = make_interp_spline(xs, ys)
Y1 = spline1(X1)

X2 = np.linspace(xch.min(), xch.max(), 500)
spline2 = make_interp_spline(xch, ych)
Y2 = spline2(X2)


plt.plot(X1, Y1, color='blue')
plt.plot(X2, Y2, color='red')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.title('Интерполяционный полином в форме Лагранжа \n по сетке-корням полинома Чебышева')
plt.grid(True)
plt.show()
