import numpy as np
rng=np.random.default_rng(97)
print("Can the |L| term be DROPPED from the left side?  i.e. does the rational inequality")
print("   4S * det K  >=  g1^2 K22 - 2 g1 g2 K12 + g2^2 K11    already hold?")
print("(if yes, the 2|L|/c^2 term is pure slack and the conjecture follows from a rational inequality)")
n=0; bad=0; worst=1e18; wp=None
while n<200000:
    a,b=rng.random(2); c=(rng.random()*2-1)*0.55
    t=c*c
    if t<=1e-10 or t>=min(a*b,(1-a)*(1-b))-1e-9: continue
    p=np.array([(1-a)*(1-b)-t, a*(1-b)+t, (1-a)*b+t, a*b-t])
    if p.min()<=1e-9: continue
    n+=1
    g=np.array([[b-1,a-1,-2*c],[1-b,-a,2*c],[-b,1-a,2*c],[b,a,-2*c]],dtype=float)
    G=sum(np.outer(g[i],g[i])/p[i] for i in range(4))
    absL=np.log(p[1]*p[2]/(p[0]*p[3]))
    K11,K22,K12=G[0,0],G[1,1],G[0,1]-absL
    detK=K11*K22-K12*K12
    g1,g2=G[0,2]/c,G[1,2]/c
    S=(1.0/p).sum()
    lhs=4*S*detK
    rhs=g1*g1*K22-2*g1*g2*K12+g2*g2*K11
    m=lhs-rhs
    if m<worst: worst=m; wp=(a,b,c)
    if m<0: bad+=1
print(f"  n={n}   violations of the rational form: {bad}")
print(f"  min (LHS-RHS) = {worst:+.6e} at (a,b,c)={tuple(round(v,4) for v in wp) if wp else None}")
