#!/usr/bin/env python3
"""Rigorous checker for one asymmetric arity-5 FEI gate slice.

Inputs X_0,...,X_3 are unbiased; P[X_4=1]=1/4.
We enumerate every Boolean gate with output event probability 1/8.
Writing A_b for negative points in the X_4=b slice, this means
3|A_0|+|A_1|=8, hence (|A_0|,|A_1|)=(0,8),(1,5),(2,2).

For the read-once base potential Gamma_RO with Gamma_RO(1/2)=6.4548
and its exact dyadic AND-chain values, the checker proves D_Gamma>=0
for all such gates.  It also proves that every gate depending on all
five inputs satisfies c_G <= -0.72768 for the base margin.

All logarithmic sign decisions use exact rational atanh-series
enclosures; float arithmetic is not used for certification.
"""
from itertools import combinations
from fractions import Fraction
from collections import Counter, defaultdict

C0 = Fraction(16137, 2500)
ACTIVE_RATIO = Fraction(2274, 3125)
DEN = 4096

def walsh_slice(neg):
    neg = set(neg)
    out = []
    for s in range(16):
        z = 0
        for x in range(16):
            f = -1 if x in neg else 1
            chi = -1 if ((s & x).bit_count() & 1) else 1
            z += f * chi
        out.append(z)
    return tuple(out)

def ln_unit_interval(y, terms=18):
    if y == 1:
        return Fraction(0), Fraction(0)
    z = (y - 1) / (y + 1)
    assert 0 < z <= Fraction(1,3)
    p = Fraction(0)
    zz = z
    z2 = z*z
    for j in range(terms):
        p += Fraction(2, 2*j+1) * zz
        zz *= z2
    first = z ** (2*terms+1)
    rem = Fraction(2, 2*terms+1) * first / (1-z2)
    return p, p + rem

_L2_LO, _L2_HI = ln_unit_interval(Fraction(2), 24)

def log2_int_interval(n):
    assert n >= 1
    if n & (n-1) == 0:
        return Fraction(n.bit_length()-1), Fraction(n.bit_length()-1)
    k = n.bit_length()-1
    y = Fraction(n, 1 << k)
    ly_lo, ly_hi = ln_unit_interval(y, 24)
    return Fraction(k) + ly_lo/_L2_HI, Fraction(k) + ly_hi/_L2_LO

_LOG_CACHE = {}
def log2i(n):
    if n not in _LOG_CACHE:
        _LOG_CACHE[n] = log2_int_interval(n)
    return _LOG_CACHE[n]

def signature_data(u0,u1):
    n0=[]; n5=[]
    for s in range(16):
        n0.append((3*u0[s]+u1[s])**2)
        n5.append(3*(u1[s]-u0[s])**2)
    assert sum(n0)+sum(n5) == DEN
    bnum=sum(n5)
    anum=sum(s.bit_count()*(n0[s]+n5[s]) for s in range(16))
    its=[sum(n0[s]+n5[s] for s in range(16) if (s>>i)&1) for i in range(4)]
    its.append(bnum)
    masses=tuple(sorted(n for n in n0+n5 if n))
    return anum,bnum,tuple(its),masses

_BLOCKS=[]
for size in (2,3,4):
    for inds in combinations(range(5),size):
        Ainds=tuple(inds)
        Binds=tuple(i for i in range(5) if i not in Ainds)
        pairs=[]
        for x in range(32):
            ai=sum(((x>>i)&1)<<j for j,i in enumerate(Ainds))
            bi=sum(((x>>i)&1)<<j for j,i in enumerate(Binds))
            pairs.append((ai,bi))
        _BLOCKS.append((1<<size,1<<(5-size),tuple(pairs)))

def truth_table(neg0,neg1):
    tt=0
    for x in neg0:
        tt |= 1<<x
    for x in neg1:
        tt |= 1<<(16+x)
    return tt

def composition_prime(tt):
    for i in range(5):
        if all(((tt>>x)&1)==((tt>>(x^(1<<i)))&1) for x in range(32)):
            return False
    for na,nb,pairs in _BLOCKS:
        rows=[0]*na
        for x,(ai,bi) in enumerate(pairs):
            if (tt>>x)&1:
                rows[ai] |= 1<<bi
        if len(set(rows))<=2:
            return False
    return True

