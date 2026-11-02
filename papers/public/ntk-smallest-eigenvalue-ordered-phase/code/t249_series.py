import numpy as np
from numpy.polynomial.hermite_e import hermegauss
from math import factorial, sqrt
x, w = hermegauss(200); w = w/w.sum()
def run(sw2, sb2, K=24, L=80):
    q = 1.0
    for _ in range(2000): q = sw2*np.dot(w, np.tanh(sqrt(q)*x)**2) + sb2
    He = [np.ones_like(x), x.copy()]
    for k in range(1, K): He.append(x*He[k] - k*He[k-1])
    ph = np.tanh(sqrt(q)*x)
    a = np.array([sw2*np.dot(w, ph*He[k])**2/factorial(k) for k in range(K+1)])/q
    a[0] = sb2/q
    chi = sw2*np.dot(w, (1-ph**2)**2)
    def comp(p, f):  # p(f(c)) truncated to degree K
        r = np.zeros(K+1); fp = np.zeros(K+1); fp[0] = 1
        for j in range(K+1):
            r += p[j]*fp; fp = np.convolve(fp, f)[:K+1]
        return r
    g = a.copy()  # f^l
    for l in range(1, L): g = comp(g, a)
    Phi = g/chi**L; Phi[0] -= 1/chi**L
    return q, chi, a[1], sum(a), Phi
for sw2, sb2 in [(1.5, 0.3), (1.2, 0.3), (1.5, 0.05)]:
    q, chi, a1, s, Phi = run(sw2, sb2)
    print(f"sw2 {sw2} sb2 {sb2}: q* {q:.4f} chi1 {chi:.4f} a1 {a1:.4f} sum a {s:.6f}")
    print("  p_1..p_12:", " ".join(f"{v:.3g}" for v in Phi[1:13]), " min p_1..p_24:", f"{Phi[1:].min():.3g}")
