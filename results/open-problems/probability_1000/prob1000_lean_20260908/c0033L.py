import numpy as np
rng=np.random.default_rng(97)
viol=[]
n=0
while n<300000:
    a,b=rng.random(2); c=(rng.random()*2-1)*0.55
    t=c*c
    p=np.array([(1-a)*(1-b)-t, a*(1-b)+t, (1-a)*b+t, a*b-t])
    if p.min()<=1e-9: continue          # strict admissibility, no tolerance games
    n+=1
    g=np.array([[b-1,a-1,-2*c],[1-b,-a,2*c],[-b,1-a,2*c],[b,a,-2*c]],dtype=float)
    G=sum(np.outer(g[i],g[i])/p[i] for i in range(4))
    absL=np.log(p[1]*p[2]/(p[0]*p[3]))
    K=np.array([[G[0,0],G[0,1]-absL],[G[0,1]-absL,G[1,1]]])
    detK=np.linalg.det(K)
    gv=np.array([G[0,2]/c,G[1,2]/c])
    S=(1.0/p).sum()
    rhs=gv@np.linalg.solve(K,gv)
    if rhs>4*S:
        viol.append((a,b,c,p.min(),detK,rhs/(4*S)))
print(f"n={n} strictly-admissible points.  RHS > 4S at {len(viol)} of them.")
if viol:
    print("  full-precision violating points:")
    for v in viol[:10]:
        print(f"    a={v[0]!r} b={v[1]!r} c={v[2]!r}  min p={v[3]:.3e}  detK={v[4]:.3e}  RHS/(4S)={v[5]:.6f}")
print()
print("Also: is det K > 0 everywhere (so the multiplied and unmultiplied forms agree)?")
n=0; neg=0; mind=1e18
rng2=np.random.default_rng(1234)
while n<200000:
    a,b=rng2.random(2); c=(rng2.random()*2-1)*0.55
    t=c*c
    p=np.array([(1-a)*(1-b)-t, a*(1-b)+t, (1-a)*b+t, a*b-t])
    if p.min()<=1e-9: continue
    n+=1
    g=np.array([[b-1,a-1,-2*c],[1-b,-a,2*c],[-b,1-a,2*c],[b,a,-2*c]],dtype=float)
    G=sum(np.outer(g[i],g[i])/p[i] for i in range(4))
    absL=np.log(p[1]*p[2]/(p[0]*p[3]))
    d=G[0,0]*G[1,1]-(G[0,1]-absL)**2
    mind=min(mind,d)
    if d<=0: neg+=1
print(f"  n={n}  det K <= 0 at {neg} points; min det K = {mind:.4f}")
