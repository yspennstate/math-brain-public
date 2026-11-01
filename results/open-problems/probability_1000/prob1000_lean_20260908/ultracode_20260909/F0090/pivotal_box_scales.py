# Second, independent check for F0090: simulate the pivotal set of the left-right crossing of an
# R x R box of critical site percolation on the triangular lattice and count, at every dyadic
# scale r, the number N_r of r-boxes that contain a pivotal site. The memo's bound is
#   H(P) <= log 2 + log 15 * sum_r E[N_r]   (N_1 = number of pivotal sites, E[N_1] = I(f)),
# and the argument claims sum_r E[N_r] <= C * I(f) with the sum dominated by the finest scale,
# E[N_r] ~ (R/r)^{3/4}. So the ratio sum_r E[N_r] / I(f) should be bounded (about 2.5) and
# stable as R grows, and log2(E N_r / E N_{2r}) should sit near 3/4.
import numpy as np, sys, time
from scipy import ndimage
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
rng=np.random.default_rng(20260909)
# triangular lattice as Z^2 with the (1,1) diagonal: 6 neighbours
struct=np.array([[1,1,0],[1,1,1],[0,1,1]],bool)
def touches(lab, nlab, mask_side):
    t=np.zeros(nlab+1,bool); t[np.unique(lab[mask_side])]=True; t[0]=False; return t
def pivotal_sites(w):
    R=w.shape[0]
    lo,no=ndimage.label(w,structure=struct); lc,nc=ndimage.label(~w,structure=struct)
    L=np.zeros_like(w); L[:,0]=True; Rt=np.zeros_like(w); Rt[:,-1]=True
    T=np.zeros_like(w); T[0,:]=True; Bt=np.zeros_like(w); Bt[-1,:]=True
    oL=touches(lo,no,L); oR=touches(lo,no,Rt); cT=touches(lc,nc,T); cB=touches(lc,nc,Bt)
    # for each site x: does some open cluster among x's 6 neighbours (or x itself if open) touch L / R
    def anyflag(lab,flag,inc_self):
        f=flag[lab]                      # per-site flag of its own cluster (0 for the other colour)
        acc=f.copy() if inc_self else np.zeros_like(f)
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)):
            s=np.zeros_like(f)
            src=f[max(0,-di):R-max(0,di), max(0,-dj):R-max(0,dj)]
            s[max(0,di):R-max(0,-di), max(0,dj):R-max(0,-dj)]=src
            acc|=s
        return acc
    A=anyflag(lo,oL,True)&anyflag(lo,oR,True)
    B=anyflag(lc,cT,True)&anyflag(lc,cB,True)
    return A&B
def box_counts(piv):
    R=piv.shape[0]; out=[]; cur=piv.copy(); r=1
    while r<=R:
        out.append(int(cur.sum()))
        if r==R: break
        cur=cur.reshape(R//r//2,2,R//r//2,2).any(axis=(1,3)); r*=2
    return out
for R in (32,64,128,256):
    ns={32:2000,64:1000,128:400,256:150}[R]; t0=time.time()
    acc=None; cross=0
    for _ in range(ns):
        w=rng.random((R,R))<0.5
        piv=pivotal_sites(w)
        c=np.array(box_counts(piv),float); acc=c if acc is None else acc+c
    EN=acc/ns; I=EN[0]; S=EN[:-1].sum()   # boxes with children only (exclude the whole box level, side R)
    ratios=[np.log2(EN[k]/EN[k+1]) if EN[k+1]>0 else float('nan') for k in range(len(EN)-1)]
    print(f"R={R:4d} samples={ns}: I(f)=E#piv={I:.2f}  sum_r E N_r (r<R) = {S:.2f}  ratio={S/I:.3f}  "
          f"log2(EN_r/EN_2r) by scale: {np.round(ratios,2).tolist()}  [{time.time()-t0:.0f}s]")
print("prediction: ratio -> about 1/(1-2^(-3/4)) =", round(1/(1-2**-0.75),3), "if E N_r = c (R/r)^{3/4} at every scale")
