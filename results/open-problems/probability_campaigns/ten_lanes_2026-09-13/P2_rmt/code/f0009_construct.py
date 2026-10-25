"""Explicit constructions of symmetric +-1 matrices with
   (a) two eigenvalues summing to zero, lambda != 0   [F0009 / Vu Conj 8.5]
   (b) a repeated eigenvalue                          [F0008 / Vu Conj 8.4]
   built from two disjoint support-2 eigenvectors.  Exact integer arithmetic."""
import itertools, random
from sympy import Matrix, symbols, factor_list, Poly, Rational, sqrt, nsimplify

def build(n, i, j, k, l, mode, rng):
    """mode='opposite'  -> e_i+e_j eigvec with mu, e_k-e_l eigvec with -mu
       mode='repeat'    -> e_i-e_j eigvec with lam, e_k-e_l eigvec with lam"""
    M = [[None]*n for _ in range(n)]
    def setsym(a,b,v):
        M[a][b]=v; M[b][a]=v
    free = lambda: rng.choice([1,-1])
    S = {i,j,k,l}
    out = [m for m in range(n) if m not in S]
    if mode=='opposite':
        # (A) e_i+e_j eigenvector: M[m][i] = -M[m][j] for m not in {i,j}
        # (B) e_k-e_l eigenvector: M[m][k] =  M[m][l] for m not in {k,l}
        for m in out:
            s = free(); setsym(m,i,s); setsym(m,j,-s)
            t = free(); setsym(m,k,t); setsym(m,l,t)
        # cross block: M[k][i]=-M[k][j], M[l][i]=-M[l][j], M[i][k]=M[i][l], M[j][k]=M[j][l]
        s = free()
        setsym(i,k,s); setsym(i,l,s); setsym(j,k,-s); setsym(j,l,-s)
        # diagonals: M[i][i]=M[j][j], M[k][k]=M[l][l]
        # eigenvalues mu = M[i][i]+M[i][j],  nu = M[k][k]-M[k][l];  need nu = -mu
        M[i][i]=M[j][j]=1; setsym(i,j,1)          # mu = 2
        M[k][k]=M[l][l]=-1; setsym(k,l,1)         # nu = -1-1 = -2
        # remaining diagonal entries free
        for m in out: M[m][m]=free()
        # remaining outside-outside entries free
        for a,b in itertools.combinations(out,2):
            setsym(a,b,free())
        return M, 2, -2
    else:
        # (A) e_i-e_j: M[m][i]=M[m][j] for m not in {i,j}
        # (B) e_k-e_l: M[m][k]=M[m][l] for m not in {k,l}
        for m in out:
            s = free(); setsym(m,i,s); setsym(m,j,s)
            t = free(); setsym(m,k,t); setsym(m,l,t)
        s = free()
        setsym(i,k,s); setsym(i,l,s); setsym(j,k,s); setsym(j,l,s)
        M[i][i]=M[j][j]=1; setsym(i,j,-1)         # lam = M_ii - M_ij = 2
        M[k][k]=M[l][l]=1; setsym(k,l,-1)         # lam = 2
        for m in out: M[m][m]=free()
        for a,b in itertools.combinations(out,2):
            setsym(a,b,free())
        return M, 2, 2

rng = random.Random(20260913)
for n in [4,5,6,7,8,9]:
    for mode in ['opposite','repeat']:
        M,mu,nu = build(n,0,1,2,3,mode,rng)
        A = Matrix(M)
        assert A == A.T
        assert all(abs(A[a,b])==1 for a in range(n) for b in range(n)), "entries must be +-1"
        p = A.charpoly()
        # exact eigenvalues with multiplicity
        ev = A.eigenvals()
        # check claimed structure
        if mode=='opposite':
            ok = (mu in ev) and (nu in ev)
            extra = f"mu={mu} in spec: {mu in ev}; -mu={nu} in spec: {nu in ev}"
        else:
            ok = (mu in ev) and ev[mu] >= 2
            extra = f"lam={mu} multiplicity {ev.get(mu)}"
        print(f"n={n:2d} {mode:9s} ok={ok}  {extra}   charpoly={p.as_expr()}")
