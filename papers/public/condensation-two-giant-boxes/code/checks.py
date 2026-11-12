#!/usr/bin/env python3
"""Computer checks for "Two giant boxes in random allocations".

Standard library only.  Part A concerns the weights of Theorem 1.1 (w_{k+1}/w_k -> infinity), Part B the
weights of Theorem 1.2 (nonincreasing weights).  Every check prints its counts; the script ends with
ALL CHECKS PASS if every assertion holds.  The exact parts (A1, A2, B1, B3) use integer or rational
arithmetic.  The probabilities compared with bounds (A3, B4, B5) are sums of positive terms evaluated in
double precision, in the log domain for Part A; the controls of B4 and B5 subtract a probability from 1.
"""
import math
import operator
import sys
from fractions import Fraction

NEG = float("-inf")
FAILED = []


def check(cond, label):
    if not cond:
        FAILED.append(label)
        print("  FAIL:", label)


# ----------------------------------------------------------------------------------------------------------
# Part A.  d_j = j^3 at powers of two, d_j = j otherwise (d_0 = 0); L(k) = log w_k = sum_{j<k} d_j.
# ----------------------------------------------------------------------------------------------------------

def is_pow2(j):
    return j > 0 and j & (j - 1) == 0


def d_spike(j):
    if j == 0:
        return 0
    return j ** 3 if is_pow2(j) else j


def d_plain(j):
    return j


def log_weights(dfun, top):
    L = [0] * (top + 1)
    for k in range(1, top + 1):
        L[k] = L[k - 1] + dfun(k - 1)
    return L


def Q_of(y):
    return sum(j for j in range(1, y) if not is_pow2(j))


def S_of(y):
    return sum(8 ** l for l in range(0, y.bit_length() + 1) if 2 ** l < y)


def part_a1(L):
    print("A1. The decomposition L = Q + S and the bounds on Q and S (Lemma 2.1)")
    n_checks = 0
    Q = 0
    for y in range(1, 4097):
        if y >= 2 and not is_pow2(y - 1):
            Q += y - 1
        S = S_of(y)
        check(L[y] == Q + S, "L(%d) = Q + S" % y)
        check(2 * Q <= y * (y - 1) and 2 * Q > y * (y - 1) - 4 * y, "bounds on Q(%d)" % y)
        if y == 1:
            check(S == 0, "S(1) = 0")
        else:
            l = (y - 1).bit_length() - 1          # 2^l < y <= 2^(l+1)
            check(2 ** l < y <= 2 ** (l + 1) and 7 * S == 8 ** (l + 1) - 1, "S(%d)" % y)
        n_checks += 3
    for k in range(1, 4096):
        check(L[k + 1] - L[k] == d_spike(k) and d_spike(k) >= k, "ratio w_{k+1}/w_k = e^{d_k}, d_k >= k")
        n_checks += 1
    print("  %d checks for y <= 4096" % n_checks)


def dust_best(L, r_max, D):
    """best[r] = max of sum L(p) over multisets of parts p in [1, D] with sum r."""
    best = [NEG] * (r_max + 1)
    best[0] = 0
    for r in range(1, r_max + 1):
        b = NEG
        for p in range(1, min(r, D) + 1):
            v = L[p] + best[r - p]
            if v > b:
                b = v
        best[r] = b
    return best


