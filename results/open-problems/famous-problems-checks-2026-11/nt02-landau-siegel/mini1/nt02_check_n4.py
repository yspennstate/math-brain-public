# Tests for "Uniform exclusion of Landau-Siegel zeros" (OpenAI, 1 Oct 2026).
#
# K = Q(a, b), a^2 = d, b^2 = 2, R = Z[a, b].  theta_n = n1 + n2 a + n3 b + n4 ab, n in {0..N-1}^4.
# sigma: a -> -a, tau: b -> -b.  Row of alpha: theta^a1 * sigma(theta)^a2 * (sigma tau)(theta)^a3.
# Rows are taken in order of weight a1 + H (a2 + a3); a row is retained when it increases the span.
# Delta = determinant of the M = N^4 retained rows.
#
# Part A  the retained set (computed modulo two primes that split completely in K) and the sums of Lemma 6.
# Part B  the exact integer Norm(Delta) by the Chinese remainder theorem, its p-adic valuations, and
#         the comparison with 4 * E_p, E_p = sum floor(a1 / p)  (Lemma 7), for every Frobenius class.
# Part C  the smallest cube of degrees on which evaluation is onto, against condition (3.1) of Lemma 3.
import sys, os, time, math, itertools
import numpy as np
from sympy import nextprime

T0 = time.time()


def out(*a):
    print(*a, flush=True)
    if os.path.exists(os.path.expanduser("~/nt02_ls/STOP_n4")):
        sys.exit(3)


def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def frob(d, p):
    if p == 2 or d % p == 0:
        return "ramified"
    c, t = legendre(d, p), legendre(2, p)
    if c == -1:
        return "sigma" if t == 1 else "sigma*tau"
    return "id" if t == 1 else "tau"


