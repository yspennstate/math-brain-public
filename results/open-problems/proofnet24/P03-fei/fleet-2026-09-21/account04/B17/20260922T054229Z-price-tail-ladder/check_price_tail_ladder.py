"""Exact checker: Boolean adversary to one-tail price KL and tail-ladder replacement.

Standard library only.  Two tasks:
  (1) verify a balanced 4-bit Boolean gate whose three-price packet proves that
      one monotone binary price tail does not preserve the packet/price KL;
  (2) reconstruct the exact 18-bit Numaro source and verify that, for that live
      source, all nonzero price-within-magnitude KL is carried by exactly three
      two-price packets, so one binary price hazard in each packet recovers the
      entire indispensable price credit.
"""
from fractions import Fraction
from collections import Counter, defaultdict
import hashlib

LOG_TERMS = 32
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
    return Fraction(k)+yl/l2h, Fraction(k)+yh/l2l


def kl_interval(P, Q):
    """Binary/categorical KL(P||Q), exact rational probabilities."""
    lo = hi = Fraction(0)
    assert sum(P) == 1 and sum(Q) == 1 and len(P) == len(Q)
    for p, q in zip(P, Q):
        if p == 0:
            continue
        assert q > 0
        l, h = log2_interval(p/q)
        lo += p*l
        hi += p*h
    return lo, hi


def scale_iv(a, x):
    assert a >= 0
    return a*x[0], a*x[1]


def add_iv(a, b):
    return a[0]+b[0], a[1]+b[1]


