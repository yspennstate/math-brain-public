#!/usr/bin/env python3
"""Exact-symbolic exhaustive check of the A097 rank-one critical transfer."""

from fractions import Fraction
from functools import lru_cache


PRIMES = (2, 3, 5, 7, 11, 13)


def factor(a):
    out = {}
    for p in PRIMES:
        while a > 1 and a % p == 0:
            out[p] = out.get(p, 0) + 1
            a //= p
    assert a == 1
    return out


def ln_interval(q, N=360):
    if q == 1: return Fraction(0), Fraction(0)
    z = Fraction(q - 1, q + 1)
    s, pw = Fraction(0), z
    for k in range(N):
        s += pw / (2*k + 1)
        pw *= z*z
    lo = 2*s
    return lo, lo + 2*pw/((2*N+1)*(1-z*z))


@lru_cache(None)
def log2_interval(p):
    if p == 2: return Fraction(1), Fraction(1)
    a,b = ln_interval(p); c,d = ln_interval(2)
    return a/d, b/c


class Sig:
    def __init__(self, const=0, logs=None):
        d = dict(logs or {})
        const = Fraction(const) + d.pop(2, Fraction(0))
        self.const = const
        self.logs = tuple(sorted((p,Fraction(c)) for p,c in d.items() if c))
    def __add__(self, o):
        d=dict(self.logs)
        for p,c in o.logs: d[p]=d.get(p,Fraction(0))+c
        return Sig(self.const+o.const,d)
    def scale(self,c): return Sig(self.const*Fraction(c),{p:a*Fraction(c) for p,a in self.logs})
    def __sub__(self,o): return self+o.scale(-1)
    def __eq__(self,o): return self.const==o.const and self.logs==o.logs
    def sign(self):
        if self.const==0 and not self.logs: return 0
        lo=hi=self.const
        for p,c in self.logs:
            a,b=log2_interval(p)
            if c>=0: lo+=c*a; hi+=c*b
            else: lo+=c*b; hi+=c*a
        if lo>0:return 1
        if hi<0:return -1
        raise AssertionError("unresolved sign")


def restrict_raw(t,n,i,b):
    out=[]
    for y in range(1<<(n-1)):
        x=(y&((1<<i)-1)) | (b<<i) | ((y>>i)<<(i+1))
        out.append(t[x])
    return tuple(out)


@lru_cache(None)
def canon(t,n):
    t=tuple(t)
    while n:
        found=False
        for i in range(n):
            a,b=restrict_raw(t,n,i,0),restrict_raw(t,n,i,1)
            if a==b:
                t,n=a,n-1; found=True; break
        if not found: break
    if t[0]<0:t=tuple(-x for x in t)
    return t,n


@lru_cache(None)
def metric(t,n):
    a=list(t)
    step=1
    while step<len(a):
        for i in range(0,len(a),2*step):
            for j in range(step):
                x,y=a[i+j],a[i+j+step]
                a[i+j],a[i+j+step]=x+y,x-y
        step*=2
    den=1<<(2*n); H=Sig(); I=Fraction(0)
    for S,w in enumerate(a):
        if not w: continue
        p=Fraction(w*w,den); logs={q:-2*e*p for q,e in factor(abs(w)).items()}
        H=H+Sig(2*n*p,logs); I+=S.bit_count()*p
    return H,I


def ratio(obj):
    H,I=metric(*obj); return H.scale(1/I)


def cmp(a,b): return (ratio(a)-ratio(b)).sign()


@lru_cache(None)
def descendants(t,n):
    out={(t,n)}
    for i in range(n):
        for b in (0,1):
            ch=canon(restrict_raw(t,n,i,b),n-1)
            if ch[1] and len(set(ch[0]))>1: out.update(descendants(*ch))
    return frozenset(out)


def critical(obj): return all(cmp(obj,h)>=0 for h in descendants(*obj))


def product_ratio(a,b):
    Ha,Ia=metric(*a); Hb,Ib=metric(*b)
    return (Ha+Hb).scale(1/(Ia+Ib))


def all_functions(n, balanced=False):
    out=set()
    for mask in range(1<<((1<<n)-1)):
        t=(1,)+tuple(1 if (mask>>(x-1))&1 else -1 for x in range(1,1<<n))
        g=canon(t,n)
        if g[1] and len(set(g[0]))>1 and (not balanced or sum(g[0])==0):out.add(g)
    return out


def main():
    controllers=set(); cores=set()
    for n in range(1,4):
        controllers.update(all_functions(n))
        cores.update(all_functions(n,balanced=True))
    pairs=converses=eta_checks=0
    for s in controllers:
        for g in cores:
            Rs,Rg=ratio(s),ratio(g)
            Hs,Is=metric(*s); Hg,Ig=metric(*g)
            RF=product_ratio(s,g)
            assert RF==(Rs.scale(Is/(Is+Ig))+Rg.scale(Ig/(Is+Ig)))
            # Any nontrivial tensor has a factor ratio >= root: strict-core exclusion.
            assert (Rs-RF).sign()>=0 or (Rg-RF).sign()>=0
            pairs+=1
            eq=(Rs-Rg).sign()==0
            if eq and critical(s) and critical(g):
                for u in descendants(*s):
                    for v in descendants(*g):
                        assert (RF-product_ratio(u,v)).sign()>=0
                        converses+=1
            # Quantitative identity behind the eta bound.
            assert (Rs-RF)==(Rs-Rg).scale(Ig/(Is+Ig))
            assert (Rg-RF)==(Rg-Rs).scale(Is/(Is+Ig))
            eta_checks+=2
    print("A097 rank-one critical transfer audit: PASS")
    print(f"controller/core pairs checked: {pairs}")
    print(f"critical-converse descendant products checked: {converses}")
    print(f"exact eta-gap identities checked: {eta_checks}")
    print("Walsh weights and influences were exact Fractions; entropy was an exact Q-linear log-prime form.")


if __name__=='__main__': main()