def part_a2(L, Lplain):
    print("A2. Lemma 2.2: exact maxima over the allocations of m = 2^(i+1) balls with Y_(2) <= m/8 (any number of boxes)")
    top_y = 2 ** 13
    S = [S_of(y) for y in range(0, top_y + 1)]
    Q = [L[y] - S[y] for y in range(0, top_y + 1)]
    rows = []
    for i in range(2, 13):
        m, D = 2 ** (i + 1), 2 ** (i - 2)
        a, b = 2 ** i + 1, 2 ** i - 1
        Lstar, Sstar, Qstar = L[a] + L[b], S[a] + S[b], Q[a] + Q[b]

        def top(arr):
            best = dust_best(arr, m, D)
            return max(arr[y1] + best[m - y1] for y1 in range(0, m + 1))

        ML, MS, MQ = top(L), top(S), top(Q)
        check(7 * Sstar == 8 ** (i + 1) + 8 ** i - 2, "S(a*) + S(b*) = (8^(i+1) + 8^i - 2)/7, i = %d" % i)
        check(4 * Qstar > m * m - 10 * m + 4, "Q(a*) + Q(b*) > m^2/4 - 5m/2 + 1, i = %d" % i)
        check(7 * (Sstar - MS) > 7 * 8 ** (i - 1) - 1, "S(a*) + S(b*) - max S-sum > 8^(i-1) - 1/7, i = %d" % i)
        check(2 * MQ <= m * (m - 1), "max Q-sum <= m(m-1)/2, i = %d" % i)
        chain = Fraction(m * m, 4) + 2 * m - Fraction(6, 7) <= Fraction(m ** 3, 128)
        if i >= 5:
            check(128 * (Lstar - ML) >= m ** 3, "Lemma 2.2: max <= L* - m^3/128, i = %d" % i)
            check(chain, "m^2/4 + 2m - 6/7 <= m^3/128, i = %d" % i)
        # control: the weights without spikes (d_j = j); one box then beats the reference configuration
        bestP = dust_best(Lplain, m, D)
        MLp = max(Lplain[y1] + bestP[m - y1] for y1 in range(0, m + 1))
        Lstar_p = Lplain[a] + Lplain[b]
        check(Lstar_p < MLp, "control: without spikes the maximum exceeds L*, i = %d" % i)
        rows.append((i, m, Lstar, ML, float(Fraction(Lstar - ML, m ** 3)), Sstar - MS, 8 ** (i - 1),
                     MQ - Qstar, m * m // 4 + 2 * m, chain, Lstar_p - MLp))
    print("   i     m              L*         max L-sum (L*-max)/m^3  S-deficit   8^(i-1)  Q-excess m^2/4+2m"
          "  chain  control")
    for r in rows:
        print("  %2d %5d %15d %17d %10.4f %10d %9d %9d %9d %6s %8d" % r)
    print("  S-deficit = S(a*) + S(b*) - max S-sum; Q-excess = max Q-sum - Q(a*) - Q(b*); chain: m^2/4 + 2m - 6/7"
          " <= m^3/128;")
    print("  control: L* - max L-sum for d_j = j at every j")
    return rows


def lconv(a, b, cap):
    """log-domain product of two power series given by log-coefficients, truncated at degree cap."""
    la, lb = len(a), len(b)
    deg = min(cap, la + lb - 2)
    out = [NEG] * (deg + 1)
    for dd in range(deg + 1):
        lo, hi = max(0, dd - lb + 1), min(dd, la - 1)
        vals = [a[k] + b[dd - k] for k in range(lo, hi + 1) if a[k] != NEG and b[dd - k] != NEG]
        if vals:
            mx = max(vals)
            out[dd] = mx + math.log(sum(math.exp(v - mx) for v in vals))
    return out


def lpow(a, e, cap):
    result = [0.0]
    base = a[:cap + 1]
    while e:
        if e & 1:
            result = lconv(result, base, cap)
        e >>= 1
        if e:
            base = lconv(base, base, cap)
    return result


def lse(vals):
    vals = [v for v in vals if v != NEG]
    if not vals:
        return NEG
    mx = max(vals)
    return mx + math.log(sum(math.exp(v - mx) for v in vals))


def log_prob_B(L, m, n):
    """log P(Y_(2) <= m/8) for B_{m,n} with log-weights L (Theorem 1.1)."""
    D = m // 8
    full = [float(L[k]) for k in range(m + 1)]
    low = [float(L[k]) for k in range(D + 1)]
    logZ = lpow(full, n, m)[m]
    low_nm1 = lpow(low, n - 1, m)
    low_n = lconv(low_nm1, low, m)
    terms = [low_n[m] if m < len(low_n) else NEG]
    for y in range(D + 1, m + 1):
        if m - y < len(low_nm1):
            terms.append(math.log(n) + L[y] + low_nm1[m - y])
    return lse(terms) - logZ


def part_a3(L, Lplain):
    print("A3. log P(Y_(2) <= m/8) for the weights of Theorem 1.1, against the bound m log(m+n) - m^3/128")
    print("     m      n     log P            bound        control (no spikes): log P")
    out = []
    for m, n in [(64, 32), (64, 64), (64, 65), (64, 128), (128, 128), (128, 129), (128, 256), (256, 512)]:
        lp = log_prob_B(L, m, n)
        bound = m * math.log(m + n) - m ** 3 / 128
        check(lp <= bound, "log P <= bound at m=%d n=%d" % (m, n))
        lpc = log_prob_B(Lplain, m, n) if m <= 128 else float("nan")
        if m <= 128:
            check(lpc > -1e-6, "control: P(Y_(2) <= m/8) close to 1 without spikes, m=%d n=%d" % (m, n))
        ctrl = "%16.3g" % lpc if m <= 128 else "%16s" % "not run"
        print("  %5d %6d %14.1f %14.1f %s" % (m, n, lp, bound, ctrl))
        out.append((m, n, lp))
    return out


# ----------------------------------------------------------------------------------------------------------
# Part B.  g(j) = max(3j, max{6 J_r + 4 : J_r <= j}), w_0 = 1, w_k = exp(-g(floor(log2 k))) for k >= 1.
# ----------------------------------------------------------------------------------------------------------

def cliffs_from(J1, gap=6, top=10 ** 6):
    out = [J1]
    while 2 * out[-1] + gap <= top:
        out.append(2 * out[-1] + gap)
    return out


def g_fun(cliffs):
    def g(j):
        best = 3 * j
        for J in cliffs:
            if J <= j and 6 * J + 4 > best:
                best = 6 * J + 4
        return best
    return g


def part_b1():
    print("B1. Lemma 3.1: the facts about g")
    n_checks = 0
    for J1 in range(1, 13):
        for gap in (6, 7, 9):
            cl = cliffs_from(J1, gap, 400)
            g = g_fun(cl)
            for j in range(0, 401):
                check(g(j) <= g(j + 1), "g nondecreasing")
                check(3 * j <= g(j) <= 6 * j + 4, "3j <= g(j) <= 6j + 4")
                n_checks += 2
            for J in cl:
                check(g(J) == 6 * J + 4, "g(J) = 6J + 4 at a cliff")
                for j in range(max(0, J - 4), J):
                    check(g(j) == 3 * j, "g(j) = 3j on [J-4, J-1]")
                    n_checks += 1
                n_checks += 1
    # negative control: with J_{r+1} = 2 J_r + 4 the identity g(J-3) = 3(J-3) fails
    bad = 0
    for J1 in range(1, 13):
        cl = cliffs_from(J1, 4, 400)
        g = g_fun(cl)
        bad += sum(1 for J in cl[1:] if g(J - 3) != 3 * (J - 3))
    check(bad > 0, "control: spacing 2J+4 must break g(J-3) = 3(J-3)")
    print("  %d checks (cliff sequences J_1 = 1..12, J_{r+1} = 2J_r + 6, +7, +9, j <= 400);"
          " control with spacing 2J_r + 4: g(J-3) = 3(J-3) fails at %d cliffs" % (n_checks, bad))


def moments(cliffs, jmax=400):
    """Phi(1), Phi'(1), sum k^2 w_k, by blocks [2^j, 2^(j+1)) on which w_k = e^{-g(j)}."""
    g = g_fun(cliffs)
    P0, P1, P2 = 1.0, 0.0, 0.0
    for j in range(0, jmax):
        w = math.exp(-g(j))
        lo, hi = 2 ** j, 2 ** (j + 1) - 1
        cnt = hi - lo + 1
        s1 = (lo + hi) * cnt / 2
        s2 = (hi * (hi + 1) * (2 * hi + 1) - (lo - 1) * lo * (2 * lo - 1)) / 6
        P0 += w * cnt
        P1 += w * s1
        P2 += w * s2
        if w * s2 < 1e-30 * P2 and j > 40:
            break
    nu = P1 / P0
    var = P2 / P0 - nu * nu
    return P0, nu, var


def part_b2():
    print("B2. Lemma 3.1: nu and sigma^2: nu < 0.7 for every cliff sequence, nu_0 for g(j) = 3j")
    P0, nu0, var0 = moments([10 ** 9])
    exact0 = (1.5 / (1 - 4 * math.exp(-3)) - 0.5 / (1 - 2 * math.exp(-3))) / (1 + 1 / (1 - 2 * math.exp(-3)))
    check(abs(nu0 - exact0) < 1e-12, "closed form of nu_0")
    print("  no cliffs: Phi(1) = %.6f, nu_0 = %.6f (closed form %.6f), sigma^2 = %.6f" % (P0, nu0, exact0, var0))
    for J1 in range(1, 13):
        P0c, nu, var = moments(cliffs_from(J1, 6, 400))
        check(0 < nu < nu0 < 0.7 and var > 0, "0 < nu < nu_0 < 0.7, J_1 = %d" % J1)
    P0c, nu, var = moments(cliffs_from(1, 6, 400))
    print("  J_1 = 1 (most weight removed): nu = %.6f; for J_1 = 1..12 all nu lie in (0, nu_0)" % nu)
    return nu0


def part_b3():
    print("B3. Pair counts N(s) = #{a, b in [B, 2B): a + b = 3B + s} >= B - |s| - 1 (Section 4)")
    n_checks = 0
    for J in range(3, 15):
        B = 2 ** (J - 1)
        for s in range(-B + 1, B):
            if B <= 64:
                N = sum(1 for a in range(B, 2 * B) if B <= 3 * B + s - a < 2 * B)
            else:
                lo, hi = max(B, B + s + 1), min(2 * B - 1, 2 * B + s)
                N = max(0, hi - lo + 1)
            check(N >= B - abs(s) - 1, "N(s) >= B - |s| - 1")
            n_checks += 1
    print("  %d checks, J = 3..14, every |s| < B (brute force for B <= 64)" % n_checks)


def conv(a, b, cap):
    la, lb = len(a), len(b)
    deg = min(cap, la + lb - 2)
    rb = b[::-1]
    out = [0.0] * (deg + 1)
    for dd in range(deg + 1):
        lo, hi = max(0, dd - lb + 1), min(dd, la - 1)
        if lo <= hi:
            out[dd] = sum(map(operator.mul, a[lo:hi + 1], rb[lb - 1 - dd + lo:lb - dd + hi]))
    return out


def ppow(a, e, cap):
    result = [1.0]
    base = a[:cap + 1]
    while e:
        if e & 1:
            result = conv(result, base, cap)
        e >>= 1
        if e:
            base = conv(base, base, cap)
    return result


def law(cliffs, top):
    """pi_k = w_k / Phi(1) for k <= top."""
    g = g_fun(cliffs)
    P0, nu, var = moments(cliffs)
    p = [1.0 / P0] + [math.exp(-g(k.bit_length() - 1)) / P0 for k in range(1, top + 1)]
    return p, nu, var


def part_b4():
    print("B4. Lemma 4.1 (truncated exponential bound) against exact probabilities")
    p_all, nu, var = law(cliffs_from(8), 4000)
    worst, n_cases, viol_ctrl, n_ctrl = 0.0, 0, 0, 0
    for N in (5, 10, 30, 100):
        for h in (1, 2, 4, 8, 16, 32):
            if N * (h + 1) > 3300:
                continue
            top = int(math.floor(h + nu))
            trunc = p_all[:top + 1]
            dist = ppow(trunc, N, N * top)
            for mult in (1, 2, 4, 8, 12):
                x = mult * h
                thr = math.ceil(x + nu * N - 1e-12)
                exact = sum(dist[thr:]) if thr < len(dist) else 0.0
                bound = (math.e / (1 + x * h / (N * var))) ** (x / h)
                check(exact <= bound * (1 + 1e-9), "Lemma 4.1 at N=%d h=%d x=%d" % (N, h, x))
                if bound > 0:
                    worst = max(worst, exact / bound)
                n_cases += 1
                # control: drop the truncation event; P(S_N >= x + nu N) without max X_i <= h
                full = ppow(p_all[:thr + 1], N, thr)
                below = sum(full[:thr])
                untr = 1.0 - below
                n_ctrl += 1
                if untr > bound * 1.01:
                    viol_ctrl += 1
    print("  %d cases (N <= 100, h <= 32, x/h in {1,2,4,8,12}); all hold, largest ratio exact/bound %.4f" % (n_cases, worst))
    check(viol_ctrl > 0, "control: without the truncation the bound must fail somewhere")
    print("  control without the event max X_i <= h: the bound fails in %d of %d cases" % (viol_ctrl, n_ctrl))


def prob_second(p, m, n, ys):
    """P(Y_(2) >= y) for each y in ys, for B_{m,n} with tilted law p (pi_k = w_k/Phi(1))."""
    full = ppow(p, n, m)
    Z = full[m]
    res = {}
    for y in ys:
        low = p[:y]
        low_nm1 = ppow(low, n - 1, m)
        low_n = conv(low_nm1, low, m)
        A0 = low_n[m] if m < len(low_n) else 0.0
        A1 = n * sum(p[k] * low_nm1[m - k] for k in range(y, m + 1) if m - k < len(low_nm1))
        res[y] = (1.0 - (A0 + A1) / Z, A0 / Z, A1 / Z)
    return res


def pair(nu, K, case):
    """(n, m) for the excess K: lambda - nu = 1 (n = K) or the tree (m = n - 1)."""
    if case == "1":
        return K, K + int(math.floor(nu * K))
    n = int(math.ceil((K + 1) / (1 - nu)))
    return n, n - 1


def part_b5():
    print("B5. Theorem 1.2: P(Y_(2) < N/8) with the cliffs J_1 < J_2 < ... (N = 2^J, J a cliff), and P(Y_(2) >= N/8)")
    print("    for the weights without cliffs (g(j) = 3j, nu = nu_0); lambda - nu = 1: n = K, m = K + floor(nu n);"
          " tree: m = n - 1, n = ceil((K + 1)/(1 - nu))")
    print("    no cliffs (a): the same (m, n); no cliffs (b): (m, n) from the same rule with nu_0 (the control)")
    print("    J  J_1  case      n      m    nu        P(Y_(2) < N/8)   P(Y_(2) < N/4)"
          "   no cliffs (a): P(Y_(2) >= N/8)   (b)")
    fails = {}
    _, nu0, _ = law([10 ** 9], 1)
    for J, J1, case in [(8, 8, "1"), (9, 9, "1"), (10, 10, "1"), (8, 1, "1"),
                        (8, 8, "tree"), (9, 9, "tree"), (10, 10, "tree"), (8, 1, "tree")]:
        cl = cliffs_from(J1)
        check(J in cl, "J is a cliff of the sequence")
        B, K = 2 ** (J - 1), 3 * 2 ** (J - 1)
        _, nu, _ = law(cl, 1)
        n, m = pair(nu, K, case)
        check(abs(m - nu * n - K) <= 1, "|m - nu n - K| <= 1")
        n0, m0 = pair(nu0, K, case)
        check(abs(m0 - nu0 * n0 - K) <= 1, "|m - nu_0 n - K| <= 1 (control)")
        pc, _, _ = law(cl, m)
        pn, _, _ = law([10 ** 9], max(m, m0))
        ys = [B // 4, B // 2]
        rc = prob_second(pc, m, n, ys)
        rn = prob_second(pn[:m + 1], m, n, ys)
        rn0 = rn if (n0, m0) == (n, m) else prob_second(pn[:m0 + 1], m0, n0, ys)
        f8 = rc[B // 4][1] + rc[B // 4][2]
        f4 = rc[B // 2][1] + rc[B // 2][2]
        print("  %3d %4d %5s %6d %6d %8.5f %16.3e %16.3e %32.3e %10.3e"
              % (J, J1, case, n, m, nu, f8, f4, rn[B // 4][0], rn0[B // 4][0]))
        check(rn0[B // 4][0] < 0.01, "control: without cliffs Y_(2) >= N/8 is rare, J=%d (%s)" % (J, case))
        if J1 == J:
            fails.setdefault(case, []).append(f8)
    for case, f in fails.items():
        check(all(f[k + 1] < f[k] for k in range(len(f) - 1)), "P(Y_(2) < N/8) decreases in J (%s)" % case)
        check(f[-1] < 1e-3, "P(Y_(2) < N/8) < 0.001 at J = 10 (%s)" % case)


def main():
    L = log_weights(d_spike, 2 ** 13)
    Lplain = log_weights(d_plain, 2 ** 13)
    part_a1(L)
    part_a2(L, Lplain)
    part_a3(L, Lplain)
    part_b1()
    part_b2()
    part_b3()
    part_b4()
    part_b5()
    if FAILED:
        print("FAILED: %d checks" % len(FAILED))
        sys.exit(1)
    print("ALL CHECKS PASS")


if __name__ == "__main__":
    main()