def dec_bounds(lo, hi, digits=15):
    scale = 10**digits
    flo = (lo.numerator*scale)//lo.denominator
    fhi = -((-hi.numerator*scale)//hi.denominator)
    def fmt(q):
        sign = "-" if q < 0 else ""
        q = abs(q)
        return f"{sign}{q//scale}.{q%scale:0{digits}d}"
    return fmt(flo), fmt(fhi)


def four_bit_adversary():
    minus = {0,1,2,3,4,5,10,15}
    vals = [-1 if x in minus else 1 for x in range(16)]
    assert sum(vals) == 0
    W = fwht_int(vals)
    assert W == [0,0,0,0,-4,-4,4,4,-8,0,-8,0,-4,4,4,-4]
    N2 = 16*16
    inf = []
    for i in range(4):
        inf.append(Fraction(sum(w*w for s,w in enumerate(W) if (s>>i)&1), N2))
    assert inf == [Fraction(1,4), Fraction(1,2), Fraction(1,2), Fraction(3,4)]
    I = sum(inf)
    assert I == 2
    q = [x/I for x in inf]
    assert q == [Fraction(1,8), Fraction(1,4), Fraction(1,4), Fraction(3,8)]

    rows = []
    for s,w in enumerate(W):
        if s.bit_count() == 2 and abs(w) == 4:
            price = Fraction(1)
            for i in range(4):
                if (s>>i)&1:
                    price *= q[i]
            rows.append((s, w, price))
    assert rows == [(5,-4,Fraction(1,32)), (6,4,Fraction(1,16)), (12,-4,Fraction(3,32))]

    P = [Fraction(1,3)]*3
    Q = [Fraction(1,6), Fraction(1,3), Fraction(1,2)]
    full = kl_interval(P,Q)
    low = kl_interval([Fraction(1,3),Fraction(2,3)], [Fraction(1,6),Fraction(5,6)])
    high = kl_interval([Fraction(2,3),Fraction(1,3)], [Fraction(1,2),Fraction(1,2)])
    assert low[0] > high[1]
    assert full[0] > low[1]

    gap_formula = scale_iv(Fraction(1,3), log2_interval(Fraction(25,24)))
    gap_direct = (full[0]-low[1], full[1]-low[0])
    assert not (gap_direct[1] < gap_formula[0] or gap_formula[1] < gap_direct[0])
    weighted_gap = scale_iv(Fraction(3,16), gap_formula)

    residual = scale_iv(Fraction(2,3), kl_interval(
        [Fraction(1,2),Fraction(1,2)], [Fraction(2,5),Fraction(3,5)]))
    assert not (residual[1] < gap_formula[0] or gap_formula[1] < residual[0])
    return full, low, high, weighted_gap


def reconstruct_numaro():
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    seen = base
    hosts = []
    for mask in masks:
        assert mask.bit_count() == 2 and not (seen & mask)
        seen |= mask
        hosts.append([x for x in range(512) if (mask >> x) & 1])
    core = [-1 if (base >> x) & 1 else 1 for x in range(512)]
    table = []
    for y in range(512):
        row = core.copy()
        for j,cells in enumerate(hosts):
            if (y >> j) & 1:
                for x in cells:
                    row[x] = -1
        table.extend(row)
    digest = hashlib.sha256(",".join(map(str,table)).encode()).hexdigest()
    assert digest == EXPECTED_SHA and sum(table) == 0
    return table


def numaro_tail_ladder():
    table = reconstruct_numaro()
    W = fwht_int(table)
    N = len(W); N2 = N*N
    inf_num = [0]*18
    level_num = [0]*19
    for s,w in enumerate(W):
        ww = w*w
        level_num[s.bit_count()] += ww
        for i in range(18):
            if (s>>i)&1:
                inf_num[i] += ww
    j = [Fraction(x,N2) for x in inf_num]
    assert j[:9] == [Fraction(57,256)]*9
    assert j[9:] == [Fraction(1,256)]*9
    I = sum(j); beta = I-1
    assert I == Fraction(261,128) and beta == Fraction(133,128)
    q = [x/I for x in j]
    assert q[:9] == [Fraction(19,174)]*9
    assert q[9:] == [Fraction(1,522)]*9
    Wk = [Fraction(x,N2) for x in level_num]

    e = [Fraction(0)]*19; e[0] = 1
    for x in q:
        for k in range(18,0,-1):
            e[k] += e[k-1]*x

    Cmask = (1<<9)-1
    count = Counter()
    actual = defaultdict(Fraction)
    for s,w in enumerate(W):
        k = s.bit_count()
        if k == 0 or Wk[k] == 0:
            continue
        aw = abs(w)
        c = (s & Cmask).bit_count()
        count[(k,aw,c)] += 1
        if w:
            actual[(k,aw,c)] += Fraction(w*w,N2)

    packets = defaultdict(set)
    for k,aw,c in count:
        packets[(k,aw)].add(c)
    nonzero = []
    total_price = (Fraction(0),Fraction(0))
    for (k,aw), cs0 in packets.items():
        cs = sorted(cs0)
        A = [actual.get((k,aw,c),Fraction(0)) for c in cs]
        Atot = sum(A)
        if Atot == 0:
            continue
        R = [Fraction(count[(k,aw,c)]) * q[0]**c * q[9]**(k-c) / e[k] for c in cs]
        Rtot = sum(R)
        P = [x/Atot for x in A]
        Q = [x/Rtot for x in R]
        d = kl_interval(P,Q)
        if d[1] > 0:
            if P == Q:
                continue
            nonzero.append((k,aw,cs,Atot,P,Q,d))
            total_price = add_iv(total_price, scale_iv(Atot,d))

    assert [(x[0],x[1],x[2]) for x in nonzero] == [
        (5,1024,[4,5]), (7,1024,[6,7]), (9,1024,[8,9])]
    expected = {
        5: (Fraction(351,32768), [Fraction(35,39),Fraction(4,39)], [Fraction(35,263),Fraction(228,263)]),
        7: (Fraction(9,2048), [Fraction(7,8),Fraction(1,8)], [Fraction(7,64),Fraction(57,64)]),
        9: (Fraction(5,32768), [Fraction(9,10),Fraction(1,10)], [Fraction(3,22),Fraction(19,22)]),
    }
    for k,aw,cs,Atot,P,Q,d in nonzero:
        assert (Atot,P,Q) == expected[k]

    ratio = (total_price[0]/beta, total_price[1]/beta)
    assert ratio[0] > Fraction(32137106754,10**12)
    assert ratio[1] < Fraction(32137106755,10**12)
    assert ratio[0] > Fraction(32131617678,10**12)
    return beta, nonzero, total_price, ratio


def main():
    full, low, high, weighted_gap = four_bit_adversary()
    beta, packets, total_price, ratio = numaro_tail_ladder()
    print("PASS")
    print("four_bit_minus_set", "0,1,2,3,4,5,10,15")
    print("four_bit_influences", "1/4,1/2,1/2,3/4")
    print("three_price_packet_P", "1/3,1/3,1/3")
    print("three_price_packet_Q", "1/6,1/3,1/2")
    print("full_packet_price_KL", *dec_bounds(*full))
    print("best_one_tail_KL", *dec_bounds(*low))
    print("other_one_tail_KL", *dec_bounds(*high))
    print("weighted_one_tail_loss", *dec_bounds(*weighted_gap))
    print("weighted_one_tail_loss_exact", "(1/16) log2(25/24)")
    print("numaro_truth_table_sha256", EXPECTED_SHA)
    print("numaro_beta", f"{beta.numerator}/{beta.denominator}")
    for k,aw,cs,A,P,Q,d in packets:
        print("numaro_binary_price_packet", k, aw,
              "source_mass", f"{A.numerator}/{A.denominator}",
              "actual", ",".join(f"{x.numerator}/{x.denominator}" for x in P),
              "reference", ",".join(f"{x.numerator}/{x.denominator}" for x in Q))
    print("numaro_three_hazard_price_KL_over_beta", *dec_bounds(*ratio, digits=12))
    print("numaro_price_credit_structure", "EXACT_THREE_BINARY_HAZARDS")
    print("universal_one_tail_exactness", "REFUTED_BY_FOUR_BIT_BOOLEAN_GATE")
    print("tail_ladder_replacement", "EXACT_BY_KL_CHAIN_RULE")

if __name__ == "__main__":
    main()
