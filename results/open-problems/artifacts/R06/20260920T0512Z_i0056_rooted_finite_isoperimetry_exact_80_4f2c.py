from collections import deque, defaultdict
from fractions import Fraction
import hashlib
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from scipy.sparse import csr_matrix

# Exact arithmetic in Z[a,b], a^2=2, b^2=b+1 (b=golden ratio).
def add(x,y): return tuple(x[i]+y[i] for i in range(4))
def mul(x,y):
    x0,x1,x2,x3=x; y0,y1,y2,y3=y
    return (
        x0*y0 + 2*x1*y1 + x2*y2 + 2*x3*y3,
        x0*y1 + x1*y0 + x2*y3 + x3*y2,
        x0*y2 + x2*y0 + x2*y2 + 2*x1*y3 + 2*x3*y1 + 2*x3*y3,
        x0*y3 + x3*y0 + x1*y2 + x2*y1 + x2*y3 + x3*y2,
    )
Z=(0,0,0,0); ONE=(1,0,0,0); A=(0,1,0,0); B=(0,0,1,0); MONE=(-1,0,0,0)
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

S1=((MONE,A,Z),(Z,ONE,Z),(Z,Z,ONE))
S2=((ONE,Z,Z),(A,MONE,B),(Z,Z,ONE))
S3=((ONE,Z,Z),(Z,ONE,Z),(Z,B,MONE))
assert mm(S1,S1)==I and mm(S2,S2)==I and mm(S3,S3)==I
assert mpow(mm(S1,S2),4)==I and mpow(mm(S2,S3),5)==I and mpow(mm(S1,S3),2)==I
R=mm(S2,S3); Ri=mpow(R,4)
Q=mm(mm(S1,R),S1); Qi=mpow(Q,4)
assert mpow(R,5)==I and mpow(Q,5)==I and mpow(mm(R,Qi),2)==I
MID=(A,(2,0,0,0),B)
assert mv(S1,MID)==MID and mv(S3,MID)==MID
NAMES=('r','R','q','Q'); GENS=(R,Ri,Q,Qi)
assert len({mv(g,MID) for g in GENS})==4

# Exact BFS in the tetrapentagonal Schreier graph through the one-step
# neighbourhood of the search domain. Canonical words are discovery-independent
# identifiers fixed by generator order.
MAX_R=14
dist={MID:0}; word={MID:''}; dq=deque([MID]); byd=defaultdict(list)
while dq:
    v=dq.popleft(); d=dist[v]; byd[d].append(v)
    if d==MAX_R: continue
    for name,g in zip(NAMES,GENS):
        w=mv(g,v)
        if w not in dist:
            dist[w]=d+1; word[w]=word[v]+name; dq.append(w)

shell=[len(byd[n]) for n in range(MAX_R+1)]
expected=[1,4,10,20,38,70,130,240,446,824,1528,2824,5234,9680,17934]
assert shell==expected
for n in range(MAX_R):
    for v in byd[n]:
        ns=[mv(g,v) for g in GENS]
        assert len(set(ns))==4
        assert all(u in dist for u in ns)

# Discovery-only MILP on K subset B_13(root), with root forced in K.
# IMPORTANT: no optimality assertion from floating-point MILP is used in the
# mathematical claim. The returned binary set is independently re-counted below
# using exact group arithmetic; only that exact recount certifies the upper bound.
X=[v for n in range(14) for v in byd[n]]
Y=[v for n in range(15) for v in byd[n]]
xi={v:i for i,v in enumerate(X)}
yi={v:len(X)+i for i,v in enumerate(Y)}
N=len(X)+len(Y)
rows=[]; cols=[]; vals=[]; lower=[]; upper=[]; row=0
for v in X:
    for g in GENS:
        w=mv(g,v)
        # y_w >= x_v-x_w, with x_w=0 when w lies outside B_13.
        rows.extend((row,row)); cols.extend((yi[w],xi[v])); vals.extend((1.0,-1.0))
        if w in xi:
            rows.append(row); cols.append(xi[w]); vals.append(1.0)
        lower.append(0.0); upper.append(np.inf); row+=1
M=csr_matrix((vals,(rows,cols)),shape=(row,N))
lb=np.zeros(N); ub=np.ones(N); lb[xi[MID]]=ub[xi[MID]]=1.0
trial=Fraction(9946,12517)
c=np.zeros(N)
c[:len(X)]=-float(trial)
c[len(X):]=1.0
res=milp(c,integrality=np.ones(N),bounds=Bounds(lb,ub),
         constraints=LinearConstraint(M,np.asarray(lower),np.asarray(upper)),
         options={'mip_rel_gap':0.0})
assert res.x is not None
assert max(abs(z-round(z)) for z in res.x) < 1e-7
K={v for v,z in zip(X,res.x[:len(X)]) if z>0.5}

# Exact certification of the returned set: no solver objective, relaxation,
# or floating-point geometry enters these counts.
boundary=set()
for v in K:
    for g in GENS:
        w=mv(g,v)
        if w not in K:
            boundary.add(w)
assert all(w in dist for w in boundary)
assert len(K)==12517
assert len(boundary)==9946
assert Fraction(len(boundary),len(K))==Fraction(9946,12517)

selected_shell=[sum(v in K for v in byd[n]) for n in range(14)]
boundary_shell=[sum(v in boundary for v in byd[n]) for n in range(15)]
assert selected_shell==[1,4,10,20,38,70,130,240,446,824,1528,2824,3978,2404]
assert boundary_shell==[0,0,0,0,0,0,0,0,0,0,0,0,1256,4764,3926]

# Exact strict improvement over the previous certified upper bound.
old=Fraction(113708,133611); new=Fraction(9946,12517)
assert new < old
margin=old.numerator*new.denominator-new.numerator*old.denominator
assert margin==94388030

# Canonical exact-coordinate witness fingerprint (BFS word order fixed above).
words=sorted(word[v] for v in K)
digest=hashlib.sha256(('\n'.join(words)+'\n').encode()).hexdigest()
assert digest=='957938bd6b6d5a285db6f0924e03dba750e552beced45e453d5eec30fb5b88cb'

print('EXACT_GROUP_RELATIONS_PASS')
print('T_SHELLS_0_TO_14', shell)
print('WITNESS_SELECTED_SHELL_COUNTS_0_TO_13', selected_shell)
print('WITNESS_BOUNDARY_SHELL_COUNTS_0_TO_14', boundary_shell)
print('WITNESS_SIZE', len(K))
print('WITNESS_OUTER_VERTEX_BOUNDARY', len(boundary))
print('WITNESS_RATIO', f'{new.numerator}/{new.denominator}')
print('OLD_UPPER', f'{old.numerator}/{old.denominator}')
print('STRICT_IMPROVEMENT_CROSS_MARGIN', margin)
print('WITNESS_CANONICAL_WORD_SHA256', digest)
print('MILP_ROLE', 'DISCOVERY_ONLY; EXACT_RECOUNT_CERTIFIES_EXISTENCE')
print('ALL_EXACT_CHECKS_PASS')
