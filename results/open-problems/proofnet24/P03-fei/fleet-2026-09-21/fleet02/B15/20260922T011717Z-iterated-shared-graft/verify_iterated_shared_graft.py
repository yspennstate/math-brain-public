#!/usr/bin/env python3
"""Rigorous verifier for the iterated shared-core graft FEI lower-bound update.

Consumes only source-certified entropy intervals for the 18-bit seed and the
162-bit shared graft. Reconstructs the seed's 9-bit core from the preserved
hex slices, proves the 162-bit graft's reusable core singleton coefficient,
certifies the new core entropy correction with rational atanh log bounds, and
checks the exact balanced-excess gain.

This verifies a finite Boolean construction; it is not a proof of FEI.
"""
from fractions import Fraction
from hashlib import sha256
import json

EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
 (TOP, BOT),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
 ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00", "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
 (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
 ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
 ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
 ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]
PIVOTS = [0, 3, 8, 4, 1, 7, 5, 2, 6]

H0_LO = Fraction("6.776605309005978082519790221891882314787235038")
H0_HI = Fraction("6.776605309005978082519790221891882314787235039")
H1_LO = Fraction("7.014850042680291613033104756310658624299893163")
H1_HI = Fraction("7.014850042680291613033104756310658624299893164")
I0 = Fraction(261, 128)
I1 = Fraction(68013, 32768)
W = Fraction(1, 256)
AWEIGHT = 9 * W

def fwht(a):
    a = list(map(int, a))
    h = 1
    while h < len(a):
        for s in range(0, len(a), 2*h):
            for j in range(h):
                x, y = a[s+j], a[s+j+h]
                a[s+j], a[s+j+h] = x+y, x-y
        h *= 2
    return a

def reconstruct():
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    seen = base
    hosts = []
    for m in masks:
        assert not (seen & m)
        assert m.bit_count() == 2
        seen |= m
        hosts.append([x for x in range(512) if (m >> x) & 1])
    core = [-1 if (base >> x) & 1 else 1 for x in range(512)]

    # Reproduce the source-bound 18-bit table hash.
    tab = []
    for state in range(1 << len(hosts)):
        row = core[:]
        for j, cells in enumerate(hosts):
            if state & (1 << j):
                for x in cells:
                    row[x] = -1
        tab.extend(row)
    got = sha256(",".join(map(str, tab)).encode()).hexdigest()
    assert got == EXPECTED_SHA
    assert sum(tab) == 0
    return core, hosts

def log2_integer_interval(n, terms=90):
    """Rigorous rational interval for log2(n), n a positive integer."""
    assert n >= 1
    if n == 1:
        return Fraction(0), Fraction(0)
    k = n.bit_length() - 1
    y = Fraction(n, 1 << k)  # in [1,2)
    z = (y - 1) / (y + 1)
    z2 = z*z
    s = Fraction(0)
    zp = z
    for m in range(terms):
        s += zp / (2*m + 1)
        zp *= z2
    ln_y_lo = 2*s
    ln_y_hi = ln_y_lo + 2*zp / ((2*terms + 1) * (1-z2))

    z = Fraction(1, 3)
    z2 = z*z
    s = Fraction(0)
    zp = z
    for m in range(terms):
        s += zp / (2*m + 1)
        zp *= z2
    ln2_lo = 2*s
    ln2_hi = ln2_lo + 2*zp / ((2*terms + 1) * (1-z2))
    return Fraction(k) + ln_y_lo/ln2_hi, Fraction(k) + ln_y_hi/ln2_lo

def entropy_sq_dyadic_interval(nums, denom_power, terms=90):
    """Bounds sum phi((m/2^denom_power)^2), phi(u)=-u log2 u."""
    cache = {}
    lo = Fraction(0)
    hi = Fraction(0)
    den2 = 1 << (2*denom_power)
    for raw in nums:
        m = abs(int(raw))
        if not m:
            continue
        if m not in cache:
            cache[m] = log2_integer_interval(m, terms)
        log_lo, log_hi = cache[m]
        q = Fraction(m*m, den2)
        lo += q * (2*denom_power - 2*log_hi)
        hi += q * (2*denom_power - 2*log_lo)
    return lo, hi

def decimal(fr, digits=60):
    # Deterministic decimal truncation/rounding is not used for decisions.
    sign = "-" if fr < 0 else ""
    fr = abs(fr)
    n, d = fr.numerator, fr.denominator
    whole, rem = divmod(n, d)
    out = [sign + str(whole), "."]
    for _ in range(digits):
        rem *= 10
        q, rem = divmod(rem, d)
        out.append(str(q))
    return "".join(out)