def factor_2_3(n):
    a=b=0
    while n%2==0:
        a+=1;n//=2
    while n%3==0:
        b+=1;n//=3
    return a,b,n

def symbolic_D_if_23(anum,bnum,masses):
    rat = C0*(Fraction(anum,DEN)+Fraction(4*bnum,3*DEN)-Fraction(3,4))-8
    l3 = -Fraction(bnum,DEN)-Fraction(9,8)
    for n,cnt in Counter(masses).items():
        a,b,rest=factor_2_3(n)
        if rest != 1:
            return None
        rat += Fraction(cnt*n*a,DEN)
        l3 += Fraction(cnt*n*b,DEN)
    return rat,l3

def d_interval(anum,bnum,masses):
    t = Fraction(anum,DEN)+Fraction(4*bnum,3*DEN)-Fraction(3,4)
    lo = hi = C0*t - 8
    for n,cnt in Counter(masses).items():
        l,u=log2i(n)
        lo += Fraction(cnt*n,DEN)*l
        hi += Fraction(cnt*n,DEN)*u
    l3,u3=log2i(3)
    coef=Fraction(bnum,DEN)+Fraction(9,8)
    lo -= coef*u3
    hi -= coef*l3
    return lo,hi

def decimal_string(q, digits=18):
    sign='-' if q<0 else ''
    q=abs(q)
    scale=10**digits
    z=(q.numerator*scale)//q.denominator
    return f"{sign}{z//scale}.{z%scale:0{digits}d}"

cache={}
for k in (0,1,2,5,8):
    cache[k]=[(c,walsh_slice(c)) for c in combinations(range(16),k)]

counts=defaultdict(int)
sig_mult=Counter()
active_sig_mult=Counter()
prime_sig_mult=Counter()

for a0,a1 in ((0,8),(1,5),(2,2)):
    for neg0,u0 in cache[a0]:
        for neg1,u1 in cache[a1]:
            counts[(a0,a1)] += 1
            anum,bnum,its,masses=signature_data(u0,u1)
            sig=(anum,bnum,masses)
            sig_mult[sig]+=1
            if all(x>0 for x in its):
                active_sig_mult[sig]+=1
            if composition_prime(truth_table(neg0,neg1)):
                prime_sig_mult[sig]+=1

assert counts[(0,8)] == 12870
assert counts[(1,5)] == 69888
assert counts[(2,2)] == 14400
assert sum(counts.values()) == 97158
assert len(sig_mult) == 73
assert sum(active_sig_mult.values()) == 96562
assert len(active_sig_mult) == 66
assert sum(prime_sig_mult.values()) == 73016
assert len(prime_sig_mult) == 43

zero_sigs=set()
min_nonzero_lo=None
min_active_gap_lo=None
for sig,mult in sig_mult.items():
    anum,bnum,masses=sig
    sym=symbolic_D_if_23(anum,bnum,masses)
    if sym is not None and sym==(Fraction(0),Fraction(0)):
        zero_sigs.add(sig)
        continue
    lo,hi=d_interval(anum,bnum,masses)
    assert lo > 0
    if min_nonzero_lo is None or lo<min_nonzero_lo:
        min_nonzero_lo=lo

assert len(zero_sigs)==2
assert sum(sig_mult[s] for s in zero_sigs)==40

zero_count_geometric=0
for neg0,u0 in cache[0]:
    for neg1,u1 in cache[8]:
        sig=signature_data(u0,u1)
        key=(sig[0],sig[1],sig[3])
        if key in zero_sigs:
            ok=any(all(((x>>i)&1)==b for x in neg1) for i in range(4) for b in (0,1))
            assert ok
            zero_count_geometric+=1
for neg0,u0 in cache[2]:
    for neg1,u1 in cache[2]:
        sig=signature_data(u0,u1)
        key=(sig[0],sig[1],sig[3])
        if key in zero_sigs:
            assert neg0==neg1
            x,y=neg0
            assert (x^y).bit_count()==1
            zero_count_geometric+=1
assert zero_count_geometric==40

