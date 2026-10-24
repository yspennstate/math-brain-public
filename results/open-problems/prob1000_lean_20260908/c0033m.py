import numpy as np
rng=np.random.default_rng(808)
print("Check the Cauchy-Schwarz lower bound on the 2x2 block, then whether it suffices.")
print("Claim A:  x^T G2 x >= u^2/(a(1-a))   and   >= v^2/(b(1-b))")
n=0; badA=0; badB=0; worstB=1e18; wp=None
while n<200000:
    a,b=rng.random(2); c=(rng.random()*2-1)*0.55
    t=c*c
    p=np.array([(1-a)*(1-b)-t, a*(1-b)+t, (1-a)*b+t, a*b-t])
    if p.min()<=1e-9: continue
    n+=1
    gp=np.array([[b-1,a-1],[1-b,-a],[-b,1-a],[b,a]],dtype=float)
    G2=sum(np.outer(gp[i],gp[i])/p[i] for i in range(4))
    for _ in range(3):
        x=rng.normal(size=2)
        q=x@G2@x
        if q < x[0]**2/(a*(1-a))-1e-9 or q < x[1]**2/(b*(1-b))-1e-9: badA+=1
    absL=np.log(p[1]*p[2]/(p[0]*p[3]))
    # explicit lower bound B for K
    B=np.array([[0.5/(a*(1-a)), -absL],[-absL, 0.5/(b*(1-b))]])
    g=np.array([[b-1,a-1,-2*c],[1-b,-a,2*c],[-b,1-a,2*c],[b,a,-2*c]],dtype=float)
    G=sum(np.outer(g[i],g[i])/p[i] for i in range(4))
    K=np.array([[G[0,0],G[0,1]-absL],[G[0,1]-absL,G[1,1]]])
    if min(np.linalg.eigvalsh(K-B))<-1e-8: badB+=1
    S=(1.0/p).sum()
    if min(np.linalg.eigvalsh(B))>1e-12:
        gv=np.array([G[0,2]/c,G[1,2]/c])
        try: rhsB=gv@np.linalg.solve(B,gv)
        except Exception: continue
        m=4*S+2*absL/t-rhsB
        if m<worstB: worstB=m; wp=(a,b,c)
print(f"  n={n}")
print(f"  Claim A violations (over 3 random directions each): {badA}")
print(f"  K - B not PSD at: {badB} points")
print(f"  min of  4S + 2|L|/c^2 - (g)B^-1(g)^T  = {worstB:+.4e} at {tuple(round(v,4) for v in wp) if wp else None}")
