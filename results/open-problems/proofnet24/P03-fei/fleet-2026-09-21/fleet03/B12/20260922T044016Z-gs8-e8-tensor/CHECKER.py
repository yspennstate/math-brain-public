"""Rigorous E8 certificate for the full physical restriction closure of G_*.

This extends the fleet02/B16 GS8 existence certificate.  It reconstructs the
source-bound 10-input gate from the fleet03/B12 source, enumerates all 3^10
coordinate restrictions, and rigorously proves the aggregate spectral-edge
inequality

    sum_i L_i(F) <= 8 * ( I(F) - W_1(F) ) = 8 sum_i C_i(F).

Entropy comparisons use exact Walsh integers and rational log2 intervals.
This is a finite certificate for this source-bound restriction closure only;
the accompanying report proves tensor-product closure algebraically.
"""
from fractions import Fraction
from collections import Counter
from functools import lru_cache
from itertools import product
import hashlib, json

EXPECTED_PARENT_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
EXPECTED_WITNESS_SHA = "3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4"

TOP = "fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00"
BOT = "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"
SLICES = [
    (TOP, BOT),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fcfcccccf0f0c0000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf000f000fefeccccf0f000000000000000000000"),
    ("fefefefefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc00eeaacc00",
     "fefefefef0f0f000faaafaaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000feaafeaaf000f000fcfcccccf0f000000000000000000000"),
    (TOP, "fefefeeef0f0f000faaafaaaf0a0f000fcfcccccf0f000000000000000000000"),
    ("fefefeeefefefc00feaafeaafeaafc00fefeccccfefecc00eeaacc00eeaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00feaacc00feaacc00", BOT),
    ("fefefeeefefafc00feaafeaafeaafc00fefeccccfefacc00eeaacc88eeaacc00", BOT),
    ("fefefeeefefafe00feaafeaafeaafe00fefeccccfefacc00eeaacc00eeaacc00", BOT),
]
FIXED = {9:0, 10:0, 11:0, 12:1, 13:1, 14:0, 15:1, 16:1}
FREE = [0,1,2,3,4,5,6,7,8,17]


def reconstruct_parent():
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    seen = base
    hosts = []
    for mask in masks:
        assert mask.bit_count() == 2
        assert not (seen & mask)
        seen |= mask
        hosts.append([x for x in range(512) if (mask >> x) & 1])
    core = [-1 if (base >> x) & 1 else 1 for x in range(512)]
    table = []
    for y in range(512):
        row = core.copy()
        for j, cells in enumerate(hosts):
            if (y >> j) & 1:
                for x in cells:
                    row[x] = -1
        table.extend(row)
    digest = hashlib.sha256(",".join(map(str, table)).encode()).hexdigest()
    assert digest == EXPECTED_PARENT_SHA
    assert sum(table) == 0
    return table


def restrict_parent(parent):
    out = []
    base = sum(v << i for i, v in FIXED.items())
    for z in range(1 << len(FREE)):
        idx = base
        for j, i in enumerate(FREE):
            idx |= ((z >> j) & 1) << i
        out.append(parent[idx])
    digest = hashlib.sha256(",".join(map(str, out)).encode()).hexdigest()
    assert digest == EXPECTED_WITNESS_SHA
    return out


