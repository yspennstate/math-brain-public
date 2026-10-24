import sys, time, numpy as np
from feicore import *
polite()

def random_regular(s, d, rng):
    # configuration model with retries; simple graph
    for _ in range(10000):
        stubs = np.repeat(np.arange(s), d); rng.shuffle(stubs)
        e = stubs.reshape(-1, 2)
        if np.any(e[:,0]==e[:,1]): continue
        key = set()
        ok = True
        for a,b in e:
            k = (min(a,b),max(a,b))
            if k in key: ok=False;break
            key.add(k)
        if ok: return [tuple(sorted(x)) for x in e]
    raise RuntimeError

def circulant(s, offs):
    E=set()
    for u in range(s):
        for o in offs:
            v=(u+o)%s; E.add((min(u,v),max(u,v)))
    return sorted(E)

def star_tt(s, edges):
    n = len(edges); N = 1<<n
    xs = np.arange(N, dtype=np.int64)
    val = np.zeros(N, dtype=bool)
    for u in range(s):
        m = 0
        for j,(a,b) in enumerate(edges):
            if a==u or b==u: m |= 1<<j
        val |= (xs & m) == m
    return np.where(val, -1, 1).astype(np.int8)

def stats(tt, n):
    P = spectrum(tt)
    H = entropy(P); I = total_influence(P, n)
    p = float((tt==-1).mean())
    return H, I, p

rng = np.random.default_rng(7)
for (s,d) in [(8,3),(10,3),(12,3),(14,3),(16,3),(8,4),(10,4),(12,4),(10,5)]:
    n = s*d//2
    for kind in ['random','circ']:
        if kind=='random': E = random_regular(s,d,rng)
        else:
            offs = {3:None,4:[1,2],5:None}[d]
            if offs is None:
                if d==3 and s%2==0: E = sorted(set([(min(u,(u+1)%s),max(u,(u+1)%s)) for u in range(s)] + [(u, u+s//2) for u in range(s//2)]))
                else: continue
            else: E = circulant(s, offs)
        assert len(E)==n, (len(E), n)
        t=time.time(); tt = star_tt(s,E); H,I,p = stats(tt,n)
        print(f"s={s:2d} d={d} n={n:2d} {kind:6s} Pr[f=1]={p:.3f} H={H:.4f} I={I:.4f} H/I={H/I:.4f}  ({time.time()-t:.1f}s)", flush=True)
