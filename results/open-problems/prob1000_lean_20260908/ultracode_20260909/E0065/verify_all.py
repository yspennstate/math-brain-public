# Independent numerical checks for E0065 (kept small; single process).
import numpy as np, sys
from scipy.optimize import fsolve
rng=np.random.default_rng(7)
def V(P,x): return np.einsum('ijk,i,j->k',P,x,x)
def build_swap(m,al):
    # states 1,2 swap; states 3..m bystanders. min coefficient = alpha.
    P=np.full((m,m,m),al)
    big=1-(m-1)*al
    P[1,1,0]=big
    P[0,0,1]=big
    for j in range(2,m):
        P[1,j,0]=P[j,1,0]=big
        P[0,j,1]=P[j,0,1]=big
    # (1,2) pair and bystander pairs send the rest into the bystanders, spread evenly
    if m>2:
        for k in range(2,m):
            P[0,1,k]=P[1,0,k]=al+(1-m*al)/(m-2)
            for j in range(2,m):
                for jp in range(2,m):
                    P[j,jp,k]=al+(1-m*al)/(m-2)
    return P
def check_qso(P):
    m=P.shape[0]
    assert np.allclose(P,P.transpose(1,0,2)); assert np.allclose(P.sum(axis=2),1); assert (P>=0).all()
print("=== m=3 and m=4 swap construction: explicit 2-cycle, alpha below (1-1/sqrt(m+1))/(2m)")
for m,al in [(3,0.08),(3,0.083),(4,0.066),(4,0.069),(5,0.058)]:
    P=build_swap(m,al); check_qso(P)
    thr=(1-1/np.sqrt(m+1))/(2*m)
    s=m*al/(1-m*al); S=1-s; Pr=al/(1-m*al); disc=S*S-4*Pr
    x1=(S+np.sqrt(disc))/2; x2=(S-np.sqrt(disc))/2
    x=np.array([x1,x2]+[s/(m-2)]*(m-2))
    Vx=V(P,x); VVx=V(P,Vx)
    print(f"m={m} alpha={al} (thr={thr:.5f}) minP={P.min():.4f} x={np.round(x,5)} V(x)={np.round(Vx,5)} |V^2(x)-x|={abs(VVx-x).max():.1e} x1!=x2: {abs(x1-x2):.4f}")
    # independent: Newton/fsolve on V^2(x)=x from random starts, collect non-fixed solutions
    found=[]
    for _ in range(300):
        y0=rng.dirichlet(np.ones(m))
        sol,info,ier,msg=fsolve(lambda y: np.append(V(P,np.append(y,1-y.sum()))[:-1]-y, 0)[:m-1] if False else V(P,V(P,np.append(y,1-y.sum())))[:m-1]-y, y0[:m-1], full_output=True)
        y=np.append(sol,1-sol.sum())
        if ier==1 and (y>=-1e-9).all() and abs(V(P,V(P,y))-y).max()<1e-10 and abs(V(P,y)-y).max()>1e-6:
            if not any(abs(y-f).max()<1e-6 for f in found): found.append(y)
    print("   fsolve found period-2 points:",[np.round(f,5) for f in found])
    # iterate from random points: attractor
    y=rng.dirichlet(np.ones(m))
    for _ in range(5000): y=V(P,y)
    tail=[y]; 
    for _ in range(3): y=V(P,y); tail.append(y)
    print("   iteration tail:",[np.round(t,5) for t in tail])
print("=== m=2: a=b=alpha, c=1-alpha at alpha=0.08 (<(3-sqrt7)/4=%.5f): 2-cycle?"%((3-7**0.5)/4))
al=0.08; f=lambda x: al*x*x+2*al*x*(1-x)+(1-al)*(1-x)**2
x=0.3
for _ in range(3000): x=f(x)
print("   iteration tail:",[round(x,6),round(f(x),6),round(f(f(x)),6)])
print("=== m=2 random search: min P > (3-sqrt7)/4 => every fixed point has f'(p) > -1 ?")
al0=(3-7**0.5)/4; worst=0
for _ in range(40000):
    a,b,c=rng.uniform(al0,1-al0,3)
    A=a-2*b+c; B=2*b-2*c-1
    r=np.roots([A,B,c]) if abs(A)>1e-14 else np.array([-c/B])
    for p in r:
        if abs(p.imag)<1e-9 and 0<=p.real<=1:
            d=2*A*p.real+(2*b-2*c); worst=min(worst,d)
print("   most negative f'(p) seen:",worst)
print("=== upper bound: contraction factor 2(1-alpha)(1-m alpha) on D={x_i>=alpha}, random test")
for m in (3,4):
    al=0.1; kappa=2*(1-al)*(1-m*al); ratio=0
    for _ in range(3000):
        P=np.full((m,m,m),0.0)
        for i in range(m):
            for j in range(i,m):
                d=rng.dirichlet(np.ones(m)*0.3); P[i,j]=P[j,i]=al+(1-m*al)*d
        x=al+(1-m*al)*rng.dirichlet(np.ones(m)*0.3); y=al+(1-m*al)*rng.dirichlet(np.ones(m)*0.3)
        ratio=max(ratio,abs(V(P,x)-V(P,y)).sum()/abs(x-y).sum())
    print(f"   m={m} alpha={al}: max observed ||V(x)-V(y)||/||x-y|| = {ratio:.4f}  bound kappa={kappa:.4f}")
print("=== regularity check just above the new upper bound, m=3, alpha=0.14 (bound 0.13962): random QSOs converge?")
m=3; al=0.14; maxres=0
for _ in range(300):
    P=np.zeros((m,m,m))
    for i in range(m):
        for j in range(i,m):
            d=rng.dirichlet(np.ones(m)*0.2); P[i,j]=P[j,i]=al+(1-m*al)*d
    x=rng.dirichlet(np.ones(m))
    for _ in range(400): x=V(P,x)
    maxres=max(maxres,abs(V(P,x)-x).max())
print("   max |V(x)-x| after 400 iterations over 300 random operators:",maxres)
