"""Checks for the paper "The stationary law of the leftmost particles in Aldous's drift-jump process".

Three independent computations of the joint survival function
    S = P(X_{k_a} > t_a for every a)
of the stationary particles:
  (1) the finite determinant of Theorem 2 (formula (2.3));
  (2) exhaustive enumeration of permutations of n <= NMAX letters, using only
      Theorem 1 (X_j is the first x at which the longest increasing chain of the
      Poisson points in [0, x] x [0, 1] reaches j), with a rigorous tail bound;
  (3) Monte Carlo of the particle dynamics itself, which uses neither theorem.
It also checks the expectations c(i) = E(X_i - X_{i-1}) against Aldous-Diaconis.
Run:  python checks.py   (numpy, scipy, mpmath).  Output: checks_output.txt.
"""
import itertools, bisect, math, random, sys
from collections import Counter
import mpmath as mp

mp.mp.dps = 40
OUT = []


def say(s):
    OUT.append(s)
    print(s, flush=True)


# ---------- (1) the determinant of Theorem 2 ----------
def E(u, a, b):
    """E_u(a,b) = sum_{n >= max(0,b-a)} u^n / (n! (a+n-b)!)."""
    u = mp.mpf(u)
    n0 = max(0, b - a)
    s = mp.mpf(0)
    n = n0
    while True:
        term = u ** n / (mp.factorial(n) * mp.factorial(a + n - b))
        s += term
        if n > n0 + 5 and abs(term) < mp.mpf(10) ** (-45) * (1 + abs(s)):
            break
        n += 1
    return s


def p(u, y, x):
    if y < x:
        return mp.mpf(0)
    if u == 0:
        return mp.mpf(1 if y == x else 0)
    return mp.mpf(u) ** (y - x) / mp.factorial(y - x)


def normalize(obs):
    """obs: list of (t, k). Returns sorted list of (t_a, m_a) with m nondecreasing, after the reductions."""
    best = {}
    for t, k in obs:
        if t <= 0:
            continue
        best[t] = min(best.get(t, k), k)
    ts = sorted(best)
    ks = [best[t] for t in ts]
    for a in range(len(ks) - 2, -1, -1):
        ks[a] = min(ks[a], ks[a + 1])
    return [(mp.mpf(t), k - 1) for t, k in zip(ts, ks)]


def S_det(obs, return_size=False):
    ob = normalize(obs)
    if not ob:
        return (mp.mpf(1), 0) if return_size else mp.mpf(1)
    T, d = ob[-1]
    if d == 0:
        return (mp.e ** (-T), 0) if return_size else mp.e ** (-T)
    b = list(range(d))
    J = [(t, x) for (t, m) in ob[:-1] for x in range(d - m)]
    J.sort(key=lambda z: z[0])
    q = len(J)
    N = d + q
    M = mp.zeros(N, N)
    for i in range(d):
        for j in range(d):
            M[i, j] = E(T, b[i], b[j])
        for al, (s, x) in enumerate(J):
            M[i, d + al] = p(s, x, b[i])
    for al, (s, x) in enumerate(J):
        for j in range(d):
            M[d + al, j] = -E(T - s, x, b[j])
        for be, (s2, x2) in enumerate(J):
            M[d + al, d + be] = -(p(s2 - s, x2, x) if s < s2 else 0)
    val = mp.e ** (-T) * mp.det(M)
    return (val, N) if return_size else val


# ---------- (2) exhaustive enumeration (Theorem 1 only) ----------
NMAX = 9


def prefix_lis(seq):
    piles, out = [], []
    for v in seq:
        i = bisect.bisect_left(piles, v)
        if i == len(piles):
            piles.append(v)
        else:
            piles[i] = v
        out.append(len(piles))
    return tuple(out)


TABLE = {}
print("building the permutation table, n <= %d" % NMAX, flush=True)
for n in range(NMAX + 1):
    TABLE[n] = Counter(prefix_lis(pm) for pm in itertools.permutations(range(n)))


def compositions(n, r):
    if r == 1:
        yield (n,)
        return
    for h in range(n + 1):
        for rest in compositions(n - h, r - 1):
            yield (h,) + rest


def S_enum(obs):
    """Truncated sum over N(T) <= NMAX, plus the bound P(N(T) > NMAX) on the omitted mass."""
    best = {}
    for t, k in obs:
        if t > 0:
            best[t] = min(best.get(t, k), k)
    ts = sorted(best)
    ks = [best[t] for t in ts]
    T = mp.mpf(ts[-1])
    deltas = [mp.mpf(ts[0])] + [mp.mpf(ts[a]) - mp.mpf(ts[a - 1]) for a in range(1, len(ts))]
    total = mp.mpf(0)
    for n in range(NMAX + 1):
        fact = mp.factorial(n)
        for h in compositions(n, len(ts)):
            cum = list(itertools.accumulate(h))
            good = 0
            for vec, c in TABLE[n].items():
                if all((cum[a] == 0) or (vec[cum[a] - 1] < ks[a]) for a in range(len(ts))):
                    good += c
            w = mp.mpf(1)
            for dl, hh in zip(deltas, h):
                w *= dl ** hh / mp.factorial(hh)
            total += w * good / fact
    total *= mp.e ** (-T)
    tail = 1 - sum(mp.e ** (-T) * T ** n / mp.factorial(n) for n in range(NMAX + 1))
    return total, tail


