#!/usr/bin/env python3
"""Exact checks for UNITARY_ERASURE_OBSTRUCTION.md; standard library only."""
from __future__ import annotations
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json
from verify_polynomial_symmetry import LogForm, ZERO, binary_entropy, fwht


def matmul(A, B):
    columns=list(zip(*B))
    return [[sum(x*y for x,y in zip(row,col)) for col in columns] for row in A]

def is_diagonal_scalar(A, scalar):
    return all(x==(scalar if i==j else 0) for i,row in enumerate(A) for j,x in enumerate(row))

def transpose(A):
    return [list(x) for x in zip(*A)]

def phase(y,k):
    bit=0
    for j in range(0,k,2): bit^=((y>>j)&1)*((y>>(j+1))&1)
    return -1 if bit else 1

def run():
    pattern=[]
    for k in (2,4,6,8):
        M=1<<k
        d=tuple(phase(y,k) for y in range(M))
        a0=fwht(tuple(d[y] if not(y&1) else 0 for y in range(M)))
        for z in range(M):
            assert abs(a0[z])==(0 if z&2 else 1<<(k//2))
        # Orthogonality of every pair of Walsh rows, without floating point.
        W=tuple(tuple(-1 if (z&y).bit_count()%2 else 1 for y in range(M)) for z in range(M))
        for i in range(M):
            for j in range(i+1):
                assert sum(a*b for a,b in zip(W[i],W[j]))==(M if i==j else 0)
        pattern.append({'M':M,'walsh_rows':M,'nonzero_entries_per_A0_column':M//2,
                        'A0_nonzero_magnitude':'1/'+str(1<<(k//2)),
                        'rank_one_branch_entry_magnitude':'1/'+str(M)})
    # Smallest nontrivial full ambient example.
    k=2;M=1<<k;selected=tuple(y for y in range(M) if y&1);m=len(selected)
    NA=1<<M;N=NA*(1<<m);n=M+m
    d=tuple(phase(y,k) for y in range(M))
    a0=fwht(tuple(d[y] if not(y&1) else 0 for y in range(M)))
    A=[[0]*N for _ in range(N)]  # A = M U, exactly integral.
    for anc in range(NA):
        for b in range(1<<m):
            col=anc|(b<<M)
            if anc.bit_count()!=1:
                A[col][col]=M
                continue
            w=anc.bit_length()-1
            for z in range(M):
                row=(1<<z)|(b<<M)
                A[row][col]=a0[z^w]
                for t,y in enumerate(selected):
                    flipped=(1<<z)|((b^(1<<t))<<M)
                    A[flipped][col]=d[y]*(-1 if ((z^w)&y).bit_count()%2 else 1)
    assert A==transpose(A)
    assert is_diagonal_scalar(matmul(A,A),M*M)
    erasures=[]
    pair_terms=0
    for i in range(n):
        total=ZERO
        for col in range(N):
            for row in range(N):
                if row&(1<<i): continue
                x=A[row][col]**2;y=A[row^(1<<i)][col]**2
                if x+y:
                    total=total+binary_entropy(F(x,x+y))*F(x+y,M*M*N)
                pair_terms+=1
        erasures.append(total)
    assert all(e.zero() for e in erasures[:M])
    target=binary_entropy(F(1,M+1))*F(M+1,2*NA)
    assert all((e-target).zero() for e in erasures[M:])
    total=ZERO
    for e in erasures:total=total+e
    assert (total-target*m).zero()
    commutator_checks=[]
    for i in range(M,n):
        z=[-1 if row&(1<<i) else 1 for row in range(N)]
        C=[[A[row][col]*(z[col]-z[row]) for col in range(N)] for row in range(N)]
        Q=matmul(transpose(C),C)
        Q2=matmul(Q,Q)
        assert all(Q2[row][col]==4*M*M*Q[row][col] for row in range(N) for col in range(N))
        rank=F(sum(Q[j][j] for j in range(N)),4*M*M)
        assert rank==1<<m
        V=rank/N  # singular values of [U,Z_i] are exactly 0 or 2.
        assert V==F(1,NA)
        commutator_checks.append({'physical_bit':i,'rank':int(rank),'normalized_trace_cost':str(V)})
    lo,hi=total.interval()
    return {'status':'PASS','classical_FEI_counterexample':False,
            'operator_relaxation_refuted':True,'independent_audit':False,'formal_verification':False,
            'construction':'real symmetric orthogonal involutions; not Walsh-diagonal convolution matrices',
            'arithmetic':'exact integer matrix products, exact rational influences, exact prime-log entropy identities',
            'walsh_pattern_checks':pattern,'full_matrix':{'M':M,'target_bits':m,'physical_bits':n,'dimension':N,
                'scaled_matrix_symmetric':True,'scaled_matrix_square':M*M,'column_pair_terms_checked':pair_terms,
                'zero_ancillary_erasure_bits':M,'total_erasure_lower':str(lo),'total_erasure_upper':str(hi),
                'target_trace_norm_checks':commutator_checks},
            'analytical_divergence':'B(U)/V(U) > log_2(M)/10 for every M=2^k with even k>=2; large matrices are not enumerated',
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=Path('unitary_verification.json'))
    args=parser.parse_args()
    out=run()
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2,sort_keys=True))
