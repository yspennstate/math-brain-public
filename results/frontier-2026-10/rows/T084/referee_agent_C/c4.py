import random, itertools
from math import comb
from collections import defaultdict
import brute
rnd=random.Random(84)
fails=0; checks=0; negs=0
for trial in range(60):
    n=rnd.randint(4,7)
    allE=list(itertools.combinations(range(n),2))
    m=rnd.randint(2,min(len(allE),15))
    E=rnd.sample(allE,m); e,f=rnd.sample(E,2)
    N=brute.N_of(n,E,e,f)
    lhs=defaultdict(int)
    for (i,j),c in N.items():
        if j==1: lhs[i]+=c
    rest=[x for x in E if x not in (e,f)]
    S=defaultdict(int)
    for mask in range(1<<len(rest)):
        B=[rest[i] for i in range(len(rest)) if mask>>i&1]
        k00=brute.comps(n,B); k10=brute.comps(n,B+[e]); k01=brute.comps(n,B+[f]); k11=brute.comps(n,B+[e,f])
        D=k00-k10-k01+k11
        assert D>=0
        if D: S[len(B)]+=D
    rhs=defaultdict(int)
    for s,c in S.items():
        for t in range(m-1):  # (1+lam)^(m-2)
            rhs[s+2+t]+=c*comb(m-2,t)
    L={k:v for k,v in lhs.items() if v}; R={k:v for k,v in rhs.items() if v}
    checks+=1; fails+= (L!=R)
    # sign of whole N at a few (lam,q) points
    for lam in (0.3,1.0,4.0):
        for q in (0.1,0.5,0.9):
            u=1-q; val=sum(c*lam**i*u**j for (i,j),c in N.items())
            if val< -1e-9: negs+=1
print('C4 checks',checks,'fails',fails,'; N<0 at sample points:',negs)