# ---------- (3) Monte Carlo of the dynamics ----------
def simulate(k, nsamp, spacing, burn, seed):
    """k-particle drift-jump process: dX/dt = X; rate-1 space-time Poisson events; the nearest particle
    to the right of an event moves to it. Exact event-by-event simulation; samples every `spacing`."""
    rng = random.Random(seed)
    x = [float(i + 1) for i in range(k)]
    samples = []
    t_next_sample = burn
    t = 0.0
    while len(samples) < nsamp:
        # time to next relevant event: integrated rate X_k (e^s - 1)
        e = rng.expovariate(1.0)
        s = math.log1p(e / x[-1])
        if t + s >= t_next_sample:
            g = math.exp(t_next_sample - t)
            samples.append([xi * g for xi in x])
            x = [xi * g for xi in x]
            t = t_next_sample
            t_next_sample += spacing
            continue  # memoryless: redraw from the new state
        g = math.exp(s)
        x = [xi * g for xi in x]
        t += s
        x0 = rng.random() * x[-1]
        i = bisect.bisect_right(x, x0)
        x[i] = x0
    return samples


def main():
    say("== (1) vs (2): determinant against exhaustive enumeration (N(T) <= %d) ==" % NMAX)
    cases = [
        [(0.7, 1)], [(0.8, 2)], [(1.0, 3)], [(1.0, 4)],
        [(0.3, 1), (1.0, 2)], [(0.4, 2), (1.0, 3)], [(0.2, 1), (0.6, 2), (1.0, 3)],
        [(0.3, 2), (0.5, 3), (0.9, 4)], [(0.25, 1), (0.5, 3), (1.0, 4)],
        [(0.5, 3), (1.0, 2)],          # reduction: later smaller index
        [(0.6, 3), (0.6, 2), (1.0, 4)],  # repeated time
        [(0.1, 1), (0.2, 2), (0.3, 3), (0.4, 4), (1.0, 5)],
    ]
    worst = 0
    for obs in cases:
        v, size = S_det(obs, return_size=True)
        w, tail = S_enum(obs)
        diff = abs(v - w)
        ok = diff <= tail + mp.mpf(10) ** (-30) and v >= w - mp.mpf(10) ** (-30)
        worst = max(worst, diff / max(tail, mp.mpf(10) ** (-30)))
        say("obs=%-46s size=%2d det=%s enum=%s diff=%.2e tail<=%.2e %s" % (
            obs, size, mp.nstr(v, 15), mp.nstr(w, 15), float(diff), float(tail), "PASS" if ok else "FAIL"))
        assert ok
    say("all %d cases: 0 <= det - enum <= P(N(T) > %d)  PASS" % (len(cases), NMAX))

    say("\n== closed forms for two particles ==")
    for T in [0.5, 1, 2, 3.5]:
        a = S_det([(T, 2)])
        b = mp.e ** (-T) * mp.besseli(0, 2 * mp.sqrt(T))
        say("P(X2>%s): det=%s  e^-T I0(2 sqrt T)=%s" % (T, mp.nstr(a, 20), mp.nstr(b, 20)))
        assert abs(a - b) < mp.mpf(10) ** (-30)
        for t1 in [T / 4, T / 2]:
            a = S_det([(t1, 1), (T, 2)])
            b = mp.e ** (-T) * mp.besseli(0, 2 * mp.sqrt(T - t1))
            say("P(X1>%s, X2>%s): det=%s  e^-T I0(2 sqrt(T-t1))=%s" % (t1, T, mp.nstr(a, 20), mp.nstr(b, 20)))
            assert abs(a - b) < mp.mpf(10) ** (-30)
    say("Gessel check, P(X_{d+1}>T) = e^-T det[I_{i-j}(2 sqrt T)]:")
    for d, T in [(2, 1.5), (3, 2.0), (4, 3.0)]:
        a = S_det([(T, d + 1)])
        G = mp.matrix(d, d)
        for i in range(d):
            for j in range(d):
                G[i, j] = mp.besseli(abs(i - j), 2 * mp.sqrt(T))
        b = mp.e ** (-T) * mp.det(G)
        say("  d=%d T=%s det=%s Toeplitz=%s" % (d, T, mp.nstr(a, 20), mp.nstr(b, 20)))
        assert abs(a - b) < mp.mpf(10) ** (-30)

    say("\n== c(i) = E(X_i - X_{i-1}) (Aldous-Diaconis 1999, Prop. 9: c(1)=1, c(2)=e-1, c(3)~2.3724) ==")
    # One observation (T, j): the matrix of Theorem 2 is A alone, A_ab = E_T(a, b) = T^((b-a)/2) I_(a-b)(2 sqrt T).
    # The Bessel form is checked against the series first, then used for the integral over [0, T0];
    # the tail beyond T0 is bounded by the diagonal-cell estimate (Section 5 of the paper).
    mp.mp.dps = 30

    def E_bessel(u, a, b):
        u = mp.mpf(u)
        return u ** (mp.mpf(b - a) / 2) * mp.besseli(abs(a - b), 2 * mp.sqrt(u))

    for u in (0.5, 5, 20, 60):
        for a in range(4):
            for b_ in range(4):
                assert abs(E_bessel(u, a, b_) - E(u, a, b_)) < mp.mpf(10) ** (-25) * (1 + abs(E(u, a, b_)))
    say("E_u(a,b) = u^((b-a)/2) I_(a-b)(2 sqrt u) for u in {0.5,5,20,60}, 0<=a,b<=3  PASS")

    def P1(T, j):
        if T <= 0:
            return mp.mpf(1)
        d = j - 1
        if d == 0:
            return mp.e ** (-T)
        A = mp.matrix(d, d)
        for a in range(d):
            for b_ in range(d):
                A[a, b_] = E_bessel(T, a, b_)
        return mp.e ** (-T) * mp.det(A)

    for (T, j) in ((3.0, 3), (12.0, 4)):
        assert abs(P1(T, j) - S_det([(T, j)])) < mp.mpf(10) ** (-25)

    T0 = 400

    def tail_bound(j):
        # P(X_j > T) = P(L(T) <= j-1) <= C(m, m-j+1) exp(-(m-j+1) T / m^2) for every m >= j
        best = mp.inf
        for m in range(j, 40):
            r = mp.mpf(m - j + 1) / m ** 2
            best = min(best, mp.binomial(m, m - j + 1) * mp.e ** (-r * T0) / r)
        return best

    EX = [mp.mpf(0)]
    tails = [mp.mpf(0)]
    for j in range(1, 5):
        EX.append(mp.quad(lambda T: P1(T, j), [0, 2, 5, 10, 20, 40, 80, 160, T0]))
        tails.append(tail_bound(j))
    say("integrals over [0, %d]; tails beyond it at most %s" % (T0, [mp.nstr(t, 3) for t in tails[1:]]))
    assert max(tails) < 1e-11
    c = [EX[j] - EX[j - 1] for j in range(1, 5)]
    c3 = mp.nsum(lambda kk: (mp.binomial(2 * kk, kk) / (kk + 1) - 1) / mp.factorial(kk), [1, mp.inf])
    say("E X_1..E X_4 = %s" % [mp.nstr(v, 12) for v in EX[1:]])
    say("c(1)=%s c(2)=%s (e-1=%s) c(3)=%s (series %s) c(4)=%s" % (
        mp.nstr(c[0], 12), mp.nstr(c[1], 12), mp.nstr(mp.e - 1, 12), mp.nstr(c[2], 12), mp.nstr(c3, 12), mp.nstr(c[3], 12)))
    assert abs(c[0] - 1) < 1e-10 and abs(c[1] - (mp.e - 1)) < 1e-10 and abs(c[2] - c3) < 1e-10
    mp.mp.dps = 40

    say("\n== (1) vs (3): determinant against Monte Carlo of the dynamics (k = 4) ==")
    nsamp, spacing = 120000, 2.0
    samp = simulate(4, nsamp, spacing, burn=30.0, seed=20261016)
    mc_cases = [
        [(1.0, 1)], [(2.0, 2)], [(3.0, 3)], [(4.0, 4)],
        [(0.5, 1), (2.0, 2)], [(1.0, 2), (3.0, 4)], [(0.5, 1), (1.5, 2), (3.0, 3), (5.0, 4)],
        [(1.0, 2), (2.0, 3)], [(2.0, 3), (2.5, 4)],
    ]
    nb = 50
    bs = nsamp // nb
    for obs in mc_cases:
        hits = [all(xv[k - 1] > t for t, k in obs) for xv in samp]
        phat = sum(hits) / nsamp
        means = [sum(hits[i * bs:(i + 1) * bs]) / bs for i in range(nb)]
        se = (sum((m - phat) ** 2 for m in means) / (nb - 1)) ** 0.5 / nb ** 0.5
        v = float(S_det(obs))
        z = (phat - v) / se
        say("obs=%-46s det=%.5f MC=%.5f se=%.5f z=%+.2f %s" % (obs, v, phat, se, z, "PASS" if abs(z) < 4 else "FAIL"))
        assert abs(z) < 4
    say("\nALL CHECKS PASS")
    with open("checks_output.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(OUT) + "\n")


if __name__ == "__main__":
    main()
