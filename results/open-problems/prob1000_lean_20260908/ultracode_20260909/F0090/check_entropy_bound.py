# Exact enumeration check for F0090 (Kalai Conjecture 8).
# Site percolation on an n x m square grid, p = 1/2, f = left-right crossing.
# For every configuration we compute f, the pivotal set, and (via Walsh transform)
# the spectral distribution. We check:
#  (1) the identity Q[S cap B != 0] = E[Var(f | F_{B^c})] / E[f^2]... (in the +-1 normalisation
#      the spectral measure is a probability), and the one-box bound
#      Q[S cap B != 0] <= P(B is pivotal as a set) for every dyadic box B;
#  (2) the general entropy inequality H(S) <= log 2 + log 15 * sum_k sum_B P(S cap B != 0)
#      for the spectral sample and for the pivotal set;
#  (3) H(S), H(P), I(f) for small sizes (a sanity trend, not an asymptotic).
import numpy as np, itertools, math, sys
def ent(p):
    p=np.asarray(p,float); p=p[p>0]; return float(-(p*np.log(p)).sum())
def crossings(n,m):
    # sites (i,j) i in 0..n-1 rows, j in 0..m-1 columns; left-right crossing through open sites, 4-neighbour
    N=n*m; conf=np.arange(1<<N)
    bits=((conf[:,None]>>np.arange(N))&1).astype(np.uint8)  # (2^N, N)
    f=np.zeros(1<<N,np.uint8)
    idx=lambda i,j:i*m+j
    for c in range(1<<N):
        b=bits[c]; seen=np.zeros(N,bool); st=[idx(i,0) for i in range(n) if b[idx(i,0)]]
        for s in st: seen[s]=True
        ok=False
        while st:
            s=st.pop(); i,j=divmod(s,m)
            if j==m-1: ok=True;break
            for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
                ii,jj=i+di,j+dj
                if 0<=ii<n and 0<=jj<m:
                    t=idx(ii,jj)
                    if b[t] and not seen[t]: seen[t]=True; st.append(t)
        f[c]=ok
    return bits,f
def walsh(v):
    v=v.astype(float).copy(); h=1; N=len(v)
    while h<N:
        v=v.reshape(-1,2*h); a=v[:,:h].copy(); b=v[:,h:].copy(); v[:,:h]=a+b; v[:,h:]=a-b; v=v.reshape(-1); h*=2
    return v/N
def run(n,m):
    N=n*m; bits,f=crossings(n,m)
    g=2*f.astype(float)-1                      # +-1 valued
    fh=walsh(g)                                 # Fourier coefficients indexed by subset mask
    Q=fh**2; assert abs(Q.sum()-1)<1e-9
    # pivotal set distribution
    piv=np.zeros(1<<N,np.int64)
    for i in range(N):
        flipped=f[np.arange(1<<N)^(1<<i)]
        piv|=((flipped!=f).astype(np.int64)<<i)
    Pdist=np.bincount(piv,minlength=1<<N)/(1<<N)
    I=float((piv[:,None]>>np.arange(N)&1).sum(1).mean())     # total influence = E|pivotal set|
    HS=ent(Q); HP=ent(Pdist)
    ES=float(sum(Q[s]*bin(s).count('1') for s in range(1<<N)))
    # boxes: use a dyadic-like partition tree on the grid: split rows and columns in halves recursively
    def boxes(r0,r1,c0,c1):
        yield (r0,r1,c0,c1)
        if r1-r0>1 or c1-c0>1:
            rm=(r0+r1+1)//2; cm=(c0+c1+1)//2
            for a,b in ([(r0,rm),(rm,r1)] if r1-r0>1 else [(r0,r1)]):
                for c,d in ([(c0,cm),(cm,c1)] if c1-c0>1 else [(c0,c1)]):
                    yield from boxes(a,b,c,d)
    tot_S=0.0; tot_P=0.0; worst=0.0
    for (r0,r1,c0,c1) in boxes(0,n,0,m):
        mask=0
        for i in range(r0,r1):
            for j in range(c0,c1): mask|=1<<(i*m+j)
        qS=float(Q[(np.arange(1<<N)&mask)!=0].sum())
        pP=float(Pdist[(np.arange(1<<N)&mask)!=0].sum())
        # E Var(f | F_{B^c}) for the +-1 function: group configs by bits outside B
        outside=np.arange(1<<N)&~mask
        order=np.argsort(outside,kind='stable'); o=outside[order]; gg=g[order]
        starts=np.flatnonzero(np.r_[True,o[1:]!=o[:-1]]); ends=np.r_[starts[1:],len(o)]
        ev=0.0; pB=0.0
        for s,e in zip(starts,ends):
            blk=gg[s:e]; ev+=blk.var(); pB+=float(blk.max()!=blk.min())
        ev/=len(starts); pB/=len(starts)
        assert abs(ev-qS)<1e-9, (ev,qS)
        assert qS<=pB+1e-12 and pP<=pB+1e-12
        worst=max(worst,qS/pB if pB>0 else 0)
        tot_S+=qS; tot_P+=pP
    # the tree here splits each box into at most 4 children: children count per box <=4, so
    # the bound H <= log2 + log15 * sum over non-leaf boxes P(hit). We summed over all boxes
    # (leaves included), which only weakens the bound; fine for a check.
    bS=math.log(2)+math.log(15)*tot_S; bP=math.log(2)+math.log(15)*tot_P
    print(f"n={n} m={m}: I(f)={I:.4f} E|S|={ES:.4f} H(S)={HS:.4f} H(P)={HP:.4f} | bound_S={bS:.3f} bound_P={bP:.3f} | max Q[S hits B]/P(B piv)={worst:.3f}")
    assert HS<=bS and HP<=bP
    return I,HS,HP
for (n,m) in [(2,2),(2,3),(3,3),(3,4),(4,4)]:
    run(n,m)
print("all identities and inequalities verified by exact enumeration")
