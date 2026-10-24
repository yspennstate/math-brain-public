#!/usr/bin/env python3
"""
PROB10-10 NONRIGOROUS SCREEN ONLY.

Simulates the proposed asynchronous carried-boundary strip recursion for
undirected Exp(1) FPP in rotated coordinates s=x+y, d=x-y.  It also screens
a conservative rounded/capped projection P_{eps,H}.  The output is numerical
evidence only; it is not a proof or a source-level bound.
"""
import heapq, math, random, statistics

THRESHOLD = 0.6005646

def sample_band(L, W, rng):
    verts = []
    idx = {}
    for s in range(2*L + 1):
        for d in range(-W, W + 1):
            if (s - d) % 2 == 0:
                idx[(s,d)] = len(verts)
                verts.append((s,d))
    adj = [[] for _ in verts]
    for (s,d), i in idx.items():
        if s < 2*L:
            for nd in (d-1, d+1):
                j = idx.get((s+1, nd))
                if j is not None:
                    w = rng.expovariate(1.0)
                    adj[i].append((j,w))
                    adj[j].append((i,w))
    left = [(d,idx[(0,d)]) for d in range(-W,W+1) if (0,d) in idx]
    right = [(d,idx[(2*L,d)]) for d in range(-W,W+1) if (2*L,d) in idx]
    return adj,left,right

def apply_band(y, L, W, rng):
    adj,left,right = sample_band(L,W,rng)
    dist = [math.inf] * len(adj)
    pq = []
    for d,i in left:
        val = y.get(d, math.inf)
        if math.isfinite(val):
            dist[i] = val
            heapq.heappush(pq,(val,i))
    while pq:
        du,u = heapq.heappop(pq)
        if du != dist[u]:
            continue
        for v,w in adj[u]:
            nv = du+w
            if nv < dist[v]:
                dist[v] = nv
                heapq.heappush(pq,(nv,v))
    out = {d:dist[i] for d,i in right}
    g = min(out.values())
    return g, {d:v-g for d,v in out.items()}

def project(y, eps=None, H=None):
    if eps is None and H is None:
        return y
    out = {}
    for d,v in y.items():
        if not math.isfinite(v):
            out[d] = math.inf
        elif v == 0.0:
            out[d] = 0.0
        elif H is not None and v > H:
            out[d] = math.inf
        elif eps is not None:
            q = math.ceil(v/eps - 1e-12)*eps
            out[d] = math.inf if (H is not None and q > H) else q
        else:
            out[d] = v
    assert min(out.values()) == 0.0
    return out

def one_run(L,W,blocks,burn,seed,eps=None,H=None):
    rng = random.Random(seed)
    y = {d:(0.0 if d==0 else math.inf)
         for d in range(-W,W+1) if d % 2 == 0}
    vals = []
    for j in range(blocks):
        g,y = apply_band(y,L,W,rng)
        y = project(y,eps,H)
        if j >= burn:
            vals.append(g/L)
    return statistics.mean(vals)

def summarize(label,L,W,eps=None,H=None,blocks=3000,burn=300,reps=4):
    vals = []
    for r in range(reps):
        seed = 17000 + 100*W + 10000*L + r + (500000 if eps is not None else 0)
        vals.append(one_run(L,W,blocks,burn,seed,eps,H))
    mean = statistics.mean(vals)
    se = statistics.pstdev(vals)/(len(vals)**0.5)
    print(f"{label}: L={L} W={W} eps={eps} H={H} blocks={blocks} burn={burn} reps={reps}")
    print("  replicate_means =", " ".join(f"{x:.12f}" for x in vals))
    print(f"  mean={mean:.12f} batch_SE={se:.12f} threshold={THRESHOLD:.7f} mean_minus_threshold={mean-THRESHOLD:+.12f}")

print("PROB10-10 asynchronous boundary carry numerical screen")
print("NONRIGOROUS_SCREEN = True")
summarize("unprojected",4,20)
summarize("unprojected",4,30)
summarize("unprojected",4,40)
summarize("projected",4,40,eps=0.05,H=5.0)
summarize("projected",4,48,eps=0.05,H=5.0)
