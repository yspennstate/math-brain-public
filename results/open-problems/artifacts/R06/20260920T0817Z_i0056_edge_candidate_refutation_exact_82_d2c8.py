from collections import deque, defaultdict, Counter
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import maximum_flow

# Exact ring Z[a,b], a^2=2, b^2=b+1, basis (1,a,b,ab).
Z=(0,0,0,0); ONE=(1,0,0,0); A=(0,1,0,0); B=(0,0,1,0); MONE=(-1,0,0,0)
def add(x,y): return (x[0]+y[0],x[1]+y[1],x[2]+y[2],x[3]+y[3])
def neg(x): return (-x[0],-x[1],-x[2],-x[3])
def mul(x,y):
    x0,x1,x2,x3=x; y0,y1,y2,y3=y
    return (
        x0*y0 + 2*x1*y1 + x2*y2 + 2*x3*y3,
        x0*y1 + x1*y0 + x2*y3 + x3*y2,
        x0*y2 + x2*y0 + x2*y2 + 2*x1*y3 + 2*x3*y1 + 2*x3*y3,
        x0*y3 + x3*y0 + x1*y2 + x2*y1 + x2*y3 + x3*y2,
    )
def sring(xs):
    z=Z
    for x in xs: z=add(z,x)
    return z
def mm(X,Y):
    return tuple(tuple(sring(mul(X[i][k],Y[k][j]) for k in range(3))
                       for j in range(3)) for i in range(3))
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
assert mpow(mm(S1,S2),4)==I
assert mpow(mm(S2,S3),5)==I
assert mpow(mm(S1,S3),2)==I
R=mm(S2,S3); Ri=mpow(R,4)
Q=mm(mm(S1,R),S1); Qi=mpow(Q,4)
assert mpow(R,5)==I and mpow(Q,5)==I and mpow(mm(R,Qi),2)==I
MID=(A,(2,0,0,0),B)
GENS=(R,Ri,Q,Qi)
assert len({mv(g,MID) for g in GENS})==4

def s1f(v):
    x,y,z=v
    return (add(neg(x),mul(A,y)),y,z)
def s3f(v):
    x,y,z=v
    return (x,y,add(mul(B,y),neg(z)))
def orbit(v):
    return {v,s1f(v),s3f(v),s1f(s3f(v))}
def repH(v):
    return min(orbit(v))

# Exact BFS through radius 19, enough to charge all edges leaving selectable B_18.
dist={MID:0}
front=[MID]
shells=[1]
for r in range(19):
    nxt=[]
    for v in front:
        for g in GENS:
            u=mv(g,v)
            if u not in dist:
                dist[u]=r+1
                nxt.append(u)
    shells.append(len(nxt))
    front=nxt

EXPECTED=[1,4,10,20,38,70,130,240,446,824,1528,2824,5234,9680,
          17934,33178,61450,113708,210566,389692]
assert shells==EXPECTED
assert len(dist)==847577

RSEL=18
verts=[v for v,d in dist.items() if d<=RSEL]
assert len(verts)==457885

# Exact quotient by the order-four root stabilizer H=<s1,s3>.
rep_to_idx={}
reps=[]
weights=[]
for v in verts:
    rr=repH(v)
    j=rep_to_idx.get(rr)
    if j is None:
        j=len(reps)
        rep_to_idx[rr]=j
        reps.append(rr)
        weights.append(0)
    weights[j]+=1
assert len(reps)==114478
assert sum(weights)==457885
assert Counter(weights)==Counter({4:114465,2:12,1:1})

edge_counts=defaultdict(int)
boundary=[0]*len(reps)
for v in verts:
    i=rep_to_idx[repH(v)]
    for g in GENS:
        u=mv(g,v)
        du=dist.get(u)
        if du is not None and du<=RSEL:
            if v<u:  # each undirected internal edge once
                j=rep_to_idx[repH(u)]
                if i!=j:
                    a,b=sorted((i,j))
                    edge_counts[(a,b)]+=1
        else:
            # every such edge goes from S_18 to S_19 and must be charged
            assert dist[u]==19
            boundary[i]+=1
assert sum(boundary)==470004

# Move #6 exact decision at r=p/q=4227/5000.
# Minimize q*|partial_E K|-p*|K| on H-invariant subsets of B_18.
# Source->orbit capacity p|O|, quotient edge capacities q*m in both directions,
# and orbit->sink q times the number of graph edges leaving B_18.
p,q=4227,5000
n=len(reps); S=n; T=n+1; N=n+2
rows=[]; cols=[]; data=[]
for i,w in enumerate(weights):
    rows.append(S); cols.append(i); data.append(p*w)
    if boundary[i]:
        rows.append(i); cols.append(T); data.append(q*boundary[i])
for (i,j),m in edge_counts.items():
    c=q*m
    rows.extend((i,j)); cols.extend((j,i)); data.extend((c,c))
C=coo_matrix((data,(rows,cols)),shape=(N,N),dtype="int64").tocsr()
flow=maximum_flow(C,S,T,method="dinic")
total_source=p*sum(weights)
surplus=total_source-int(flow.flow_value)
assert surplus==30485 and surplus>0

# Recover source side in the exact residual graph.
Res=(C-flow.flow).tocsr()
seen=bytearray(N); seen[S]=1
dq=deque([S])
while dq:
    x=dq.popleft()
    for k in range(Res.indptr[x],Res.indptr[x+1]):
        if Res.data[k]>0:
            y=int(Res.indices[k])
            if not seen[y]:
                seen[y]=1
                dq.append(y)
selected_orbits=[i for i in range(n) if seen[i]]

# Expand and independently recount in the full exact graph.
K=set()
for i in selected_orbits:
    K.update(orbit(reps[i]))
assert len(K)==154055

edge_boundary=0
outer_mult=Counter()
for v in K:
    for g in GENS:
        u=mv(g,v)
        if u not in K:
            edge_boundary+=1
            outer_mult[u]+=1
outer_vertex_boundary=len(outer_mult)

assert edge_boundary==130232
assert outer_vertex_boundary==130232
assert set(outer_mult.values())=={1}

# Exact objective and exact refutation of 2/sqrt(5).
assert p*len(K)-q*edge_boundary==30485
square_margin=4*len(K)*len(K)-5*edge_boundary*edge_boundary
assert square_margin==10129902980 and square_margin>0

print("SHELLS_0_TO_19",",".join(map(str,shells)))
print("SELECTABLE_B18",len(verts))
print("H_ORBITS",len(reps))
print("EDGE_THRESHOLD","4227/5000")
print("POSITIVE_CUT_SURPLUS",surplus)
print("SELECTED_SIZE",len(K))
print("EDGE_BOUNDARY",edge_boundary)
print("OUTER_VERTEX_BOUNDARY",outer_vertex_boundary)
print("EDGE_UPPER_BOUND","130232/154055")
print("REFUTES_2_OVER_SQRT5_SQUARE_MARGIN",square_margin)
print("BOUNDARY_MULTIPLICITIES",dict(sorted(Counter(outer_mult.values()).items())))
print("ALL_EXACT_CHECKS_PASS")
