import numpy as np
rng=np.random.default_rng(41)
def stats(a,b,c):
    t=c*c
    p=np.array([(1-a)*(1-b)-t, a*(1-b)+t, (1-a)*b+t, a*b-t])
    if p.min()<=0: return None
    g=np.array([[b-1,a-1,-2*c],[1-b,-a,2*c],[-b,1-a,2*c],[b,a,-2*c]],dtype=float)
    G=sum(np.outer(g[i],g[i])/p[i] for i in range(4))
    absL=np.log(p[1]*p[2]/(p[0]*p[3]))
    S=(1.0/p).sum()
    K=np.array([[G[0,0],G[0,1]-absL],[G[0,1]-absL,G[1,1]]])
    gv=np.array([G[0,2]/c,G[1,2]/c])
    LHS=4*S+2*absL/t; RHS=gv@np.linalg.solve(K,gv)
    return LHS,RHS,p,absL
rows=[]
n=0
while n<300000:
    a,b=rng.random(2); c=(rng.random()*2-1)*0.55
    t=c*c
    if t<=1e-10 or t>=min(a*b,(1-a)*(1-b))-1e-12: continue
    r=stats(a,b,c)
    if r is None or r[2].min()<=1e-12: continue
    n+=1
    LHS,RHS,p,absL=r
    rows.append((RHS/LHS, a,b,c, p.min(), LHS-RHS, LHS))
rows.sort(reverse=True)
print("The corner where the RATIO approaches 1 (both sides blowing up):")
print(f"{'RHS/LHS':>10} {'a':>7} {'b':>7} {'c':>8} {'min p':>10} {'LHS-RHS':>12} {'LHS':>12}")
for r in rows[:8]:
    print(f"{r[0]:>10.6f} {r[1]:>7.4f} {r[2]:>7.4f} {r[3]:>8.4f} {r[4]:>10.2e} {r[5]:>12.2f} {r[6]:>12.2e}")
print()
print("min of (LHS - RHS) over the whole sample:", f"{min(r[5] for r in rows):+.4f}")
print("=> the ABSOLUTE margin stays bounded away from 0; the ratio ->1 only where both sides diverge (min p -> 0, i.e. the boundary of the admissible region).")
