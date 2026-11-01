"""Relaxed two-cell problem (real orthonormal leaves): sup over laws of theta with E[cos^2 theta]=p1, E[sin 2theta]=0
of E[f(theta+alpha) - f(theta)] - f(alpha), f(t)=h2(cos^2 t), sin^2 alpha = p1.  LP on a fine grid.
Reports sup and sup/(p1 p2): a bounded ratio would support a 'half-sharp' bound with an additive kappa*B term."""
import numpy as np
from scipy.optimize import linprog
def h2(t):
    t = np.clip(t, 1e-300, 1-1e-16); return -t*np.log2(t) - (1-t)*np.log2(1-t)
th = np.linspace(-np.pi/2, np.pi/2, 20001)
for p1 in (0.5, 0.4, 0.25, 0.1, 0.03, 0.01, 0.001):
    al = np.arcsin(np.sqrt(p1))
    obj = h2(np.cos(th+al)**2) - h2(np.cos(th)**2) - h2(p1)
    A_eq = np.vstack([np.ones_like(th), np.cos(th)**2, np.sin(2*th)])
    b_eq = np.array([1.0, p1, 0.0])
    r = linprog(-obj, A_eq=A_eq, b_eq=b_eq, bounds=(0, None), method='highs')
    sup = -r.fun
    sup_atoms = th[r.x > 1e-9]
    print('p1=%.3f  sup=%.6f  sup/(p1 p2)=%.4f  atoms(theta)=%s' % (p1, sup, sup/(p1*(1-p1)), np.round(sup_atoms, 4)[:6]))
