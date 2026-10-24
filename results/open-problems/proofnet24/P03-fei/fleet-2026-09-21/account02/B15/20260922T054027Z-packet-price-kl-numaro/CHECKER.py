"""Exact-source checker for B15 packet/price KL payment on the Numaro gate.

Reconstructs the 18-variable balanced Numaro Boolean seed from the committed
source slices, checks its truth-table hash, computes the exact integer Walsh
spectrum, level law and influences, and encloses every logarithm rigorously by
rational atanh series.

Source-specific conclusions (not unrestricted FEI):
  C_coll/(I-1) > 4.7677;
  (H-H(K))/(I-1) > 4.5829;
  D_level/(I-1) > 0.1848;
  magnitude-packet KL/(I-1) > 0.1527;
  the remaining original-coordinate price-within-packet KL/(I-1) > 0.03213.
At live center C*=6.5218512, the credit-free collision proxy is negative by
>0.18484(I-1), magnitude packets alone remain negative by >0.03213(I-1),
but packet + original-coordinate price KL recovers the exact positive margin.
"""
from fractions import Fraction
from collections import Counter, defaultdict
import hashlib

EXPECTED_SHA = "f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839"
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
LOG_TERMS = 26
CSTAR = Fraction(65218512, 10_000_000)


def reconstruct_seed():
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
    assert digest == EXPECTED_SHA
    assert sum(table) == 0
    return table


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


def pow2(k):
    return Fraction(1 << k, 1) if k >= 0 else Fraction(1, 1 << (-k))


def normalize_pow2(x):
    assert x > 0
    k = x.numerator.bit_length() - x.denominator.bit_length()
    while x < pow2(k):
        k -= 1
    while x >= pow2(k+1):
        k += 1
    y = x / pow2(k)
    assert 1 <= y < 2
    return k, y


def ln_interval_unit(y, terms=LOG_TERMS):
    assert 1 <= y <= 2
    z = (y-1)/(y+1)
    if z == 0:
        return Fraction(0), Fraction(0)
    z2 = z*z
    zp = z
    partial = Fraction(0)
    for r in range(terms):
        if r:
            zp *= z2
        partial += zp/(2*r+1)
    lo = 2*partial
    rem = 2*z**(2*terms+1)/((2*terms+1)*(1-z2))
    return lo, lo+rem


def log2_interval(x):
    k, y = normalize_pow2(x)
    yl, yh = ln_interval_unit(y)
    l2l, l2h = ln_interval_unit(Fraction(2))
    return Fraction(k) + yl/l2h, Fraction(k) + yh/l2l


