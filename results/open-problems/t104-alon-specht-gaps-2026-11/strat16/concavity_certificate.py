"""Exact polynomial matrix certificate for fixed-u concavity, n=5.

Uses sparse rational polynomial rings. A coefficient matrix being indefinite
only rejects that sufficient certificate; it does not disprove concavity.
"""
import itertools
import json
import time
from pathlib import Path
import sympy as s
from sympy.polys.rings import ring
from sympy.polys.domains import QQ


def is_psd(M):
    """Exact symmetric elimination, including singular pivots."""
    M = s.MutableDenseMatrix(M)
    while M.rows:
        if any(M[i,i] < 0 for i in range(M.rows)):
            return False
        nz = next((i for i in range(M.rows) if M[i,i] > 0), None)
        if nz is None:
            return M.is_zero_matrix
        order = [nz] + [i for i in range(M.rows) if i != nz]
        M = M.extract(order, order)
        M = M[1:,1:] - M[1:,0]*M[0,1:]/M[0,0]
    return True


def construct():
    rr,x,y,z,t,h = ring('x,y,z,t,h',QQ)
    gaps = (x,y,z,t)
    U = [sum((5-j if i<j else -j)*gaps[j-1] for j in range(1,5)) for i in range(5)]
    R = sum(v*v for v in U)
    K = [[rr.zero for j in range(3)] for i in range(5)]
    for c,j in enumerate(range(1,4)):
        K[0][c]=U[4]-U[j];K[j][c]=U[0]-U[4];K[4][c]=U[j]-U[0]
    assert sum(U)==0
    assert all(sum(K[i][c] for i in range(5))==0 for c in range(3))
    assert all(sum(U[i]*K[i][c] for i in range(5))==0 for c in range(3))
    es=[]
    for a,b in itertools.combinations_with_replacement(range(3),2):
        es.append([[K[i][a]*K[j][b]+(K[i][b]*K[j][a] if a!=b else 0)
                    for j in range(5)]for i in range(5)])
    k=5+h
    def negative_q(E):
        tr2=sum(E[i][j]*E[i][j]for i in range(5)for j in range(5))
        B=sum(U[i]*U[j]*E[i][j]**2 for i in range(5)for j in range(5))
        c=sum(U[i]**2*E[i][j]**2 for i in range(5)for j in range(5))
        pd=sum(U[i]**2*E[i][i]for i in range(5))
        pEd=sum(U[i]**2*E[i][j]*E[j][j]for i in range(5)for j in range(5))
        m=sum(E[i][i]for i in range(5))/2
        return 2*R*k*k*tr2+(2*k*k-4*k)*B-4*k*k*c+2*k*k*pEd+4*k*R*m*m-2*(k+2)*m*pd
    diag=[negative_q(E)for E in es]
    M=[[rr.zero for j in range(6)]for i in range(6)]
    for i in range(6):
        M[i][i]=diag[i]
        for j in range(i):
            E=[[es[i][a][b]+es[j][a][b]for b in range(5)]for a in range(5)]
            M[i][j]=M[j][i]=(negative_q(E)-diag[i]-diag[j])/2
    return rr,U,K,M


def coefficient_matrices(M):
    exps=sorted(set().union(*(set(p)for row in M for p in row)))
    return [(e,s.Matrix(6,6,[s.Rational(p.get(e,0)) for row in M for p in row]))for e in exps]


def main():
    tick=time.monotonic();rr,U,K,M=construct()
    raw=coefficient_matrices(M)
    bad=[e for e,m in raw if not is_psd(m)]
    print('raw coefficient matrices',len(raw),'not PSD',len(bad),flush=True)
    records=[]
    for perm in itertools.permutations(range(4)):
        # Simultaneous polynomial composition into an isomorphic ring.
        dest,*gens=ring('a,b,c,d,h',QQ)
        repl=[None]*5;repl[4]=gens[4]
        for j,i in enumerate(perm):repl[i]=sum(gens[j:4])
        def compose(p):
            out=dest.zero
            for m,c in p.items():
                term=dest(c)
                for g,e in zip(repl,m):term*=g**e
                out+=term
            return out
        MM=[[compose(p)for p in row]for row in M]
        coeff=coefficient_matrices(MM)
        fails=[e for e,m in coeff if not is_psd(m)]
        records.append(dict(permutation=perm,count=len(coeff),failed=fails))
        print(perm,len(coeff),'not PSD',len(fails),flush=True)
    Path('concavity_coefficients.json').write_text(json.dumps(dict(raw_failed=bad,cones=records,seconds_NUMERICAL=time.monotonic()-tick),indent=2)+'\n')
    assert all(not r['failed']for r in records),'This cone coefficient certificate is insufficient.'
    print('PROVED (concavity_certificate.py): fixed-selected-projector concavity for k>=5, including infinity.')

if __name__=='__main__':main()
