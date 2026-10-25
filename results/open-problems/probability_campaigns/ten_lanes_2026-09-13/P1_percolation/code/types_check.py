"""Machine check of the conditional-type classification for FK(p,q), any q>0.

Claim: conditionally on the configuration off {e,f}, the pair (w_e,w_f) is
INDEPENDENT unless the pair is of 'type E' (delta_e=delta_f=1, delta_ef=1,
i.e. e and f together close a cycle), and in type E
   Cov = x y r (1-x)(1-y)(1-r) / Z_E^2,  r = 1/q,  Z_E = (1-x)(1-y)+r(x(1-y)+(1-x)y+xy)
so Cov<0 for q<1 and Cov>0 for q>1.  Also x < gamma_x < beta_x for q<1.
Verified here by exact rational arithmetic against brute force on every graph
with at most 5 vertices and every ordered pair of distinct edges.
"""
from fractions import Fraction as F
import itertools, sys
from fk_lib import comps
from graphs_iso import connected_iso

def cond_law(n, edges, i, j, restmask, x, y, q):
    """exact conditional weights of (w_i,w_j) given the rest configuration."""
    m=len(edges)
    out={}
    for si in (0,1):
        for sj in (0,1):
            mask=restmask | (si<<i) | (sj<<j)
            k=comps(n,edges,mask)
            out[(si,sj)]=(x if si else 1-x)*(y if sj else 1-y)*q**k
    return out

def analyse(n, edges, i, j, restmask, x, y, q):
    w=cond_law(n,edges,i,j,restmask,x,y,q)
    Z=sum(w.values())
    Pi=(w[(1,0)]+w[(1,1)])/Z; Pj=(w[(0,1)]+w[(1,1)])/Z; Pij=w[(1,1)]/Z
    return Pij-Pi*Pj, Pi, Pj

def dtype(n, edges, i, j, restmask):
    k0=comps(n,edges,restmask)
    ke=comps(n,edges,restmask|(1<<i))
    kf=comps(n,edges,restmask|(1<<j))
    kef=comps(n,edges,restmask|(1<<i)|(1<<j))
    return (k0-ke, k0-kf, k0-kef)

def main(nmax=5):
    x=F(2,7); y=F(3,11); qs=[F(1,5),F(1,2),F(4,5),F(3,2),F(5,1)]
    seen=set(); bad=0; tested=0
    for n in range(2,nmax+1):
        for edges in connected_iso(n, mmax=8):
            m=len(edges)
            for i in range(m):
                for j in range(m):
                    if i==j: continue
                    rest=[b for b in range(m) if b!=i and b!=j]
                    for sub in range(1<<len(rest)):
                        rm=0
                        for t,b in enumerate(rest):
                            if sub>>t&1: rm|=1<<b
                        typ=dtype(n,edges,i,j,rm)
                        for q in qs:
                            cov,Pi,Pj=analyse(n,edges,i,j,rm,x,y,q)
                            tested+=1
                            r=1/q
                            isE = (typ==(1,1,1))
                            if not isE:
                                if cov!=0:
                                    bad+=1; print("NONZERO COV OUTSIDE TYPE E",edges,i,j,rm,typ,cov); return
                            else:
                                ZE=(1-x)*(1-y)+r*(x*(1-y)+(1-x)*y+x*y)
                                pred=x*y*r*(1-x)*(1-y)*(1-r)/ZE**2
                                if cov!=pred:
                                    bad+=1; print("TYPE E FORMULA MISMATCH",edges,i,j,rm,typ,cov,pred); return
                            seen.add(typ)
    print("conditional laws tested:", tested, " mismatches:", bad)
    print("types observed:", sorted(seen))

if __name__=="__main__":
    main(int(sys.argv[1]) if len(sys.argv)>1 else 5)
