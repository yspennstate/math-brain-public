from fractions import Fraction
from itertools import combinations

N=6

def subsets_of(s):
    t=s
    out=[]
    while True:
        out.append(t)
        if t==0: break
        t=(t-1)&s
    return out

DOWN=[]
for s in range(1<<N):
    mask=0
    for t in subsets_of(s):
        mask |= 1<<t
    DOWN.append(mask)

# Enumerate every down-set of size <=13 by adjoining minimal missing elements.
by_size={1:{1}}  # {empty set}
for sz in range(1,13):
    nxt=set()
    for I in by_size[sz]:
        for s in range(1,1<<N):
            if (I>>s)&1:
                continue
            proper=DOWN[s] & ~(1<<s)
            if proper & ~I == 0:
                nxt.add(I | (1<<s))
    by_size[sz+1]=nxt

def elems(I):
    return [s for s in range(1<<N) if (I>>s)&1]

def diameter(I):
    E=elems(I)
    return max((s^t).bit_count() for s in E for t in E)

def classify(I):
    E=elems(I)
    if diameter(I)>3:
        return None
    maxrank=max(s.bit_count() for s in E)
    singles=[s for s in E if s.bit_count()==1]
    edges=[s for s in E if s.bit_count()==2]
    triples=[s for s in E if s.bit_count()==3]
    if maxrank>=3:
        # Diameter<=3 + down-set forces exactly one 3-cube.
        assert maxrank==3
        assert len(triples)==1
        T=triples[0]
        assert I==DOWN[T]
        return ("cube",3)
    if not edges:
        return ("rank1",len(singles))
    # edge family must be intersecting
    for a,b in combinations(edges,2):
        assert a & b
    common=edges[0]
    for e in edges[1:]:
        common &= e
    if common:
        # star, choose one common center
        center=(common & -common)
        q=len(edges)
        incident=set()
        for e in edges:
            assert e & center
            for j in range(N):
                if (e>>j)&1:
                    incident.add(j)
        singidx={j for j in range(N) if (I>>(1<<j))&1}
        # All edge endpoints are singletons by down-set property.
        assert incident <= singidx
        l=len(singidx)-len(incident)
        assert len(incident)==q+1
        assert q+l<=5
        return ("star",q,l)
    # No common vertex. Pairwise-intersecting graph must be a triangle.
    assert len(edges)==3
    union=0
    for e in edges:
        union |= e
    assert union.bit_count()==3
    tri_vertices={j for j in range(N) if (union>>j)&1}
    expected={ (1<<i)|(1<<j) for i,j in combinations(sorted(tri_vertices),2)}
    assert set(edges)==expected
    singidx={j for j in range(N) if (I>>(1<<j))&1}
    l=len(singidx-tri_vertices)
    assert 0<=l<=3
    return ("triangle",l)

diam3=[]
for sz in range(1,14):
    for I in by_size[sz]:
        if diameter(I)<=3:
            diam3.append((sz,I,classify(I)))

# Exact consequence of the classification: no diameter<=3 down-set has size 13.
assert not any(sz==13 for sz,_,_ in diam3)
max_size=max(sz for sz,_,_ in diam3)
assert max_size==12

def q_rank1(k):
    b=k+1
    return Fraction(k*(k-1)**2,(k+1)**2) + (6-k)

def q_triangle(l):
    # uniform distribution on empty, 3+l singletons, and 3 triangle edges.
    b=7+l
    # Triangle coordinates each occur in 1 singleton +2 edges =3 sets.
    mt=Fraction(b-6,b)
    # each isolated singleton occurs once
    mi=Fraction(b-2,b)
    inactive=3-l
    return 3*mt*mt + l*mi*mi + inactive

def q_star(q,l):
    b=2+2*q+l
    if q>=l:
        # Distribution supported on q edges, q leaf singletons, l isolated singletons:
        # edge mass p=1/(2q), leaf singleton mass s=1/(q+l)-1/(2q),
        # isolate mass h=1/(q+l). Center mean=0; all other active coordinates
        # have mean 1-2/(q+l).
        k=q+l
        p=Fraction(1,2*q)
        s=Fraction(1,k)-Fraction(1,2*q)
        h=Fraction(1,k) if l else Fraction(0,1)
        assert p>=0 and s>=0 and h>=0
        total=q*p + q*s + l*h
        assert total==1
        m=1-Fraction(2,k)
        inactive=5-k
        return k*m*m + inactive
    # Four possible q<l cases; uniform distribution is enough.
    # empty + center singleton + q leaf singletons + l isolated singletons + q edges
    # center occurs in 1+q sets; each leaf in singleton+edge; isolate in singleton.
    mc=Fraction(b-2*(1+q),b)
    ml=Fraction(b-4,b)
    mi=Fraction(b-2,b)
    inactive=5-q-l
    return mc*mc + q*ml*ml + l*mi*mi + inactive

# Verify certificate inequality ||c||^2 <= 24/b for every classified type.
for k in range(0,7):
    b=k+1
    qv=q_rank1(k)
    assert qv <= Fraction(24,b), ("rank1",k,qv,Fraction(24,b))

# cube b=8, uniform on all 8 vertices => mean zero on cube coords, +1 on 3 others
assert Fraction(3,1) == Fraction(24,8)

for l in range(0,4):
    b=7+l
    qv=q_triangle(l)
    assert qv <= Fraction(24,b), ("triangle",l,qv,Fraction(24,b))

for q in range(1,6):
    for l in range(0,6-q):
        b=2+2*q+l
        qv=q_star(q,l)
        assert qv <= Fraction(24,b), ("star",q,l,qv,Fraction(24,b))

# Check every actual diameter<=3 down-set maps to a type whose certificate meets its own 24/b target.
for sz,I,typ in diam3:
    if typ[0]=="rank1":
        qv=q_rank1(typ[1])
    elif typ[0]=="cube":
        qv=Fraction(3,1)
    elif typ[0]=="triangle":
        qv=q_triangle(typ[1])
    elif typ[0]=="star":
        qv=q_star(typ[1],typ[2])
    else:
        raise AssertionError(typ)
    assert qv <= Fraction(24,sz), (sz,typ,qv,Fraction(24,sz))

# Algebraic tail coefficient at t0=3/sqrt(2):
# t0^2 = 9/2; (9/2)/(24/b) = 3b/16.
assert Fraction(9,2) / Fraction(24,1) == Fraction(3,16)

# Global six-column incidence threshold:
# b_i < (16/3)||r_i||^2 and sum_i ||r_i||^2 <=6 => total bad incidences <32.
assert Fraction(16,3)*6 == 32

print("R13 exact n=6 cube-diameter checker")
print("downsets_size_1_to_13 =", sum(len(by_size[k]) for k in range(1,14)))
print("diameter_le_3_downsets =", len(diam3))
print("max_diameter_le_3_downset_size =", max_size)
print("rank1_certificate_cases = 7")
print("triangle_certificate_cases = 4")
print("star_certificate_cases = 15")
print("cube_certificate_cases = 1")
print("tail_threshold_squared = 9/2")
print("row_charge_coefficient = 16/3")
print("global_bad_incidence_strict_upper = 32")
print("ALL_EXACT_CHECKS_PASS")
