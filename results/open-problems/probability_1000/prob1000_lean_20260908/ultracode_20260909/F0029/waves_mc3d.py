# 3D Monte Carlo: sandpile Markov chain on a box K=[0,L)^3 (wired boundary), avalanche at the centre o decomposed into waves.
# Compares  P(W_1 contains a nbr of o)  and  E #{k : W_k contains a nbr of o}  with  G_K(o,o) * P^{(0)}(T contains a nbr of o),
# where T is the o-component of a uniform 2-forest of K (roots o and the sink), sampled by Wilson's algorithm.
# The all-waves identity predicts the second equals the third; LLS Lemma 2.14 claims the first equals the third.
import numpy as np, sys, time
rng=np.random.default_rng(20260909)
L=int(sys.argv[1]) if len(sys.argv)>1 else 9
d=3; deg=6
n=L**3
def idx(x,y,z): return (x*L+y)*L+z
coords=np.array([(x,y,z) for x in range(L) for y in range(L) for z in range(L)])
nbrs=[[] for _ in range(n)]
for i,(x,y,z) in enumerate(coords):
    for dx,dy,dz in ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)):
        X,Y,Z=x+dx,y+dy,z+dz
        if 0<=X<L and 0<=Y<L and 0<=Z<L: nbrs[i].append(idx(X,Y,Z))
o=idx(L//2,L//2,L//2); N0=set(nbrs[o])
# Green's function
Lap=np.zeros((n,n))
for i in range(n):
    Lap[i,i]=deg
    for j in nbrs[i]: Lap[i,j]-=1
G=np.linalg.inv(Lap)
print(f"L={L} n={n} G_K(o,o)={G[o,o]:.5f}  (G(o,o) on Z^3 = 0.25273)")

def stabilize(h):
    # full stabilization (all vertices), used for the Markov chain
    stack=[i for i in range(n) if h[i]>=deg]
    while stack:
        x=stack.pop()
        if h[x]<deg: continue
        k=h[x]//deg; h[x]-=k*deg
        for y in nbrs[x]:
            h[y]+=k
            if h[y]>=deg: stack.append(y)

def waves(h0):
    h=h0.copy(); h[o]+=1; W=[]
    while h[o]>=deg:
        wave={o}; h[o]-=deg
        for y in nbrs[o]: h[y]+=1
        stack=[y for y in nbrs[o] if h[y]>=deg]
        while stack:
            x=stack.pop()
            if x==o or h[x]<deg: continue
            wave.add(x); h[x]-=deg
            for y in nbrs[x]:
                h[y]+=1
                if y!=o and h[y]>=deg: stack.append(y)
        W.append(wave)
    return W

# Markov chain: start from the all-5 configuration (recurrent), burn in
h=np.full(n,deg-1,dtype=np.int64)
burn=int(sys.argv[2]) if len(sys.argv)>2 else 200000
t0=time.time()
for it in range(burn):
    h[rng.integers(n)]+=1
    if h.max()>=deg: stabilize(h)
print(f"burn-in {burn} additions in {time.time()-t0:.1f}s")
samples=int(sys.argv[3]) if len(sys.argv)>3 else 20000
gap=10
cnt_first=0; cnt_all=0; cnt_N1=0; Nsum=0; cnt_first_any=0
xs=[idx(L//2+r,L//2,L//2) for r in range(1,L//2+1)]
inW1=np.zeros(len(xs)); inAv=np.zeros(len(xs)); ntop=np.zeros(len(xs))
for s in range(samples):
    for it in range(gap):
        h[rng.integers(n)]+=1
        if h.max()>=deg: stabilize(h)
    W=waves(h)
    Nsum+=len(W)
    if W:
        cnt_N1+=1
        if W[0]&N0: cnt_first+=1
        cnt_all+=sum(1 for w in W if w&N0)
        for j,x in enumerate(xs):
            if x in W[0]: inW1[j]+=1
            c=sum(1 for w in W if x in w)
            if c: inAv[j]+=1
            ntop[j]+=c
print(f"samples={samples}: P(N>=1)=P(eta(o)=5)={cnt_N1/samples:.4f}   E N={Nsum/samples:.4f} (Dhar: G_K(o,o)={G[o,o]:.4f})")
print(f"  P(W_1 contains a nbr of o) = {cnt_first/samples:.4f}")
print(f"  E #{{k: W_k contains a nbr of o}} = {cnt_all/samples:.4f}")
# Wilson's algorithm for the 2-forest with roots {o, sink}
def wilson_sample():
    intree=np.zeros(n,dtype=bool); intree[o]=True
    root=np.full(n,-1,dtype=np.int64); root[o]=o   # root label: o or -2 (sink)
    nxt=np.full(n,-1,dtype=np.int64)
    for start in range(n):
        if intree[start]: continue
        u=start; path=[]
        while not intree[u]:
            # step: with prob (deg-len(nbrs))/deg go to sink
            k=rng.integers(deg)
            if k<len(nbrs[u]):
                v=nbrs[u][k]; nxt[u]=v; u=v
            else:
                nxt[u]=-2; u=-2; break
        # retrace from start following nxt (loop-erased automatically by overwriting nxt)
        r = -2 if u==-2 else root[u]
        u=start
        while u!=-2 and not intree[u]:
            intree[u]=True; root[u]=r; u=nxt[u]
    return root
M=int(sys.argv[4]) if len(sys.argv)>4 else 20000
cnt=0; inT=np.zeros(len(xs))
for s in range(M):
    root=wilson_sample()
    if any(root[y]==o for y in N0): cnt+=1
    for j,x in enumerate(xs):
        if root[x]==o: inT[j]+=1
p=cnt/M
print(f"  Wilson ({M} forests): P^(0)(T contains a nbr of o) = {p:.4f};  G_K(o,o)*P^(0) = {G[o,o]*p:.4f}")
print("  -> all-waves identity predicts E#{k: W_k contains nbr} = G*P^(0);  LLS Lemma 2.14 predicts P(W_1 contains nbr) = G*P^(0)")
print("\n one-point functions along the axis (r = distance from o):")
print("  r   P(x in W_1)   P(x in Av)   E n(o,x)   G_K(o,x)   G*P^(0)(x in T)")
for j,x in enumerate(xs):
    print(f"  {j+1:2d}   {inW1[j]/samples:.4f}      {inAv[j]/samples:.4f}     {ntop[j]/samples:.4f}    {G[o,x]:.4f}    {G[o,o]*inT[j]/M:.4f}")
