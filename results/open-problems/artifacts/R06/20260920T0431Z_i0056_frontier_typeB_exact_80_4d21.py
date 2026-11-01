from collections import deque, Counter, defaultdict
from fractions import Fraction
from itertools import combinations

# Exact arithmetic in Z[a,b], a^2=2, b^2=b+1 (b=phi).
def add(x,y):
    return (x[0]+y[0],x[1]+y[1],x[2]+y[2],x[3]+y[3])
def mul(x,y):
    x0,x1,x2,x3=x; y0,y1,y2,y3=y
    return (
        x0*y0 + 2*x1*y1 + x2*y2 + 2*x3*y3,
        x0*y1 + x1*y0 + x2*y3 + x3*y2,
        x0*y2 + x2*y0 + x2*y2 + 2*x1*y3 + 2*x3*y1 + 2*x3*y3,
        x0*y3 + x3*y0 + x1*y2 + x2*y1 + x2*y3 + x3*y2,
    )
Z=(0,0,0,0); ONE=(1,0,0,0); AALG=(0,1,0,0); BALG=(0,0,1,0); MONE=(-1,0,0,0)
def sring(items):
    z=Z
    for x in items: z=add(z,x)
    return z
def mm(X,Y):
    return tuple(tuple(sring(mul(X[i][k],Y[k][j]) for k in range(3)) for j in range(3)) for i in range(3))
def mv(X,v):
    return tuple(sring(mul(X[i][k],v[k]) for k in range(3)) for i in range(3))
I=tuple(tuple(ONE if i==j else Z for j in range(3)) for i in range(3))
def mpow(X,n):
    Y=I
    for _ in range(n): Y=mm(X,Y)
    return Y

S1=((MONE,AALG,Z),(Z,ONE,Z),(Z,Z,ONE))
S2=((ONE,Z,Z),(AALG,MONE,BALG),(Z,Z,ONE))
S3=((ONE,Z,Z),(Z,ONE,Z),(Z,BALG,MONE))
assert mm(S1,S1)==I and mm(S2,S2)==I and mm(S3,S3)==I
assert mpow(mm(S1,S2),4)==I and mpow(mm(S2,S3),5)==I and mpow(mm(S1,S3),2)==I
R=mm(S2,S3); Ri=mpow(R,4)
Q=mm(mm(S1,R),S1); Qi=mpow(Q,4)
assert mpow(R,5)==I and mpow(Q,5)==I and mpow(mm(R,Qi),2)==I
MID=(AALG,(2,0,0,0),BALG)
assert mv(S1,MID)==MID and mv(S3,MID)==MID
GENS=(R,Ri,Q,Qi)
assert len({mv(g,MID) for g in GENS})==4

# Exact development through S_18, enough to expose every neighbour of S_17.
MAX_R=18
dist={MID:0}; q=deque([MID])
while q:
    v=q.popleft(); d=dist[v]
    if d==MAX_R: continue
    for g in GENS:
        w=mv(g,v)
        if w not in dist:
            dist[w]=d+1; q.append(w)
byd=defaultdict(list)
for v,d in dist.items(): byd[d].append(v)
shell=[len(byd[n]) for n in range(MAX_R+1)]
expected=[1,4,10,20,38,70,130,240,446,824,1528,2824,5234,9680,17934,33178,61450,113708,210566]
assert shell==expected

# Radius-16 ball and S_17 frontier.
B16=sum(shell[:17])
S17=set(byd[17]); S18=set(byd[18])
assert B16==133611 and len(S17)==113708 and len(S18)==210566

# Proven all-radius type vocabulary; classify the fully exposed S_17 exactly.
ptype={}
counts=Counter()
for v in S17:
    ds=[dist[mv(g,v)]-17 for g in GENS]
    t=(ds.count(-1),ds.count(0),ds.count(1))
    assert t in {(1,0,3),(1,1,2),(2,0,2)}
    ptype[v]=t; counts[t]+=1
A=(1,0,3); B=(1,1,2); C=(2,0,2)
assert counts[A]==26320 and counts[B]==63924 and counts[C]==23464

# Exact one-frontier objective K=B_16 union W.
def departure_union(W):
    N=set()
    for v in W:
        for g in GENS:
            w=mv(g,v)
            if dist[w]==18:
                N.add(w)
    return N

def ratio_for(W):
    N=departure_union(W)
    k=B16+len(W)
    bd=len(S17)-len(W)+len(N)
    return k,bd,len(N),Fraction(bd,k)

classes={'A':{v for v in S17 if ptype[v]==A},
         'B':{v for v in S17 if ptype[v]==B},
         'C':{v for v in S17 if ptype[v]==C}}

# Evaluate all seven nonempty unions of the three exact frontier types.
results={}
for r in (1,2,3):
    for names in combinations(('A','B','C'),r):
        W=set().union(*(classes[name] for name in names))
        results['+'.join(names)]=ratio_for(W)

k,bd,nplus,rat=results['B']
assert len(classes['B'])==63924
assert nplus==117022
assert k==197535
assert bd==166806
assert rat==Fraction(55602,65845)

# Strictly better than the preceding radius-16 ball witness.
old=Fraction(113708,133611)
assert rat < old
cross=113708*65845-55602*133611
assert cross==58064438

# Among unions of whole frontier types, B alone is uniquely best.
assert all(rat < val[3] for key,val in results.items() if key!='B')

# Structural overlap diagnostic: S_18 vertices with two B parents are where the gain comes from.
bb_two_parent=0
parent_pair_counts=Counter()
for w in S18:
    parents=[]
    for g in GENS:
        v=mv(g,w)
        if dist.get(v)==17:
            parents.append(ptype[v])
    if len(parents)==2:
        key=tuple(sorted(parents))
        parent_pair_counts[key]+=1
        if parents[0]==B and parents[1]==B:
            bb_two_parent+=1
assert bb_two_parent==10826

print('T_SHELLS_0_TO_18', shell)
print('B16_SIZE', B16)
print('S17_TYPE_COUNTS', {'A':counts[A], 'B':counts[B], 'C':counts[C]})
for key in sorted(results):
    kk,bb,nn,rr=results[key]
    print('TYPE_UNION', key, 'K', kk, 'BOUNDARY', bb, 'NPLUS', nn, 'RATIO', f'{rr.numerator}/{rr.denominator}')
print('TYPE_B_SELECTED', len(classes['B']))
print('TYPE_B_DEPARTURE_UNION', nplus)
print('NEW_WITNESS_SIZE', k)
print('NEW_WITNESS_BOUNDARY', bd)
print('NEW_UPPER_BOUND_REDUCED', f'{rat.numerator}/{rat.denominator}')
print('STRICT_IMPROVEMENT_CROSS_MARGIN', cross)
print('B_B_TWO_PARENT_CHILDREN', bb_two_parent)
print('TWO_PARENT_TYPE_PAIR_COUNTS', dict(parent_pair_counts))
print('ALL_EXACT_CHECKS_PASS')
