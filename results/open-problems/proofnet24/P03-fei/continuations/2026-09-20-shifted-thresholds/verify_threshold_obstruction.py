#!/usr/bin/env python3
"""Exact checks for the shifted-threshold obstruction to Han Question 3.1.

The all-dimensional divergence is proved analytically in REPORT.md. This
program only checks finite identities and rational witnesses; it is not a
proof by enumeration of an unbounded-dimensional statement. Standard library.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import comb, isqrt
from pathlib import Path
import time


def binomial_row(n: int) -> list[int]:
    if n < 0:
        raise ValueError('n must be nonnegative')
    row = [1]
    for k in range(n):
        row.append(row[-1] * (n-k) // (k+1))
    return row


def threshold_spectrum(n: int, s: int) -> tuple[list[int], int]:
    """Returns integer Walsh numerators 2**n * a_k and pivotal numerator.

    f=+1 for at most s negative input signs, and -1 otherwise. There are
    C(n,k) copies of a_k. Each coordinate influence is pivotal/2**(n-1).
    """
    if not 0 <= s < n:
        raise ValueError('Require n >= 1 and 0 <= s < n')
    N = n-1
    choose = binomial_row(N)
    pivotal = choose[s]
    r = N-2*s
    K = [1]
    if N:
        K.append(r)
    for j in range(1, N):
        value = r*K[j] - (N-j+1)*K[j-1]
        assert value % (j+1) == 0
        K.append(value//(j+1))
    row_n = binomial_row(n)
    W = [2*sum(row_n[:s+1]) - (1<<n)]
    for j in range(N+1):
        value = pivotal*K[j]
        assert value % choose[j] == 0
        W.append(2*(value//choose[j]))
    assert sum(row_n[k]*W[k]**2 for k in range(n+1)) == 1<<(2*n)
    assert sum(choose[k-1]*W[k]**2 for k in range(1,n+1)) == pivotal*(1<<(n+1))
    return W, pivotal


def fwht(values: list[int]) -> list[int]:
    result = values.copy()
    h = 1
    while h < len(result):
        for i in range(0,len(result),2*h):
            for j in range(i,i+h):
                a,b = result[j],result[j+h]
                result[j],result[j+h] = a+b,a-b
        h *= 2
    return result


def interval(x: Fraction, places: int = 12) -> dict[str,str]:
    scale = 10**places
    lower = x.numerator*scale//x.denominator
    def dec(v: int) -> str:
        return f'{v//scale}.{v%scale:0{places}d}'
    return {'lower':dec(lower), 'upper':dec(lower+1)}


def overlap_ratio(n: int, s: int) -> tuple[Fraction,list[int],int]:
    W,pivotal = threshold_spectrum(n,s)
    row = binomial_row(n-1)
    numerator = sum(row[k]*abs(W[k]*W[k+1]) for k in range(n))
    ratio = Fraction(numerator,pivotal*(1<<(n+1)))
    return ratio,W,pivotal


def run(max_m: int) -> dict:
    count = 0
    for n in range(1,11):
        for s in range(n):
            W,pivotal = threshold_spectrum(n,s)
            direct = fwht([1 if x.bit_count() <= s else -1 for x in range(1<<n)])
            assert direct == [W[x.bit_count()] for x in range(1<<n)]
            # Separately evaluate each coordinate, not just the symmetric formula.
            ratios=[]
            for i in range(n):
                bit=1<<i
                num=sum(abs(direct[x]*direct[x|bit]) for x in range(1<<n) if not x&bit)
                den=sum(direct[x]**2 for x in range(1<<n) if x&bit)
                ratios.append(Fraction(num,den))
            assert len(set(ratios))==1
            assert ratios[0]==overlap_ratio(n,s)[0]
            count+=1
    examples=[]
    for m in (2,4,8,16,32,64,128):
        if m>max_m:
            continue
        N=m*m; n=N+1; s=(N-m)//2
        assert N-2*s==m and isqrt(N)==m
        ratio,W,pivotal=overlap_ratio(n,s)
        blocks=[]
        row=binomial_row(N)
        for cutoff in (4,16,64,256):
            if cutoff>=n:
                continue
            partial=Fraction(sum(row[k]*abs(W[k]*W[k+1]) for k in range(1,cutoff+1)),pivotal*(1<<(n+1)))
            blocks.append({'max_level':cutoff,'ratio_interval':interval(partial)})
        examples.append({'m':m,'n':n,'negative_count_cutoff':s,
                         'ratio_interval':interval(ratio),
                         'all_coordinates_identical':True,
                         'partial_low_level_ratios':blocks,
                         'ratio_numerator_bits':ratio.numerator.bit_length(),
                         'ratio_denominator_bits':ratio.denominator.bit_length()})
    # A small exact certificate contradicting coefficient 2.
    ratio,_,_=overlap_ratio(32,21)  # original t=22
    assert ratio>2
    return {'status':'ALL_CHECKS_PASS',
            'full_FEI_proved':False,'independent_audit':False,'lean_used':False,
            'small_thresholds_FWHT_crosschecked':count,
            'small_dimensions':list(range(1,11)),
            'finite_counterexample_to_constant_two':{
                'n':32,'negative_count_cutoff':21,
                'ratio_numerator':str(ratio.numerator),
                'ratio_denominator':str(ratio.denominator),
                'ratio_interval':interval(ratio)},
            'shifted_threshold_sequence':examples,
            'scope':'Exact finite Walsh coefficients, Parseval, directional influence, all-coordinate overlap, and rational intervals. Infinite divergence uses the report proof, not extrapolation.'}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-m',type=int,default=64)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if args.max_m<2:
        parser.error('--max-m must be at least 2')
    start=time.monotonic()
    result=run(args.max_m)
    result['script_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
    result['elapsed_seconds']=round(time.monotonic()-start,3)
    text=json.dumps(result,indent=2)+'\n'
    if args.output:
        args.output.write_text(text)
    print(text)

if __name__=='__main__':
    main()
