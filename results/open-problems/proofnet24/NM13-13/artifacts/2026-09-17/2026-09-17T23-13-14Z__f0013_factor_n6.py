#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction
from multiprocessing import Pool, cpu_count
from sympy.polys.factortools import dup_zz_factor
from sympy.polys.domains import ZZ
import sys

def classify(row):
    coeffs, weight = row
    content, facs = dup_zz_factor([1] + list(coeffs), ZZ)
    assert content == 1
    degs=[]
    recon=[1]
    def mul(a,b):
        out=[0]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): out[i+j]+=int(x)*int(y)
        return out
    for f,m in facs:
        ff=[int(v) for v in f]
        d=len(ff)-1
        degs.extend([d]*m)
        for _ in range(m): recon=mul(recon,ff)
    assert sum(degs)==6
    assert recon == [1] + list(coeffs)
    return tuple(sorted(degs)), weight

def read_rows(path):
    meta=None; rows=[]
    with open(path) as fh:
        first=fh.readline().rstrip('\n')
        assert first.startswith('META\t')
        meta=first
        for line in fh:
            p=line.rstrip('\n').split('\t')
            assert p[0]=='P' and len(p)==8
            coeffs=tuple(map(int,p[1:7])); w=int(p[7])
            rows.append((coeffs,w))
    return meta, rows

def main():
    path=sys.argv[1] if len(sys.argv)>1 else '/tmp/f0013_n6.tsv'
    meta, rows=read_rows(path)
    print(meta)
    print(f'rows={len(rows)}')
    pattern_weight=Counter(); pattern_poly=Counter()
    with Pool(processes=min(5,cpu_count())) as pool:
        for pat,w in pool.imap_unordered(classify, rows, chunksize=256):
            pattern_weight[pat]+=w; pattern_poly[pat]+=1
    total=sum(pattern_weight.values())
    print(f'factor_weight_sum={total}')
    assert total==2**36
    print('factor_degree_census:')
    for pat in sorted(pattern_weight):
        print(f"{','.join(map(str,pat))}\tpolynomials={pattern_poly[pat]}\tmatrices={pattern_weight[pat]}")
    irr=pattern_weight[(6,)]
    frac=Fraction(irr,total)
    print(f'irreducible_matrices={irr}')
    print(f'irreducible_probability={frac.numerator}/{frac.denominator}')
    print(f'reducible_matrices={total-irr}')
    print(f'reducible_probability={(Fraction(total-irr,total)).numerator}/{(Fraction(total-irr,total)).denominator}')
    nonlinear=sum(w for pat,w in pattern_weight.items() if len(pat)>1 and 1 not in pat)
    print(f'reducible_without_linear_factor_matrices={nonlinear}')
    print(f'reducible_without_linear_factor_probability={Fraction(nonlinear,total).numerator}/{Fraction(nonlinear,total).denominator}')
    print('ALL_EXACT_FACTORIZATIONS_PASS')

if __name__=='__main__': main()
