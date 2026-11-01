"""Exact certificate attempt for pairwise negative correlation in FK(q<1).

Write w_e = p_e/(1-p_e) in (0, inf) and s = 1 - q in (0,1).  Then
    Cov(w_e, w_f) * Z^2  =  N_ef * Z - N_e * N_f
is a polynomial in (w_1,...,w_m, s) with integer coefficients.  If every
coefficient is <= 0 then negative correlation holds for ALL edge weights and
all q in (0,1) simultaneously -- a certificate, not a grid scan.
"""
import sys, itertools
from sympy import symbols, Poly, expand, simplify
from fk_lib import comps

def cov_poly(n, edges, i, j, qsub=True):
    m=len(edges)
    W=symbols('w0:%d'%m, nonnegative=True)
    s=symbols('s', nonnegative=True)
    q=1-s if qsub else symbols('q')
    Z=0; Ni=0; Nj=0; Nij=0
    for mask in range(1<<m):
        k=comps(n,edges,mask)
        t=q**k
        for b in range(m):
            if mask>>b&1: t=t*W[b]
        Z=Z+t
        if mask>>i&1:
            Ni=Ni+t
            if mask>>j&1: Nij=Nij+t
        if mask>>j&1: Nj=Nj+t
    expr=expand(Nij*Z-Ni*Nj)
    return expr, W, s

def check(n, edges, verbose=True):
    m=len(edges)
    W=symbols('w0:%d'%m, nonnegative=True); s=symbols('s', nonnegative=True)
    bad=[]
    for i in range(m):
        for j in range(i+1,m):
            expr,_,_=cov_poly(n,edges,i,j)
            P=Poly(expr, *W, s)
            pos=[(mono,c) for mono,c in zip(P.monoms(),P.coeffs()) if c>0]
            if pos: bad.append(((i,j), pos[:6], len(pos)))
    if verbose:
        if not bad: print("  ALL COEFFICIENTS <= 0  (certificate holds) for", edges)
        else:
            print("  positive coefficients present for", edges)
            for b in bad[:3]: print("   ", b)
    return bad

if __name__=="__main__":
    tri=[(0,1),(1,2),(0,2)]
    print("triangle:"); check(3,tri)
    path=[(0,1),(1,2)]
    print("path P3:"); check(3,path)
    k4=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    print("K4:"); check(4,k4)
