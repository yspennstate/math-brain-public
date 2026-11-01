from sympy import Matrix, Rational, I, conjugate, simplify, factor, symbols, Poly, zeros, eye
from itertools import combinations, permutations, product

EDGES=list(combinations(range(6),2))
EIDX={e:i for i,e in enumerate(EDGES)}
PAIRS=EDGES
COLS=[(0,1),(2,3),(4,5)]

def coeffvec(nonzero):
    v=[0]*45
    for c,e,a in nonzero:
        v[15*c+EIDX[tuple(e)]]=a
    return v

# Base fixed K6 facet objectives: F<=0.
V2160=coeffvec(
    [(0,e,-1) for e in [(0,4),(0,5),(1,4),(1,5),(2,4),(3,5),(4,5)]]+
    [(1,e,-1) for e in [(0,4),(1,5),(4,5)]]+
    [(2,e, 1) for e in [(0,2),(1,3),(2,3)]])
V1080=coeffvec(
    [(0,e, 1) for e in [(0,1),(4,5)]]+
    [(1,e,-1) for e in [(2,3),(2,4),(3,5)]]+
    [(2,e,-1) for e in [(0,2),(0,3),(1,2),(1,3),(2,3),(2,5),(3,4)]])
V540=coeffvec(
    [(0,e, 1) for e in [(0,4),(0,5),(2,4),(2,5),(3,4),(3,5),(4,5)]]+
    [(1,e, 1) for e in [(0,4),(0,5),(4,5)]]+
    [(2,(4,5),1),(2,(1,2),-1),(2,(1,3),-1)])
CONSTS=[Rational(0),Rational(0),Rational(-1)]
BASE=[V2160,V1080,V540]

# B18 exact normalization: subtract color constants whose sum cancels the affine constant.
CENTERS=[
    [Rational(-1,3),Rational(-1,3),Rational(2,3)],
    [Rational(2,3),Rational(-1,3),Rational(-1,3)],
    [Rational(1,2),Rational(1,2),Rational(0)],
]
SCALES=[Rational(3,2),Rational(3,2),Rational(1)]
for name,v,k,cent,sc in zip(["2160","1080","540"],BASE,CONSTS,CENTERS,SCALES):
    assert sum(cent)==-k
    d=[]
    for c in range(3):
        d.extend([Rational(v[15*c+j])-cent[c] for j in range(15)])
    assert max(abs(x) for x in d)*sc==1
    vals=[]
    for c0 in combinations(range(6),2):
        rem=[x for x in range(6) if x not in c0]
        for c1 in combinations(rem,2):
            c2=tuple(x for x in rem if x not in c1)
            state=[tuple(sorted(c0)),tuple(sorted(c1)),tuple(sorted(c2))]
            val=k+sum(Rational(v[15*c+EIDX[state[c]]]) for c in range(3))
            vals.append(val)
    assert len(vals)==90
    assert max(vals)<=0
    print("NORMALIZATION",name,"dual_scale",sc,"deterministic_max",max(vals),"min",min(vals))

def exact_cayley(vec,scale):
    A=zeros(6)
    for val,(i,j) in zip(vec,PAIRS):
        A[i,j]=Rational(val,scale)
        A[j,i]=-Rational(val,scale)
    return (eye(6)+A).inv()*(eye(6)-A)

def probs(Q):
    p=[]
    for a,b in COLS:
        for i,j in EDGES:
            z=simplify(Q[i,a]*Q[j,b]-Q[i,b]*Q[j,a])
            p.append(simplify(z*z))
    return p

def objective(p,v,k):
    return simplify(k+sum(Rational(a)*b for a,b in zip(v,p)))

def transformed(base, pv, pc):
    out=[0]*45
    for c in range(3):
        for e in EDGES:
            a=base[15*c+EIDX[e]]
            if a:
                ne=tuple(sorted((pv[e[0]],pv[e[1]])))
                out[15*pc[c]+EIDX[ne]]=a
    return out

def orbit_contains(base,target):
    for pv in permutations(range(6)):
        for pc in permutations(range(3)):
            if transformed(base,pv,pc)==target:
                return True
    return False

REAL=[
("2160",[-5,1,1,-3,3,-2,-2,0,-5,5,-1,-1,-2,1,5],1,
 [(0,(0,2),-1),(0,(0,3),-1),(0,(1,2),-1),(0,(2,3),-1),(0,(2,5),-1),(0,(3,4),-1),(0,(3,5),-1),
  (1,(0,1),1),(1,(1,4),1),(1,(4,5),1),(2,(0,2),-1),(2,(2,3),-1),(2,(3,5),-1)],
 Rational(-897244,785961225),Rational(16,785961225)),
("1080",[1,1,4,5,4,-5,3,0,0,0,-2,-2,-4,-5,5],6,
 [(0,(0,1),-1),(0,(0,4),-1),(0,(4,5),-1),(1,(0,2),-1),(1,(0,3),-1),(1,(0,4),-1),(1,(0,5),-1),(1,(1,4),-1),(1,(2,4),-1),(1,(3,4),-1),(2,(1,5),1),(2,(2,3),1)],
 Rational(-96121,180499225),Rational(4,180499225)),
("540",[3,5,1,4,0,3,-5,2,1,0,0,2,0,1,-4],1,
 [(0,(0,2),1),(0,(1,5),-1),(0,(3,5),-1),(1,(0,1),1),(1,(0,2),1),(1,(0,3),1),(1,(0,4),1),(1,(1,2),1),(1,(2,3),1),(1,(2,4),1),(2,(0,2),1),(2,(0,4),1),(2,(2,4),1)],
 Rational(-97376,265362075),Rational(256,796086225))
]
name_to_i={"2160":0,"1080":1,"540":2}
for name,vec,sc,nz,expected,min_expected in REAL:
    i=name_to_i[name]
    Q=exact_cayley(vec,sc)
    assert simplify(Q.T*Q-eye(6))==zeros(6)
    p=probs(Q)
    assert all(x>0 for x in p)
    assert min(p)==min_expected
    target=coeffvec(nz)
    assert orbit_contains(BASE[i],target)
    val=objective(p,target,CONSTS[i])
    assert val==expected and val<0
    print("REAL_NOMINEE",name,"raw",val,"normalized",simplify(SCALES[i]*val),"min_plucker",min(p))

print("ALL EXACT REAL NOMINEE CHECKS PASSED")
