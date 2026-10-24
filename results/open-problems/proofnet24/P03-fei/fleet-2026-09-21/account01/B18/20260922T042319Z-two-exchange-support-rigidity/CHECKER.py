#!/usr/bin/env python3
"""Exact/fixed-point certificate for radius-two support rigidity of the n=18 FEI source family.

The host-bank comparison is inherited mathematically from account02/B17: for every
partition of an 18-row support into nine two-row hosts, host entropy is 9/16 and
host influence is at least 45/256. This checker reconstructs the exact nine-bit
source, enumerates every support at two-row exchange distance 2 from T, and proves
the optimistic ratio using host influence 45/256 is < 3239/500 = 6.478.

Entropy logarithms are upper-bounded by rational atanh series, then rounded upward
to a fixed scale. The final comparison is integer arithmetic.
"""
from fractions import Fraction
import itertools, math
import numpy as np

N = 512
SCALE = 10**17
CNUM, CDEN = 3239, 500
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
EXPECTED_T = [78,79,113,121,228,484,170,186,149,151,338,466,284,316,291,295,393,457]


def ln_interval_unit(num, den, terms=40):
    assert den <= num <= 2*den
    t = Fraction(num-den, num+den)
    s = Fraction(0, 1)
    tp = t
    for j in range(terms):
        s += tp / (2*j+1)
        tp *= t*t
    lo = 2*s
    if t == 0:
        return lo, lo
    first = t**(2*terms+1)
    rem = 2*first / (2*terms+1) / (1-t*t)
    return lo, lo + rem


def entropy_upper_table():
    ln2_lo, _ = ln_interval_unit(2, 1)
    tab = np.zeros(N+1, dtype=np.int64)
    for z in range(1, N+1):
        x = N / z
        k = int(math.floor(math.log2(x)))
        den = z * (1 << k)
        _, lq_hi = ln_interval_unit(N, den)
        log2_hi = Fraction(k, 1) + lq_hi / ln2_lo
        h_hi = Fraction(2*z*z, N*N) * log2_hi
        tab[z] = (h_hi.numerator*SCALE + h_hi.denominator - 1)//h_hi.denominator
    return tab


def main():
    base = int("".join(SLICES[0]), 16)
    masks = [int("".join(row), 16) ^ base for row in SLICES[1:]]
    T = [x for m in masks for x in range(N) if (m >> x) & 1]
    assert T == EXPECTED_T
    base_true = np.array([(base >> x) & 1 for x in range(N)], dtype=np.int8)
    assert int(base_true.sum()) == 247
    assert all(base_true[x] == 0 for x in T)

    source_true = base_true.copy()
    source_true[T] = 1
    assert int(source_true.sum()) == 265
    P = [x for x in range(N) if source_true[x] and x not in set(T)]
    assert len(P) == 247

    g0 = np.where(source_true == 1, 1, -1).astype(np.int16)
    a = g0.copy(); a[T] = 0

    ids = np.arange(N, dtype=np.int64)
    pc = np.array([int(i).bit_count() for i in range(N)], dtype=np.int16)
    W = (1 - 2*(pc[(ids[:,None] & ids[None,:])] & 1)).astype(np.int16)
    A = a @ W
    levels = pc.astype(np.int64)
    J0 = int(np.dot(levels, A.astype(np.int64)**2))
    assert J0 == 488448

    LA = (W @ (levels*A)).astype(np.int64)

    Y = np.array(list(itertools.combinations(P, 2)), dtype=np.int16)
    assert len(Y) == math.comb(247,2) == 30381
    Ysum = W[Y[:,0]].astype(np.int16) + W[Y[:,1]].astype(np.int16)
    ysumL = LA[Y[:,0]] + LA[Y[:,1]]
    yyadj = np.array([int((int(u)^int(v)).bit_count() == 1) for u,v in Y], dtype=np.int64)
    pidx = {y:i for i,y in enumerate(P)}
    yidx0 = np.array([pidx[int(y)] for y in Y[:,0]], dtype=np.int32)
    yidx1 = np.array([pidx[int(y)] for y in Y[:,1]], dtype=np.int32)
    adj_to_P = {
        x: np.array([int((x^int(y)).bit_count() == 1) for y in P], dtype=np.int64)
        for x in T
    }

    hfix = entropy_upper_table()
    maxH_by_den = {}
    min_deltaJ = None
    arg_min_deltaJ = None
    descriptive_best = (-1.0, None)
    candidates = 0
    chunk = 2048

    for x1,x2 in itertools.combinations(T,2):
        Rsum = W[x1].astype(np.int16) + W[x2].astype(np.int16)
        rr = int((x1^x2).bit_count() == 1)
        cp = adj_to_P[x1] + adj_to_P[x2]
        cross = cp[yidx0] + cp[yidx1]
        deltaJ = (2*(int(LA[x1])+int(LA[x2])-ysumL)
                  + 9216 - 512*rr - 512*yyadj + 512*cross)
        jmin = int(deltaJ.argmin())
        if min_deltaJ is None or int(deltaJ[jmin]) < min_deltaJ:
            min_deltaJ = int(deltaJ[jmin])
            arg_min_deltaJ = (x1,x2,int(Y[jmin,0]),int(Y[jmin,1]))

        dennum = J0 + deltaJ + 46080 - N*N

        for j0 in range(0, len(Y), chunk):
            j1 = min(j0+chunk, len(Y))
            vals = A[None,:] + Rsum[None,:] - Ysum[j0:j1]
            Hscaled = hfix[np.abs(vals)].sum(axis=1, dtype=np.int64) + (9*SCALE)//16
            dns = dennum[j0:j1]
            candidates += j1-j0

            for d in np.unique(dns):
                hv = int(Hscaled[dns == d].max())
                d = int(d)
                if hv > maxH_by_den.get(d, -1):
                    maxH_by_den[d] = hv

            Hdesc = np.array(Hscaled, dtype=np.float64)/SCALE
            Rdesc = Hdesc / (np.array(dns, dtype=np.float64)/(N*N))
            j = int(Rdesc.argmax())
            if float(Rdesc[j]) > descriptive_best[0]:
                descriptive_best = (float(Rdesc[j]),
                    (x1,x2,int(Y[j0+j,0]),int(Y[j0+j,1]),int(dns[j])))

    assert candidates == math.comb(18,2)*math.comb(247,2) == 4648293
    assert min_deltaJ == 2048

    min_slack = None
    min_slack_den = None
    for d, Hs in maxH_by_den.items():
        slack = SCALE*CNUM*d - Hs*CDEN*N*N
        if min_slack is None or slack < min_slack:
            min_slack = int(slack)
            min_slack_den = d
    assert min_slack > 0

    print("PASS")
    print("supports_checked =", candidates)
    print("positive_source_rows =", 265)
    print("outside_positive_rows =", len(P))
    print("min_core_influence_numerator_increase =", min_deltaJ)
    print("min_core_influence_increase = 1/128")
    print("argmin_influence_exchange =", arg_min_deltaJ)
    print("distinct_optimistic_denominators =", len(maxH_by_den))
    print("certified_ratio_upper = 3239/500 = 6.478")
    print("minimum_integer_slack =", min_slack)
    print("minimum_slack_denominator_numerator =", min_slack_den)
    print("descriptive_best_upper_ratio = %.15f" % descriptive_best[0])
    print("descriptive_best_exchange =", descriptive_best[1])

if __name__ == "__main__":
    main()
