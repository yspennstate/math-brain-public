"""
Numerical support for the Gumbel fluctuation conjecture (conj:gumbel) and the spherical base.
Run: python verify_gumbel.py

Conjectured limit: P{log M_m + b_m <= x} -> 1 - exp(-exp(d_F x)).  Equivalently W=-d_F(log M_m+b_m)
is standard (max) Gumbel.  Centering-free predictions:
   std(log M_m) -> pi/(d_F sqrt 6)         (real 1.2825, complex 0.6413)
   skewness(log M_m) -> -1.1395            (reflected/min Gumbel; Gaussian would be 0)
Also confirms the spherical-frame base (cor:spherical-pr): rows uniform on sphere of radius sqrt(m),
N=2m-1, should give (1/m)log M_m -> -log 4, same as Gaussian.
"""
import numpy as np
from itertools import combinations
from math import log, pi, sqrt
from scipy import stats

rng = np.random.default_rng(20260628)
def real_gauss(s): return rng.standard_normal(s)
def cplx_gauss(s): return (rng.standard_normal(s)+1j*rng.standard_normal(s))/np.sqrt(2)

def logMm_samples(m, N, gen, trials):
    subs=[list(S) for S in combinations(range(N),m)]
    out=np.empty(trials)
    for j in range(trials):
        A=gen((N,m))
        out[j]=log(min(np.linalg.svd(A[S],compute_uv=False)[-1] for S in subs))
    return out

print("="*70)
print("E. Gumbel fluctuation scale and shape  (N=2m-1)")
print(f"   predictions: std -> pi/(d_F sqrt6)  [real {pi/sqrt(6):.4f}, complex {pi/(2*sqrt(6)):.4f}];"
      f"  skewness -> {-1.1395:.4f}")
print("="*70)
for name,gen,d in [("real",real_gauss,1),("complex",cplx_gauss,2)]:
    print(f"  --- {name} (d_F={d}); target std={pi/(d*sqrt(6)):.4f} ---")
    for m in range(5,9):
        N=2*m-1; tr={5:4000,6:3000,7:1800,8:900}[m]
        x=logMm_samples(m,N,gen,tr)
        print(f"    m={m}: std(log M_m)={x.std():.4f}  skew={stats.skew(x):+.3f}  "
              f"mean(1/m logM)={x.mean()/m:+.4f}")
print("  (std should hover near the target and stay ~flat in m; skew negative toward -1.14.)")

print("="*70)
print("F. Spherical-frame base (cor:spherical-pr): rows uniform on sphere radius sqrt(m), real, N=2m-1")
print(f"   target (1/m)log M_m -> -log4 = {-log(4):.4f}")
print("="*70)
def sphere_gen(m):
    def g(shape):
        N=shape[0]; V=rng.standard_normal((N,m)); V/=np.linalg.norm(V,axis=1,keepdims=True); return V*sqrt(m)
    return g
for m in [6,8]:
    N=2*m-1; tr=400
    x=logMm_samples(m,N,sphere_gen(m),tr)
    print(f"    m={m}: (1/m)log M_m mean={x.mean()/m:+.4f}  std(log M_m)={x.std():.4f}  (cf. Gaussian session-8 trend)")
print("DONE.")
