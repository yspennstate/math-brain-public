#!/usr/bin/env python3
import heapq, random, math

# SCREEN ONLY / NOT A PROOF.  This probes the deterministic expected-profile
# subeigenvector route at the same L=4,W=48 geometry used by a prior projected
# asynchronous-carry screen.  It is route-triage, not sampled curvature.

L=4
W=48
S=2*L
boundary_ds=list(range(-W, W+1, 2))

verts=[]
idx={}
for s in range(S+1):
    for d in range(-W, W+1):
        if (s-d)%2==0:
            idx[(s,d)] = len(verts)
            verts.append((s,d))

edges=[]
adj=[[] for _ in verts]
for (s,d),u in idx.items():
    if s<S:
        for nd in (d-1,d+1):
            v=idx.get((s+1,nd))
            if v is not None:
                eid=len(edges)
                edges.append((u,v))
                adj[u].append((v,eid))
                adj[v].append((u,eid))
left=[idx[(0,d)] for d in boundary_ds]
right=[idx[(S,d)] for d in boundary_ds]

def one_sample(z, rng):
    weights=[rng.expovariate(1.0) for _ in edges]
    dist=[float('inf')]*len(verts)
    pq=[]
    for k,u in enumerate(left):
        dist[u]=z[k]
        heapq.heappush(pq,(z[k],u))
    while pq:
        du,u=heapq.heappop(pq)
        if du != dist[u]:
            continue
        for v,eid in adj[u]:
            nv=du+weights[eid]
            if nv<dist[v]:
                dist[v]=nv
                heapq.heappush(pq,(nv,v))
    return [dist[v] for v in right]

z=[0.0]*len(left)
iters=8
samples=1200
base_seed=20260920171253
print('SCREEN_ONLY_NOT_PROOF')
print('purpose = route triage for deterministic mean-profile subeigenvector at L=4,W=48')
print('model = iid Exp(1) undirected finite rotated band')
print('iterations =', iters, 'samples_per_iteration =', samples)
print('boundary_states =', len(left), 'vertices =', len(verts), 'edges =', len(edges))
print('source_threshold_per_L = 0.6005646')
for it in range(iters):
    rng=random.Random(base_seed+it)
    sums=[0.0]*len(right)
    sqs=[0.0]*len(right)
    for _ in range(samples):
        vals=one_sample(z,rng)
        for j,x in enumerate(vals):
            sums[j]+=x
            sqs[j]+=x*x
    T=[x/samples for x in sums]
    residual=[T[j]-z[j] for j in range(len(z))]
    center=len(z)//2
    var=max(0.0, sqs[center]/samples-T[center]*T[center])
    se=math.sqrt(var/samples)
    print(f'iter={it} residual_per_L_min={min(residual)/L:.9f} residual_per_L_max={max(residual)/L:.9f} center_SE_per_L={se/L:.9f}')
    c=T[center]
    z=[x-c for x in T]
    mn=min(z)
    z=[x-mn for x in z]
print('interpretation = the one-block deterministic-mean profile route screens far above threshold; this is not a rigorous lower bound on its optimum and is not curvature evidence')
