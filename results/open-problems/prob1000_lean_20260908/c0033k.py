import numpy as np
rng=np.random.default_rng(5150)
def data(r,m,k):
    z=1.0/(1+k+m+k*m/r); w=z*k*m/r; x=z*k; y=z*m
    p=np.array([w,x,y,z])
    if p.min()<=1e-12: return None
    c2=x*y-w*z
    if c2<=1e-14: return None
    c=np.sqrt(c2); a=x+z; b=y+z
    g=np.array([[b-1,a-1,-2*c],[1-b,-a,2*c],[-b,1-a,2*c],[b,a,-2*c]],dtype=float)
    G=sum(np.outer(g[i],g[i])/p[i] for i in range(4))
    absL=np.log(r)
    K=np.array([[G[0,0],G[0,1]-absL],[G[0,1]-absL,G[1,1]]])
    gv=np.array([G[0,2]/c,G[1,2]/c])
    try: rhs=gv@np.linalg.solve(K,gv)
    except Exception: return None
    S=(1.0/p).sum()
    return S,absL,c2,rhs
print("Where does the WEAKER claim  RHS <= 4S  fail?  (that is the region needing the log term)")
rs=[]; n=0; fails=[]
while n<300000:
    r=1+abs(rng.normal())*4; m=np.exp(rng.normal()*1.6); k=np.exp(rng.normal()*1.6)
    d=data(r,m,k)
    if d is None: continue
    n+=1
    S,absL,c2,rhs=d
    if rhs>4*S: fails.append((r,m,k,rhs/(4*S),2*absL/c2))
print(f"  n={n}   RHS>4S at {len(fails)} points")
if fails:
    fr=np.array([f[0] for f in fails])
    print(f"  those points have r in [{fr.min():.3f}, {fr.max():.3f}], median {np.median(fr):.3f}")
    print(f"  worst ratio RHS/(4S) = {max(f[3] for f in fails):.4f}")
    print("  and at those points the log term 2|L|/c^2 is:")
    lt=np.array([f[4] for f in fails]); print(f"    min {lt.min():.1f}, median {np.median(lt):.1f}  (vs the shortfall RHS-4S)")
    sh=[ (f[3]-1)*4 for f in fails]
    print(f"  in every case does 2|L|/c^2 cover the shortfall? ", all(f[4] > (f[3]-1)*4*1 for f in fails))