def dec_bounds(lo, hi, digits=12):
    scale = 10**digits
    flo = (lo.numerator*scale)//lo.denominator
    fhi = -((-hi.numerator*scale)//hi.denominator)
    def fmt(q):
        sign = "-" if q < 0 else ""
        a = abs(q)
        return f"{sign}{a//scale}.{a%scale:0{digits}d}"
    return fmt(flo), fmt(fhi)


def kl_interval(act_uncond, ref_cond, Wk):
    loT = hiT = Fraction(0)
    for key, mass in act_uncond.items():
        k = key[0]
        pa = mass/Wk[k]
        rv = ref_cond(key)
        assert pa > 0 and rv > 0
        lo, hi = log2_interval(pa/rv)
        loT += mass*lo
        hiT += mass*hi
    return loT, hiT


def main():
    table = reconstruct_seed()
    W = fwht_int(table)
    N = len(W)
    N2 = N*N
    assert N == 1 << 18
    assert sum(w*w for w in W) == N2

    level_num = [0]*19
    inf_num = [0]*18
    hist = Counter()
    for s, w in enumerate(W):
        ww = w*w
        if ww == 0:
            continue
        hist[abs(w)] += 1
        level_num[s.bit_count()] += ww
        for i in range(18):
            if (s >> i) & 1:
                inf_num[i] += ww

    Wk = [Fraction(x, N2) for x in level_num]
    j = [Fraction(x, N2) for x in inf_num]
    assert j[:9] == [Fraction(57,256)]*9
    assert j[9:] == [Fraction(1,256)]*9
    I = sum(j)
    beta = I-1
    assert I == Fraction(261,128)
    assert beta == Fraction(133,128)

    expected_levels = {
        1: Fraction(14625,32768), 2: Fraction(2187,8192),
        3: Fraction(651,4096), 4: Fraction(675,8192),
        5: Fraction(441,16384), 6: Fraction(105,8192),
        7: Fraction(9,2048), 8: Fraction(9,8192),
        9: Fraction(5,32768),
    }
    assert {k:w for k,w in enumerate(Wk) if w} == expected_levels

    e = [Fraction(0)]*19
    e[0] = Fraction(1)
    for x in j:
        for k in range(18,0,-1):
            e[k] += e[k-1]*x
    q = [x/I for x in j]
    eq = [Fraction(1)] + [e[k]/(I**k) for k in range(1,19)]

    Clo = Chi = Fraction(0)
    for x in j:
        lo, hi = log2_interval(1/x)
        Clo += x*lo
        Chi += x*hi
    for k, wk in enumerate(Wk):
        if k and wk:
            lo, hi = log2_interval(e[k])
            Clo += wk*lo
            Chi += wk*hi

    Hlo = Hhi = Fraction(0)
    for aw, count in hist.items():
        p = Fraction(aw*aw, N2)
        lo, hi = log2_interval(1/p)
        mass = Fraction(count*aw*aw, N2)
        Hlo += mass*lo
        Hhi += mass*hi
    HKlo = HKhi = Fraction(0)
    for wk in Wk:
        if wk:
            lo, hi = log2_interval(1/wk)
            HKlo += wk*lo
            HKhi += wk*hi

    cond_lo, cond_hi = Hlo-HKhi, Hhi-HKlo
    Dlo, Dhi = Clo-cond_hi, Chi-cond_lo

    count_pp = Counter()
    count_p = Counter()
    act_pp = defaultdict(Fraction)
    act_p = defaultdict(Fraction)
    Cmask = (1 << 9)-1
    for s, w in enumerate(W):
        k = s.bit_count()
        if k == 0 or not Wk[k]:
            continue
        aw = abs(w)
        c = (s & Cmask).bit_count()
        count_pp[(k,aw,c)] += 1
        count_p[(k,aw)] += 1
        if w:
            mass = Fraction(w*w, N2)
            act_pp[(k,aw,c)] += mass
            act_p[(k,aw)] += mass

    qC, qA = q[0], q[9]
    def ref_pp(key):
        k, aw, c = key
        return Fraction(count_pp[key])*(qC**c)*(qA**(k-c))/eq[k]
    def ref_p(key):
        k, aw = key
        total = Fraction(0)
        for c in range(max(0,k-9), min(9,k)+1):
            cnt = count_pp.get((k,aw,c), 0)
            if cnt:
                total += Fraction(cnt)*(qC**c)*(qA**(k-c))/eq[k]
        return total

    Dpp_lo, Dpp_hi = kl_interval(act_pp, ref_pp, Wk)
    Dp_lo, Dp_hi = kl_interval(act_p, ref_p, Wk)
    Dwithin_lo, Dwithin_hi = Dpp_lo-Dp_hi, Dpp_hi-Dp_lo

    assert Dpp_lo <= Dhi and Dlo <= Dpp_hi
    assert Dpp_lo-Dlo < Fraction(1,10**20)
    assert Dhi-Dpp_hi < Fraction(1,10**20)

    c_ratio = (Clo/beta, Chi/beta)
    hcond_ratio = (cond_lo/beta, cond_hi/beta)
    d_ratio = (Dlo/beta, Dhi/beta)
    dp_ratio = (Dp_lo/beta, Dp_hi/beta)
    dwithin_ratio = (Dwithin_lo/beta, Dwithin_hi/beta)

    live_lo, live_hi = CSTAR-Hhi/beta, CSTAR-Hlo/beta
    creditless_lo = CSTAR-HKhi/beta-Chi/beta
    creditless_hi = CSTAR-HKlo/beta-Clo/beta
    packetonly_lo = creditless_lo + Dp_lo/beta
    packetonly_hi = creditless_hi + Dp_hi/beta

    assert c_ratio[0] > Fraction(47677,10000)
    assert hcond_ratio[0] > Fraction(45829,10000)
    assert d_ratio[0] > Fraction(1848,10000)
    assert dp_ratio[0] > Fraction(1527,10000)
    assert dwithin_ratio[0] > Fraction(3213,100000)
    assert creditless_hi < -Fraction(18484,100000)
    assert packetonly_hi < -Fraction(3213,100000)
    assert live_lo > Fraction(5,1_000_000)

    print("PASS")
    print("truth_table_sha256", EXPECTED_SHA)
    print("I", f"{I.numerator}/{I.denominator}")
    print("beta", f"{beta.numerator}/{beta.denominator}")
    print("influence_classes", "57/256 x9 ; 1/256 x9")
    print("level_law", ";".join(f"{k}:{w.numerator}/{w.denominator}" for k,w in enumerate(Wk) if w))
    print("Ccoll_over_beta_bounds", *dec_bounds(*c_ratio))
    print("HminusHK_over_beta_bounds", *dec_bounds(*hcond_ratio))
    print("Dlevel_over_beta_bounds", *dec_bounds(*d_ratio))
    print("magnitude_packet_KL_over_beta_bounds", *dec_bounds(*dp_ratio))
    print("price_within_packet_KL_over_beta_bounds", *dec_bounds(*dwithin_ratio))
    print("live_margin_over_beta_bounds", *dec_bounds(live_lo, live_hi, 15))
    print("creditless_margin_over_beta_bounds", *dec_bounds(creditless_lo, creditless_hi))
    print("packet_only_margin_over_beta_bounds", *dec_bounds(packetonly_lo, packetonly_hi))
    print("coefficient4_collision_candidate", "REFUTED_ON_THIS_BOOLEAN_SOURCE")
    print("coefficient4_even_with_full_level_KL_refund", "REFUTED_ON_THIS_BOOLEAN_SOURCE")
    print("packet_plus_coordinate_price_KL", "EXACTLY_RECOVERS_LEVEL_MISMATCH_CREDIT")


if __name__ == "__main__":
    main()
