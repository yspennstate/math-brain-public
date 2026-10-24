#!/usr/bin/env python3
"""Self-check for B16 one-sided ordered-min q-flip multiplier payment.

This checks only finite algebra/numerics supporting the written proof.  It does
not prove full FEI and does not rerun the read-once certificate.
"""
from fractions import Fraction
import itertools
import math

def parity(x):
    return x.bit_count() & 1

def choose(n,k):
    if k < 0 or k > n:
        return 0
    return math.comb(n,k)

def direct_kernel_q(n, q):
    """Unnormalized K(w); q is dict c -> nonnegative Fraction."""
    m = n-1
    K = []
    for w in range(1 << m):
        k = w.bit_count()
        if k == 0:
            K.append(Fraction(0))
            continue
        s = Fraction(0)
        for c in range(k+1,n+1):
            s += q[c] * Fraction(choose(c-1,k), choose(n-1,k))
        K.append(s / n)
    return K

def direct_multiplier(n, r, q):
    """hat(mathcal K)(U), |U|=r, where mathcal K=2^(n-1)K."""
    K = direct_kernel_q(n,q)
    U = (1 << r)-1
    return sum(K[w] * (-1 if parity(U&w) else 1) for w in range(1 << (n-1)))

def formula_multiplier(n,r,q):
    s=Fraction(0)
    for c in range(2,n+1):
        R=Fraction(choose(n-1-r,c-1),choose(n-1,c-1))
        s += q[c]*(2**(c-1)*R-1)
    return s/n

def exact_q_checks():
    count=0
    for n in range(2,9):
        q={c:Fraction(c+1,c) for c in range(2,n+1)}
        Q=sum(q.values(),Fraction(0))
        for r in range(0,n):
            a=direct_multiplier(n,r,q)
            b=formula_multiplier(n,r,q)
            assert a==b,(n,r,a,b)
            if r:
                assert a >= -Q/n
            count += 1

        # Sharpness: top frequency r=n-1 has A=-Q/n, and the cut
        # eta=(1-chi_U)/2 puts all nonconstant cut energy at U.
        r=n-1
        assert formula_multiplier(n,r,q) == -Q/n
        m=n-1
        U=(1<<m)-1
        eta=[Fraction(1-(-1 if parity(U&w) else 1),2) for w in range(1<<m)]
        alpha=sum(eta,Fraction(0))/(1<<m)
        E=alpha*(1-alpha)
        K=direct_kernel_q(n,q)
        mathcal=[(1<<m)*x for x in K]
        mu=sum(mathcal,Fraction(0))/(1<<m)
        centered=[x-mu for x in mathcal]
        p=[]
        for w in range(1<<m):
            p.append(sum(Fraction(1) if eta[x]!=eta[x^w] else Fraction(0)
                         for x in range(1<<m))/(1<<m))
        pairing=sum(centered[w]*p[w] for w in range(1<<m))/(1<<m)
        assert pairing == 2*Q*E/n
    return count

def Hc(c):
    eps=2.0**(2-c)-2.0**(2-2*c)
    p0=1.0-eps
    return -p0*math.log2(p0)+(2**c-1)*2.0**(2-2*c)*(2*c-2)

def raw_kernel(n):
    m=n-1
    q={c:Hc(c) for c in range(2,n+1)}
    K=[]
    for w in range(1<<m):
        k=w.bit_count()
        if k==0:
            K.append(0.0)
        else:
            K.append(sum(q[c]*choose(c-1,k)/choose(n-1,k)
                         for c in range(k+1,n+1))/n)
    return [(1<<m)*x for x in K],sum(q.values())

def eta_from_truth(vals,n,i):
    others=[j for j in range(n) if j!=i]
    eta=[]
    for w in range(1<<(n-1)):
        x=0
        for b,j in enumerate(others):
            if (w>>b)&1:
                x |= 1<<j
        eta.append(0.5*(1-vals[x]*vals[x^(1<<i)]))
    return eta

def qflip_profile(eta):
    M=len(eta)
    return [sum(1.0 if eta[x]!=eta[x^w] else 0.0 for x in range(M))/M
            for w in range(M)]

def exhaustive_boolean_raw():
    tested=0
    worst=-1e100
    for n in (2,3):
        mathcal,Q=raw_kernel(n)
        mu=sum(mathcal)/len(mathcal)
        centered=[x-mu for x in mathcal]
        for truth_bits in range(1<<(1<<n)):
            vals=[1 if ((truth_bits>>x)&1) else -1 for x in range(1<<n)]
            for i in range(n):
                eta=eta_from_truth(vals,n,i)
                alpha=sum(eta)/len(eta)
                E=alpha*(1-alpha)
                p=qflip_profile(eta)
                lhs=sum(centered[w]*p[w] for w in range(len(p)))/len(p)
                rhs=2*Q*E/n
                assert lhs <= rhs + 1e-11,(n,truth_bits,i,lhs,rhs)
                if E>1e-15:
                    worst=max(worst,lhs/rhs if rhs else -1e100)
                tested += 1
    return tested,worst

if __name__=="__main__":
    exact=exact_q_checks()
    tested,worst=exhaustive_boolean_raw()
    Q100=sum(Hc(c) for c in range(2,101))
    print("PASS")
    print("exact_multiplier_cases",exact)
    print("exhaustive_boolean_coordinate_cases",tested)
    print("worst_raw_ratio_to_sharp_bound",repr(worst))
    print("Q_raw_100",repr(Q100))
    print("theorem_elementary_uniform_bound","Q_raw_infty < 12")