def main():
    core, hosts = reconstruct()
    assert hosts == [[78,79],[113,121],[228,484],[170,186],[149,151],
                     [338,466],[284,316],[291,295],[393,457]]

    a = core[:]
    for cells in hosts:
        for x in cells:
            a[x] = 0
    A_num = fwht(a)  # denominator 512

    Q_nums = []
    for cells, piv in zip(hosts, PIVOTS):
        q = [0]*512
        for x in cells:
            q[x] = 1 if ((x >> piv) & 1) == 0 else -1
        Q_nums.append(fwht(q))
    sumQ_num = [sum(Q_nums[j][s] for j in range(9)) for s in range(512)]

    # The 162-bit shared graft has nine equal outer-core singleton coefficients.
    singleton = []
    for k in range(9):
        s = 1 << k
        val = Fraction(A_num[s], 512) + W*Fraction(sumQ_num[s], 512)
        singleton.append(val)
    assert len(set(singleton)) == 1
    ell = singleton[0]
    assert ell == Fraction(14593, 65536)

    # Four-level disjoint self-composition of the 162-bit graft.
    depth = 4
    Ih = I1**depth
    delta_h = Ih - 1
    ent_mult = sum(I1**j for j in range(depth))
    b = ell**depth
    assert b.denominator == 1 << 64
    bnum = b.numerator

    # Core entropy correction K(b) for the outer 18-bit skeleton.
    # A + b sum Q has denominator 2^(9+64)=2^73.
    nums_b = [A_num[s]*(1 << 64) + sumQ_num[s]*bnum for s in range(512)]
    Hcb_lo, Hcb_hi = entropy_sq_dyadic_interval(nums_b, 73)
    Hc0_lo, Hc0_hi = entropy_sq_dyadic_interval(A_num, 9)
    logb_lo, logb_hi = log2_integer_interval(bnum)
    b2 = b*b
    phi_b_lo = b2 * (128 - 2*logb_hi)
    phi_b_hi = b2 * (128 - 2*logb_lo)
    K_lo = Hcb_lo - Hc0_hi - AWEIGHT*(phi_b_hi + 16*b2)
    K_hi = Hcb_hi - Hc0_lo - AWEIGHT*(phi_b_lo + 16*b2)
    assert K_lo > 0

    # Graft h into all nine hosts, sharing its distinguished leaf coordinate.
    # Dimension: 9 + 9*(162^4 - 1) = 9*162^4.
    n_h = 162**depth
    n_new = 9*n_h
    delta0 = I0 - 1
    delta1 = I1 - 1
    delta_new = delta0 + AWEIGHT*delta_h
    I_new = 1 + delta_new

    Hh_lo = ent_mult*H1_LO
    Hh_hi = ent_mult*H1_HI
    Hnew_lo = H0_LO + AWEIGHT*Hh_lo + K_lo
    Hnew_hi = H0_HI + AWEIGHT*Hh_hi + K_hi
    rho_new_lo = Hnew_lo/delta_new
    rho_new_hi = Hnew_hi/delta_new
    rho_old_lo = H1_LO/delta1
    rho_old_hi = H1_HI/delta1
    gain_lo = rho_new_lo - rho_old_hi
    assert gain_lo > 0

    out = {
        "source_truth_table_sha256": EXPECTED_SHA,
        "source_hosts": hosts,
        "reusable_core_singleton_exact": str(ell),
        "reusable_core_singleton_decimal": decimal(ell, 30),
        "self_composition_depth": depth,
        "gadget_dimension": n_h,
        "new_dimension": n_new,
        "gadget_influence_exact": str(Ih),
        "gadget_entropy_multiplier_exact": str(ent_mult),
        "shared_leaf_coefficient_exact": str(b),
        "core_correction_K_lower": decimal(K_lo, 75),
        "core_correction_K_upper": decimal(K_hi, 75),
        "new_influence_exact": str(I_new),
        "new_entropy_lower": decimal(Hnew_lo, 60),
        "new_entropy_upper": decimal(Hnew_hi, 60),
        "old_balanced_excess_lower": decimal(rho_old_lo, 60),
        "old_balanced_excess_upper": decimal(rho_old_hi, 60),
        "new_balanced_excess_lower": decimal(rho_new_lo, 60),
        "new_balanced_excess_upper": decimal(rho_new_hi, 60),
        "certified_gain_new_lower_minus_old_upper": decimal(gain_lo, 70),
        "checks": [
            "source n=18 truth-table SHA-256 matched",
            "nine host edges and pivots reconstructed",
            "162-bit graft outer-core singleton = 14593/65536 exactly",
            "four-level disjoint self-composition formulas used exactly",
            "K(b)>0 certified with rational atanh log intervals",
            "new balanced-excess lower endpoint exceeds old 162-bit upper endpoint"
        ]
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