def fwht_int(a):
    a = list(a)
    h = 1
    while h < len(a):
        for start in range(0, len(a), 2*h):
            for j in range(start, start+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def restriction_truth(root, state):
    free = [i for i,s in enumerate(state) if s == 2]
    base = sum(s << i for i,s in enumerate(state) if s != 2)
    vals = []
    for mask in range(1 << len(free)):
        idx = base
        for j,i in enumerate(free):
            idx |= ((mask >> j) & 1) << i
        vals.append(root[idx])
    return vals, free


def ln2_interval(K=32):
    z = Fraction(1,3)
    S = Fraction(0)
    zp = z
    for k in range(K+1):
        S += zp / Fraction(2*k+1)
        zp *= z*z
    lo = 2*S
    hi = lo + 2*zp / Fraction(2*K+3) / (1-z*z)
    return lo, hi

LN2_LO, LN2_HI = ln2_interval()


@lru_cache(None)
def log2_inv_p_interval(absw, N):
    p = Fraction(absw*absw, N*N)
    if p.numerator == 1 and p.denominator & (p.denominator-1) == 0:
        e = Fraction(p.denominator.bit_length()-1)
        return e, e
    x = 1/p
    n,d = x.numerator, x.denominator
    e = n.bit_length() - d.bit_length()
    if e >= 0:
        while Fraction(1 << e, 1) > x: e -= 1
        while Fraction(1 << (e+1), 1) <= x: e += 1
        tw = Fraction(1 << e, 1)
    else:
        while Fraction(1, 1 << (-e)) > x: e -= 1
        while Fraction(1, 1 << (-(e+1))) <= x: e += 1
        tw = Fraction(1, 1 << (-e))
    y = x/tw
    assert 1 <= y < 2
    z = (y-1)/(y+1)
    K = 20
    S = Fraction(0)
    zp = z
    for k in range(K+1):
        S += zp / Fraction(2*k+1)
        zp *= z*z
    lo = 2*S
    hi = lo + (2*zp/Fraction(2*K+3)/(1-z*z) if z else 0)
    return Fraction(e)+lo/LN2_HI, Fraction(e)+hi/LN2_LO


@lru_cache(None)
def entropy_hist_interval(N, hist):
    lo = Fraction(0)
    hi = Fraction(0)
    for absw, count in hist:
        p = Fraction(absw*absw, N*N)
        llo, lhi = log2_inv_p_interval(absw, N)
        lo += count*p*llo
        hi += count*p*lhi
    return lo, hi


def state_stats(root, state):
    vals, free = restriction_truth(root, state)
    W = fwht_int(vals)
    N = len(vals)
    den = N*N
    hist = tuple(sorted(Counter(abs(w) for w in W if w).items()))
    Hlo, Hhi = entropy_hist_interval(N, hist)
    I_num = sum(s.bit_count()*w*w for s,w in enumerate(W))
    W1_num = sum(W[1 << j]**2 for j in range(len(free)))
    Csum = Fraction(I_num-W1_num, den)
    return Hlo, Hhi, Csum, len(free)


def dec_lo(q, digits=15):
    z = q.numerator*10**digits // q.denominator
    return f"{z//10**digits}.{z%10**digits:0{digits}d}"


def dec_hi(q, digits=15):
    z = (q.numerator*10**digits + q.denominator-1)//q.denominator
    return f"{z//10**digits}.{z%10**digits:0{digits}d}"


def main():
    root = restrict_parent(reconstruct_parent())
    states = list(product(range(3), repeat=10))
    data = {state: state_stats(root, state) for state in states}

    negative = 0
    equality = 0
    equality_positive_bank = 0
    min_positive = None
    min_positive_state = None
    max_ratio_lo = None
    max_ratio_hi = None
    max_ratio_state = None

    for state, (Hlo,Hhi,Csum,m) in data.items():
        child_lo = Fraction(0)
        child_hi = Fraction(0)
        for i,s in enumerate(state):
            if s != 2:
                continue
            a = list(state); a[i] = 0
            b = list(state); b[i] = 1
            child_lo += data[tuple(a)][0] + data[tuple(b)][0]
            child_hi += data[tuple(a)][1] + data[tuple(b)][1]
        # Lsum = sum_i [H(F) - (H(F_i0)+H(F_i1))/2].
        Llo = m*Hlo - child_hi/2
        Lhi = m*Hhi - child_lo/2
        Rlo = 8*Csum - Lhi
        Rhi = 8*Csum - Llo
        if Rhi < 0:
            negative += 1
        assert Rlo >= 0, (state, Rlo, Rhi)
        if Rlo == 0 and Rhi == 0:
            equality += 1
            if Csum > 0:
                equality_positive_bank += 1
        elif Rlo > 0 and (min_positive is None or Rlo < min_positive):
            min_positive = Rlo
            min_positive_state = state
        if Csum > 0:
            qlo, qhi = Llo/Csum, Lhi/Csum
            if max_ratio_lo is None or qlo > max_ratio_lo:
                max_ratio_lo, max_ratio_hi, max_ratio_state = qlo, qhi, state

    assert negative == 0
    assert equality == 41904
    assert equality_positive_bank == 9888
    assert max_ratio_lo == 8 and max_ratio_hi == 8
    assert min_positive > Fraction(46,100)

    root_state = (2,)*10
    Hlo,Hhi,Csum,m = data[root_state]
    child_lo = child_hi = Fraction(0)
    for i in range(10):
        a=list(root_state); a[i]=0
        b=list(root_state); b[i]=1
        child_lo += data[tuple(a)][0]+data[tuple(b)][0]
        child_hi += data[tuple(a)][1]+data[tuple(b)][1]
    Llo = 10*Hlo-child_hi/2
    Lhi = 10*Hhi-child_lo/2
    Rlo = 8*Csum-Lhi
    Rhi = 8*Csum-Llo

    out = {
      "status":"PASS",
      "witness_sha256":EXPECTED_WITNESS_SHA,
      "restrictions_checked":3**10,
      "e8_negative_states":negative,
      "e8_exact_equality_states":equality,
      "e8_equality_states_with_positive_bank":equality_positive_bank,
      "max_Lsum_over_Csum_exact":"8",
      "max_ratio_state":"".join(map(str,max_ratio_state)),
      "strict_min_positive_E8_residual_lower":dec_lo(min_positive,15),
      "strict_min_positive_state":"".join(map(str,min_positive_state)),
      "root_Csum_I_minus_W1":str(Csum),
      "root_Lsum_lower":dec_lo(Llo,15),
      "root_Lsum_upper":dec_hi(Lhi,15),
      "root_E8_residual_lower":dec_lo(Rlo,15),
      "root_E8_residual_upper":dec_hi(Rhi,15),
      "root_Lsum_over_Csum_lower":dec_lo(Llo/Csum,15),
      "root_Lsum_over_Csum_upper":dec_hi(Lhi/Csum,15),
      "interpretation":"Every physical coordinate restriction of G_* satisfies aggregate E8; equality with positive bank occurs only on the same essential-arity-two AND/OR-type layer identified by the peer GS8 checker. Full FEI is not proved."
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
