import itertools, math
import numpy as np

rng = np.random.default_rng(20260923)

def detsq(M,S,T):
    return float(np.linalg.det(M[np.ix_(S,T)])**2)

def one_check(M):
    nr,nc=M.shape
    triples=[]
    Z=0.0
    rowmass=np.zeros(nr)
    for S in itertools.combinations(range(nr),3):
        for T in itertools.combinations(range(nc),3):
            w=detsq(M,S,T)
            if w>1e-24:
                triples.append((S,T,w))
                Z+=w
                for i in S:
                    rowmass[i]+=w
    alpha=rowmass/Z
    i=int(np.argmax(alpha))
    Wi=alpha[i]*Z
    eta={}
    for S,T,w in triples:
        if i in S:
            R=tuple(k for k in S if k!=i)
            eta[R]=eta.get(R,0.0)+w/Wi
    a=np.zeros(nr)
    H=0.0
    elogD=0.0
    for R,p in eta.items():
        for k in R:
            a[k]+=p
        D=sum(detsq(M,R,T) for T in itertools.combinations(range(nc),2))
        H-=p*math.log(p)
        elogD+=p*math.log(D)
    K2=math.exp(H+elogD)
    lower=Wi/(np.linalg.norm(M[i])**2)
    return Z,alpha[i],float(a.max()),K2,lower,K2/lower

mins=1e100
for trial in range(200):
    M=rng.normal(size=(7,5))
    out=one_check(M)
    mins=min(mins,out[-1])

print('minimum randomized K2/lower ratio over 200 tests =',repr(mins))
print('constant alpha->1 =',repr(10*math.sqrt(math.e)*2**(-1/5)))
print('constant alpha>=1/2 =',repr(10*math.sqrt(math.e)*2**(-1/10)))
assert mins >= 1-1e-10
print('STATUS=PASS')
