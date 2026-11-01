#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict

def inv(a,p): return pow(a%p,p-2,p)
def qrset(p): return {x*x%p for x in range(1,p)}
def chi(a,p,Q=None):
    a%=p
    if a==0:return 0
    if Q is None: Q=qrset(p)
    return 1 if a in Q else -1

# B8 exact level-8 quotient obstruction.
p=53; a2=(-8)%p; a4=7%p; Q=qrset(p)
def neg(P):
    if P is None:return None
    x,y=P; return (x,(-y)%p)
def add(P,R):
    if P is None:return R
    if R is None:return P
    x1,y1=P; x2,y2=R
    if x1==x2 and (y1+y2)%p==0:return None
    if P!=R:m=(y2-y1)*inv(x2-x1,p)%p
    else:
        if y1%p==0:return None
        m=(3*x1*x1+2*a2*x1+a4)*inv(2*y1,p)%p
    x3=(m*m-a2-x1-x2)%p
    y3=(-y1 + m*(x1-x3))%p
    return (x3,y3)
def mul(n,P):
    R=None; A=P
    while n:
        if n&1:R=add(R,A)
        A=add(A,A); n//=2
    return R
def rhs(x): return x*(x-1)*(x-7)%p
E=[None]
for x in range(p):
    r=rhs(x)
    for y in range(p):
        if y*y%p==r:E.append((x,y))
assert len(E)==64
E2=set(mul(2,P) for P in E); E4=set(mul(2,P) for P in E2); E8=set(mul(2,P) for P in E4)
assert (len(E2),len(E4),len(E8))==(16,4,2)
def key(P): return (-1,-1) if P is None else P
unseen=set(E2); cosets=[]
while unseen:
    P=min(unseen,key=key); C={add(P,H) for H in E8}; cosets.append(C); unseen-=C
cosets.sort(key=lambda C:min(key(z) for z in C)); cid={z:i for i,C in enumerate(cosets) for z in C}
common=[]
for x in range(p):
    if x in (0,1,7):continue
    if x in Q and (x-1)%p in Q and (x-7)%p in Q:
        ys=[y for y in range(p) if y*y%p==rhs(x)]; P=(x,ys[0]); common.append((x,tuple(sorted((cid[P],cid[neg(P)])))))
assert len(common)==6
amb=defaultdict(lambda:{True:[],False:[]})
for (x,lx),(y,ly) in combinations(common,2):
    lp=tuple(sorted((lx,ly))); edge=((x-y)%p in Q); amb[lp][edge].append((x,y,(x-y)%p))
witness=next((lp,d[True][0],d[False][0]) for lp,d in amb.items() if d[True] and d[False])
print('B8_LEVEL8_P=53_E_ORDER=64 E2=16 E4=4 E8=2 COSETS=8')
print('B8_COMMON_LABELS='+';'.join(f'{x}:{lab}' for x,lab in common))
print(f'B8_AMBIGUOUS_LABEL_PAIR={witness[0]} EDGE_PAIR={witness[1]} NONEDGE_PAIR={witness[2]}')
print('B8_LEVEL8_SIGN_ORBIT_LABELS_DO_NOT_DETERMINE_ADJACENCY=PASS')

# B13 exact finite exploration.
def primes_upto(n):
    return [m for m in range(2,n+1) if all(m%d for d in range(2,int(m**0.5)+1))]
def point_count_cubic(T,p,Q):
    s=0
    for x in range(p):
        f=1
        for a in T:f=f*(x-a)%p
        s+=chi(f,p,Q)
    return p+1+s
def point_count_quartic(C,p,Q):
    s=0
    for x in range(p):
        f=1
        for a in C:f=f*(x-a)%p
        s+=chi(f,p,Q)
    return p+2+s
checked=0; formula_checked=0; per_prime=[]
for pp in [q for q in primes_upto(97) if q%4==1]:
    Qp=qrset(pp); adj=[set() for _ in range(pp)]
    for i in range(pp):
        for j in range(i+1,pp):
            if (i-j)%pp in Qp:adj[i].add(j);adj[j].add(i)
    c4=[]
    for a in range(pp):
        for b in sorted(v for v in adj[a] if v>a):
            common2=adj[a]&adj[b]
            for c in sorted(v for v in common2 if v>b):
                common3=common2&adj[c]
                for d in sorted(v for v in common3 if v>c):c4.append((a,b,c,d))
    bad=0; fp=0
    for C in c4:
        nc=set(range(pp))
        for a in C:nc &= adj[a]
        if len(nc)%2 != (1 if pp%8==1 else 0):bad+=1
        checked+=1
    for C in c4[:min(8,len(c4))]:
        Ns=[point_count_cubic(T,pp,Qp) for T in combinations(C,3)]
        assert all(n%16==0 for n in Ns)
        N4=point_count_quartic(C,pp,Qp); assert N4%16==0
        nc=set(range(pp))
        for a in C:nc &= adj[a]
        t=len(nc); assert 16*t == sum(Ns)+N4-4*pp-44
        assert (sum(n//16 for n in Ns)+N4//16)%2==0
        formula_checked+=1;fp+=1
    assert bad==0
    if c4: per_prime.append((pp,len(c4),fp))
print('B13_4CLIQUE_PARITY_SAMPLE_PRIMES=' + ','.join(f'{p}:{n}' for p,n,_ in per_prime))
print(f'B13_4CLIQUE_PARITY_TOTAL_CLIQUES={checked} FORMULA_SAMPLES={formula_checked}')
print('B13_OBSERVED_PARITY=common_neighbor_count mod2 equals 1[p mod8=1]')
print('B13_EXACT_FORMULA=16*t4=sum_four_cubic_orders+quartic_order-4p-44')
print('B13_NORMALIZED_FIVE_CURVE_PARITY_EVEN_ON_ALL_FORMULA_SAMPLES=PASS')
print('B13_STATUS=EXPLORATORY_NOT_A_THEOREM')
print('ALL_I0099_NEW_METHOD_SELF_CHECKS_PASS')
