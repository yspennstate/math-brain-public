"""Exhaustive verification of the exact per-quadruple probabilities claimed for the
   two-disjoint-support-2-eigenvector templates in symmetric +-1 matrices.

   Claim A (pair summing to zero, 'opposite' type (+,-)):
       for fixed ordered disjoint pairs ({i,j},{k,l}),
       P[ e_i+e_j eigvec with mu  AND  e_k-e_l eigvec with -mu ] = 3 * 4^{-n}
       and restricted to mu != 0 the probability is exactly 1 * 4^{-n}.
   Claim B (repeated eigenvalue, 'equal' type (-,-)):
       P[ e_i-e_j eigvec with lam AND e_k-e_l eigvec with lam ] = 3 * 4^{-n}
       and restricted to lam != 0 the probability is exactly 1 * 4^{-n}.
   Verified by exhaustive enumeration of ALL 2^{n(n+1)/2} symmetric +-1 matrices.
"""
import itertools, numpy as np
from fractions import Fraction

def check(n):
    idx=[(i,j) for i in range(n) for j in range(i,n)]
    nf=len(idx); tot=1<<nf
    i,j,k,l = 0,1,2,3
    cA=cAnz=cB=cBnz=0
    for bits in range(tot):
        M=[[0]*n for _ in range(n)]
        for t,(a,b) in enumerate(idx):
            v = 1 if not (bits>>t)&1 else -1
            M[a][b]=v; M[b][a]=v
        # --- A: e_i+e_j eigenvector, e_k-e_l eigenvector, eigenvalues sum to 0
        okA = all(M[m][i]==-M[m][j] for m in range(n) if m not in (i,j)) and M[i][i]==M[j][j] \
          and all(M[m][k]== M[m][l] for m in range(n) if m not in (k,l)) and M[k][k]==M[l][l]
        if okA:
            mu = M[i][i]+M[i][j]; nu = M[k][k]-M[k][l]
            if mu+nu==0:
                cA+=1
                if mu!=0: cAnz+=1
        # --- B: e_i-e_j and e_k-e_l eigenvectors with equal eigenvalues
        okB = all(M[m][i]== M[m][j] for m in range(n) if m not in (i,j)) and M[i][i]==M[j][j] \
          and all(M[m][k]== M[m][l] for m in range(n) if m not in (k,l)) and M[k][k]==M[l][l]
        if okB:
            l1 = M[i][i]-M[i][j]; l2 = M[k][k]-M[k][l]
            if l1==l2:
                cB+=1
                if l1!=0: cBnz+=1
    return tot,cA,cAnz,cB,cBnz

for n in [4,5,6]:
    tot,cA,cAnz,cB,cBnz = check(n)
    f = 4**n
    print(f"n={n}: total={tot}")
    print(f"   A  (pair sums to 0)     count={cA:7d}  P={Fraction(cA,tot)}  P*4^n = {Fraction(cA*f,tot)}   [claim 3]")
    print(f"   A' (pair sums 0, mu!=0) count={cAnz:7d}  P*4^n = {Fraction(cAnz*f,tot)}   [claim 1]")
    print(f"   B  (repeated eigval)    count={cB:7d}  P*4^n = {Fraction(cB*f,tot)}   [claim 3]")
    print(f"   B' (repeated, lam!=0)   count={cBnz:7d}  P*4^n = {Fraction(cBnz*f,tot)}   [claim 1]")