tight_active=0
for sig,mult in active_sig_mult.items():
    anum,bnum,masses=sig
    W=Fraction(anum+bnum,4*DEN)-Fraction(7,64)
    assert W>0
    sym=symbolic_D_if_23(anum,bnum,masses)
    if sym is not None and sym[1]==0:
        D_exact=sym[0]
        gap=D_exact-ACTIVE_RATIO*W
        if gap==0:
            tight_active += mult
        else:
            assert gap>0
    else:
        lo,_=d_interval(anum,bnum,masses)
        gap=lo-ACTIVE_RATIO*W
        assert gap>0
assert tight_active==192

tight_verified=False
for sig in active_sig_mult:
    anum,bnum,masses=sig
    W=Fraction(anum+bnum,4*DEN)-Fraction(7,64)
    sym=symbolic_D_if_23(anum,bnum,masses)
    if sym is not None and sym[1]==0 and sym[0]-ACTIVE_RATIO*W==0:
        assert sym[0] == (C0-6)/8
        assert W == Fraction(5,64)
        tight_verified=True
assert tight_verified

RPR_RAT=Fraction(2387,1250)
RPR_L3=Fraction(9,4)
l3lo,l3hi=log2i(3)
rpr_lo=RPR_RAT+RPR_L3*l3lo
rpr_hi=RPR_RAT+RPR_L3*l3hi
prime_tight=0
for sig,mult in prime_sig_mult.items():
    anum,bnum,masses=sig
    W=Fraction(anum+bnum,4*DEN)-Fraction(7,64)
    assert W>0
    sym=symbolic_D_if_23(anum,bnum,masses)
    if sym is not None:
        rat,l3c=sym
        grat=rat-W*RPR_RAT
        gl3=l3c-W*RPR_L3
        if grat==0 and gl3==0:
            prime_tight += mult
            continue
    dlo,_=d_interval(anum,bnum,masses)
    assert dlo-W*rpr_hi>0
assert prime_tight==2000

tight_prime_verified=False
for sig in prime_sig_mult:
    anum,bnum,masses=sig
    W=Fraction(anum+bnum,4*DEN)-Fraction(7,64)
    sym=symbolic_D_if_23(anum,bnum,masses)
    if sym==(Fraction(2387,10000),Fraction(9,32)) and W==Fraction(1,8):
        tight_prime_verified=True
assert tight_prime_verified

A_STAR=Fraction(167628,625000)
assert A_STAR == Fraction(2682048,10_000_000)
min_lift_lo=None
for sig,mult in sig_mult.items():
    anum,bnum,masses=sig
    W=Fraction(anum+bnum,4*DEN)-Fraction(7,64)
    assert W>=0
    sym=symbolic_D_if_23(anum,bnum,masses)
    if sym is not None and sym[1]==0:
        lo=sym[0]+A_STAR*W
        assert lo>0
    else:
        dlo,_=d_interval(anum,bnum,masses)
        lo=dlo+A_STAR*W
        assert lo>0
    if min_lift_lo is None or lo<min_lift_lo:
        min_lift_lo=lo

print("PASS asymmetric dyadic-spine slice")
print("gates_total",sum(counts.values()))
print("case_counts",dict(counts))
print("unique_exact_signatures",len(sig_mult))
print("all_five_inputs_active_gates",sum(active_sig_mult.values()))
print("active_signatures",len(active_sig_mult))
print("composition_prime_gates",sum(prime_sig_mult.values()))
print("composition_prime_signatures",len(prime_sig_mult))
print("base_zero_gates",sum(sig_mult[s] for s in zero_sigs))
print("base_zero_signatures",len(zero_sigs))
print("zero_geometry","8 biased-AND2 halfcubes + 32 unbiased-AND3 edges")
print("min_nonzero_D_lower",decimal_string(min_nonzero_lo,18))
print("essential_margin_upper","-"+decimal_string(ACTIVE_RATIO,18))
print("essential_tight_gate_count",tight_active)
print("prime_margin_upper_exact","-(2387/1250+(9/4)log2(3))")
print("prime_margin_upper_interval","["+decimal_string(-rpr_hi,18)+","+decimal_string(-rpr_lo,18)+"]")
print("prime_tight_gate_count",prime_tight)
print("tight_D",decimal_string((C0-6)/8,18))
print("tight_W",decimal_string(Fraction(5,64),18))
print("min_lifted_D_lower",decimal_string(min_lift_lo,18))
print("candidate","LIMIT-PRIME-GATE-LIFT-v1")
print("status","SLICE_CERTIFIED_FULL_FEI_OPEN")
