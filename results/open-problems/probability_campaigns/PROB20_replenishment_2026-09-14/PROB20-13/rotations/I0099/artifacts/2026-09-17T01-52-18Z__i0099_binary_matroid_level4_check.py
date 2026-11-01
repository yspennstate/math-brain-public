#!/usr/bin/env python3
"""
I0099 exact self-check: binary nonneighbor-incidence algebra and the
failure of the level-4 elliptic quotient to determine adjacency.

All computations use exact integer/F_2/F_p arithmetic.
"""

from itertools import combinations

PRIMES = [13,17,29,37,41,53,61,73,89,97,101,109,113,137,149,157,173,181,193,197]

def isprime(n):
    if n < 2: return False
    d = 2
    while d*d <= n:
        if n % d == 0: return n == d
        d += 1 if d == 2 else 2
    return True

def qrset(p):
    return {x*x % p for x in range(1,p)}

def paley_nonneighbor_rows(p):
    qr = qrset(p)
    rows=[]
    for a in range(p):
        r=0
        for x in range(p):
            if x != a and (x-a) % p not in qr:
                r |= 1 << x
        rows.append(r)
    return rows

def gf2_rank(rows):
    basis={}
    for x in rows:
        y=x
        while y:
            b=y.bit_length()-1
            if b in basis:
                y ^= basis[b]
            else:
                basis[b]=y
                break
    return len(basis)

def parity(x): return x.bit_count() & 1

def matvec(rows, v):
    # symmetric matrix rows, returns M v as bit-vector
    out=0
    for i,r in enumerate(rows):
        if parity(r & v):
            out |= 1 << i
    return out

