#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
import hashlib, json

# Exact finite-state certificate for a two-terminal side A on Q union {x,y}.
# Internal component Q is connected and each terminal has at least one neighbour in Q.
# The optional edge xy is included in A when present. Unit forest counts split as:
# D(A)=# forests disconnecting x,y, C(A)=# forests connecting x,y.
# Collapsing A into the other side gives one virtual edge of exact weight lambda=C/D.

def zeta_counts(n):
    poss=list(combinations(range(n),2))
    m=len(poss)
    N=1<<m
    forest=[0]*N
    conn=[0]*N
    for mask in range(N):
        p=list(range(n))
        def find(a):
            while p[a]!=a:
                p[a]=p[p[a]]; a=p[a]
            return a
        ok=True
        for i,(u,v) in enumerate(poss):
            if (mask>>i)&1:
                a,b=find(u),find(v)
                if a==b:
                    ok=False; break
                p[b]=a
        if ok:
            forest[mask]=1
            conn[mask]=int(find(0)==find(1))
    F=forest[:]
    C=conn[:]
    for i in range(m):
        bit=1<<i
        for mask in range(N):
            if mask & bit:
                F[mask]+=F[mask^bit]
                C[mask]+=C[mask^bit]
    return poss,F,C

def internal_connected(k,mask,poss):
    if k<=1: return True
    p=list(range(k))
    def find(a):
        while p[a]!=a:
            p[a]=p[p[a]]; a=p[a]
        return a
    for i,(u,v) in enumerate(poss):
        if not ((mask>>i)&1): continue
        if u>=2 and v>=2:
            a,b=find(u-2),find(v-2)
            if a!=b: p[b]=a
    return len({find(i) for i in range(k)})==1

def terminal_hits(k,mask,poss,t):
    return any(((mask>>i)&1) and ((u==t and v>=2) or (v==t and u>=2))
               for i,(u,v) in enumerate(poss))

rows=[]
all_states=set()
for k in range(1,5):
    n=k+2
    poss,F,C=zeta_counts(n)
    states=set(); graphs=0
    for mask in range(1<<len(poss)):
        if not internal_connected(k,mask,poss): continue
        if not terminal_hits(k,mask,poss,0): continue
        if not terminal_hits(k,mask,poss,1): continue
        graphs+=1
        c=C[mask]; d=F[mask]-c
        assert d>0 and c>0
        states.add(Fraction(c,d))
    all_states |= states
    rows.append((k,graphs,len(states),min(states),max(states),tuple(sorted(states))))

assert [(k,g,s) for k,g,s,*_ in rows] == [(1,2,2),(2,18,8),(3,392,44),(4,17100,368)]
assert rows[0][5] == (Fraction(1,3),Fraction(4,3))
assert rows[1][5] == (Fraction(1,7),Fraction(1,3),Fraction(2,5),Fraction(5,7),Fraction(8,7),Fraction(4,3),Fraction(7,5),Fraction(12,7))
assert len(all_states)==368
assert min(all_states)==Fraction(1,31)
assert max(all_states)==Fraction(1055,411)

payload={
    'claim':'P14-2CUT-FINITE-STATE-56',
    'interpretation':'two-terminal unit-forest effective weights lambda=C/D for a connected component Q of size k<=4, terminals x,y each adjacent to Q, xy optional and assigned to the small side',
    'rows':[{
        'k':k,'eligible_labeled_sides':g,'distinct_lambda':s,
        'min':str(lo),'max':str(hi),'states':[str(x) for x in states]
    } for k,g,s,lo,hi,states in rows],
    'union_distinct_lambda':len(all_states),
    'union_min':str(min(all_states)),
    'union_max':str(max(all_states)),
}
raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
print('claim=P14-2CUT-FINITE-STATE-56')
for k,g,s,lo,hi,states in rows:
    print(f'k={k} eligible_labeled_sides={g} distinct_lambda={s} min={lo} max={hi}')
    if k<=2: print('states_k%d='%k + ','.join(str(x) for x in states))
print('union_distinct_lambda=%d union_min=%s union_max=%s' % (len(all_states),min(all_states),max(all_states)))
print('payload_sha256='+hashlib.sha256(raw).hexdigest())
print('EXACT_CHECK_PASS')
