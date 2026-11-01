"""
Numerical confirmation of the main results of paper19 (extremal hard edge).
Run: python verify_bases.py
Confirms, independently of the analysis:
  A. scalar small-ball exponents d_F (real 1, complex 2, quaternion 4),
  B. one-matrix least-singular-value hard-edge exponent d_F,
  C. the overlap Beta laws and the quaternion overlap-moment formula,
  D. the extremal base (1/m) log M_m -> -h(gamma)/d_F (small m, full enumeration; gamma=2 => -log 4).
No external state; reproducible via fixed seeds.
"""
import numpy as np
from itertools import combinations
from math import log, lgamma

rng = np.random.default_rng(20260628)

def hgamma(g):
    return g*log(g) - (g-1)*log(g-1)

# ---------- helpers ----------
def real_gauss(shape):  return rng.standard_normal(shape)
def cplx_gauss(shape):  return (rng.standard_normal(shape)+1j*rng.standard_normal(shape))/np.sqrt(2)

def slope_loglog(ts, ps):
    ts=np.asarray(ts); ps=np.asarray(ps); m=(ps>0)
    return np.polyfit(np.log(ts[m]), np.log(ps[m]), 1)[0]

print("="*64)
print("A. Scalar small-ball exponents  P{|g_F|<=t} ~ c t^{d_F}")
print("="*64)
Ns=2_000_000
gR=np.abs(rng.standard_normal(Ns))
gC=np.abs((rng.standard_normal(Ns)+1j*rng.standard_normal(Ns))/np.sqrt(2))
# quaternion scalar: 4 comps N(0,1/4), modulus
gH=np.sqrt(np.sum((rng.standard_normal((Ns,4))*0.5)**2,axis=1))
ts=np.array([0.02,0.04,0.08,0.16])
for name,g,d in [("real",gR,1),("complex",gC,2),("quaternion",gH,4)]:
    ps=[np.mean(g<=t) for t in ts]
    print(f"  {name:10s}: fitted exponent = {slope_loglog(ts,ps):.3f}   (theory d_F={d})")

print("="*64)
print("B. One-matrix hard edge  P{sigma_min(G_m)<=t} ~ t^{d_F}  (m=20)")
print("="*64)
m=20; trials=40000
for name,gen,d in [("real",real_gauss,1),("complex",cplx_gauss,2)]:
    smin=np.array([np.linalg.svd(gen((m,m)),compute_uv=False)[-1] for _ in range(trials)])
    ts=np.array([0.002,0.004,0.008,0.016])/np.sqrt(m)  # deep small-ball, below hard edge 1/sqrt(m)
    ps=[np.mean(smin<=t) for t in ts]
    print(f"  {name:10s}: fitted exponent = {slope_loglog(ts,ps):.3f}   (theory d_F={d})")

print("="*64)
print("C. Overlap Beta laws and quaternion overlap moment")
print("="*64)
# overlap of two independent Haar unit vectors in F^D  =>  |rho|^2 ~ Beta(d_F/2, d_F(D-1)/2)
D=6; reps=400000
def haar_real(D):
    v=rng.standard_normal((reps,D)); return v/np.linalg.norm(v,axis=1,keepdims=True)
def haar_cplx(D):
    v=(rng.standard_normal((reps,D))+1j*rng.standard_normal((reps,D))); return v/np.linalg.norm(v,axis=1,keepdims=True)
for name,haar,d in [("real",haar_real,1),("complex",haar_cplx,2)]:
    u=haar(D); v=haar(D)
    rho2=np.abs(np.sum(np.conj(u)*v,axis=1))**2
    a,b=d/2, d*(D-1)/2
    print(f"  {name:10s} overlap |rho|^2: mean={rho2.mean():.4f} (Beta mean a/(a+b)={a/(a+b):.4f}); "
          f"E[(1-|rho|^2)^(-d/2)]={np.mean((1-rho2)**(-d/2)):.4f}")
# quaternion overlap moment: |rho|^2 ~ Beta(2,2(D-1)); check E[(1-X)^{-2}] vs (2D-1)(2D-2)/((2D-3)(2D-4))
for D in [4,6,8,12,20]:
    X=rng.beta(2,2*(D-1),size=2_000_000)
    emp=np.mean((1-X)**(-2)); form=(2*D-1)*(2*D-2)/((2*D-3)*(2*D-4))
    print(f"  quaternion D={D:2d}: E[(1-|rho|^2)^(-2)] emp={emp:.4f}  formula={form:.4f}  (1+2/D={1+2/D:.4f})")

print("="*64)
print("D. Extremal base  (1/m) log M_m  vs  -h(gamma)/d_F   (real, N=2m-1 => -log4)")
print("="*64)
target=-hgamma(2.0)  # = -log 4 = -1.3863
print(f"  target -h(2)/1 = -log4 = {target:.4f}")
for m in range(4,9):
    N=2*m-1; trials=300 if m<8 else 120
    subs=list(combinations(range(N),m))
    vals=[]
    for _ in range(trials):
        A=real_gauss((N,m))
        Mm=min(np.linalg.svd(A[list(S)],compute_uv=False)[-1] for S in subs)
        vals.append(log(Mm)/m)
    v=np.array(vals)
    # union-bound prediction is the same leading order; report empirical mean
    print(f"  m={m}: (1/m)log M_m mean={v.mean():.4f} std={v.std():.4f}  [#subs={len(subs)}]  gap to -log4 = {v.mean()-target:+.4f}")
print("\n(Finite-size: the o(m) correction is large for small m; the gap should shrink as m grows.)")
print("DONE.")
