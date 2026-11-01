import numpy as np, math, json

rng=np.random.default_rng(20260923204505)
viol=0
min_margin=float('inf')
min_eta_margin=float('inf')
cases=0
closed=0
for _ in range(10000):
    m=int(rng.integers(3,12))
    q=int(rng.integers(2,15))
    u=rng.normal(size=m); u/=np.linalg.norm(u)
    lam=float(rng.uniform(1.0,4.0))*(1 if rng.random()<.5 else -1)
    c=0.8*abs(lam)
    b=float(rng.uniform(0.05,0.35))*c/m
    Z=rng.normal(size=(m,m)); Z=(Z+Z.T)/2
    P=np.eye(m)-np.outer(u,u)
    E=P@Z@P
    op=np.linalg.norm(E,2)
    if op>0: E*=0.9*b/op
    C=lam*np.outer(u,u)+E
    B=rng.normal(size=(m,q))*rng.uniform(.2,2.0)
    G=C@C+B@B.T
    eig=np.linalg.eigvalsh(G)[::-1]
    g=math.sqrt(max(eig[2],0))
    sC=np.linalg.svd(C,compute_uv=False)
    if not (sC[1] <= b+1e-8 and b<c/m and g>b):
        continue
    i=int(np.argmax(np.abs(u)))
    K=[j for j in range(m) if j!=i]
    a=C[i,i]
    r=C[K,i]
    eta=r/a
    alpha=c/m-b
    L=(c/math.sqrt(m)+b)/alpha
    min_eta_margin=min(min_eta_margin,L-np.linalg.norm(eta))
    d=math.sqrt(max(g*g-b*b,0))
    h=np.linalg.norm(B[i,:])
    Bk=B[K,:]
    Bp=Bk-np.outer(eta,B[i,:])
    sBp=np.linalg.svd(Bp,compute_uv=False)
    s2bp=sBp[1] if len(sBp)>1 else 0
    Delta=math.sqrt(max(d*d-h*h,0))-L*h
    margin=s2bp-Delta
    min_margin=min(min_margin,margin)
    cases+=1
    if Delta>0: closed+=1
    if margin < -1e-7 or np.linalg.norm(eta)>L+1e-7 or abs(a)<alpha-1e-7:
        viol+=1
        break

print(json.dumps({
    'seed':20260923204505,
    'admissible_cases':cases,
    'violations':viol,
    'positive_Delta_cases':closed,
    'minimum_singular_margin':min_margin,
    'minimum_eta_budget_margin':min_eta_margin,
    'status':'sanity_check_only_not_proof'
},indent=2))
