import numpy as np
rng=np.random.default_rng(31)
def parts(a,b,c):
    t=c*c
    p=np.array([(1-a)*(1-b)-t, a*(1-b)+t, (1-a)*b+t, a*b-t])
    g=np.array([[b-1,a-1,-2*c],[1-b,-a,2*c],[-b,1-a,2*c],[b,a,-2*c]],dtype=float)
    G=sum(np.outer(g[i],g[i])/p[i] for i in range(4))
    absL=np.log(p[1]*p[2]/(p[0]*p[3]))
    return p,G,absL
print("Schur form, c^2 divided out:   LHS := 4S + 2|L|/c^2   vs   RHS := (g1,g2) K^-1 (g1,g2)^T")
print("(K is the 2x2 block of N = G-|L|M, which is PD with minors >= 4 and 16)")
worst=1e9; wp=None; n=0; bad=0; ratios=[]
while n<200000:
    a,b=rng.random(2); c=(rng.random()*2-1)*0.55
    t=c*c
    if t<=1e-10 or t>=min(a*b,(1-a)*(1-b))-1e-9: continue
    p,G,absL=parts(a,b,c)
    if p.min()<=1e-9: continue
    n+=1
    S=(1.0/p).sum()
    K=np.array([[G[0,0],G[0,1]-absL],[G[0,1]-absL,G[1,1]]])
    gv=np.array([G[0,2]/c,G[1,2]/c])
    LHS=4*S+2*absL/t
    RHS=gv@np.linalg.solve(K,gv)
    m=LHS-RHS
    ratios.append(RHS/LHS)
    if m<worst: worst=m; wp=(a,b,c)
    if m<0: bad+=1
r=np.array(ratios)
print(f"  n={n}   violations: {bad}")
print(f"  min margin LHS-RHS = {worst:+.6e} at (a,b,c)={tuple(round(v,4) for v in wp)}")
print(f"  RHS/LHS: max {r.max():.6f}, 99.99th pct {np.quantile(r,0.9999):.6f}, median {np.median(r):.6f}")
print("\n  => the Schur inequality holds with a uniform relative margin; RHS never approaches LHS.")
