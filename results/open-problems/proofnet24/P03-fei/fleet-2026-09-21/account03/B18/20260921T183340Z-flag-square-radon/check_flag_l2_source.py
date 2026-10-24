#!/usr/bin/env python3
"""Exact falsification checks for the B18 ordered-flag physical L2 theorem.

Standard library only. All probabilities are fractions.
This is a self-check; the all-dimensional theorem is proved algebraically in REPORT.md.
"""
from fractions import Fraction
from itertools import permutations
import json

def dotparity(a,b):
    return (a & b).bit_count() & 1

def compact_coords(x,n,i):
    y=0
    k=0
    for j in range(n):
        if j==i:
            continue
        if (x>>j)&1:
            y |= 1<<k
        k += 1
    return y

def expand_coords(y,n,i):
    x=0
    k=0
    for j in range(n):
        if j==i:
            continue
        if (y>>k)&1:
            x |= 1<<j
        k += 1
    return x

def derivative_pattern(fmask,n,i):
    """eta_i on representatives x_i=0, encoded on n-1 bits."""
    pat=0
    k=0
    for x in range(1<<n):
        if (x>>i)&1:
            continue
        if ((fmask>>x)&1) ^ ((fmask>>(x^(1<<i)))&1):
            pat |= 1<<k
        k += 1
    return pat

def p_of_w(pat,m,w):
    N=1<<m
    d=0
    for x in range(N):
        d += ((pat>>x)&1) ^ ((pat>>(x^w))&1)
    return Fraction(d,N)

def flag_p2(pat,m,Lmask):
    ws=[w for w in range(1<<m) if (w & ~Lmask)==0]
    vals=[p_of_w(pat,m,w) for w in ws]
    return sum((p*p for p in vals), Fraction(0))/len(vals)

def walsh_energies(pat,m):
    """Nonconstant squared normalized Walsh coefficients of a 0/1 function."""
    N=1<<m
    out={}
    for U in range(1,1<<m):
        s=0
        for x in range(N):
            eta=(pat>>x)&1
            s += eta * (-1 if dotparity(U,x) else 1)
        out[U]=Fraction(s*s,N*N)
    return out

def trace_mask(U,Lmask):
    return U & Lmask

def exact_flag_formula(pat,m,Lmask):
    a=walsh_energies(pat,m)
    grouped={}
    for U,val in a.items():
        V=U & Lmask
        if V:
            grouped[V]=grouped.get(V,Fraction(0))+val
    T=sum(grouped.values(),Fraction(0))
    rhs=4*T*T + 4*sum((v*v for v in grouped.values()),Fraction(0))
    mean=2*T
    return mean,rhs,T,a

def precompute_q(n,i):
    m=n-1
    out={}
    # every Boolean eta on quotient, every later-coordinate subspace
    for pat in range(1<<(1<<m)):
        for Lfull in range(1<<n):
            if (Lfull>>i)&1:
                continue
            Lc=compact_coords(Lfull,n,i)
            out[(pat,Lfull)] = flag_p2(pat,m,Lc)
    return out

def all_function_order_bound(n):
    qs=[precompute_q(n,i) for i in range(n)]
    orders=list(permutations(range(n)))
    checked=0
    best=Fraction(-1)
    best_data=None
    for f in range(1<<(1<<n)):
        pats=[derivative_pattern(f,n,i) for i in range(n)]
        infl=[Fraction(p.bit_count(),1<<(n-1)) for p in pats]
        I=sum(infl,Fraction(0))
        beta=[min(a,1-a) for a in infl]
        J=sum(beta,Fraction(0))
        for pi in orders:
            source=Fraction(0)
            for pos,i in enumerate(pi):
                Lfull=0
                for j in pi[pos+1:]:
                    Lfull |= 1<<j
                source += qs[i][(pats[i],Lfull)]
            # theorem: source <= J <= I
            assert source <= J
            assert J <= I
            checked += 1
            if I and source/I > best:
                best=source/I
                best_data=(f,pi,I,J,source)
    return checked,best,best_data

