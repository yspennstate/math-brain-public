#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product
from decimal import Decimal, getcontext
from functools import lru_cache

WITNESS = (7, 15, 119, 127)
NVAR = 5
LABELS = ("y1","y2","x0","x1","x2")

def bitval(bits):
    y1,y2,x0,x1,x2 = bits
    z = x0 | (x1 << 1) | (x2 << 2)
    return (WITNESS[(y1 << 1) | y2] >> z) & 1

PTS = list(product((0,1), repeat=NVAR))
ONES = {x for x in PTS if bitval(x)}
ZEROS = set(PTS) - ONES

# The peer slice uses p(y1)=p(y2)=1/4 and unbiased x0,x1,x2.
counts = tuple(m.bit_count() for m in WITNESS)
assert counts == (3,4,6,7)
assert 9*counts[0] + 3*counts[1] + 3*counts[2] + counts[3] == 64

# Essentiality under the ordinary uniform cube.
infl = []
for i in range(NVAR):
    directed = 0
    for x in PTS:
        y = list(x); y[i] ^= 1
        directed += (bitval(x) != bitval(tuple(y)))
    infl.append(Fraction(directed, len(PTS)))
assert all(q > 0 for q in infl)
assert infl == [Fraction(3,8), Fraction(1,8), Fraction(1,4), Fraction(1,4), Fraction(1,2)]

def projection(T, inds):
    return {tuple(x[i] for i in inds) for x in T}

# For an AND-type binary decomposition across A|B, one of ONES or ZEROS
# (after possible output negation) must be a Cartesian rectangle.
# Input negations only permute the corresponding coordinate assignments.
partitions = []
V = set(range(NVAR))
for r in (1,2):
    for A in combinations(range(NVAR), r):
        A = tuple(A)
        B = tuple(sorted(V - set(A)))
        partitions.append((A,B))
assert len(partitions) == 15

rect_rows = []
xor_rows = []
for A,B in partitions:
    poA,poB = projection(ONES,A),projection(ONES,B)
    pzA,pzB = projection(ZEROS,A),projection(ZEROS,B)
    d1 = len(poA)*len(poB)-len(ONES)
    d0 = len(pzA)*len(pzB)-len(ZEROS)
    assert d1 > 0 and d0 > 0
    rect_rows.append((A,B,d1,d0))

    # For an XOR/XNOR-type decomposition, the sign matrix across A|B has rank 1.
    av = list(product((0,1), repeat=len(A)))
    bv = list(product((0,1), repeat=len(B)))
    M = []
    for aa in av:
        row=[]
        for bb in bv:
            x=[0]*NVAR
            for i,v in zip(A,aa): x[i]=v
            for i,v in zip(B,bb): x[i]=v
            row.append(1 if bitval(tuple(x)) == 0 else -1)
        M.append(row)
    witness_minor = None
    for r1,r2 in combinations(range(len(M)),2):
        for c1,c2 in combinations(range(len(M[0])),2):
            det = M[r1][c1]*M[r2][c2] - M[r1][c2]*M[r2][c1]
            if det:
                witness_minor=(r1,r2,c1,c2,det)
                break
        if witness_minor:
            break
    assert witness_minor is not None
    assert abs(witness_minor[-1]) == 2
    xor_rows.append((A,B,witness_minor))

assert min(r[2] for r in rect_rows) == 1
assert min(r[3] for r in rect_rows) == 2
assert len(xor_rows) == 15

# Every essential two-input Boolean outer gate is NPN-equivalent to AND or XOR.
# The preceding two checks therefore certify binary composition-primality.

# Separate analytic read-once parity check: leaf probabilities are odd numerators
# over 4,4,2,2,2. Under disjoint AND and OR, odd numerators remain odd over the
# product denominator, so an essential five-leaf formula has odd numerator / 128.
bias = {0:Fraction(1,4),1:Fraction(1,4),2:Fraction(1,2),3:Fraction(1,2),4:Fraction(1,2)}
@lru_cache(None)
def reachable(vs):
    vs=tuple(sorted(vs))
    if len(vs)==1:
        p=bias[vs[0]]
        return {p,1-p}
    out=set()
    s=set(vs); m=min(s); rest=sorted(s-{m})
    for r in range(len(rest)+1):
        for extra in combinations(rest,r):
            A={m,*extra}
            if len(A)==len(s): continue
            B=s-A
            for p in reachable(tuple(A)):
                for q in reachable(tuple(B)):
                    out.add(p*q)
                    out.add(p+q-p*q)
    return out

rv=reachable(tuple(range(NVAR)))
assert Fraction(1,2) not in rv
assert len(rv)==64
assert {p.numerator for p in rv if p.denominator==128} == set(range(1,128,2))
assert all(p.denominator == 128 for p in rv)

# Independent exact/high-precision replay of the peer witness's C_req.
def walsh3(mask,T):
    s=0
    for z in range(8):
        parity=((z&T).bit_count() & 1)
        val=1 if ((mask>>z)&1) else -1
        s += val * (1 if parity==0 else -1)
    return s

n0=[]; n1=[]; n2=[]; n12=[]
for T in range(8):
    s00,s01,s10,s11=[walsh3(m,T) for m in WITNESS]
    n0.append((9*s00+3*s01+3*s10+s11)**2)
    n1.append(3*(3*(s10-s00)+(s11-s01))**2)
    n2.append(3*(3*(s01-s00)+(s11-s10))**2)
    n12.append(9*(s00-s01-s10+s11)**2)
assert sum(n0)+sum(n1)+sum(n2)+sum(n12)==16384
A=Fraction(sum(n1)+sum(n2)+2*sum(n12), 16384)*Fraction(4,3)
deg=[T.bit_count() for T in range(8)]
B=Fraction(sum(deg[T]*(n0[T]+n1[T]+n2[T]+n12[T]) for T in range(8)),16384)
assert A==Fraction(1,2) and B==Fraction(9,8)

getcontext().prec=80
D=Decimal
ln2=D(2).ln()
log2=lambda n: D(n).ln()/ln2
H=D(0)
for n in n0+n1+n2+n12:
    if n:
        p=D(n)/D(16384)
        H += p*(D(14)-log2(n))
Creq=(H + D(3)/D(4)*log2(3)*(D(A.numerator)/D(A.denominator))) / (
    D(A.numerator)/D(A.denominator) + D(B.numerator)/D(B.denominator)-D(1))
Cexact=D(51)/D(5)-D(27)/D(40)*log2(3)-D(5)/D(4)*log2(5)
assert abs(Creq-Cexact) < D("1e-70")
cg=D(5)*(Cexact-D("6.4548"))
assert cg < 0

print("PASS binary-composition-prime two-quarter maximizer")
print("branch_counts", counts)
print("uniform_influences", " ".join(str(q) for q in infl))
print("partitions_checked", len(partitions))
print("and_or_min_one_rectangle_deficit", min(r[2] for r in rect_rows))
print("and_or_min_zero_rectangle_deficit", min(r[3] for r in rect_rows))
print("xor_nonzero_minor_partitions", len(xor_rows))
print("xor_minor_abs", sorted({abs(r[2][-1]) for r in xor_rows}))
print("essential_readonce_reachable_probabilities", len(rv))
print("essential_readonce_balanced_possible", Fraction(1,2) in rv)
print("A_B", A, B)
print("Creq", Creq)
print("cG_at_C0_6.4548", cg)