def verify_matrix_relation(p):
    rows=paley_nonneighbor_rows(p)
    all1=(1<<p)-1
    q=(p-1)//4
    # N^2 = N + q(I+J) over F2, tested columnwise exactly.
    for j in range(p):
        e=1<<j
        lhs=matvec(rows, matvec(rows,e))
        rhs=matvec(rows,e)
        if q&1:
            rhs ^= e ^ all1   # (I+J)e_j = e_j + 1
        assert lhs==rhs, (p,j,lhs,rhs)
    # N 1 = 0
    assert matvec(rows,all1)==0
    rank=gf2_rank(rows)
    expected=(p-1 if p%8==5 else (p-1)//2)
    assert rank==expected,(p,rank,expected)
    if p%8==5:
        # Row span is exactly the even-weight hyperplane:
        # all rows even and rank p-1.
        assert all((r.bit_count()&1)==0 for r in rows)
    return rank

# Elliptic curve y^2=x^3+a2 x^2+a4 x+a6, a1=a3=0.
def inv(a,p): return pow(a%p,p-2,p)

def ec_add(P,Q,p,a2,a4,a6):
    if P is None: return Q
    if Q is None: return P
    x1,y1=P; x2,y2=Q
    if x1==x2 and (y1+y2)%p==0:
        return None
    if P==Q:
        assert y1%p
        m=(3*x1*x1+2*a2*x1+a4)*inv(2*y1,p)%p
    else:
        m=(y2-y1)*inv(x2-x1,p)%p
    x3=(m*m-a2-x1-x2)%p
    y3=(-y1+m*(x1-x3))%p
    return (x3,y3)

def ec_mul(n,P,p,a2,a4,a6):
    R=None
    Q=P
    while n:
        if n&1: R=ec_add(R,Q,p,a2,a4,a6)
        Q=ec_add(Q,Q,p,a2,a4,a6)
        n//=2
    return R

def ec_curve(p,a,b,c):
    a2=(-(a+b+c))%p
    a4=(a*b+a*c+b*c)%p
    a6=(-a*b*c)%p
    pts=[None]
    for x in range(p):
        rhs=((x-a)*(x-b)*(x-c))%p
        for y in range(p):
            if y*y%p==rhs:
                pts.append((x,y))
    return pts,(a2,a4,a6)

def p53_level4_counterexample():
    p=53; a,b,c=0,1,7
    qr=qrset(p)
    assert all((u-v)%p in qr for u,v in combinations([a,b,c],2))
    pts,coef=ec_curve(p,a,b,c)
    a2,a4,a6=coef
    two={ec_mul(2,P,p,*coef) for P in pts}
    four={ec_mul(4,P,p,*coef) for P in pts}
    # Full rational 4-torsion consequences for this exact example.
    E2={P for P in pts if ec_mul(2,P,p,*coef) is None}
    E4={P for P in pts if ec_mul(4,P,p,*coef) is None}
    assert len(E2)==4
    assert len(E4)==16
    assert len(pts)==64 and len(two)==16 and len(four)==4

    # Canonicalize the four cosets of 4E in 2E by their sorted point encodings.
    def enc(P):
        return (-1,-1) if P is None else P
    unseen=set(two); cosets=[]
    while unseen:
        rep=min(unseen,key=enc)
        C={ec_add(rep,Q,p,*coef) for Q in four}
        cosets.append(C); unseen-=C
    cosets.sort(key=lambda C: min(enc(P) for P in C))
    assert len(cosets)==4
    def cls(P):
        for i,C in enumerate(cosets):
            if P in C: return i
        raise AssertionError("no class")
    common=[]
    for x in range(p):
        if x in (a,b,c): continue
        if all((x-r)%p in qr for r in (a,b,c)):
            rhs=((x-a)*(x-b)*(x-c))%p
            ys=[y for y in range(p) if y*y%p==rhs]
            assert len(ys)==2
            P=(x,min(ys))
            assert P in two
            # +/- P have the same class in 2E/4E.
            Pneg=(x,(-P[1])%p)
            assert cls(P)==cls(Pneg)
            common.append((x,P,cls(P)))
    assert len(common)==6

    # Find a fixed pair of quotient classes with both edge and nonedge examples.
    witnesses=[]
    for (x,P,cx),(y,Q,cy) in combinations(common,2):
        status=((x-y)%p in qr)
        witnesses.append((tuple(sorted((cx,cy))),status,x,y,(x-y)%p))
    amb={}
    for key,status,x,y,d in witnesses:
        amb.setdefault(key,[]).append((status,x,y,d))
    target=None
    for key,ls in amb.items():
        if {z[0] for z in ls}=={False,True}:
            target=(key,ls); break
    assert target is not None
    key,ls=target
    e=next(z for z in ls if z[0])
    ne=next(z for z in ls if not z[0])
    return {
        "triangle":(a,b,c),
        "E_order":len(pts),
        "twoE":len(two),
        "fourE":len(four),
        "common":[(x,cl) for x,P,cl in common],
        "class_pair":key,
        "edge":e,
        "nonedge":ne,
    }

def main():
    for p in PRIMES:
        assert isprime(p) and p%4==1
        r=verify_matrix_relation(p)
        print(f"RANK p={p} mod8={p%8} rankN={r} expected={p-1 if p%8==5 else (p-1)//2} PASS")
    ex=p53_level4_counterexample()
    print("P53_TRIANGLE", ex["triangle"])
    print(f"P53_E_ORDER={ex['E_order']} TWO_E={ex['twoE']} FOUR_E={ex['fourE']} QUOTIENT_CLASSES=4")
    print("P53_COMMON_X_CLASS=" + ",".join(f"{x}:{c}" for x,c in ex["common"]))
    key=ex["class_pair"]; e=ex["edge"]; ne=ex["nonedge"]
    print(f"P53_SAME_QUOTIENT_CLASS_PAIR={key}")
    print(f"P53_EDGE_EXAMPLE x={e[1]} y={e[2]} diff={e[3]} edge=1")
    print(f"P53_NONEDGE_EXAMPLE x={ne[1]} y={ne[2]} diff={ne[3]} edge=0")
    print("LEVEL4_QUOTIENT_DOES_NOT_DETERMINE_ADJACENCY=PASS")
    print("ALL_I0099_BINARY_MATROID_LEVEL4_SELF_CHECKS_PASS")

if __name__=="__main__":
    main()
