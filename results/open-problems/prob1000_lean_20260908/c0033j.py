import numpy as np
rng=np.random.default_rng(2027)
def from_rmk(r,m,k):
    z=1.0/(1+k+m+k*m/r); w=z*k*m/r; x=z*k; y=z*m
    return w,x,y,z
def check(r,m,k):
    w,x,y,z=from_rmk(r,m,k)
    p=np.array([w,x,y,z])
    if p.min()<=0: return None
    c2=x*y-w*z
    if c2<=0: return None
    c=np.sqrt(c2)
    a=x+z; b=y+z
    g=np.array([[b-1,a-1,-2*c],[1-b,-a,2*c],[-b,1-a,2*c],[b,a,-2*c]],dtype=float)
    G=sum(np.outer(g[i],g[i])/p[i] for i in range(4))
    absL=np.log(x*y/(w*z))
    # closed forms predicted
    g1_pred=2*(r-1)*(r-m*m)/(m*r); g2_pred=2*(r-1)*(r-k*k)/(k*r)
    return G,absL,c2,p,(G[0,2]/c,G[1,2]/c),(g1_pred,g2_pred)
print("Check the closed forms g1 = 2(r-1)(r-m^2)/(mr),  g2 = 2(r-1)(r-k^2)/(kr):")
err=0
for _ in range(3000):
    r=1+abs(rng.normal())*2; m=np.exp(rng.normal()); k=np.exp(rng.normal())
    out=check(r,m,k)
    if out is None: continue
    G,absL,c2,p,gact,gpred=out
    err=max(err,abs(gact[0]-gpred[0]),abs(gact[1]-gpred[1]))
print(f"  max |actual - closed form| over 3000 random (r,m,k): {err:.3e}")
print()
print("Now the inequality  4S + 2|L|/c^2  >=  (g1,g2) K^-1 (g1,g2)^T  in (r,m,k) coordinates:")
worst=1e18; wp=None; n=0; bad=0
while n<300000:
    r=1+abs(rng.normal())*3; m=np.exp(rng.normal()*1.5); k=np.exp(rng.normal()*1.5)
    out=check(r,m,k)
    if out is None: continue
    G,absL,c2,p,gact,_=out
    if p.min()<1e-10: continue
    n+=1
    S=(1.0/p).sum()
    K=np.array([[G[0,0],G[0,1]-absL],[G[0,1]-absL,G[1,1]]])
    gv=np.array(gact)
    try: rhs=gv@np.linalg.solve(K,gv)
    except Exception: continue
    lhs=4*S+2*absL/c2
    if lhs-rhs<worst: worst=lhs-rhs; wp=(r,m,k)
    if lhs-rhs<0: bad+=1
print(f"  n={n}  violations: {bad}   min margin {worst:+.6f} at (r,m,k)={tuple(round(v,4) for v in wp)}")
