#!/usr/bin/env python3
"""Exact reference-orbit rotation atlas for HARD8-08.

Source data encoded from Parts, arXiv:2010.12665v2:
- base coordinate map (a,b,c,d) -> (a+b*sqrt(33)+i*c*sqrt(3)+i*d*sqrt(11))/12;
- orbit generators tau_1,...,tau_5;
- Type-M reference orbit generator (0,4,4,0);
- historical rotation rho=(7+i*sqrt(15))/8.

All arithmetic is exact over Q(sqrt(3),sqrt(5),sqrt(11)).
No floating-point comparison is used for any asserted equality/count.
"""
from fractions import Fraction
from collections import deque, defaultdict, Counter

D = (3,5,11) # basis bit 0=sqrt3, bit1=sqrt5, bit2=sqrt11

def q(x): return Fraction(x)

def madd(A,B):
    C=dict(A)
    for m,v in B.items():
        C[m]=C.get(m,Fraction(0))+v
        if C[m]==0: del C[m]
    return C

def mscale(A,s):
    s=Fraction(s)
    return {m:v*s for m,v in A.items() if v*s}

def mmul(A,B):
    C={}
    for ma,va in A.items():
        for mb,vb in B.items():
            common=ma & mb
            fac=1
            for i,d in enumerate(D):
                if (common>>i)&1: fac*=d
            m=ma ^ mb
            C[m]=C.get(m,Fraction(0))+va*vb*fac
    return {m:v for m,v in C.items() if v}

def mkey(A): return tuple(A.get(m,Fraction(0)) for m in range(8))
ZERO={}
ONE={0:Fraction(1)}

def cadd(z,w): return (madd(z[0],w[0]),madd(z[1],w[1]))
def cneg(z): return (mscale(z[0],-1),mscale(z[1],-1))
def csub(z,w): return cadd(z,cneg(w))
def cmul(z,w):
    return (madd(mmul(z[0],w[0]),mscale(mmul(z[1],w[1]),-1)),
            madd(mmul(z[0],w[1]),mmul(z[1],w[0])))
def cconj(z): return (z[0],mscale(z[1],-1))
def cscale(z,s): return (mscale(z[0],s),mscale(z[1],s))
def cnorm2(z):
    p=cmul(z,cconj(z))
    assert not p[1]
    return p[0]
def ckey(z): return mkey(z[0])+mkey(z[1])
def cpow(z,n):
    out=(ONE,ZERO); b=z
    while n:
        if n&1: out=cmul(out,b)
        b=cmul(b,b); n//=2
    return out

def matvec(M,v):
    return tuple(sum((M[i][j]*v[j] for j in range(4)),Fraction(0)) for i in range(4))

# Exact Parts orbit generators (Section 2, h=1 notation).
h=Fraction(1,2)
tau1=(( -h,0,-3*h,0),(0,-h,0,-h),(h,0,-h,0),(0,3*h,0,-h))
tau2=(( -h,0, 3*h,0),(0,-h,0,h),(-h,0,-h,0),(0,-3*h,0,-h))
tau3=((-1,0,0,0),(0,-1,0,0),(0,0,1,0),(0,0,0,1))
tau4=((1,0,0,0),(0,1,0,0),(0,0,-1,0),(0,0,0,-1))
tau5=((1,0,0,0),(0,-1,0,0),(0,0,1,0),(0,0,0,-1))
GENS=(tau1,tau2,tau3,tau4,tau5)

def orbit(v0):
    v0=tuple(Fraction(x) for x in v0)
    seen={v0}; todo=deque([v0])
    while todo:
        v=todo.popleft()
        for g in GENS:
            w=matvec(g,v)
            if w not in seen:
                seen.add(w); todo.append(w)
    return sorted(seen)

def coord(v):
    a,b,c,d=v
    # sqrt33 = sqrt3*sqrt11 -> bit 101
    re={0:a/Fraction(12),0b101:b/Fraction(12)}
    im={0b001:c/Fraction(12),0b100:d/Fraction(12)}
    return ({m:x for m,x in re.items() if x},{m:x for m,x in im.items() if x})

ref_vecs=orbit((0,4,4,0))
assert len(ref_vecs)==12, len(ref_vecs)
O=[coord(v) for v in ref_vecs]
FOUR={0:Fraction(4)}
assert all(cnorm2(z)==FOUR for z in O)

# rho = (7+i sqrt15)/8, zeta_6 = (1+i sqrt3)/2.
rho=({0:Fraction(7,8)},{0b011:Fraction(1,8)})
rhobar=cconj(rho)
zeta=({0:Fraction(1,2)},{0b001:Fraction(1,2)})
assert cnorm2(rho)==ONE and cnorm2(zeta)==ONE

