"""Exact check of the uniform-forest covariance identity and of its two corollaries.

For the uniform measure on acyclic edge subsets of a finite multigraph, and distinct
edges e,f, let eta be the configuration off {e,f} and set
  A_e = 1{eta+e acyclic}, A_f = 1{eta+f acyclic}, B = 1{eta+e+f acyclic},
  Xi  = A_e A_f - B   (both edges insertable separately but not together).
Claim (identity):
  Cov(w_e,w_f) = -(1/9) E[Xi] + (1/4) Cov(A_e,A_f)
                 - (1/12)( Cov(A_e,Xi) + Cov(A_f,Xi) ) + (1/36) Var(Xi),
all moments under the eta-marginal of the uniform forest measure (a tilted measure:
eta has weight N(eta) = 1 + A_e + A_f + B).
"""
import sys, random
from fractions import Fraction as Fr
from fk_lib import comps

def acyclic(n, edges, mask):
    return comps(n,edges,mask)==n-bin(mask).count("1")

def check(n, edges, i, j):
    m=len(edges)
    rest=[b for b in range(m) if b!=i and b!=j]
    # direct covariance
    tot=0; ci=0; cj=0; cij=0
    for mask in range(1<<m):
        if not acyclic(n,edges,mask): continue
        tot+=1
        if mask>>i&1:
            ci+=1
            if mask>>j&1: cij+=1
        if mask>>j&1: cj+=1
    if tot==0: return None
    cov=Fr(cij,tot)-Fr(ci,tot)*Fr(cj,tot)
    # identity side
    EX=Fr(0); EAe=Fr(0); EAf=Fr(0); EAeAf=Fr(0); EAeX=Fr(0); EAfX=Fr(0); EX2=Fr(0); W=0
    for sub in range(1<<len(rest)):
        rm=0
        for t,b in enumerate(rest):
            if sub>>t&1: rm|=1<<b
        if not acyclic(n,edges,rm): continue
        Ae=1 if acyclic(n,edges,rm|(1<<i)) else 0
        Af=1 if acyclic(n,edges,rm|(1<<j)) else 0
        B =1 if acyclic(n,edges,rm|(1<<i)|(1<<j)) else 0
        Xi=Ae*Af-B
        N=1+Ae+Af+B
        W+=N
        EX+=N*Xi; EAe+=N*Ae; EAf+=N*Af; EAeAf+=N*Ae*Af
        EAeX+=N*Ae*Xi; EAfX+=N*Af*Xi; EX2+=N*Xi*Xi
    EX/=W; EAe/=W; EAf/=W; EAeAf/=W; EAeX/=W; EAfX/=W; EX2/=W
    rhs = -Fr(1,9)*EX + Fr(1,4)*(EAeAf-EAe*EAf) \
          - Fr(1,12)*((EAeX-EAe*EX)+(EAfX-EAf*EX)) + Fr(1,36)*(EX2-EX*EX)
    return cov, rhs, EX

if __name__=="__main__":
    from graphs_iso import connected_iso
    bad=0; tested=0; pos=0
    for n in range(3,7):
        for edges in connected_iso(n, mmax=8):
            m=len(edges)
            for i in range(m):
                for j in range(i+1,m):
                    r=check(n,edges,i,j)
                    if r is None: continue
                    cov,rhs,EX=r; tested+=1
                    if cov!=rhs: bad+=1; print("IDENTITY FAILS",n,edges,i,j,cov,rhs)
                    if cov>0: pos+=1; print("POSITIVE COVARIANCE",n,edges,i,j,cov)
    print("uniform-forest identity checked on %d edge pairs, %d failures, %d positive covariances"%(tested,bad,pos))