def split_primes(d, start, count):
    res, p = [], start
    while len(res) < count:
        p = nextprime(p)
        if p % 8 == 7 and pow(d % p, (p - 1) // 2, p) == 1:
            res.append(int(p))
    return res


def points(N):
    g = np.array(list(itertools.product(range(N), repeat=4)), dtype=np.int64)
    return g[:, 0], g[:, 1], g[:, 2], g[:, 3]


def variables(d, N, p, ea=1, eb=1):
    sa = pow(d % p, (p + 1) // 4, p)
    sb = pow(2, (p + 1) // 4, p)
    assert sa * sa % p == d % p and sb * sb % p == 2
    sab = sa * sb % p
    n1, n2, n3, n4 = points(N)

    def th(x, y):
        return (n1 + (x * sa % p) * n2 + (y * sb % p) * n3 + (x * y * sab % p) * n4) % p
    return th(ea, eb), th(-ea, eb), th(-ea, -eb)


def power_table(x, top, p):
    t = np.empty((top + 1, x.size), dtype=np.int64)
    t[0] = 1
    for e in range(1, top + 1):
        t[e] = t[e - 1] * x % p
    return t


def greedy(d, N, H, p, order="weight"):
    M = N ** 4
    X = variables(d, N, p)
    cap = 8
    tabs = [power_table(x, cap, p) for x in X]
    basis, kept = [], []
    w = 0
    while len(kept) < M:
        if order == "weight":
            cands = [(w - H * s, a2, s - a2) for s in range(w // H + 1) for a2 in range(s + 1)]
        else:  # cube order: all alpha with max coordinate equal to w
            cands = [(x, y, z) for x in range(w + 1) for y in range(w + 1) for z in range(w + 1)
                     if max(x, y, z) == w]
        for al in cands:
            if max(al) > cap:
                cap = 2 * max(al)
                tabs = [power_table(x, cap, p) for x in X]
            r = tabs[0][al[0]] * tabs[1][al[1]] % p * tabs[2][al[2]] % p
            for pc, bv in basis:
                c = int(r[pc])
                if c:
                    r = (r - c * bv) % p
            nz = np.nonzero(r)[0]
            if nz.size:
                pc = int(nz[0])
                r = r * pow(int(r[pc]), p - 2, p) % p
                basis.append((pc, r))
                kept.append(al)
                if len(kept) == M:
                    break
        w += 1
    return kept


def det_mod(A, p):
    A = A.copy()
    n = A.shape[0]
    det = 1
    for k in range(n):
        nz = np.nonzero(A[k:, k])[0]
        if nz.size == 0:
            return 0
        i = k + int(nz[0])
        if i != k:
            A[[k, i]] = A[[i, k]]
            det = -det
        piv = int(A[k, k])
        det = det * piv % p
        if k + 1 < n:
            f = A[k + 1:, k] * pow(piv, p - 2, p) % p
            A[k + 1:, k + 1:] = (A[k + 1:, k + 1:] - np.outer(f, A[k, k + 1:])) % p
    return det % p


def norm_mod(d, N, kept, p):
    top = max(max(al) for al in kept)
    a1 = np.array([al[0] for al in kept])
    a2 = np.array([al[1] for al in kept])
    a3 = np.array([al[2] for al in kept])
    res = 1
    for ea in (1, -1):
        for eb in (1, -1):
            X = variables(d, N, p, ea, eb)
            t = [power_table(x, top, p) for x in X]
            A = t[0][a1] * t[1][a2] % p * t[2][a3] % p
            res = res * det_mod(A, p) % p
    return res


def exact_norm(d, N, kept, primes):
    M = N ** 4
    thmax = (N - 1) * (1 + math.sqrt(abs(d))) * (1 + math.sqrt(2))
    sumdeg = sum(sum(al) for al in kept)
    bits = 4 * (0.5 * M * math.log2(M) + sumdeg * math.log2(thmax)) + 4
    x, m, used = 0, 1, 0
    for p in primes:
        r = norm_mod(d, N, kept, p)
        t = (r - x) * pow(m, -1, p) % p
        x += m * t
        m *= p
        used += 1
        if m.bit_length() > bits + 2:
            break
    assert m.bit_length() > bits + 2, "not enough primes"
    val = x if x <= m // 2 else x - m
    chk = primes[-1]
    assert chk not in primes[:used]
    ok = (val % chk) == norm_mod(d, N, kept, chk)
    return val, bits, used, ok


def part_A():
    out("PART A  retained rows by weight a1 + H(a2+a3); U = N^(4/3); ideal W/(H^(2/3)U) for independent monomials = 6^(1/3) = 1.817")
    out("  d   N    M  H  same_set  Wmax/(H^.667U)  maxa1/T1  max(a2+a3)/(96H^-.333U)  S1/(M H^.667 U)  S2/(M H^-.333 U)  H*S2/S1")
    res = {}
    cases = [(13, N, H) for N in (2, 3, 4, 5) for H in (1, 2, 4) if H <= N] + [(13, 6, 2), (-7, 3, 2), (-7, 4, 2), (5, 3, 2), (5, 4, 3)]
    for d, N, H in cases:
        pr = split_primes(d, 10 ** 9 + 7 * abs(d), 2)
        k1 = greedy(d, N, H, pr[0])
        k2 = greedy(d, N, H, pr[1])
        M = N ** 4
        U = N ** (4 / 3)
        S1 = sum(al[0] for al in k1)
        S2 = sum(al[1] + al[2] for al in k1)
        W = max(al[0] + H * (al[1] + al[2]) for al in k1)
        out("%4d %3d %5d %2d  %-8s  %14.3f  %8.3f  %23.3f  %15.3f  %16.3f  %7.3f   [%.0fs]" % (
            d, N, M, H, k1 == k2, W / (H ** (2 / 3) * U), max(al[0] for al in k1) / (32 * H ** (2 / 3) * U),
            max(al[1] + al[2] for al in k1) / (96 * H ** (-1 / 3) * U), S1 / (M * H ** (2 / 3) * U),
            S2 / (M * H ** (-1 / 3) * U), H * S2 / S1, time.time() - T0))
        res[(d, N, H)] = k1
    return res


def part_B(kept_all):
    out("")
    out("PART B  exact Norm(Delta) and its valuations.  Lemma 7 claims v_p >= 4 E_p for p > H, p not dividing 2d, chi(p) = -1")
    out("        (classes sigma, sigma*tau); the same replacement works for class id.  Class tau is not covered: control.")
    cases = [(13, 4, 2), (-7, 4, 2), (5, 4, 3), (13, 4, 1)]
    fails = 0
    tested = 0
    for d, N, H in cases:
        kept = kept_all.get((d, N, H)) or greedy(d, N, H, split_primes(d, 10 ** 9 + 7 * abs(d), 1)[0])
        M = N ** 4
        thmax = (N - 1) * (1 + math.sqrt(abs(d))) * (1 + math.sqrt(2))
        sumdeg = sum(sum(al) for al in kept)
        need = int(4 * (0.5 * M * math.log2(M) + sumdeg * math.log2(thmax)) / 29.8) + 8
        primes = split_primes(d, 10 ** 9 + 10 ** 6, need)
        val, bits, used, ok = exact_norm(d, N, kept, primes)
        S1 = sum(al[0] for al in kept)
        S2 = sum(al[1] + al[2] for al in kept)
        logn = math.log(abs(val)) if val else float("-inf")
        upper = 0.5 * M * math.log(M) + (S1 + S2) * (math.log(N) + 0.5 * math.log(abs(d)) + math.log(8))
        out("d=%d N=%d H=%d  M=%d  S1=%d S2=%d  max a1=%d  Norm(Delta) != 0: %s  bits=%d  CRT primes=%d  check prime agrees: %s  [%.0fs]" % (
            d, N, H, M, S1, S2, max(al[0] for al in kept), val != 0, abs(val).bit_length(), used, ok, time.time() - T0))
        low_adm = 0.0
        low_use = 0.0
        line = []
        for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
            E = sum(al[0] // p for al in kept)
            if E == 0 and p > 13:
                continue
            v, x = 0, abs(val)
            while x % p == 0:
                x //= p
                v += 1
            cl = frob(d, p)
            covered = p > H and cl in ("sigma", "sigma*tau", "id")
            verdict = ""
            if covered:
                tested += 1
                verdict = "holds" if v >= 4 * E else "FAILS"
                fails += verdict == "FAILS"
                low_use += E * math.log(p)
                if cl != "id":
                    low_adm += E * math.log(p)
            elif cl in ("sigma", "sigma*tau", "id"):
                verdict = "(p <= H, not covered)"
            line.append("    p=%2d  class %-9s  4E_p=%4d  v_p=%4d  %s" % (p, cl, 4 * E, v, verdict))
        out("\n".join(line))
        out("    (1/4) log|Norm| = %.1f   sum over admissible p of E_p log p = %.1f   over all usable p = %.1f   bound (5.1) = %.1f   order holds: %s" % (
            logn / 4, low_adm, low_use, upper, low_use <= logn / 4 <= upper))
    out("Lemma 7 inequality: %d cases tested, %d failures" % (tested, fails))


def part_C():
    out("")
    out("PART C  smallest t with evaluation onto for degrees (t,t,t); counting needs (t+1)^3 >= N^4; (3.1) asks (t-3N+4)^3 > (4N-3)^4")
    d = 13
    for N in (2, 3, 4, 5):
        p = split_primes(d, 10 ** 9 + 91, 1)[0]
        kept = greedy(d, N, 1, p, order="cube")
        t = max(max(al) for al in kept)
        tc = math.ceil((N ** 4) ** (1 / 3) - 1e-9) - 1
        tl = 3 * (N - 1)
        while (tl - 3 * (N - 1) + 1) ** 3 <= (4 * N - 3) ** 4:
            tl += 1
        out("  N=%d  M=%4d  smallest t found = %2d   counting bound = %2d   t from (3.1) = %3d   t/N^(4/3) = %.2f   [%.0fs]" % (
            N, N ** 4, t, tc, tl, t / N ** (4 / 3), time.time() - T0))


if __name__ == "__main__":
    kept_all = {}
    part_B(kept_all)
    out("done in %.0f s" % (time.time() - T0))
