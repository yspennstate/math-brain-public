r"""Exact demonstration that the FK measures with q<1 are NOT stochastically monotone
in the EDGE-PARAMETER VECTOR: raising p_e alone strictly lowers P(omega_f = 1), and
{omega_f=1} is an increasing event.

Also checks Russo-type identity  d mu(A) / d log(w_e) = Cov(1_A, omega_e),  w_e=p_e/(1-p_e).
"""
from fractions import Fraction as Fr
from fk_lib import comps

def marg(n, edges, p, q, f):
    m=len(edges); Z=Fr(0); Nf=Fr(0)
    for mask in range(1<<m):
        t=q**comps(n,edges,mask)
        for b in range(m): t *= p[b] if (mask>>b&1) else (1-p[b])
        Z+=t
        if mask>>f&1: Nf+=t
    return Nf/Z

if __name__=="__main__":
    tri=[(0,1),(1,2),(0,2)]
    q=Fr(1,2)
    print("triangle, q=1/2, p_f=p_g=1/2, raising p_e alone:")
    prev=None
    for k in range(1,10):
        pe=Fr(k,10)
        v=marg(3,tri,[pe,Fr(1,2),Fr(1,2)],q,1)
        flag="" if prev is None else ("  DECREASED" if v<prev else "  increased")
        print("   p_e=%-5s  P(omega_f=1)=%-28s %s"%(pe, v, flag))
        prev=v
    print()
    print("same on the 4-cycle (e,f opposite edges), q=1/4:")
    c4=[(0,1),(1,2),(2,3),(3,0)]
    q=Fr(1,4); prev=None
    for k in range(1,10):
        pe=Fr(k,10)
        v=marg(4,c4,[pe,Fr(1,2),Fr(1,2),Fr(1,2)],q,2)
        flag="" if prev is None else ("  DECREASED" if v<prev else "  increased")
        print("   p_e=%-5s  P(omega_f=1)=%-30s %s"%(pe, v, flag))
        prev=v
