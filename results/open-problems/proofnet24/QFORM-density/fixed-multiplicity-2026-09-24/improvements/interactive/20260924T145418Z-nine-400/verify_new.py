#!/usr/bin/env python3
"""Exact finite checks and explicitly numerical diagnostics; not formal verification."""
from __future__ import annotations
import argparse, hashlib, itertools, json, math
from fractions import Fraction as F
from pathlib import Path
import numpy as np
import sympy as sp


def norm2(M: sp.Matrix) -> sp.Expr:
    return sum(x*x for x in M)


def determinant(A: sp.Matrix, rows: tuple[int,...], cols: tuple[int,...]) -> sp.Expr:
    return A.extract(rows, cols).det()


def vol(A: sp.Matrix, r: int) -> sp.Expr:
    if r == 0:
        return sp.Integer(1)
    total = sp.Integer(0)
    for S in itertools.combinations(range(A.rows), r):
        for T in itertools.combinations([i for i in range(A.rows) if i not in S], r):
            total += determinant(A, S, T)**2
    return total


def seed_data(A: sp.Matrix, S: tuple[int,...], T: tuple[int,...]):
    n = A.rows; B = A.extract(S,T)
    if B.det() == 0:
        return None
    L = tuple(i for i in range(n) if i not in S+T)
    P = A[:,list(T)] * B.inv() * A[list(S),:]
    D=sp.zeros(n); E=sp.zeros(n)
    for i in L:
        D[i,i]=A[i,i]-P[i,i]
        for j in L:
            if i != j:
                E[i,j]=A[i,j]-P[i,j]
    R=A-D-E
    assert norm2(A-R) == norm2(D)+norm2(E)
    assert R.rank()<=3*len(S)
    assert R.extract(L,L).rank()<=len(S)
    assert all(D[i,i]==0 for i in S+T)
    assert all(E[i,i]==0 for i in range(n))
    for i in L:
        assert determinant(A,tuple(sorted(S+(i,))),tuple(sorted(T+(i,))))**2 == B.det()**2 * D[i,i]**2
    return B.det()**2,norm2(D),norm2(E)


def main(output: Path):
    rng=np.random.default_rng(20260924145418)
    d,p,h=F(3,40),F(1,400),F(2,25)
    gamma_bound=F(8,5)*F(10,13)*F(8,5)*(F(8,3)-F(8,11)+F(4,19)+F(3,8))
    assert gamma_bound < 5
    assert p+d*d < F(1,121)
    margins={r:1-d-F(r,11)-(r+1)**2*h for r in (1,2)}
    assert margins=={1:F(1131,2200),2:F(51,2200)}
    c3six=15**6-26244*F(11,4)**6
    assert c3six==F(40788279,1024)>0
    assert sum(F(7,10)**j/math.factorial(j) for j in range(4))>2
    assert sum(F(17,10)**j/math.factorial(j) for j in range(5))>5
    assert 4+F(142,5)/d==F(1148,3)<400
    assert 200+80*F(12,5)+F(1,2)==F(785,2)<400
    exact_seeds=0; overlap_cases=0; diagnostics=[]
    for symmetric in (True,False):
        for n,r in ((5,1),(7,2)):
            for trial in range(2):
                raw=rng.integers(-3,4,size=(n,n))
                if symmetric:
                    raw=raw+raw.T
                A=sp.Matrix(raw.tolist())
                Vr=vol(A,r); Vnext=vol(A,r+1)
                assert Vr>0
                weighted_D=sp.Integer(0); weighted_E=sp.Integer(0); direct_W=sp.Integer(0)
                seeds=[]
                for S in itertools.combinations(range(n),r):
                    for T in itertools.combinations([i for i in range(n) if i not in S],r):
                        b2=determinant(A,S,T)**2
                        if b2==0:
                            continue
                        L=tuple(i for i in range(n) if i not in S+T)
                        P=A[:,list(T)]*A.extract(S,T).inv()*A[list(S),:]
                        dsq=sum((A[i,i]-P[i,i])**2 for i in L)
                        esq=sum((A[i,j]-P[i,j])**2 for i in L for j in L if i!=j)
                        weighted_D+=b2*dsq; weighted_E+=b2*esq
                        direct_W+=sum(determinant(A,tuple(sorted(S+(i,))),tuple(sorted(T+(i,))))**2 for i in L)
                        if len(seeds)<12:
                            seeds.append((S,T))
                assert weighted_D==direct_W
                assert weighted_E<=(r+1)**2*Vnext
                for S,T in seeds:
                    assert seed_data(A,S,T) is not None
                    exact_seeds+=1
                overlap_cases+=1
                sv=np.linalg.svd(np.array(A.tolist(),dtype=float),compute_uv=False)
                lhs=float(direct_W+(r+1)**2*Vnext)
                rhs=float(Vr)*float(np.sum(sv[3*r:]**2))
                assert lhs+1e-7>=rhs
                diagnostics.append({'n':n,'r':r,'symmetric':symmetric,'trial':trial,'left_minus_right_float':lhs-rhs})
    vals={
      'C3':3*math.sqrt(2)*math.e*(9/2)**(1/6),
      'C2':8*math.sqrt(math.e)*2**(-1/8),
      'no_pivot_density':25*3*math.sqrt(2)*math.e*(9/2)**(1/6),
      'scalar_scalar_density':1/math.sqrt(float(d))+(math.pi+4*math.log(2)+8+8*math.log(5))/float(d),
      'indefinite_pair_density':200+80*math.log(10)+1/math.e,
      'pair_half_potential_unit_scale':12+5*math.log(2)
    }
    result={'status':'PASS','seed':20260924145418,'exact_interpolation_seeds':exact_seeds,
       'exact_aggregate_overlap_cases':overlap_cases,'exact_constants':{'r1_margin':str(margins[1]),'r2_margin':str(margins[2]),'gamma_coefficient_upper':str(gamma_bound),'C3_sixth_power_slack':str(c3six),'scalar_scalar_bound':str(F(1148,3)),'indefinite_bound':str(F(785,2))},
       'numerical_spectral_tail_diagnostics':diagnostics,'floating_constants':vals,
       'limitations':'Finite exact checks verify their instances; floating spectral tests are diagnostics. Neither replaces the written general proofs or independent review.'}
    output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path,default=Path('checks_new.json'))
    args=ap.parse_args(); main(args.output)
