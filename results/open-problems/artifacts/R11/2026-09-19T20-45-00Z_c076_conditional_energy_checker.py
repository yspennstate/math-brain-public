from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial, gcd

A=0
def ck(x,msg=""):
    global A
    A+=1
    if not x: raise AssertionError(msg or A)

def H(n): return sum((F(1,j) for j in range(1,n+1)),F())
def Lp(p,r): return H(r)-H(p-1-r)
def sn(v): return sum((x*x for x in v),F())
def plus(a,b): return [x+y for x,y in zip(a,b)]
def minus(a,b): return [x-y for x,y in zip(a,b)]

def coords(K):
    out=[]
    for m in range(2,K+1):
        for V in combinations(range(K),m):
            seen=set(); VS=set(V)
            for r in range(1,m):
                for aa in combinations(V,r):
                    bb=tuple(sorted(VS-set(aa)))
                    key=tuple(sorted((tuple(aa),bb)))
                    if key not in seen:
                        seen.add(key); out.append((V,key))
    return out

def gv(K,p,d,t,C=None):
    C=C or coords(K); vals={v:pow((t+v)%p,d,p) for v in range(K)}
    out=[]
    for V,key in C:
        VS=set(V); s=F()
        for u in range(1,p):
            aa=tuple(sorted(v for v in V if vals[v]<u))
            bb=tuple(sorted(VS-set(aa)))
            if aa and bb and tuple(sorted((aa,bb)))==key:
                s+=F(p,2*u*(p-u))
        out.append(s)
    return out

def mean(V):
    return [sum((v[j] for v in V),F())/len(V) for j in range(len(V[0]))]

def cexp(sel,rem,need,z):
    S=[F() for _ in z[0]]
    for t in sel: S=plus(S,z[t])
    if need==0: return sn(S)
    n=len(rem); ck(1<=need<=n)
    if need==n:
        for t in rem: S=plus(S,z[t])
        return sn(S)
    Q=sum((sn(z[t]) for t in rem),F())
    return F((n-need)*(n-need-1),n*(n-1))*sn(S)+F(need*(n-need),n*(n-1))*Q

def greedy(K,p,d,L):
    C=coords(K); G=[gv(K,p,d,t,C) for t in range(p)]
    mu=mean(G); z=[minus(v,mu) for v in G]
    sel=[]; rem=list(range(p)); hist=[]
    while len(sel)<L:
        need=L-len(sel)-1; cand=[]
        for t in rem:
            rr=[x for x in rem if x!=t]
            cand.append((cexp(sel+[t],rr,need,z),t))
        val,t=min(cand)
        sel.append(t); rem.remove(t); hist.append((t,val))
    return sel,C,G,mu,z,hist

# U054 harmonic energy input.
for p in (3,5,7,11,13,17,19):
    for r in range(p): ck(Lp(p,p-1-r)==-Lp(p,r))
    ck(sum((Lp(p,r)**2 for r in range(p)),F())/p<8)

# Exact split-vector energy identities and O(K 2^K) bound.
for p,d in ((5,3),(7,5),(11,3),(11,7),(13,5),(17,3)):
    if gcd(d,p-1)!=1: continue
    for K in range(2,min(5,p)+1):
        C=coords(K); G=[gv(K,p,d,t,C) for t in range(p)]
        E=sum((sn(v) for v in G),F())/p
        bound=F(8*K*(2**(K-1)-1))
        ck(E<bound,(p,d,K,E,bound))
        mu=mean(G); Z=[minus(v,mu) for v in G]
        ck(sum((sn(v) for v in Z),F())/p<=E)
        for t in range(p):
            vals={v:pow((t+v)%p,d,p) for v in range(K)}
            for m in range(2,K+1):
                for V in combinations(range(K),m):
                    xs=sorted(vals[v] for v in V)
                    rhs=sum(((F(1,2)*(Lp(p,xs[r+1])-Lp(p,xs[r])))**2 for r in range(m-1)),F())
                    lhs=sum((G[t][j]**2 for j,(VV,_) in enumerate(C) if VV==V),F())
                    ck(lhs==rhs,(p,d,K,t,V,lhs,rhs))

