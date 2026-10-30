#!/usr/bin/env python3
"""Exhaustive n<=4 falsification check for REPORT.md Theorem 2.1."""
from fractions import Fraction
import math


def vals(mask,n):
    return [1 if (mask>>x)&1 else -1 for x in range(1<<n)]


def eta(v,n,r):
    return [int(v[x]!=v[x^(1<<r)]) for x in range(1<<n)]


def inf(v,n,k):
    return Fraction(sum(v[x]!=v[x^(1<<k)] for x in range(1<<n)),1<<n)


def run_case(v,n,B,S):
    er={r:eta(v,n,r) for r in S}
    R=[]
    for r in S:
        if all(er[r][x]==er[r][x^(1<<s)] for s in S if s!=r for x in range(1<<n)):
            R.append(r)
    if not R:
        return None
    B=list(B)
    def embed(b):
        x=0
        for t,k in enumerate(B):
            if (b>>t)&1: x|=1<<k
        return x
    T=[tuple(er[r][embed(b)] for r in R) for b in range(1<<len(B))]
    count={}
    for t in T: count[t]=count.get(t,0)+1
    H=sum(-(c/len(T))*math.log2(c/len(T)) for c in count.values())
    IT=Fraction(0)
    per=[]
    for t,k in enumerate(B):
        ik=Fraction(sum(T[b]!=T[b^(1<<t)] for b in range(len(T))),len(T))
        pk=inf(v,n,k)
        IT+=ik
        per.append((ik,pk))
    return H,IT,per


def main():
    functions=qualifying=violations=equality=0
    max_ratio=Fraction(0)
    for n in range(1,5):
        for mask in range((1<<(1<<n))//2):  # one representative per global sign pair
            v=vals(mask,n); functions+=1
            for Bmask in range(1,(1<<n)-1):
                B=[i for i in range(n) if (Bmask>>i)&1]
                S=[i for i in range(n) if not((Bmask>>i)&1)]
                out=run_case(v,n,B,S)
                if out is None: continue
                qualifying+=1
                H,IT,per=out
                if H>float(IT)+1e-12: violations+=1
                for ik,pk in per:
                    if ik>2*pk: violations+=1
                    if pk and ik/pk>max_ratio: max_ratio=ik/pk
                    if ik and ik==2*pk: equality+=1
    print(f"functions_mod_sign={functions}")
    print(f"qualifying_cases={qualifying}")
    print(f"violations={violations}")
    print(f"max_directional_ratio={max_ratio.numerator}/{max_ratio.denominator}")
    print(f"positive_directional_equalities={equality}")
    assert functions==32906
    assert qualifying==148976
    assert violations==0
    assert max_ratio==2
    assert equality==144528

if __name__=="__main__": main()
