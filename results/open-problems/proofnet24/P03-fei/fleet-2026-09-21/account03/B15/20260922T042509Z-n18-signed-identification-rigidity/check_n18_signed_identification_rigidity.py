#!/usr/bin/env python3
"""Exact/rigorous certificate for one-step signed-identification rigidity of the
source-valid n=18 FEI gate.

The finite part is exact: source reconstruction + SHA-256, all 306 pairwise
signed identifications x_b=x_a xor s, balance, integer edge counts, and integer
Walsh histograms. Entropy comparisons use exact Fraction arithmetic and an
explicit positive-tail bound for the atanh series of ln.

The inherited source entropy interval is from account01/B12's source-valid
n=18 certificate. Full FEI is not asserted.
"""
from fractions import Fraction
from collections import Counter
import hashlib
import numpy as np

SOURCE_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
H0_LO = Fraction(int("6776605309005978082519790221891882314787235038"), 10**45)
H0_HI = Fraction(int("6776605309005978082519790221891882314787235039"), 10**45)
CSTAR = Fraction(65218512, 10**7)
I0 = Fraction(261, 128)
TERMS = 48

CORE_BLOCKS = [
    0x0000000000000000, 0xfcfcccccf0f00000,
    0xfaaafaaaf000f000, 0xfefefeeef0f0f000,
    0xeeaacc00eeaacc00, 0xfefeccccfefacc00,
    0xfeaafeaafeaafc00, 0xfefefeeefefafc00,
]
PAIRS = [
    (78,79),(113,121),(228,484),(170,186),(149,151),
    (338,466),(284,316),(291,295),(393,457)
]
DIRS = [0,3,8,4,1,7,5,2,6]

def core_value(x):
    return -1 if ((CORE_BLOCKS[x >> 6] >> (x & 63)) & 1) else 1

def build_source():
    out = np.empty(1 << 18, dtype=np.int8)
    pair_of = {}
    for j,(a,b) in enumerate(PAIRS):
        pair_of[a]=j; pair_of[b]=j
    for idx in range(1 << 18):
        x=idx & 511
        y=idx >> 9
        j=pair_of.get(x)
        out[idx] = (-1 if ((y >> j) & 1) else 1) if j is not None else core_value(x)
    digest=hashlib.sha256(",".join(map(str,out.tolist())).encode()).hexdigest()
    assert digest == SOURCE_SHA
    assert int(out.sum()) == 0
    return out

def fwht(a):
    a=np.asarray(a,dtype=np.int64).copy()
    h=1
    while h<a.size:
        b=a.reshape(-1,2*h)
        x=b[:,:h].copy(); y=b[:,h:].copy()
        b[:,:h]=x+y; b[:,h:]=x-y
        h <<= 1
    return a

def influence_diff_sum(a):
    N=a.size
    k=(N.bit_length()-1)
    y=np.arange(N,dtype=np.uint32)
    total=0
    for j in range(k):
        lo=y[(y & (1<<j)) == 0]
        total += int(np.count_nonzero(a[lo] != a[lo | (1<<j)]))
    return total

def hist_tuple(a):
    W=fwht(a)
    return tuple(sorted(Counter(np.abs(W[W != 0]).tolist()).items()))

def pow2(k):
    return Fraction(1<<k,1) if k>=0 else Fraction(1,1<<(-k))

def normalize_pow2(x):
    k=x.numerator.bit_length()-x.denominator.bit_length()
    while x < pow2(k): k -= 1
    while x >= pow2(k+1): k += 1
    y=x/pow2(k)
    assert 1 <= y < 2
    return k,y

def ln_interval_unit(y):
    z=(y-1)/(y+1)
    if z == 0: return Fraction(0),Fraction(0)
    z2=z*z; zp=z; s=Fraction(0)
    for j in range(TERMS):
        if j: zp *= z2
        s += zp/(2*j+1)
    lo=2*s
    rem=2*z**(2*TERMS+1)/((2*TERMS+1)*(1-z2))
    return lo,lo+rem

def log2_interval(x):
    k,y=normalize_pow2(x)
    yl,yh=ln_interval_unit(y)
    l2l,l2h=ln_interval_unit(Fraction(2))
    return Fraction(k)+yl/l2h, Fraction(k)+yh/l2l

def entropy_interval(hist,N):
    lo=Fraction(0); hi=Fraction(0)
    for w,count in hist:
        p=Fraction(int(w)*int(w),N*N)
        ll,lh=log2_interval(1/p)
        lo += int(count)*p*ll
        hi += int(count)*p*lh
    return lo,hi

