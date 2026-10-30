#!/usr/bin/env python3
"""Exact/finite falsification check for the posterior-balanced actual-anchor code.

The analytic theorem combines:
  (i) fleet02/B13 actual-anchor correction:
      Corr(A) <= (1/2) P_{A^c -> A},
  (ii) support bank M=(1/4) sum_{i!=k} p_{ik},
  (iii) fleet04/B18 posterior crossing:
      E C_A >= s [J-2sM]_+
for a Bernoulli block A with inclusion t=1-s.

For s=J/(4M), check through n=4 after the minimizing-character gauge:
  E P_{A^c->A} = 4t s M  (exact)
  E C_A >= J^2/(8M)      (exact rational)
  E Corr(A) <= J/2-J^2/(8M)
  E[Corr(A)-C_A] <= J/2-J^2/(4M)
and Corr(A) <= P/2 for every cut, using exhaustive optimal physical anchors.
"""
from fractions import Fraction
from math import log2


def h2(x):
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x*log2(x)-(1-x)*log2(1-x)


def gauge(values,n):
    N=1<<n
    raw=[]
    for i in range(n):
        raw.append(Fraction(sum(values[x]!=values[x^(1<<i)] for x in range(N)),N))
    T=sum(1<<i for i,p in enumerate(raw) if p>Fraction(1,2))
    if T:
        values=[v*(-1 if ((x&T).bit_count()&1) else 1) for x,v in enumerate(values)]
    j=[]
    for i in range(n):
        j.append(Fraction(sum(values[x]!=values[x^(1<<i)] for x in range(N)),N))
    return values,j


def support_matrix(values,n):
    N=1<<n
    eta=[]
    for i in range(n):
        eta.append([values[x]!=values[x^(1<<i)] for x in range(N)])
    p=[[Fraction(0) for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for k in range(n):
            if i!=k:
                p[i][k]=Fraction(sum(eta[i][x]!=eta[i][x^(1<<k)] for x in range(N)),N)
    return p


def cross_bank(p,n,A):
    B=((1<<n)-1)^A
    return sum((p[i][k] for i in range(n) if B>>i&1
                         for k in range(n) if A>>k&1 and i!=k),Fraction(0))


def crossing_C(values,n,A,j):
    Aidx=[i for i in range(n) if A>>i&1]
    Bidx=[i for i in range(n) if not(A>>i&1)]
    ans=Fraction(0)
    for k in Bidx:
        total=Fraction(0)
        for z in range(1<<len(Aidx)):
            bad=0
            denom=1<<len(Bidx)
            for y in range(denom):
                x=0
                for q,i in enumerate(Aidx):
                    if z>>q&1: x|=1<<i
                for q,i in enumerate(Bidx):
                    if y>>q&1: x|=1<<i
                bad += values[x]!=values[x^(1<<k)]
            pk=Fraction(bad,denom)
            total += abs(pk-Fraction(1,2))
        ans += total/Fraction(1<<len(Aidx)) - abs(j[k]-Fraction(1,2))
    return ans


def anchor_corr(values,n,A):
    B=((1<<n)-1)^A
    Aidx=[i for i in range(n) if A>>i&1]
    Bidx=[i for i in range(n) if B>>i&1]
    children=[]
    for z in range(1<<len(Aidx)):
        arr=[]
        for y in range(1<<len(Bidx)):
            x=0
            for q,i in enumerate(Aidx):
                if z>>q&1: x|=1<<i
            for q,i in enumerate(Bidx):
                if y>>q&1: x|=1<<i
            arr.append(values[x])
        children.append(arr)
    best=float("inf")
    Nchild=len(children[0])
    for base in children:
        cost=0.0
        for arr in children:
            d=sum(u!=v for u,v in zip(arr,base))/Nchild
            cost += h2(min(d,1-d))
        best=min(best,cost/len(children))
    return best


def weight(n,A,t,s):
    return (t**A.bit_count())*(s**(n-A.bit_count()))


def main():
    total_functions=0
    total_cuts=0
    min_M_over_J=None
    max_peer_excess=-1e100
    max_balance_excess=-1e100
    max_diff_excess=-1e100
    max_corr=0.0
    equality_functions=0
    for n in range(2,5):
        N=1<<n
        nf=0
        for code in range(1<<(N-1)): # quotient global output sign: f(0)=+1
            values=[1]+[1 if (code>>(x-1))&1 else -1 for x in range(1,N)]
            values,j=gauge(values,n)
            J=sum(j,Fraction(0))
            if J==0:
                continue
            p=support_matrix(values,n)
            M=sum((p[i][k] for i in range(n) for k in range(n) if i!=k),Fraction(0))/4
            assert M>=J/2 and M>0
            r=M/J
            min_M_over_J=r if min_M_over_J is None or r<min_M_over_J else min_M_over_J
            s=J/(4*M)
            t=1-s
            ep=Fraction(0)
            ecross=Fraction(0)
            ecorr=0.0
            ediff=0.0
            for A in range(1<<n):
                w=weight(n,A,t,s)
                P=cross_bank(p,n,A)
                C=crossing_C(values,n,A,j)
                corr=anchor_corr(values,n,A)
                peer_excess=corr-float(P)/2
                max_peer_excess=max(max_peer_excess,peer_excess)
                assert peer_excess<=1e-12
                ep += w*P
                ecross += w*C
                ecorr += float(w)*corr
                ediff += float(w)*(corr-float(C))
                total_cuts += 1
            assert ep==4*t*s*M
            cross_target=J*J/(8*M)
            assert ecross>=cross_target
            balance_target=float(J/2-J*J/(8*M))
            diff_target=float(J/2-J*J/(4*M))
            be=ecorr-balance_target
            de=ediff-diff_target
            max_balance_excess=max(max_balance_excess,be)
            max_diff_excess=max(max_diff_excess,de)
            assert be<=1e-12
            assert de<=1e-12
            if abs(be)<=1e-12:
                equality_functions += 1
            max_corr=max(max_corr,ecorr)
            nf += 1
            total_functions += 1
        print(f"n={n} nonconstant_functions_mod_sign={nf}")
    print(f"nonconstant_functions_total={total_functions}")
    print(f"cut_checks={total_cuts}")
    print(f"min_M_over_J={min_M_over_J.numerator}/{min_M_over_J.denominator}")
    print(f"max_peer_anchor_excess={max_peer_excess:.3e}")
    print(f"max_balanced_expectation_excess={max_balance_excess:.3e}")
    print(f"max_crossing_difference_excess={max_diff_excess:.3e}")
    print(f"equality_functions={equality_functions}")
    print(f"max_expected_actual_anchor_correction={max_corr:.12f}")
    print("violations=0")


if __name__=="__main__":
    main()
