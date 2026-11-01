import numpy as np
rng=np.random.default_rng(7)
M=np.array([[0.,1,0],[1,0,0],[0,0,-2]])
def data(a,b,c):
    t=c*c
    p=np.array([(1-a)*(1-b)-t, a*(1-b)+t, (1-a)*b+t, a*b-t])
    g=np.array([[-(1-b),-(1-a),-2*c],
                [ (1-b),   -a  , 2*c],
                [  -b   , (1-a), 2*c],
                [   b   ,   a  ,-2*c]])
    return p,g
def exact_hess(a,b,c):
    p,g=data(a,b,c)
    L=np.log(p[0])+np.log(p[3])-np.log(p[1])-np.log(p[2])
    Hs=-L*M
    for i in range(4): Hs=Hs-np.outer(g[i],g[i])/p[i]
    return Hs,L,p
# verify the analytic Hessian against finite differences once
def H(a,b,c):
    p,_=data(a,b,c); return float(-(p*np.log(p)).sum())
a,b,c=0.4,0.6,0.15; h=1e-5; x=np.array([a,b,c]); FD=np.zeros((3,3))
for i in range(3):
    for j in range(3):
        e=np.zeros(3);f=np.zeros(3);e[i]=h;f[j]=h
        FD[i,j]=(H(*(x+e+f))-H(*(x+e-f))-H(*(x-e+f))+H(*(x-e-f)))/(4*h*h)
print("analytic vs finite-difference Hessian, max abs diff:", np.abs(exact_hess(a,b,c)[0]-(FD+FD.T)/2).max())
print()
print("Scan of the admissible interior, requiring min(p) > delta:")
for delta in [1e-2, 1e-3, 1e-4, 1e-6]:
    n=0; viol=0; worst=-1e9; wp=None
    while n<40000:
        a,b=rng.random(2); c=(rng.random()*2-1)*0.55
        p,_=data(a,b,c)
        if p.min()<=delta: continue
        n+=1
        Hs,L,_=exact_hess(a,b,c)
        m=np.linalg.eigvalsh(Hs).max()
        if m>worst: worst=m; wp=(a,b,c,L)
        if m>1e-9: viol+=1
    print(f"  delta={delta:<7} n={n}  positive-eigenvalue points: {viol:<6} max eig {worst:+.3e}  at (a,b,c)={tuple(round(v,4) for v in wp[:3])}, L={wp[3]:.4f}")
