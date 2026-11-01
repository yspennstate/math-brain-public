try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
import numpy as np
rng=np.random.default_rng(7)
# (1) L^p lemma: int |psi|^p <= 4 pi / sqrt(p) for a spread-set law (uniform on N thin intervals)
def psi_spread(tau, starts, w):
    # f = (1/(N w)) * sum 1_[s, s+w]  with N*w = 1 -> density 1
    N=len(starts)
    base=(np.exp(1j*tau*w)-1)/(1j*tau*N*w)
    return base*np.exp(1j*np.outer(tau,starts)).sum(axis=1)
tau=np.linspace(-4000,4000,1600001); tau[tau==0]=1e-12
for N in [1,10,40]:
    w=1.0/N; starts=np.sort(rng.uniform(0,30*N,N))
    ps=np.abs(psi_spread(tau,starts,w))
    for p in [2,3,6,20]:
        val=np.trapezoid(ps**p,tau)
        print(f"N={N:3d} p={p:3d}  int|psi|^p={val:8.4f}   bound 4pi/sqrt(p)={4*np.pi/np.sqrt(p):7.3f}")
# (2) Fresnel-BL bound on |phi(t)| for A = sum_k lam_k r_k r_k^T + D (D diagonal), spread-set inputs
n=40
R,_=np.linalg.qr(rng.standard_normal((n,3)))
lev=(R**2).sum(1); print("max leverage",lev.max().round(3))
lam=np.array([1.0,1.0,-1.0]); D=rng.uniform(-5,5,n)
A=R@np.diag(lam)@R.T+np.diag(D)
Nint=10; w=1.0/Nint
starts=np.sort(rng.uniform(0,20,(n,Nint)),axis=1)
M=2_000_000
acc={}
ts=[20.0,80.0,320.0]
for chunk in range(4):
    idx=rng.integers(0,Nint,(M,n)); U=rng.uniform(0,w,(M,n))
    X=starts[np.arange(n),idx]+U
    Qv=np.einsum('ij,jk,ik->i',X,A,X)
    for t in ts:
        acc[t]=acc.get(t,0)+np.exp(1j*t*Qv).sum()
for t in ts:
    ph=abs(acc[t]/(4*M)); bd=(4*np.pi)**1.5*t**-1.5
    print(f"t={t:6.0f} |phi|~{ph:.5f} (MC se ~{1/np.sqrt(4*M):.5f})  Fresnel-BL bound {bd:.5f}")