# One reference cross-edge determines q=(l*conj(s)/4)*rho^(+/-1).
# Enumerate all 12*12*2 roots and group them exactly.
seeds=defaultdict(list); q_by_key={}
for i,l in enumerate(O):
    for j,s in enumerate(O):
        ratio=cscale(cmul(l,cconj(s)),Fraction(1,4))
        assert cnorm2(ratio)==ONE
        for sign,r in ((+1,rho),(-1,rhobar)):
            Q=cmul(ratio,r)
            assert cnorm2(Q)==ONE
            d=csub(l,cmul(Q,s))
            assert cnorm2(d)==ONE
            k=ckey(Q)
            q_by_key[k]=Q
            seeds[k].append((i,j,sign))

assert sum(map(len,seeds.values()))==288
assert len(seeds)==36
hist=Counter(map(len,seeds.values()))
assert hist==Counter({6:24,12:12}), hist

direct_counts={}
for k,Q in q_by_key.items():
    n=0
    for l in O:
        for s in O:
            if cnorm2(csub(l,cmul(Q,s)))==ONE:
                n+=1
    direct_counts[k]=n
assert all(direct_counts[k]==len(seeds[k]) for k in seeds)
assert Counter(direct_counts.values())==Counter({6:24,12:12})

full={k for k,n in direct_counts.items() if n==12}
target=set()
for j in range(6):
    zj=cpow(zeta,j)
    target.add(ckey(cmul(zj,rho)))
    target.add(ckey(cmul(zj,rhobar)))
assert len(target)==12
assert full==target
assert ckey(rho) in full and ckey(rhobar) in full

aux_vecs=orbit((0,0,2,6))
assert len(aux_vecs)==12
AUX=[coord(v) for v in aux_vecs]
nplus={0:Fraction(17,6),0b101:Fraction(1,6)}
nminus={0:Fraction(17,6),0b101:Fraction(-1,6)}
aux_norms=Counter(mkey(cnorm2(z)) for z in AUX)
assert aux_norms==Counter({mkey(nplus):6,mkey(nminus):6})
for nk in (mkey(nplus),mkey(nminus)):
    cls=[z for z in AUX if mkey(cnorm2(z))==nk]
    base=cls[0]
    generated={ckey(cmul(cpow(zeta,j),base)) for j in range(6)}
    assert generated=={ckey(z) for z in cls}

def exact_edge_count(X,Y,Q):
    return sum(cnorm2(csub(x,cmul(Q,y)))==ONE for x in X for y in Y)
connection_hist=Counter()
for k,Q in q_by_key.items():
    rr=exact_edge_count(O,O,Q)
    aa=exact_edge_count(AUX,AUX,Q)
    ra=exact_edge_count(O,AUX,Q)
    ar=exact_edge_count(AUX,O,Q)
    connection_hist[(rr,aa,ra,ar)]+=1
assert connection_hist==Counter({(6,0,0,0):24,(12,12,0,0):12}), connection_hist
assert all(exact_edge_count(AUX,AUX,q_by_key[k])==0 for k in set(q_by_key)-full)

# Same-radius auxiliary angle classes.
cplus={0:Fraction(205,256),0b101:Fraction(3,256)}
cminus={0:Fraction(205,256),0b101:Fraction(-3,256)}
for n,cang in ((nplus,cplus),(nminus,cminus)):
    lhs=mscale(mmul(n,madd(ONE,mscale(cang,-1))),2)
    assert lhs==ONE
histcos={0:Fraction(7,8)}
assert mkey(cplus)!=mkey(histcos) and mkey(cminus)!=mkey(histcos)
assert mkey(cplus)!=mkey(cminus)

NL,NS=374,136
N=NL*NS
assert N==50864
assert 2*N==101728
assert N*(N-1)//2==1293547816

print('reference_orbit_vertices',len(O))
print('reference_orbit_norm_squared',4)
print('raw_reference_edge_roots',12*12*2)
print('distinct_reference_rotations',len(seeds))
print('reference_edge_count_histogram',dict(sorted(Counter(direct_counts.values()).items())))
print('max_reference_edges',max(direct_counts.values()))
print('max_rotation_count',len(full))
print('max_rotations_exact_form','zeta_6^k * rho^{+/-1}, k=0,...,5')
print('historical_rho_reference_edges',direct_counts[ckey(rho)])
print('published_LS_raw_vertex_pairs',N)
print('single_edge_line_circle_root_upper_bound',2*N)
print('old_two_edge_raw_pair_systems',N*(N-1)//2)
print('auxiliary_orbit_vertices',len(AUX))
print('auxiliary_radius_classes','6 each at (17 +/- sqrt(33))/6')
print('reference_induced_connection_histogram',dict(sorted(connection_hist.items())))
print('nonhistorical_reference_induced_with_aux_edges',0)
print('same_radius_aux_cos_plus','(205 + 3*sqrt(33))/256')
print('same_radius_aux_cos_minus','(205 - 3*sqrt(33))/256')
print('ALL_EXACT_REFERENCE_ATLAS_CHECKS_PASSED')
