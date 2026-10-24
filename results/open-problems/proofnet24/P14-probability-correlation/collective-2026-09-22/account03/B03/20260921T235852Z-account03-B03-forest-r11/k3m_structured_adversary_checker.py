#!/usr/bin/env python3
"""Exact stdlib checker for the K_{3,m} structured FOREST adversary.

No floating point.  This independently checks:
(1) terminal-partition signatures for K_{3,m};
(2) exact marked counts for two spokes in one right star;
(3) the account01/B03 overlap/reconnection identity;
(4) the weighted-triangle hypersurface defect.
"""
from collections import defaultdict
from fractions import Fraction

S = (
    (4,1,1,1,1),
    (0,4,0,0,2),
    (0,0,4,0,2),
    (0,0,0,4,2),
    (0,0,0,0,4),
)
R0 = (
    (1,0,1,1,1),
    (0,1,0,0,2),
    (0,0,1,0,1),
    (0,0,0,1,1),
    (0,0,0,0,1),
)
R01 = (
    (0,0,1,0,1),
    (0,0,0,0,1),
    (0,0,0,0,0),
    (0,0,0,0,1),
    (0,0,0,0,0),
)

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B)))
                       for j in range(len(B[0]))) for i in range(len(A)))
def ident(n):
    return tuple(tuple(int(i==j) for j in range(n)) for i in range(n))
def mpow(A,n):
    out=ident(len(A))
    base=A
    while n:
        if n&1: out=mm(out,base)
        base=mm(base,base); n//=2
    return out
def rowmul(v,A):
    return tuple(sum(v[k]*A[k][j] for k in range(len(v))) for j in range(len(A[0])))
def dot(v,w):
    return sum(a*b for a,b in zip(v,w))

def canonical(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks if b),
                        key=lambda q:(q[0],len(q),q)))
def connected(st,a,b):
    return any(a in block and b in block for block in st)

def add_persistent_star(dp,rlabel,available_terms):
    nd=defaultdict(int)
    terms=tuple(available_terms)
    for st,count in dp.items():
        blocks=[set(b) for b in st]
        for mask in range(1<<len(terms)):
            selected=[terms[i] for i in range(len(terms)) if (mask>>i)&1]
            ids=[]
            ok=True
            for v in [rlabel]+selected:
                idx=next(i for i,b in enumerate(blocks) if v in b)
                if idx in ids:
                    ok=False; break
                ids.append(idx)
            if not ok:
                continue
            if selected:
                merged=set().union(*(blocks[i] for i in ids))
                nxt=[blocks[i] for i in range(len(blocks)) if i not in ids]+[merged]
            else:
                nxt=blocks
            nd[canonical(nxt)] += count
    return nd

def add_ordinary_star(dp):
    nd=defaultdict(int)
    for st,count in dp.items():
        blocks=[set(b) for b in st]
        for mask in range(8):
            selected=[t for t in range(3) if (mask>>t)&1]
            ids=[]
            ok=True
            for t in selected:
                idx=next(i for i,b in enumerate(blocks) if t in b)
                if idx in ids:
                    ok=False; break
                ids.append(idx)
            if not ok:
                continue
            if len(selected)>=2:
                merged=set().union(*(blocks[i] for i in ids))
                nxt=[blocks[i] for i in range(len(blocks)) if i not in ids]+[merged]
            else:
                nxt=blocks
            nd[canonical(nxt)] += count
    return nd

def q_same_center(m):
    # e=(r,0), f=(r,1) are removed.  Q iff 0,1 are connected
    # while r is in a distinct component.
    init=canonical([{0},{1},{2},{3}])
    dp={init:1}
    dp=add_persistent_star(dp,3,(2,))
    for _ in range(m-1):
        dp=add_ordinary_star(dp)
    return sum(c for st,c in dp.items()
               if connected(st,0,1) and not connected(st,3,0))

def marked_counts(m):
    e0=(1,0,0,0,0); one=(1,1,1,1,1)
    Sm=mpow(S,m)
    Z=dot(rowmul(e0,Sm),one)
    Ze=dot(rowmul(rowmul(e0,R0),mpow(S,m-1)),one)
    Zef=dot(rowmul(rowmul(e0,R01),mpow(S,m-1)),one)
    return Z,Ze,Zef

def formulas(m):
    C=4**(m-2)
    Z=C*(3*m*m+13*m+16)
    Ze=C*(3*m*m+23*m+38)//4
    Zef=C*2*(m+3)
    N=C*(3*m*m+7*m+6)//2
    n00=C*(m-1)*(3*m-2)//4
    n10=C*(m-1)
    n11=C*(3*m*m+11*m+18)//4
    q=C*3*(m-1)*(m+2)//4
    Delta=C*C*(m-1)*(9*m**3+51*m*m+104*m+92)//16
    return Z,Ze,Zef,N,n00,n10,n11,q,Delta

def terminal_signature(m):
    v=rowmul((1,0,0,0,0),mpow(S,m))
    return v[0],v[1],v[2],v[3],v[4]

checked=[]
for m in range(2,13):
    d,a,b,c,t=terminal_signature(m)
    assert d==4**m
    assert a==b==c==m*4**(m-1)
    assert t==m*(3*m+1)*4**m//16
    kappa=d*t-a*b-a*c-b*c
    assert kappa==m*4**(2*m-2)
    assert Fraction(kappa,d*d)==Fraction(m,16)

    Z,Ze,Zef=marked_counts(m)
    fZ,fZe,fZef,N,n00,n10,n11,q,Delta=formulas(m)
    assert (Z,Ze,Zef)==(fZ,fZe,fZef)
    assert q_same_center(m)==q
    assert N==Z-2*Ze+Zef
    assert n00+2*n10+n11==N
    assert n10+n11==Ze-Zef
    assert n11-q==Zef

    delta=Ze*Ze-Z*Zef
    assert delta==Delta
    assert delta==n10*n10-n00*n11+N*q
    assert n00*n11>n10*n10  # ordinary 10x01 switching is cardinality-impossible
    checked.append((m,Z,Ze,Zef,q,delta,kappa))

# Additivity of the fourth normalized 3-terminal coordinate:
# delta = t/d - (a*b+a*c+b*c)/d^2.
def compose(s1,s2):
    d1,a1,b1,c1,t1=s1; d2,a2,b2,c2,t2=s2
    return (
        d1*d2,
        a1*d2+d1*a2,
        b1*d2+d1*b2,
        c1*d2+d1*c2,
        t1*d2+d1*t2
        +a1*b2+b1*a2+a1*c2+c1*a2+b1*c2+c1*b2,
    )
def defect(s):
    d,a,b,c,t=s
    return Fraction(t,d)-Fraction(a*b+a*c+b*c,d*d)

star=(4,1,1,1,1)
s=(1,0,0,0,0)
for m in range(1,13):
    s=compose(s,star)
    assert s==terminal_signature(m)
    assert defect(s)==Fraction(m,16)

print("PASS exact K3m structured-adversary checks")
print("m_range=2..12")
print("same-star pair formulas and overlap identity: PASS")
print("ordinary n10*n01-only switching fails by exact cardinality for every checked m>=2")
print("three-terminal weighted-triangle defect: kappa=m*4^(2m-2), normalized_delta=m/16")
print("normalized_delta additive under parallel 3-terminal composition: PASS")
print("sample m=12:", checked[-1])
