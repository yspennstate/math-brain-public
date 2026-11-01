# Iteration checks with renormalisation (sum(V(x)) = (sum x)^2, so rounding in the sum blows up
# double-exponentially over thousands of steps unless the iterate is renormalised).
import numpy as np
rng=np.random.default_rng(3)
def V(P,x):
    y=np.einsum('ijk,i,j->k',P,x,x); return y/y.sum()
def build_swap(m,al):
    P=np.full((m,m,m),al); big=1-(m-1)*al
    P[1,1,0]=big; P[0,0,1]=big
    for j in range(2,m):
        P[1,j,0]=P[j,1,0]=big; P[0,j,1]=P[j,0,1]=big
    for k in range(2,m):
        P[0,1,k]=P[1,0,k]=al+(1-m*al)/(m-2)
        for j in range(2,m):
            for jp in range(2,m): P[j,jp,k]=al+(1-m*al)/(m-2)
    return P
for m,al in [(3,0.08),(3,0.083),(3,0.0834),(4,0.066),(4,0.069),(4,0.0692),(5,0.058)]:
    P=build_swap(m,al); thr=(1-1/np.sqrt(m+1))/(2*m)
    tails=[]
    for _ in range(5):
        y=rng.dirichlet(np.ones(m))
        for _ in range(20000): y=V(P,y)
        tails.append((np.round(y,5),np.round(V(P,y),5)))
    print(f"m={m} alpha={al} ({'below' if al<thr else 'ABOVE'} thr {thr:.5f}):")
    for t in tails[:3]: print("    x_n=",t[0]," x_{n+1}=",t[1])
print("=== regularity just above the new upper bound (m=3, alpha=0.14 > 0.13962): 300 random operators")
m=3; al=0.14; maxres=0
for _ in range(300):
    P=np.zeros((m,m,m))
    for i in range(m):
        for j in range(i,m):
            d=rng.dirichlet(np.ones(m)*0.2); P[i,j]=P[j,i]=al+(1-m*al)*d
    x=rng.dirichlet(np.ones(m))
    for _ in range(400): x=V(P,x)
    maxres=max(maxres,abs(V(P,x)-x).max())
print("   max |V(x)-x| after 400 steps:",maxres)
print("=== random search for non-regular m=3 operators with min P in (1/12, 0.1396): 2-cycles via Newton on V^2")
from scipy.optimize import fsolve
cnt=0; best=0
for trial in range(1500):
    al=rng.uniform(1/12,0.1396)
    P=np.zeros((m,m,m))
    for i in range(m):
        for j in range(i,m):
            d=rng.dirichlet(np.ones(m)*0.15); P[i,j]=P[j,i]=al+(1-m*al)*d
    V0=lambda x: np.einsum('ijk,i,j->k',P,x,x)
    for _ in range(4):
        y0=rng.dirichlet(np.ones(m))
        sol,info,ier,msg=fsolve(lambda y: V0(V0(np.append(y,1-y.sum())))[:2]-y, y0[:2], full_output=True)
        y=np.append(sol,1-sol.sum())
        if ier==1 and (y>=-1e-9).all() and abs(V0(V0(y))-y).max()<1e-10 and abs(V0(y)-y).max()>1e-6:
            cnt+=1; best=max(best,P.min()); break
print("   operators with a genuine 2-cycle found:",cnt," largest min P among them:",best)
