# Eden growth in Z^m (one slab, horizontal edges only): newborn = target of a uniformly chosen
# boundary edge. Report mean boundary / sigma(n) at several n.
import sys, random
m, nmax, runs, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
random.seed(seed)
f=[0]*(nmax+2)
for n in range(1,nmax+2): f[n]=f[n-1]+bin(n-1).count("1")
sig=lambda n: 2*m*n-2*f[n]
marks=[8,16,32,64,128,256,512]; acc={k:[] for k in marks if k<=nmax}
for r in range(runs):
    o=(0,)*m; S={o}; edges=[]
    def nb(x):
        for i in range(m):
            for s in (1,-1):
                y=list(x); y[i]+=s; yield tuple(y)
    edges=[(o,y) for y in nb(o)]
    while len(S)<nmax:
        x,y=edges[random.randrange(len(edges))]
        if y in S: continue
        S.add(y)
        edges=[(u,v) for (u,v) in edges if v!=y]+[(y,z) for z in nb(y) if z not in S]
        n=len(S)
        if n in acc: acc[n].append(len(edges)/sig(n))
for n,v in acc.items(): print(m,n,"boundary/sigma mean %.4f min %.4f"%(sum(v)/len(v),min(v)))