def decimal(x,d=18,ceil=False):
    s=10**d
    if ceil:
        q=(x.numerator*s+x.denominator-1)//x.denominator
    else:
        q=x.numerator*s//x.denominator
    return f"{q//s}.{q%s:0{d}d}"

def main():
    f=build_source()

    assert sorted(DIRS) == list(range(9))
    for j,(a,b) in enumerate(PAIRS):
        assert a ^ b == (1 << DIRS[j])
    for j in range(9):
        for l in range(j+1,9):
            outside=(PAIRS[j][0]^PAIRS[l][0]) & ~((1<<DIRS[j])|(1<<DIRS[l]))
            assert outside != 0

    ys=np.arange(1<<17,dtype=np.uint32)
    balanced=[]
    type_counts=Counter()
    exact_diff_target=133632

    for a in range(18):
        for b in range(a+1,18):
            low=ys & ((1<<b)-1)
            high=ys >> b
            base=low | (high << (b+1))
            abit=(base >> a) & 1
            for s in (0,1):
                idx=base | ((abit ^ s) << b)
                g=f[idx]
                if int(g.sum()) != 0:
                    continue
                diff=influence_diff_sum(g)
                assert diff == exact_diff_target
                ht=hist_tuple(g)
                if a>=9:
                    kind="host_host"
                elif b>=9 and (b-9) < 9 and DIRS[b-9] == a:
                    kind=f"matched_core_host_s{s}"
                else:
                    raise AssertionError(("unexpected balanced identification",a,b,s))
                type_counts[(kind,ht)] += 1
                balanced.append((a,b,s,kind,ht))

    assert len(balanced) == 90
    kind_totals=Counter(k for (k,_h),v in type_counts.items() for _ in range(v))
    assert kind_totals == Counter({
        "host_host":72,
        "matched_core_host_s0":9,
        "matched_core_host_s1":9,
    })
    assert len([x for x in type_counts if x[0]=="host_host"]) == 1
    assert len([x for x in type_counts if x[0]=="matched_core_host_s0"]) == 1
    assert len([x for x in type_counts if x[0]=="matched_core_host_s1"]) == 1

    fixed_balanced=0
    yfix=np.arange(1<<17,dtype=np.uint32)
    for q in range(18):
        low=yfix & ((1<<q)-1)
        high=yfix >> q
        base=low | (high << (q+1))
        for v in (0,1):
            idx=base | (np.uint32(v) << q)
            if int(f[idx].sum()) == 0:
                fixed_balanced += 1
    assert fixed_balanced == 0

    hh=[h for (k,h),v in type_counts.items() if k=="host_host"][0]
    ch0=[h for (k,h),v in type_counts.items() if k=="matched_core_host_s0"][0]
    ch1=[h for (k,h),v in type_counts.items() if k=="matched_core_host_s1"][0]
    N=1<<17
    Ehh=entropy_interval(hh,N)
    E0=entropy_interval(ch0,N)
    E1=entropy_interval(ch1,N)

    target_lo=H0_LO-Fraction(1,128)
    target_hi=H0_HI-Fraction(1,128)
    assert Ehh[0] >= target_lo and Ehh[1] <= target_hi
    assert E0[1] < target_lo
    assert E1[1] < target_lo

    R_lo=target_lo/(I0-1)
    R_hi=target_hi/(I0-1)
    assert R_hi < CSTAR

    print("PASS")
    print("source_sha256",SOURCE_SHA)
    print("signed_pair_identifications_checked",306)
    print("balanced_identifications",len(balanced))
    print("balanced_type_counts","host_host=72 matched_core_host_s0=9 matched_core_host_s1=9")
    print("all_balanced_influence","261/128")
    print("one_coordinate_fixings_checked",36)
    print("balanced_fixings",fixed_balanced)
    print("host_host_entropy_lower",decimal(Ehh[0],42))
    print("host_host_entropy_upper",decimal(Ehh[1],42,True))
    print("core_host_s0_entropy_upper",decimal(E0[1],30,True))
    print("core_host_s1_entropy_upper",decimal(E1[1],30,True))
    print("max_ratio_lower",decimal(R_lo,36))
    print("max_ratio_upper",decimal(R_hi,36,True))
    print("candidate_Cstar","6.5218512")
    print("candidate_gap_lower",decimal(CSTAR-R_hi,36))
    print("full_FEI","OPEN_NOT_PROVED")

if __name__=="__main__":
    main()
