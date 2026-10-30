from itertools import combinations
from fractions import Fraction
from collections import defaultdict

def closure(n, edges):
    r=[[False]*n for _ in range(n)]
    for a,b in edges:
        r[a][b]=True
    for k in range(n):
        for i in range(n):
            if r[i][k]:
                for j in range(n):
                    if r[k][j]:
                        r[i][j]=True
    assert not any(r[i][i] for i in range(n))
    return r

def linear_extensions(r):
    n=len(r)
    preds=[{i for i in range(n) if r[i][j]} for j in range(n)]
    out=[]
    def rec(seq, rem):
        if not rem:
            out.append(tuple(seq)); return
        for x in sorted(rem):
            if not (preds[x] & rem):
                rem.remove(x); seq.append(x)
                rec(seq, rem)
                seq.pop(); rem.add(x)
    rec([], set(range(n)))
    return out

def width(r):
    n=len(r)
    best=0
    for m in range(1<<n):
        A=[i for i in range(n) if (m>>i)&1]
        if all(not r[x][y] and not r[y][x] for x,y in combinations(A,2)):
            best=max(best,len(A))
    return best

def distinguishers(r,a,b):
    def rel(z,x):
        if r[z][x]: return -1
        if r[x][z]: return 1
        return 0
    return [z for z in range(len(r)) if z not in (a,b) and rel(z,a)!=rel(z,b)]

def prob(L,a,b):
    return Fraction(sum(t.index(a)<t.index(b) for t in L),len(L))

def local_interval_regression():
    cases=0
    for N in range(0,9):
        for la in range(N+1):
            for ua in range(la,N+1):
                A=range(la,ua+1)
                for lb in range(N+1):
                    for ub in range(lb,N+1):
                        B=range(lb,ub+1)
                        for h in range(N+1):
                            plus=[]; minus=[]
                            for i in A:
                                for j in B:
                                    if i<j:
                                        k=min(j,h)+(1 if i<=h else 0)
                                        plus.append(k)
                                    elif i>j:
                                        k=min(j,h)
                                        minus.append(k)
                                    else:
                                        plus.append(min(j,h)+(1 if i<=h else 0))
                                        minus.append(min(j,h))
                            if plus and minus:
                                assert Fraction(sum(plus),len(plus)) >= Fraction(sum(minus),len(minus))
                            cases += 1
    return cases

# Example A: a width-three first-element cut where all fixed-skeleton local
# terms are nonnegative but the global cross-skeleton covariance is negative.
# Q vertices: S={0,1,2,3}, T={4,5,6}.
q_edges=[(0,2),(0,5),(1,6),(2,3),(3,5),(4,6)]
rq=closure(7,q_edges)
LQ=linear_extensions(rq)
assert len(LQ)==70
a,b=1,5

def kappa(t):
    k=0
    for x in t:
        if x<4: k+=1
        else: break
    return k

groups=defaultdict(list)
for t in LQ:
    sk=tuple(x for x in t if x not in (a,b))
    groups[sk].append((t.index(a)<t.index(b),kappa(t)))

N=len(LQ)
q=prob(LQ,a,b)
EK=Fraction(sum(k for arr in groups.values() for ev,k in arr),N)
EAK=Fraction(sum(k for arr in groups.values() for ev,k in arr if ev),N)
cov=EAK-q*EK
local=Fraction(0)
for arr in groups.values():
    ns=len(arr)
    p=Fraction(sum(ev for ev,k in arr),ns)
    m=Fraction(sum(k for ev,k in arr),ns)
    eak=Fraction(sum(k for ev,k in arr if ev),ns)
    d=eak-p*m
    assert d>=0
    local += Fraction(ns,N)*d
between=cov-local

den=sum(kappa(t)+1 for t in LQ)
num=sum(kappa(t)+1 for t in LQ if t.index(a)<t.index(b))
mu=Fraction(num,den)
assert q==Fraction(32,35)
assert mu==Fraction(185,203)
assert cov==Fraction(-3,350)
assert local==Fraction(60,1309)
assert between==Fraction(-3561,65450)

# Add c=7 below every T element and incomparable with S.
p_edges=q_edges+[(7,4),(7,5),(7,6)]
rp=closure(8,p_edges)
LP=linear_extensions(rp)
assert width(rp)==3
assert len(LP)==203
assert prob(LP,a,b)==mu

# Example B: the one-distinguisher theorem is already sharp in the c-cut
# geometry. P has c=4 < 2 < 3, with 0 and 1 isolated.
r2=closure(5,[(4,2),(2,3)])
L2=linear_extensions(r2)
assert width(r2)==3
assert len(L2)==20
assert distinguishers(r2,0,3)==[2,4]
assert prob(L2,0,3)==Fraction(3,4)
assert prob(L2,4,0)==Fraction(3,4)
assert prob(L2,4,1)==Fraction(3,4)
assert prob(L2,0,2)==Fraction(1,2)

cases=local_interval_regression()
print('POS3_CROSS_SKELETON_TRANSFER_CHECK_PASS')
print('local_interval_cases', cases)
print('simpson_Q_extensions', len(LQ), 'P_extensions', len(LP), 'widthP', width(rp))
print('simpson_pair_nu', q, 'mu', mu, 'cov', cov)
print('simpson_local', local, 'between', between, 'skeletons', len(groups))
print('two_distinguisher_extensions', len(L2), 'p_0_before_3', prob(L2,0,3))
print('two_distinguisher_set', distinguishers(r2,0,3), 'c_before_0', prob(L2,4,0))
