"""T255 weak point (b): Theorem 4.2's printed drift and diffusion (2306.17759, p. 9-10, with S1, S2 as printed before Thm 4.2,
Sigma_lin from Thm 3.2: [V^ad V^bw + V^aw V^bd]) against section 1 (gen.py), entry by entry, random PD V, several m, g2, tau0."""
import numpy as np, itertools
from gen import bdrift, noise_basis
rng=np.random.default_rng(3)
def paper(V,g2,t0):
    m=V.shape[0]; xb=V.mean(1); xx=V.mean(); Vb=np.trace(V)/m
    S1=lambda a,d,b,w: V[a,b]*(V[d,w]-xb[d]-xb[w]+xx)
    S2=lambda a,d: V[a,a]*(V[d,d]-2*xb[d]+2*xx-Vb)
    b=np.zeros((m,m))
    for a in range(m):
        for be in range(m):
            s1=sum(V[n,k]*S1(a,n,be,k) for n in range(m) for k in range(m))/m**2
            s2=sum(V[be,n]*S2(a,n)+V[a,n]*S2(be,n) for n in range(m))/(2*m)
            b[a,be]=g2/t0**2*(s1+s2)
    idx=[(a,be) for a in range(m) for be in range(a,m)]
    Sig=np.zeros((len(idx),)*2)
    for i,(a,be) in enumerate(idx):
        for j,(d,w) in enumerate(idx):
            lin=V[a,d]*V[be,w]+V[a,w]*V[be,d]
            A=sum(V[a,k]*V[d,n]*S1(be,k,w,n)+V[a,k]*V[w,n]*S1(be,k,d,n)+V[be,n]*V[d,k]*S1(a,n,w,k)+V[be,n]*V[w,k]*S1(a,n,d,k)
                  for n in range(m) for k in range(m))/m**2
            Sig[i,j]=g2*(2-g2)*lin+g2**2/t0**2*A
    return b,Sig,idx
worst_b=worst_S=0
for m in (2,3,4,5):
    for g2 in (0.3,1.0):
        for t0 in (0.7,1.0,2.0):
            for _ in range(5):
                G=rng.standard_normal((m,m))*rng.uniform(0.3,3); V=G@G.T+0.1*np.eye(m)
                bp,Sp,idx=paper(V,g2,t0)
                bg=bdrift(V,g2,t0)
                E=noise_basis(V,g2,t0,att=True,lin=True)
                Sg=np.array([[sum(Ej[a,be]*Ej[d,w] for Ej in E) for (d,w) in idx] for (a,be) in idx])
                eb=np.abs(bp-bg).max()/np.abs(bp).max(); eS=np.abs(Sp-Sg).max()/np.abs(Sp).max()
                worst_b=max(worst_b,eb); worst_S=max(worst_S,eS)
            print("m %d g2 %.1f tau0 %.1f: max rel gap drift %.1e  Sigma %.1e"%(m,g2,t0,worst_b,worst_S),flush=True)
