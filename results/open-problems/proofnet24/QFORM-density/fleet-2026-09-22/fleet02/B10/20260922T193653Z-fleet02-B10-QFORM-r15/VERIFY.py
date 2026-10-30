import math
import numpy as np

rng=np.random.default_rng(20260922)
trials=0
for _ in range(200000):
    s=10**rng.uniform(-0.2,1.2)
    d=rng.normal()*s
    g=rng.normal()*s
    f=rng.choice([-1.0,1.0])*10**rng.uniform(-0.2,1.2)
    M=np.array([[0.0,s,0.0],[s,d,g],[0.0,g,f]])
    sigma=np.linalg.svd(M,compute_uv=False)[-1]
    if sigma<0.2:
        continue
    for _ in range(20):
        u=rng.normal(size=3)
        u=u/np.linalg.norm(u)*rng.uniform(math.sqrt(0.51),1.0)
        alpha,beta,gamma=u
        if beta*beta+gamma*gamma<=0.5:
            continue
        x=abs(s*beta)
        q=float(u@M@u)
        if x<=sigma/32 and abs(q)<3*sigma/8-1e-10:
            raise AssertionError((M,sigma,u,x,q))
    trials+=1

c1=1/12
k1=(c1/1024)/(math.sqrt(c1)/32+3/8)
C1=8*math.sqrt(5)*((c1/1024)*k1)**(-0.25)
c2=7/9
k2=(c2/1024)/(math.sqrt(c2)/32+3/8)
C2=8*math.sqrt(5)*((c2/1024)*k2*(0.5**4))**(-0.25)
print(f"PASS matrices={trials}")
print(f"k(1/12)={k1:.15g} pair_constant_original={C1:.12f}")
print(f"k(7/9)={k2:.15g} pair_constant_partner={C2:.12f}")
print(f"pivot_constant_partner={128*(64/3)**0.25:.12f}")
