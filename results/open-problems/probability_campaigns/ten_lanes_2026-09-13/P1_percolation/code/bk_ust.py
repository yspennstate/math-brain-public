"""Exhaustive search for a counterexample to the BK-type inequality for weighted
spanning trees (Lyons-Peres, Probability on Trees and Networks, Conj. 4.6):
   for increasing A,B,  P[T in A box B] <= P[T in A] P[T in B].

An increasing event is determined, on the support of the spanning-tree measure,
by its minimal witnesses; those may be taken to be forests of G.  We enumerate
antichains of forests of bounded size and test every ordered pair.
"""
import itertools, sys, math
from fractions import Fraction as Fr
from fk_lib import comps
from graphs_iso import connected_iso

def spanning_trees(n, edges):
    m=len(edges); out=[]
    for mask in range(1<<m):
        if bin(mask).count("1")!=n-1: continue
        if comps(n,edges,mask)==1: out.append(mask)
    return out

def forests(n, edges):
    m=len(edges); out=[]
    for mask in range(1<<m):
        c=bin(mask).count("1")
        if comps(n,edges,mask)==n-c:   # acyclic
            if mask: out.append(mask)
    return out

def antichains(items, kmax):
    """antichains (w.r.t. subset order on bitmasks) of size 1..kmax"""
    res=[]
    for k in range(1,kmax+1):
        for combo in itertools.combinations(items,k):
            ok=True
            for a,b in itertools.combinations(combo,2):
                if (a&b)==a or (a&b)==b: ok=False; break
            if ok: res.append(combo)
    return res

def analyse(n, edges, kmax=2, weights=None, report_top=3):
    m=len(edges)
    ST=spanning_trees(n,edges)
    if not ST: return None
    tidx={t:i for i,t in enumerate(ST)}
    if weights is None: wt=[Fr(1)]*len(ST)
    else:
        wt=[]
        for t in ST:
            p=Fr(1)
            for b in range(m):
                if t>>b&1: p*=weights[b]
            wt.append(p)
    Wtot=sum(wt)
    F=forests(n,edges)
    chi={}
    for f in F:
        msk=0
        for t in ST:
            if (t & f)==f: msk |= 1<<tidx[t]
        chi[f]=msk
    F=[f for f in F if chi[f]]          # drop forests in no spanning tree (none, G connected)
    AC=antichains(F,kmax)
    def wsum(bits):
        s=Fr(0); b=bits; 
        while b:
            i=(b & -b).bit_length()-1
            s+=wt[i]; b&=b-1
        return s
    cache={}
    def setof(ac):
        key=ac
        if key in cache: return cache[key]
        s=0
        for f in ac: s|=chi[f]
        cache[key]=s; return s
    best=[]
    for A in AC:
        SA=setof(A); PA=wsum(SA)
        for B in AC:
            SB=setof(B); PB=wsum(SB)
            box=0
            for f in A:
                for g in B:
                    if f & g: continue
                    box |= (chi[f] & chi[g])
            Pbox=wsum(box)
            d=Pbox*Wtot - PA*PB
            if d>0:
                best.append((d, A, B, Pbox, PA, PB, Wtot))
    best.sort(key=lambda z:-z[0])
    return ST, best[:report_top], len(AC)

if __name__=="__main__":
    nmax=int(sys.argv[1]) if len(sys.argv)>1 else 5
    mmax=int(sys.argv[2]) if len(sys.argv)>2 else 7
    kmax=int(sys.argv[3]) if len(sys.argv)>3 else 2
    total=0; viol=0
    for n in range(3,nmax+1):
        for edges in connected_iso(n, mmax=mmax, min_edges=n-1):
            r=analyse(n,edges,kmax=kmax)
            if r is None: continue
            ST,best,nac=r; total+=1
            if best:
                viol+=1
                print("VIOLATION n=%d edges=%s  (antichains %d)"%(n,edges,nac))
                for d,A,B,Pbox,PA,PB,W in best:
                    print("   A=",[format(a,'0%db'%len(edges)) for a in A],
                          " B=",[format(b,'0%db'%len(edges)) for b in B],
                          " P(AboxB)=%s  P(A)P(B)=%s"%(Fr(Pbox,W), Fr(PA*PB,W*W)))
    print("graphs tested:",total," with a violation:",viol," (kmax=%d, uniform weights)"%kmax)