def full_identity_checks(n):
    count=0
    hardy_count=0
    for f in range(1<<(1<<n)):
        for i in range(n):
            pat=derivative_pattern(f,n,i)
            m=n-1
            alpha=Fraction(pat.bit_count(),1<<m)
            beta=min(alpha,1-alpha)
            energies=walsh_energies(pat,m)
            E=sum(energies.values(),Fraction(0))
            assert E == alpha*(1-alpha)
            vals_T=[]
            vals_p2=[]
            for pi in permutations(range(n)):
                pos=pi.index(i)
                Lfull=0
                for j in pi[pos+1:]:
                    Lfull |= 1<<j
                Lc=compact_coords(Lfull,n,i)
                mean,rhs,T,a=exact_flag_formula(pat,m,Lc)
                # direct mean / second moment
                ws=[w for w in range(1<<m) if (w & ~Lc)==0]
                ps=[p_of_w(pat,m,w) for w in ws]
                direct_mean=sum(ps,Fraction(0))/len(ps)
                direct_p2=sum((p*p for p in ps),Fraction(0))/len(ps)
                assert direct_mean == mean
                assert direct_p2 == rhs
                # strengthened source payment
                assert direct_p2 <= 4*beta*T
                assert 4*beta*T <= beta
                vals_T.append(T)
                vals_p2.append(direct_p2)
                count += 1
            # random-order exact Hardy first-moment identity
            avgT=sum(vals_T,Fraction(0))/len(vals_T)
            hardy=sum(val*Fraction(U.bit_count(),U.bit_count()+1)
                      for U,val in energies.items())
            assert avgT == hardy
            hardy_count += 1
    return count,hardy_count

def sharp_example():
    # Boolean phase (-1)^(x0*x1); truth bit 1 means exponent 1 / sign -1.
    n=2
    f=0
    for x in range(1<<n):
        if ((x>>0)&1) and ((x>>1)&1):
            f |= 1<<x
    i=0
    pat=derivative_pattern(f,n,i)
    Lfull=1<<1
    Lc=compact_coords(Lfull,n,i)
    mean,rhs,T,a=exact_flag_formula(pat,n-1,Lc)
    alpha=Fraction(pat.bit_count(),2)
    beta=min(alpha,1-alpha)
    assert rhs == beta == Fraction(1,2)
    assert 4*T*T == Fraction(1,4)
    return {
        "alpha": str(alpha),
        "beta": str(beta),
        "T": str(T),
        "mean_p2": str(rhs),
        "ratio_to_beta": str(rhs/beta),
        "ratio_to_4T2": str(rhs/(4*T*T)),
    }

def main():
    identities={}
    for n in range(1,4):
        identities[str(n)] = dict(zip(
            ["flag_identity_cases","hardy_identity_cases"],
            full_identity_checks(n)
        ))
    exhaustive={}
    total=0
    for n in range(1,5):
        checked,best,data=all_function_order_bound(n)
        total += checked
        exhaustive[str(n)] = {
            "function_order_cases": checked,
            "max_source_over_I": str(best if best>=0 else Fraction(0)),
            "witness_truth_mask_hex": None if data is None else hex(data[0]),
            "witness_order": None if data is None else list(data[1]),
            "witness_I": None if data is None else str(data[2]),
            "witness_J": None if data is None else str(data[3]),
            "witness_source": None if data is None else str(data[4]),
        }
    out={
        "status":"PASS",
        "arithmetic":"exact Fraction",
        "identity_checks":identities,
        "exhaustive_source_bound_through_n4":exhaustive,
        "total_function_order_cases":total,
        "sharp_coordinate_example":sharp_example(),
        "notes":[
            "finite checks are falsification/self-check evidence, not the proof",
            "the coordinatewise constant one in E_flag p_i^2 <= beta_i is attained by (-1)^(x_i x_j)",
            "the stronger candidate E_flag p_i^2 <= 4 T_i^2 is refuted by the same example by factor 2"
        ]
    }
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
