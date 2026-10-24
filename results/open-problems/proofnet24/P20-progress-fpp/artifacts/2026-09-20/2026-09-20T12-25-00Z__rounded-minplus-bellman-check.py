from fractions import Fraction
import math, heapq
import numpy as np

INF = None

def fw_dist(n, edges):
    d=[[None]*n for _ in range(n)]
    for i in range(n): d[i][i]=Fraction(0)
    for u,v,w in edges:
        w=Fraction(w)
        if d[u][v] is None or w<d[u][v]:
            d[u][v]=d[v][u]=w
    for k in range(n):
        for i in range(n):
            if d[i][k] is None: continue
            for j in range(n):
                if d[k][j] is None: continue
                x=d[i][k]+d[k][j]
                if d[i][j] is None or x<d[i][j]:
                    d[i][j]=x
    return d

def add_inf(a,b):
    if a is None or b is None: return None
    return a+b

def minplus_F(y, I, O, d):
    F=[]
    for j in O:
        vals=[]
        for yi,i in zip(y,I):
            if yi is not None:
                vals.append(yi+d[i][j])
        F.append(min(vals))
    g=min(F)
    phi=[x-g for x in F]
    return F,g,phi

def osc(v):
    vals=[x for x in v if x is not None]
    return max(vals)-min(vals)

def supdiff(a,b):
    return max(abs(x-y) for x,y in zip(a,b))

def qround(phi, delta=Fraction(1,2), R=Fraction(1)):
    out=[]
    for x in phi:
        if x>R:
            out.append(None)
        else:
            # upward grid rounding
            q=(x.numerator*delta.denominator + x.denominator*delta.numerator - 1)//(x.denominator*delta.numerator)
            out.append(q*delta)
    assert any(x==0 for x in out if x is not None)
    return out

# A six-vertex exact rational block graph.
edges=[
    (0,2,Fraction(1,3)), (1,2,Fraction(2,5)),
    (0,3,Fraction(4,5)), (1,3,Fraction(1,2)),
    (2,3,Fraction(2,7)),
    (2,4,Fraction(3,5)), (2,5,Fraction(7,10)),
    (3,4,Fraction(5,8)), (3,5,Fraction(1,4)),
    (4,5,Fraction(3,11)),
]
d=fw_dist(6,edges)
I=[0,1]; O=[4,5]
grid=[Fraction(0),Fraction(1,2),Fraction(1)]
states=[]
for a in grid:
    for b in grid:
        if min(a,b)==0:
            states.append([a,b])

# Translation equivariance and projective nonexpansiveness.
for y in states:
    F,g,p=minplus_F(y,I,O,d)
    c=Fraction(3,7)
    F2,g2,p2=minplus_F([x+c for x in y],I,O,d)
    assert F2==[x+c for x in F]
    assert g2==g+c and p2==p

for y in states:
    for z in states:
        Fy,gy,py=minplus_F(y,I,O,d)
        Fz,gz,pz=minplus_F(z,I,O,d)
        dif=[a-b for a,b in zip(y,z)]
        lo,hi=min(dif),max(dif)
        fdif=[a-b for a,b in zip(Fy,Fz)]
        assert all(lo <= x <= hi for x in fdif)
        assert osc(fdif) <= hi-lo
        eps=supdiff(y,z)
        assert abs(gy-gz) <= eps
        assert supdiff(py,pz) <= 2*eps

# Output-span reset bound via output-to-output metric.
D=max(d[j][k] for j in O for k in O)
H=max(min(d[i][j] for j in O) for i in I)
for y in states:
    F,g,p=minplus_F(y,I,O,d)
    assert max(p) <= D
    assert g <= H

# Upward rounding/truncation is coordinatewise no smaller on retained labels,
# keeps at least one zero, and therefore preserves upper-bound semantics.
for y in states:
    F,g,p=minplus_F(y,I,O,d)
    qp=qround(p)
    for x,q in zip(p,qp):
        if q is not None:
            assert q>=x
    assert any(q==0 for q in qp if q is not None)

# Threshold arithmetic used by the source compiler.
axis_lower=Fraction(3002823,10_000_000)
diag_threshold=2*axis_lower
assert diag_threshold == Fraction(3002823,5_000_000)
assert float(diag_threshold)==0.6005646

print("EXACT_MINPLUS_CHECKS_PASS")
print("H =", H, "D =", D)
print("states_checked =", len(states))
print("source_diagonal_threshold =", diag_threshold, "=", float(diag_threshold))

# --------------------------------------------------------------------
# SCREEN ONLY: rounded asynchronous diagonal-band carry.
# This is deliberately not used as theorem evidence.
# Coordinates are (s,t)=(x+y,x-y), band 0<=s<=2L, |t|<=W.
# --------------------------------------------------------------------
def make_band(L,W):
    verts=[(s,t) for s in range(2*L+1)
           for t in range(-W,W+1) if (s+t)%2==0]
    idx={v:i for i,v in enumerate(verts)}
    edges=[]
    for s,t in verts:
        for ds,dt in ((1,1),(1,-1)):
            v=(s+ds,t+dt)
            if v in idx:
                edges.append((idx[(s,t)],idx[v]))
    inputs=[idx[(0,t)] for t in range(-W,W+1) if t%2==0]
    outputs=[idx[(2*L,t)] for t in range(-W,W+1) if (2*L+t)%2==0]
    return verts,edges,inputs,outputs

def band_apply(z, pre, rng):
    verts,edges,inputs,outputs=pre
    w=rng.exponential(1.0,len(edges))
    adj=[[] for _ in verts]
    for wt,(u,v) in zip(w,edges):
        adj[u].append((v,wt)); adj[v].append((u,wt))
    dist=[math.inf]*len(verts)
    pq=[]
    for val,u in zip(z,inputs):
        dist[u]=float(val)
        heapq.heappush(pq,(float(val),u))
    while pq:
        du,u=heapq.heappop(pq)
        if du!=dist[u]: continue
        for v,wt in adj[u]:
            nv=du+wt
            if nv<dist[v]:
                dist[v]=nv
                heapq.heappush(pq,(nv,v))
    F=np.array([dist[u] for u in outputs])
    g=float(F.min())
    return g,F-g

def screen(L=7,W=49,N=5000,burn=500,delta=0.1,R=14.0,seed=20260920):
    pre=make_band(L,W)
    m=len(pre[2])
    z=np.full(m,1e9)
    z[m//2]=0.0
    rng=np.random.default_rng(seed)
    rewards=[]
    for j in range(N+burn):
        g,p=band_apply(z,pre,rng)
        q=np.ceil(np.maximum(p-1e-12,0.0)/delta)*delta
        q[p>R]=1e9
        q[np.argmin(p)]=0.0
        z=q
        if j>=burn:
            rewards.append(g/L)
    a=np.array(rewards)
    nb=20
    batches=a[:(len(a)//nb)*nb].reshape(nb,-1).mean(axis=1)
    return a.mean(), batches.std(ddof=1)/math.sqrt(nb)

m,se=screen()
print("SCREEN_ONLY_NOT_PROOF")
print("rounded_carry_L7_W49_delta0.1_R14_mean_per_L =", f"{m:.9f}")
print("20_batch_SE_diagnostic =", f"{se:.9f}")
print("threshold =", f"{float(diag_threshold):.7f}")
print("screen_below_threshold =", bool(m<float(diag_threshold)))
