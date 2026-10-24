#!/usr/bin/env python3
"""
account03/B17 targeted exact-lattice adversary for the FEI gate candidate.

Gate B0 is the four-input Boolean gate with negative set
{0,1,2,3,4,5,8,10}. Inputs are indexed by the binary bits of 0..15,
least-significant bit first. We test the source-exact dyadic lattice

 P_12 = {1/2} union {2^-k, 1-2^-k : 2 <= k <= 12},

retaining exactly those tuples for which min(p_out,1-p_out) is also a
power of two. On these points the committed read-once base candidate
Gamma_0 is source-exact from the AND-chain equality.

All sign decisions below use mpmath interval arithmetic at 60 decimal
digits. The calculation is a finite certificate for this lattice only,
not a proof of the all-bias/all-gate FEI statement.
"""
from fractions import Fraction
import itertools, math
import mpmath as mp

mp.iv.dps = 60
iv = mp.iv
C0_STR = "6.4548"
C0 = iv.mpf(C0_STR)
LN2 = iv.log(iv.mpf(2))
NEG = {0,1,2,3,4,5,8,10}

def ivq(x):
    return iv.mpf(x.numerator) / x.denominator

def iv_h2(x):
    if float(x.b) <= 0.0 or float(x.a) >= 1.0:
        return iv.mpf(0)
    return -(x*iv.log(x) + (1-x)*iv.log(1-x)) / LN2

def iv_phi(w):
    lo = max(0.0, float(w.a))
    hi = min(1.0, float(w.b))
    if hi <= 0.0:
        return iv.mpf(0)
    if lo > 0.0:
        return -w*iv.log(w)/LN2
    # Exact-zero or tiny interval straddling zero. Bound phi on [0,hi].
    if hi <= 1.0/math.e:
        z = iv.mpf(hi)
        ub = -z*iv.log(z)/LN2
        return iv.mpf([0.0, float(ub.b)])
    return iv.mpf([0.0, 1.0/(math.e*math.log(2.0))])

def half_power_index(x):
    s = min(x, 1-x)
    if s <= 0 or s.numerator != 1:
        return None
    d = s.denominator
    if d & (d-1):
        return None
    return d.bit_length()-1

def gamma_dyadic(x):
    k = half_power_index(x)
    if k is None:
        raise ValueError("Gamma requested off the source-exact dyadic set")
    w = iv.mpf(2)**(2-2*k)
    w0 = (1-iv.mpf(2)**(1-k))**2
    H = iv_phi(w0) + (2**k-1)*iv_phi(w)
    I = iv.mpf(k)*iv.mpf(2)**(1-k)
    return C0*I-H

def output_mass(p):
    p0,p1,p2,p3 = p
    # x3=0 child: negative iff not(x1 and x2)
    # x3=1 child: negative iff (not x0) and (not x2)
    return (1-p3)*(1-p1*p2) + p3*(1-p0)*(1-p2)

def gate_intervals(p):
    coeff = [iv.mpf(0) for _ in range(16)]
    for x in range(16):
        prob = iv.mpf(1)
        basis = []
        for i,pf in enumerate(p):
            z = ivq(pf); q = 1-z
            bit = (x >> i) & 1
            prob *= z if bit else q
            basis.append(iv.sqrt(q/z) if bit else -iv.sqrt(z/q))
        f = -1 if x in NEG else 1
        for S in range(16):
            b = iv.mpf(1)
            for i in range(4):
                if (S >> i) & 1:
                    b *= basis[i]
            coeff[S] += prob*f*b

    mass = [a*a for a in coeff]
    H = sum((iv_phi(w) for w in mass), iv.mpf(0))
    It = [
        sum((mass[S] for S in range(16) if (S >> i) & 1), iv.mpf(0))
        for i in range(4)
    ]
    r = output_mass(p)
    rhs = iv.mpf(0)
    for pf,it in zip(p,It):
        z = ivq(pf)
        V = 4*z*(1-z)
        rhs += it*(gamma_dyadic(pf)+iv_h2(V))/V
    D = rhs-gamma_dyadic(r)-H
    I = sum(It, iv.mpf(0))
    rr = ivq(r)
    W = I/4-rr*(1-rr)
    return D,W,H,It

P = {Fraction(1,2)}
for k in range(2,13):
    a = Fraction(1,2**k)
    P.add(a); P.add(1-a)
P = sorted(P)

tested = 0
min_D_lo = None
max_c_hi = None
max_data = None
for p in itertools.product(P, repeat=4):
    r = output_mass(p)
    if half_power_index(r) is None:
        continue
    tested += 1
    D,W,H,It = gate_intervals(p)
    Dlo = float(D.a); Wlo = float(W.a)
    if not (Dlo > 0.0 and Wlo > 0.0):
        raise AssertionError(("uncertified tuple", p, r, D, W))
    c = -D/W
    chi = float(c.b)
    if min_D_lo is None or Dlo < min_D_lo:
        min_D_lo = Dlo
    if max_c_hi is None or chi > max_c_hi:
        max_c_hi = chi
        max_data = (p,r,D,W,c,H,It)

assert tested == 639
assert max_c_hi < 0.0

# Exact closed-form cross-check at one maximising symmetry representative.
mp.mp.dps = 80
C0mp = mp.mpf(C0_STR)
Dstar = (mp.mpf(5)/8)*C0mp - mp.mpf(51)/8 \
        + (mp.mpf(27)/64)*mp.log(3,2) + (mp.mpf(25)/32)*mp.log(5,2)
Wstar = mp.mpf(3)/32
cstar = -Dstar/Wstar

print("PASS B0 source-exact dyadic lattice")
print("lattice_input_values =", len(P))
print("source_exact_tuples =", tested)
print("minimum_certified_D_lower =", mp.nstr(min_D_lo, 18))
print("maximum_certified_c_upper =", mp.nstr(max_c_hi, 18))
print("maximizer_representative =", tuple(str(x) for x in max_data[0]))
print("maximizer_output =", str(max_data[1]))
print("exact_D_star =", mp.nstr(Dstar, 50))
print("exact_W_star =", mp.nstr(Wstar, 30))
print("exact_c_star =", mp.nstr(cstar, 50))
print("formula_D_star = (5/8)C0 - 51/8 + (27/64)log2(3) + (25/32)log2(5)")
print("FULL_FEI = OPEN")
