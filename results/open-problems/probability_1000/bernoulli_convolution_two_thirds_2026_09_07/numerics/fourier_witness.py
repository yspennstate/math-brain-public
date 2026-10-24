# Exact Fourier route.  Y = (1/3) sum_k B_k (2/3)^k with B_k fair iid, so
#   hat mu(xi) = E[e^{-2 pi i xi Y}] = prod_{k>=0} cos(pi xi (2/3)^k / 3) * (phase),
# exactly computable.  Since mu_n = law of frac(2^n Y), hat mu_n(k) = hat mu(2^n k).
# With 2U = H + Z, the square wave (-1)^{floor 2U} = (4/pi) sum_{m odd} sin(2 pi m U)/m gives
#   E[(-1)^H phi(Z)] for |phi| <= 1  =>  E[u_n^2] >= |E[(-1)^H e^{-2 pi i k Z}]|^2 ,
# and with phi = 1:  E[u_n^2] >= s_n^2,  s_n = (4/pi) sum_{m odd} Im hat mu_n(m) / m = (4/pi) sum_{m odd} Im hat mu(2^n m)/m.
import numpy as np, math, sys
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 20001     # odd m up to KMAX
NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 10
def hat_mu(xi, terms=2000):
    # returns complex hat mu(xi) = prod_k [(1 + e^{-2 pi i xi lam^k /3})/2],  lam = 2/3
    xi = np.asarray(xi, dtype=np.float64); out = np.ones(xi.shape, dtype=np.complex128)
    lam = 2.0/3.0; a = xi/3.0
    for k in range(terms):
        z = np.exp(-2j*np.pi*a); out *= (1 + z)/2
        a = a*lam
        if np.max(np.abs(a)) < 1e-16: break
    return out
ms = np.arange(1, KMAX+1, 2, dtype=np.float64)
print("n |  s_n = (4/pi) sum_odd Im hat mu(2^n m)/m  |  s_n^2 (lower bound on E[u_n^2])  |  measured E[u_n^2]")
meas = {0:2.1284e-01, 1:4.0394e-03, 2:1.1676e-03, 3:9.9085e-05, 4:2.7003e-05, 5:2.6079e-05,
        6:1.8968e-07, 7:2.3292e-08, 8:1.7489e-08, 9:9.5067e-09}
for n in range(NMAX+1):
    xi = (2.0**n)*ms
    h = hat_mu(xi)
    s = (4/np.pi)*np.sum(np.imag(h)/ms)
    m = meas.get(n)
    print(f"n={n}: s_n={s: .6e}  s_n^2={s*s:.3e}   measured Eu2={m if m is None else f'{m:.3e}'}   ratio s^2/Eu2={'' if m is None else f'{s*s/m:.4f}'}")
# how big is |hat mu| itself along the lacunary sequence
print("\n|hat mu(2^n)| for n = 0..24 (the lacunary values that control equidistribution of frac(2^n Y)):")
xs = 2.0**np.arange(0, 25)
print(np.array2string(np.abs(hat_mu(xs)), precision=4, max_line_width=200))
