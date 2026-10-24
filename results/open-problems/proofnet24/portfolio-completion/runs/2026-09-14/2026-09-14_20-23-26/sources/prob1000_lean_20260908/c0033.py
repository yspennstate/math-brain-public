import numpy as np
rng=np.random.default_rng(1)
def probs(a,b,c):
    t=c*c
    return np.array([(1-a)*(1-b)-t, a*(1-b)+t, (1-a)*b+t, a*b-t])
def H(a,b,c):
    p=probs(a,b,c); p=p[p>0]
    return float(-(p*np.log(p)).sum())
def admissible(a,b,c):
    t=c*c
    return 0<a<1 and 0<b<1 and t<min(a*b,(1-a)*(1-b))-1e-12
def hess(a,b,c,h=1e-5):
    Hs=np.zeros((3,3)); x=np.array([a,b,c])
    for i in range(3):
        for j in range(3):
            e=np.zeros(3); f=np.zeros(3); e[i]=h; f[j]=h
            Hs[i,j]=(H(*(x+e+f))-H(*(x+e-f))-H(*(x-e+f))+H(*(x-e-f)))/(4*h*h)
    return (Hs+Hs.T)/2
print("Is Ent(P_Q) concave in (a,b,c)?  Hessian eigenvalues over the admissible domain.")
worst=-1e9; worst_pt=None; n=0; viol=0
while n<60000:
    a,b=rng.random(2); c=(rng.random()*2-1)*0.5
    if not admissible(a,b,c): continue
    n+=1
    ev=np.linalg.eigvalsh(hess(a,b,c))
    if ev.max()>worst: worst=ev.max(); worst_pt=(a,b,c)
    if ev.max()>1e-6: viol+=1
print(f"  sampled {n} admissible kernels")
print(f"  points with a POSITIVE Hessian eigenvalue: {viol}")
print(f"  largest eigenvalue seen: {worst:.6e} at (a,b,c)={tuple(round(v,4) for v in worst_pt)}")

