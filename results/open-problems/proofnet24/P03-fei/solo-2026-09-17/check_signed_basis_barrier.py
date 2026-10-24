#!/usr/bin/env python3
"""Exact self-checks for SIGNED_BALANCE_AND_LINEAR_BASIS_BARRIER_2026-09-18.md."""
from fractions import Fraction as F
from pathlib import Path
import json

from certify_nand80 import wht, h, rational_interval


def log2_interval(x):
    return h(x)*F(-1,x)


def main():
    rows=[]
    for n in range(2,11):
        N=1<<n
        values=[-1]+[1]*(N-1)
        coeff=[F(x,N) for x in wht(values)]
        assert coeff[0]==F(N-2,N)
        assert all(x==F(-2,N) for x in coeff[1:])
        p=[x*x for x in coeff]
        influence=sum((S.bit_count()*p[S] for S in range(N)),F(0))
        assert influence==F(2*n,N)
        generalized=[]
        for U in range(1,N):
            alpha=sum((p[S] for S in range(N) if (S&U).bit_count()%2),F(0))
            assert alpha==F(2,N)
            # Independent truth-table verification of the physical translation.
            physical=F(sum(values[x]!=values[x^U] for x in range(N)),N)
            assert physical==alpha
            generalized.append(alpha)
        for i in range(n):
            same=F(0);opposite=F(0);K=log2_interval(F((N-2)**2,4))*F(4,N*N)
            for S in range(N):
                if S&(1<<i):continue
                product=coeff[S]*coeff[S|(1<<i)]
                if product>0:same+=product
                elif product<0:opposite-=product
            assert same==opposite==F(2*(N-2),N*N)
            formula=log2_interval(F(N-2,2))*F(8,N*N)
            assert max(K.lo,formula.lo)<=min(K.hi,formula.hi)
        H=h(p[0])+h(p[1])*(N-1)
        exact_formula=h(F((N-2)**2,N*N))+log2_interval(F(N*N,4))*F(4*(N-1),N*N)
        assert max(H.lo,exact_formula.lo)<=min(H.hi,exact_formula.hi)
        alpha=F(2,N)
        marginal_cost=(h(alpha)+h(1-alpha))*n
        rows.append({'n':n,'N':N,'nonzero_directions_checked':N-1,
                     'I_exact':str(influence),'H_interval':rational_interval(H),
                     'H_over_I_interval':rational_interval(H*F(1,influence)),
                     'any_basis_marginal_cost_over_I_interval':
                         rational_interval(marginal_cost*F(1,influence)),
                     'K_per_coordinate_interval':
                         rational_interval(log2_interval(F(N-2,2))*F(8,N*N)),
                     'same_sign_overlap_exact':str(F(2*(N-2),N*N)),
                     'opposite_sign_overlap_exact':str(F(2*(N-2),N*N))})
    projection_checks=[];partial_lift_checks=[]
    for n in range(1,4):
        N=1<<n
        for label in range(1<<N):
            f=[1-2*((label>>x)&1) for x in range(N)]
            ahat=[F(x,N) for x in wht(f)]
            p=[x*x for x in ahat]
            source_I=sum((S.bit_count()*p[S] for S in range(N)),F(0))
            for U in range(1,N):
                shifted=[f[x^U] for x in range(N)]
                A=[F(x+y,2) for x,y in zip(f,shifted)]
                B=[F(x-y,2) for x,y in zip(f,shifted)]
                assert all(x in [F(-1),F(0),F(1)] for x in A+B)
                assert all(not(x and y) for x,y in zip(A,B))
                Ahat=[F(x,N) for x in wht(A)]
                Bhat=[F(x,N) for x in wht(B)]
                for S in range(N):
                    odd=(S&U).bit_count()%2
                    assert Ahat[S]==(0 if odd else ahat[S])
                    assert Bhat[S]==(ahat[S] if odd else 0)
                alpha=sum((p[S] for S in range(N) if (S&U).bit_count()%2),F(0))
                assert sum((x*x for x in Bhat),F(0))==alpha
                assert sum((x*x for x in Ahat),F(0))==1-alpha
                projection_checks.append([n,label,U])
            # g(x,z)=f(x) on the z=+1 half and zero on the other half.
            g=f+[0]*N
            ghat=[F(x,2*N) for x in wht(g)]
            pg=[2*x*x for x in ghat]  # divide by rho=1/2
            # The selector bit is fair: each source atom splits into two atoms
            # of half its mass.
            expected=[x/2 for x in p for _ in range(2)]
            assert sorted(pg)==sorted(expected)
            lifted_I=sum((S.bit_count()*pg[S] for S in range(2*N)),F(0))
            assert lifted_I==source_I+F(1,2)
            partial_lift_checks.append([n,label])
    # Every partial Boolean function is a parity-projection branch of a
    # Boolean parent after adjoining one coordinate.
    completion_checks=0
    for n in range(1,4):
        N=1<<n
        for label in range(3**N):
            work=label; g=[]
            for _ in range(N):
                digit=work%3; work//=3
                g.append([F(-1),F(0),F(1)][digit])
            plus=[x if x else F(1) for x in g]
            minus=[x if x else F(-1) for x in g]
            parent=plus+minus
            assert all(x in [F(-1),F(1)] for x in parent)
            projected=[(parent[x]+parent[x^N])/2 for x in range(2*N)]
            assert projected==g+g
            completion_checks+=1
    result={'status':'PASS','arithmetic':'exact integer/rational arithmetic and 160-bit outward rational logarithm intervals',
            'rows':rows,
            'parity_projection_checks':len(projection_checks),
            'parity_projection_range':'every Boolean truth table through n=3 and every nonzero direction',
            'partial_boolean_lift_checks':len(partial_lift_checks),
            'partial_boolean_lift_range':'every Boolean truth table through n=3',
            'partial_projection_completion_checks':completion_checks,
            'partial_projection_completion_range':'every {0,+1,-1}-valued truth table through n=3',
            'scope':'Finite self-checks only. All-n claims are proved algebraically in the note; no independent audit.'}
    Path('signed_basis_barrier_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'PASS','dimensions':[r['n'] for r in rows],
                      'parity_projection_checks':len(projection_checks),
                      'partial_boolean_lift_checks':len(partial_lift_checks),
                      'partial_projection_completion_checks':completion_checks,
                      'last_row':rows[-1]},indent=2))


if __name__=='__main__':main()
