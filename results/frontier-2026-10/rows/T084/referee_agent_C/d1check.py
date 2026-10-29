"""D1 numerically: N from the swap sum over (A not containing e, B containing e and f) equals brute N, on K_n and random graphs.
Also a negative control for d3.series_ok_dict."""
import itertools, random
from collections import defaultdict
from math import comb
import brute, d3
def swapN(n,E,e,f):
    rest=[x for x in E if x!=e]; restB=[x for x in E if x not in (e,f)]
    W=defaultdict(int)  # (s, K, d2-d1) counts
    As=[]
    for mask in range(1<<len(rest)):
        A=[rest[i] for i in range(len(rest)) if mask>>i&1]
        k=brute.comps(n,A); d1=int(brute.comps(n,A+[e])<k); As.append((len(A),k,d1))
    Bs=[]
    for mask in range(1<<len(restB)):
        B=[restB[i] for i in range(len(restB)) if mask>>i&1]+[e,f]
        k=brute.comps(n,B); d2=int(brute.comps(n,[x for x in B if x!=e])>k); Bs.append((len(B),k,d2))
    ca=defaultdict(int); cb=defaultdict(int)
    for x in As: ca[x]+=1
    for x in Bs: cb[x]+=1
    N=defaultdict(int)   # lam^s q^K (q^(d2-d1)-1)  -> u basis
    for (sa,ka,d1),x in ca.items():
        for (sb,kb,d2),y in cb.items():
            dd=d2-d1
            if dd==0: continue
            s=sa+sb; K=ka+kb
            for p,c in ((K+dd,1),(K,-1)):
                for j in range(p+1): N[(s,j)]+=x*y*c*comb(p,j)*(-1)**j
    return {k:v for k,v in N.items() if v}
ok=0; tot=0
cases=[(4,list(itertools.combinations(range(4),2)),(0,1),(0,2)),(5,list(itertools.combinations(range(5),2)),(0,1),(0,2)),
       (5,list(itertools.combinations(range(5),2)),(0,1),(2,3))]
rnd=random.Random(7)
for t in range(30):
    n=rnd.randint(4,6); allE=list(itertools.combinations(range(n),2)); E=rnd.sample(allE,rnd.randint(2,min(10,len(allE))))
    e,f=rnd.sample(E,2); cases.append((n,E,e,f))
for n,E,e,f in cases:
    tot+=1; ok+= swapN(n,E,e,f)==brute.N_of(n,E,e,f)
print('D1 swap sum == brute N:',ok,'of',tot)
print('control: N = lam (u - 2u^2) ->', d3.series_ok_dict({(1,1):1,(1,2):-2})[0])
