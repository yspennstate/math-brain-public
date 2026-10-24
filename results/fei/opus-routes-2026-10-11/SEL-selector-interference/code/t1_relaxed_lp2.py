import numpy as np
from scipy.optimize import linprog
def h2(t):
    t = np.clip(t, 1e-300, 1-1e-16); return -t*np.log2(t) - (1-t)*np.log2(1-t)
for p1 in (1e-3, 1e-4, 1e-5, 1e-6, 1e-8):
    al = np.arcsin(np.sqrt(p1))
    # dense grid near -pi/2 (theta ~ -pi/2 + O(sqrt p1)) and a uniform grid elsewhere
    th = np.unique(np.concatenate([np.linspace(-np.pi/2, np.pi/2, 20001), -np.pi/2 + np.sqrt(p1)*np.linspace(0, 20, 4001), np.pi/2 - np.sqrt(p1)*np.linspace(0, 20, 4001)]))
    obj = h2(np.cos(th+al)**2) - h2(np.cos(th)**2) - h2(p1)
    A_eq = np.vstack([np.ones_like(th), np.cos(th)**2, np.sin(2*th)])
    r = linprog(-obj, A_eq=A_eq, b_eq=np.array([1.0, p1, 0.0]), bounds=(0, None), method='highs')
    sup = -r.fun
    at = th[r.x > 1e-12]; wt = r.x[r.x > 1e-12]
    print('p1=%.0e sup/(p1 p2)=%.4f  atoms=%s weights=%s' % (p1, sup/(p1*(1-p1)), np.round(at, 6), np.round(wt, 6)))
