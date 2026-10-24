#!/usr/bin/env python3
from fractions import Fraction

N = 8
D = 5
TARGET = Fraction(96,1)

# A family is represented by an integer whose bit S records membership of subset S of [8].
# principal_shifted(S) is the closure of {S} under deletions and ij-shifts j->i (i<j).
def principal_shifted(S):
    seen = {S}
    stack = [S]
    while stack:
        x = stack.pop()
        for j in range(N):
            if (x >> j) & 1:
                # deletion
                y = x & ~(1 << j)
                if y not in seen:
                    seen.add(y); stack.append(y)
                # left shift j -> i
                for i in range(j):
                    if not ((x >> i) & 1):
                        y = (x & ~(1 << j)) | (1 << i)
                        if y not in seen:
                            seen.add(y); stack.append(y)
    fam = 0
    for x in seen:
        fam |= 1 << x
    return fam

def members(F):
    out=[]
    x=F
    while x:
        lsb=x & -x
        out.append(lsb.bit_length()-1)
        x-=lsb
    return out

# For a downset, Hamming diameter <=D is equivalent to |A union B|<=D for all A,B.
# We test the latter directly.
def valid_diameter(F):
    L=members(F)
    return all((a|b).bit_count() <= D for a in L for b in L)

# Conflict masks allow exact monotone pruning while enumerating unions of principal shifted ideals.
CONFLICT=[0]*(1<<N)
for a in range(1<<N):
    cm=0
    for b in range(1<<N):
        if (a|b).bit_count() > D:
            cm |= 1 << b
    CONFLICT[a]=cm

principal_masks=[]
conf_of_principal={}
for S in range(1<<N):
    P=principal_shifted(S)
    if P in conf_of_principal:
        continue
    if valid_diameter(P):
        cm=0
        for a in members(P):
            cm |= CONFLICT[a]
        principal_masks.append(P)
        conf_of_principal[P]=cm
principal_masks.sort(key=lambda z:(z.bit_count(),z))
assert len(principal_masks)==74

# Branch include/exclude over every valid principal shifted ideal. Invalid unions may be pruned
# permanently because pairwise-union validity is hereditary under taking subfamilies.
families={1}  # {empty set}
for P in principal_masks:
    cm=conf_of_principal[P]
    add=set()
    for F in families:
        if F & cm:
            continue
        add.add(F|P)
    families |= add
assert len(families)==9612
assert all(valid_diameter(F) for F in families)

# Verify each enumerated family is a downset and shifted; this also guards the closure generator.
def is_down_shifted(F):
    Sset=set(members(F))
    for S in list(Sset):
        for j in range(N):
            if (S>>j)&1:
                if (S & ~(1<<j)) not in Sset:
                    return False
                for i in range(j):
                    if not ((S>>i)&1):
                        T=(S & ~(1<<j)) | (1<<i)
                        if T not in Sset:
                            return False
    return True
assert all(is_down_shifted(F) for F in families)

# Every shifted downset of diameter <=5 is the union of the principal shifted closures of its
# members, so the above include/exclude construction is exhaustive. The following facet certificate
# is then checked on every one of the 9612 families.
def facets(F):
    L=members(F)
    out=[]
    for A in L:
        if not any(A!=B and (A&B)==A for B in L):
            out.append(A)
    return out

def standard_Q(F):
    b=F.bit_count()
    M=facets(F)
    h=len(M)
    deg=[sum((A>>j)&1 for A in M) for j in range(N)]
    # Choose a facet uniformly. Conditional on that facet, thin coordinate j so its total
    # inclusion marginal is min(deg_j/h,1/2). Downward closure keeps support in F.
    cs=[]
    for dj in deg:
        if 2*dj >= h:
            cs.append(Fraction(0,1))
        else:
            cs.append(Fraction(h-2*dj,h))
    norm2=sum(c*c for c in cs)
    return Fraction(b,1)*norm2, tuple(sorted(M)), tuple(deg), norm2

fail=[]
max_standard=(Fraction(-1,1),None)
eq=[]
for F in families:
    q,fac,deg,n2=standard_Q(F)
    if q > max_standard[0]:
        max_standard=(q,F)
    if q > TARGET:
        fail.append((F,q,fac,deg,n2))
    if q == TARGET:
        eq.append((F,fac,deg))

assert len(fail)==1
Fexc,qexc,facexc,degexc,n2exc=fail[0]
expected_facets=tuple(sorted([
    0b00001111,
    0b00010111,
    0b00100111,
    0b01000111,
    0b10000011,
    0b10000101,
    0b10000110,
]))
assert facexc==expected_facets
assert Fexc.bit_count()==47
assert qexc==Fraction(4747,49)
assert degexc==(6,6,6,1,1,1,1,3)

# Exceptional family: weights 1/5 on each of the four 4-facets and 1/15 on each of the
# three 3-facets. Coverage is 14/15 on coordinates 0,1,2 and 1/5 on 3,...,7.
# Thin any coordinate with coverage >1/2 down to marginal 1/2. The resulting sign mean is
# 0 on 0,1,2 and 3/5 on 3,...,7, hence norm^2=9/5 and Q=47*9/5=423/5<96.
weights={A:(Fraction(1,5) if A.bit_count()==4 else Fraction(1,15)) for A in facexc}
assert sum(weights.values(),Fraction(0,1))==1
coverage=[]
for j in range(N):
    coverage.append(sum(w for A,w in weights.items() if (A>>j)&1))
assert coverage[:3]==[Fraction(14,15)]*3
assert coverage[3:]==[Fraction(1,5)]*5
c_exc=[max(Fraction(0,1),1-2*y) for y in coverage]
norm2_alt=sum(c*c for c in c_exc)
q_alt=Fraction(Fexc.bit_count(),1)*norm2_alt
assert norm2_alt==Fraction(9,5)
assert q_alt==Fraction(423,5)
assert q_alt<TARGET

# Also certify the sharp principal-five-cube equality is present.
P5=principal_shifted(0b00011111)
assert valid_diameter(P5) and P5.bit_count()==32
q5,fac5,deg5,n25=standard_Q(P5)
assert q5==TARGET

# Exact metric movement: sqrt(6) < 27919/10000 from the preceding R13 envelope.
assert 6 * 10000**2 < 27919**2

print('R13 n=8 shifted-diameter-5 exact checker')
print('valid_principal_shifted_ideals=',len(principal_masks))
print('shifted_downsets_diameter_le_5=',len(families))
print('standard_certificate_failures=',len(fail))
print('exception_size=',Fexc.bit_count())
print('exception_standard_Q=',qexc)
print('exception_alt_norm2=',norm2_alt)
print('exception_alt_Q=',q_alt)
print('principal_5_cube_Q=',q5)
print('metric_sqrt6_lt_27919_over_10000= PASS')
print('standard_equalities=',len(eq))
print('max_standard_Q=',max_standard[0])
print('ALL_EXACT_CHECKS_PASS')
