try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# N1: check int |psi|^p <= 4 pi / sqrt(p) (all real p>=2) and <= 2 sqrt2 pi/sqrt(p) (even p)
# for several densities bounded by 1.  psi computed in closed form for unions of unit-density intervals.
import numpy as np
def psi_union(t, intervals):
    # law: density 1 on disjoint intervals (a,b) of total length 1
    t = np.asarray(t, float); out = np.zeros_like(t, dtype=complex)
    for a, b in intervals:
        with np.errstate(divide='ignore', invalid='ignore'):
            v = (np.exp(1j*t*b) - np.exp(1j*t*a))/(1j*t)
        v[t == 0] = b - a
        out += v
    return out
laws = {
 'uniform':        [(-0.5, 0.5)],
 'two_pieces_h3':  [(-1.75, -1.25), (1.25, 1.75)],
 'lattice_10x_h7': [(k*7 - 0.05, k*7 + 0.05) for k in range(-5, 5)],
 'lattice_20x_h31':[(k*31 - 0.025, k*31 + 0.025) for k in range(-10, 10)],
}
T = 4000.0; N = 4_000_001
t = np.linspace(-T, T, N); dt = t[1]-t[0]
print("law, p, int|psi|^p, 4pi/sqrt(p), 2sqrt2 pi/sqrt(p)  (tail beyond T bounded by 2*sum(1/(|t|*len))^p ... negligible for p>=2.5)")
for name, iv in laws.items():
    a = np.abs(psi_union(t, iv))
    for p in [2, 2.5, 3, 4, 6, 10]:
        val = np.sum(a**p)*dt
        print(f"{name:16s} p={p:5.1f}  {val:9.4f}  {4*np.pi/np.sqrt(p):8.4f}  {2*np.sqrt(2)*np.pi/np.sqrt(p):8.4f}")
