from collections import deque, defaultdict
from fractions import Fraction
import hashlib
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import maximum_flow

# Exact Coxeter development of T=r{4,5} in Z[a,b], a^2=2, b^2=b+1.
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
GENS=(R,Ri,Q,Qi)
assert len({mv(g,MID) for g in GENS})==4

# Develop through radius 18. This contains every neighbour of every candidate through radius 17.
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

# Maximum-closure formulation for the integer threshold (1+r)=1795/1000.
# selected candidates: B_17; coverage nodes: B_18.
P=[]
for n in range(18): P.extend(byd[n])
C=[]
for n in range(19): C.extend(byd[n])
np_=len(P); nc=len(C); ci={v:i for i,v in enumerate(C)}
assert np_==247319 and nc==457885

imp=[]
for i,v in enumerate(P):
    imp.append((i,ci[v]))
    for g in GENS:
        w=mv(g,v)
        assert w in ci
        imp.append((i,ci[w]))
assert len(imp)==1236595

reward=1795
cover_cost=1000
source=0; p0=1; c0=1+np_; sink=c0+nc; N=sink+1
rows=[source]*np_
cols=list(range(p0,p0+np_))
data=[reward]*np_
INF=reward*np_+1
assert INF==443937606 and INF<2_147_000_000
for i,j in imp:
    rows.append(p0+i); cols.append(c0+j); data.append(INF)
rows.extend(range(c0,c0+nc)); cols.extend([sink]*nc); data.extend([cover_cost]*nc)
cap=coo_matrix((np.asarray(data,dtype=np.int64),
                (np.asarray(rows,dtype=np.int32),np.asarray(cols,dtype=np.int32))),
               shape=(N,N)).tocsr()
assert cap.nnz==1941799
res=maximum_flow(cap,source,sink,method='dinic')
assert int(res.flow_value)==443793100

# Recover the source side of the exact residual cut.
residual=(cap-res.flow).tocsr()
seen=np.zeros(N,dtype=bool); seen[source]=True; dq=deque([source])
while dq:
    u=dq.popleft()
    for k in range(residual.indptr[u],residual.indptr[u+1]):
        if residual.data[k]>0:
            v=residual.indices[k]
            if not seen[v]:
                seen[v]=True; dq.append(v)
Widx=np.flatnonzero(seen[p0:p0+np_])
Covidx=np.flatnonzero(seen[c0:c0+nc])
assert len(Widx)==147339 and len(Covidx)==264329
assert hashlib.sha256(Widx.astype('<i8').tobytes()).hexdigest()=="9421fb6797830c34f3805e8396b8446263d93cd964058adab75d723b37f420bb"
assert hashlib.sha256(Covidx.astype('<i8').tobytes()).hexdigest()=="577090beb9217daa49400d85a5743e6dd3ccca9532c68f697f2bbf9406a4814e"

# Independent exact reconstruction of K union partial K from the returned selected vertices.
W={P[i] for i in Widx}
covered=set(W)
for v in W:
    for g in GENS:
        covered.add(mv(g,v))
assert covered=={C[i] for i in Covidx}
assert len(W)==147339 and len(covered)==264329
outer=len(covered)-len(W)
assert outer==116990
ratio=Fraction(outer,len(W))
assert ratio==Fraction(116990,147339)

# Radial fingerprint of the non-round witness.
hist=[0]*18
for v in W: hist[dist[v]]+=1
expected_hist=[1,4,10,20,38,70,130,240,446,824,1528,2824,5234,9680,17934,33178,46710,28468]
assert hist==expected_hist

# Strict improvement over the preceding rigorous radius-16 ball witness.
old=Fraction(113708,133611)
assert ratio < old
cross=113708*147339-116990*133611
assert cross==1122472122

print('T_SHELLS_0_TO_18', shell)
print('CANDIDATE_VERTICES_B17', np_)
print('COVERAGE_VERTICES_B18', nc)
print('IMPLICATION_ARCS', len(imp))
print('INTEGER_CLOSURE_REWARD_COST', reward, cover_cost)
print('MAX_FLOW_VALUE', int(res.flow_value))
print('SELECTED_INDEX_SHA256', hashlib.sha256(Widx.astype('<i8').tobytes()).hexdigest())
print('COVERED_INDEX_SHA256', hashlib.sha256(Covidx.astype('<i8').tobytes()).hexdigest())
print('SELECTED_RADIAL_HISTOGRAM', hist)
print('WITNESS_SIZE', len(W))
print('WITNESS_COVERED_SIZE', len(covered))
print('WITNESS_OUTER_VERTEX_BOUNDARY', outer)
print('NEW_UPPER_BOUND', f'{ratio.numerator}/{ratio.denominator}')
print('STRICT_IMPROVEMENT_CROSS_MARGIN', cross)
print('ALL_EXACT_CHECKS_PASS')