# Conditional-expectation formula against brute-force completion.
for p,d,K,L in ((5,3,2,3),(5,3,3,3),(7,5,3,3),(7,5,3,4)):
    C=coords(K); G=[gv(K,p,d,t,C) for t in range(p)]
    mu=mean(G); z=[minus(v,mu) for v in G]
    for r in range(0,min(2,L)+1):
        for T in list(combinations(range(p),r))[:5]:
            R=[t for t in range(p) if t not in T]; need=L-r
            vals=[]
            for U in combinations(R,need):
                S=[F() for _ in C]
                for t in T+U: S=plus(S,z[t])
                vals.append(sn(S))
            ck(cexp(list(T),R,need,z)==sum(vals,F())/len(vals))

# C076 N=4 witness: K=2,p=5,d=3,L=3.
sel,C,G,mu,z,hist=greedy(2,5,3,3)
ck(sel==[4,2,0],sel)
mS=[sum((G[t][j] for t in sel),F())/3 for j in range(len(C))]
err=sn(minus(mS,mu))
avZ=sum((sn(v) for v in z),F())/5
ck(err<=F(2,12)*avZ,(err,avZ))

def rates(N,p,d,S):
    R={}
    for t in S:
        vals={l:pow((t+l)%p,d,p) for l in range(N)}
        for u in range(1,p):
            aa=tuple(sorted(l for l in range(N) if vals[l]<u))
            bb=tuple(sorted(set(range(N))-set(aa)))
            if aa and bb:
                key=tuple(sorted((aa,bb)))
                R[key]=R.get(key,F())+F(p,2*len(S)*u*(p-u))
    return R

R=rates(4,5,3,tuple(sorted(sel))); labs=set(range(4)); seen=set(); sing=[]; bal=[]
for r in (1,2):
    for aa in combinations(range(4),r):
        bb=tuple(sorted(labs-set(aa))); key=tuple(sorted((tuple(aa),bb)))
        if key in seen: continue
        seen.add(key); v=R.get(key,F())
        (sing if r==1 else bal).append(v)
ck(sorted(sing)==[F(5,24),F(25,72),F(25,72),F(5,12)])
ck(sorted(bal)==[F(5,36),F(5,36),F(5,18)])
tot=sum(sing,F())+sum(bal,F())
ck(tot==F(15,8)); ck(sum(bal,F())/tot==F(8,27))
ck(F(8,27)!=F(3,11)); ck(F(8,27)!=F(2,7))

# Full-K positivity lower bound and minimum CTCS specified-split rate.
for K in range(2,13):
    total=2**(K-1)-1; lb=(total+K-2)//(K-1)
    ck((lb-1)*(K-1)<total<=lb*(K-1))
    b=F(1,(K-1)*max(comb(K-2,j) for j in range(K-1)))
    beta=[F(factorial(i-1)*factorial(K-i-1),factorial(K-1)) for i in range(1,K)]
    ck(min(beta)==b)

print("R11-I0054-U055/C076 exact self-check")
print("ASSERTIONS="+str(A))
print("C076_N4_GREEDY_ORDER="+",".join(map(str,sel)))
print("C076_N4_SUPPORT="+",".join(map(str,sorted(sel))))
print("C076_N4_GREEDY_HISTORY="+",".join(f"{t}:{v}" for t,v in hist))
print("C076_N4_SINGLETON_MULTISET="+",".join(map(str,sorted(sing))))
print("C076_N4_BALANCED_MULTISET="+",".join(map(str,sorted(bal))))
print("C076_N4_TOTAL_ROOT_RATE="+str(tot))
print("C076_N4_BALANCED_PROB="+str(sum(bal,F())/tot))
print("SOURCE_N4_BALANCED_PROB=3/11")
print("C075_N4_BALANCED_PROB=2/7")
print("ALL_EXACT_CHECKS_PASS")
