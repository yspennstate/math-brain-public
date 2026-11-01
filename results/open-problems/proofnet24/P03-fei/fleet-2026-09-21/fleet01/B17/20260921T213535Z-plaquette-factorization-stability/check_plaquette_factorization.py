#!/usr/bin/env python3
"""Exact finite stress test for B17 plaquette-factorization stability.

Analytic claims are proved in REPORT.md. This checker:
  1. exactly verifies 4*delta_cut <= W_cross for every Boolean sign table
     on bipartitions 1+1, 1+2 and 2+2;
  2. verifies the singleton logarithmic plaquette inequality numerically
     after exact counting (the theorem itself uses cube edge-isoperimetry);
  3. searches the stronger OPEN conjecture W_cross >=
     2*delta_cut*log2(1/delta_cut) on the same finite universe and reports
     the minimum observed ratio. Passing item 3 is finite evidence only.
"""
from math import log2

def nearest_rank1_mismatch(vals, nA, nB):
    NA, NB = 1 << nA, 1 << nB
    best = NA * NB + 1
    # Gauge-fix g(0)=+1. For fixed g, optimize h(y) independently.
    for mask in range(1 << (NA - 1)):
        g = [1] + [1 if ((mask >> (x - 1)) & 1) == 0 else -1
                   for x in range(1, NA)]
        mism = 0
        for y in range(NB):
            score = sum(vals[x][y] * g[x] for x in range(NA))
            mism += (NA - abs(score)) // 2
        best = min(best, mism)
    return best

def cross_plaquette_count(vals, nA, nB):
    NA, NB = 1 << nA, 1 << nB
    total = 0
    for i in range(nA):
        for j in range(nB):
            for x in range(NA):
                for y in range(NB):
                    if (vals[x][y] * vals[x ^ (1 << i)][y]
                        * vals[x][y ^ (1 << j)]
                        * vals[x ^ (1 << i)][y ^ (1 << j)]) == -1:
                        total += 1
    return total

def singleton_rows(vals, nA, nB):
    n = nA + nB
    NA = 1 << nA
    N = 1 << n
    arr = []
    for z in range(N):
        x, y = z & (NA - 1), z >> nA
        arr.append(vals[x][y])
    for i in range(n):
        q_count = sum(arr[z] != arr[z ^ (1 << i)] for z in range(N))
        q = q_count / N
        j = min(q, 1 - q)
        p_count = 0
        for k in range(n):
            if k == i:
                continue
            for z in range(N):
                if (arr[z] * arr[z ^ (1 << i)] * arr[z ^ (1 << k)]
                    * arr[z ^ (1 << i) ^ (1 << k)]) == -1:
                    p_count += 1
        P = p_count / N
        rhs = 0.0 if j == 0 else 2 * j * log2(1 / j)
        yield j, P, rhs

def check_partition(nA, nB):
    NA, NB = 1 << nA, 1 << nB
    N = NA * NB
    total_funcs = 1 << N
    min_strong_ratio = float("inf")
    min_example = None
    for mask in range(total_funcs):
        vals = [[1] * NB for _ in range(NA)]
        for y in range(NB):
            for x in range(NA):
                vals[x][y] = -1 if ((mask >> (x + NA * y)) & 1) else 1

        mism = nearest_rank1_mismatch(vals, nA, nB)
        W_count = cross_plaquette_count(vals, nA, nB)

        # Exact proven cut inequality: 4 delta <= W.
        # Both quantities have denominator N.
        if 4 * mism > W_count:
            raise AssertionError(("cut theorem violation", nA, nB, mask,
                                  mism, W_count))

        if mism:
            delta = mism / N
            W = W_count / N
            strong_rhs = 2 * delta * log2(1 / delta)
            if W + 1e-12 < strong_rhs:
                raise AssertionError(("strong finite conjecture violation",
                                      nA, nB, mask, delta, W, strong_rhs))
            ratio = W / (delta * log2(1 / delta))
            if ratio < min_strong_ratio:
                min_strong_ratio = ratio
                min_example = (mask, delta, W)

        for j, P, rhs in singleton_rows(vals, nA, nB):
            if P + 1e-12 < rhs:
                raise AssertionError(("singleton log violation", nA, nB,
                                      mask, j, P, rhs))
    return total_funcs, min_strong_ratio, min_example

def main():
    grand = 0
    for dims in ((1, 1), (1, 2), (2, 2)):
        count, ratio, ex = check_partition(*dims)
        grand += count
        print("partition=%d+%d functions=%d cut_PASS singleton_PASS "
              "strong_finite_PASS min_strong_ratio=%.12f example=%r"
              % (dims[0], dims[1], count, ratio, ex))
    print("TOTAL_FUNCTIONS=%d" % grand)
    print("STATUS=PASS")
    print("NOTE=strong_finite_PASS is evidence only; the strong all-cut "
          "logarithmic inequality remains OPEN.")

if __name__ == "__main__":
    main()
