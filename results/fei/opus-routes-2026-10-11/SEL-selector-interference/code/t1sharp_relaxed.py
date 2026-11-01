"""Relaxed (real orthonormal leaves) T1-sharp: is E_T[Phi(c(T))] <= 0 whenever E[c c^T] = diag(p)?
Phi(c) = H(|sum_k c_k phi_k|^2) - H(c^2) - sum_k c_k^2 H(phi_k^2), phi_k = ahat_k/sqrt(p_k) (cell spectra).
Two cells on a=2 bits: A_1 = one point (p_1 = 1/4), A_2 = the rest.  Two-atom-cluster distributions near e_1, e_2."""
import numpy as np
from fei_lib import fwht_float
def H(p):
    p = np.asarray(p).ravel(); p = p[p > 1e-300]; return float(-(p*np.log2(p)).sum())
a = 2; N = 4
lab = np.array([0, 1, 1, 1])
p = np.array([np.mean(lab == k) for k in range(2)])
phis = []
for k in range(2):
    ak = (lab == k).astype(float); phis.append(fwht_float(ak)/N/np.sqrt(p[k]))
Hq = [H(ph**2) for ph in phis]
def Phi(c):
    v = c[0]*phis[0] + c[1]*phis[1]
    return H(v**2) - H(np.array(c)**2) - sum(c[k]**2*Hq[k] for k in range(2))
best = (-9, None)
for t in np.linspace(-0.4, 0.4, 161):
    # atoms: c1 = (cos t, sin t) weight w1 ; c2 = (sin s, cos s) weight w2 ; need E[c1 c2]=0, E[c_1^2]=p1
    # solve for w1, s: w1 cos t sin t + w2 sin s cos s = 0 ; w1 cos^2 t + w2 sin^2 s = p1 ; w1 + w2 = 1
    for s in np.linspace(-0.6, 0.6, 241):
        A = np.array([[np.cos(t)*np.sin(t), np.sin(s)*np.cos(s)], [np.cos(t)**2, np.sin(s)**2], [1, 1]])
        b = np.array([0, p[0], 1])
        w, res, rk, sv = np.linalg.lstsq(A, b, rcond=None)
        if np.any(w < 0) or np.linalg.norm(A@w - b) > 1e-9: continue
        val = w[0]*Phi((np.cos(t), np.sin(t))) + w[1]*Phi((np.sin(s), np.cos(s)))
        if val > best[0]: best = (val, t, s, w)
print('p =', p, ' best E[Phi] =', best)
print('--- direct check of the first-order prediction ---')
alpha = np.arcsin(np.sqrt(p[0]))
f = lambda th: H(np.array([np.cos(th)**2, np.sin(th)**2]))
fp = (f(alpha+1e-6)-f(alpha-1e-6))/2e-6
for t in (0.01, 0.03, 0.1, -0.03):
    # choose w1 ~ p1 and s from the two linear constraints
    best=None
    for s in np.linspace(-0.6,0.6,120001):
        A = np.array([[np.cos(t)*np.sin(t), np.sin(s)*np.cos(s)], [np.cos(t)**2, np.sin(s)**2]])
        b = np.array([0, p[0]])
        try: w = np.linalg.solve(A, b)
        except Exception: continue
        if abs(w.sum()-1) < 2e-6 and np.all(w>0): best=(s,w); break
    if best is None: print(t,'no solution'); continue
    s,w = best
    val = w[0]*Phi((np.cos(t), np.sin(t))) + w[1]*Phi((np.sin(s), np.cos(s)))
    print('t=',t,' s=',round(s,5),' w=',w.round(5),' E[Phi]=',val,' predicted 2 w1 t fprime=',2*w[0]*t*fp, ' Phi(e1-atom)=',Phi((np.cos(t),np.sin(t))),' Phi(e2-atom)=',Phi((np.sin(s),np.cos(s))))
