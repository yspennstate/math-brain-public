"""Exact checks for the filling construction of Theorem 2.1 on finite and Bernoulli examples.

Part A: a permutation T of a finite set E with the uniform law P. The filling recursion runs in exact rational
arithmetic. If the target fP gives every orbit its own P-mass, the recursion ends within |E| steps with b = 0 and
the accepted densities m_n add up to f; if not, a positive residual is left, as the necessity half of Theorem 2.1
says.
Part B: the Bernoulli shift on {0,1}^Z with fair bits, T the left shift, targets f depending on x_0..x_{k-1}.
The functions a_n, b_n, m_n depend on finitely many coordinates and are computed exactly: the masses of a_n and
b_n agree, the residual r_n decreases, and a Monte Carlo run of the randomized rule of Section 2 reproduces the
exact accepted sub-law.
Part C: Remark 4.2 on cycles: every deterministic shift rule n(z) gives an integer-valued density.
Run: python checks.py   (standard library only)
"""
from fractions import Fraction as F
import itertools
import random

NSTEPS = 13


def fill_perm(perm, f, steps):
    n = len(perm)
    inv = [0] * n
    for i, j in enumerate(perm):
        inv[j] = i
    a = [F(1)] * n
    b = list(f)
    acc = [F(0)] * n
    for _ in range(steps):
        m = [min(a[i], b[i]) for i in range(n)]
        for i in range(n):
            acc[i] += m[i]
        rest = [a[i] - m[i] for i in range(n)]
        a = [rest[inv[y]] for y in range(n)]      # (L h)(y) = h(T^{-1} y)
        b = [b[i] - m[i] for i in range(n)]
        assert sum(a) == sum(b)
    return acc, sum(b) / n, sum(a) / n


def orbits(perm):
    seen, out = set(), []
    for s in range(len(perm)):
        if s in seen:
            continue
        o, x = [], s
        while x not in seen:
            seen.add(x)
            o.append(x)
            x = perm[x]
        out.append(o)
    return out


def part_a(rng):
    ok_bal = ok_unbal = 0
    for _ in range(300):
        n = rng.randint(1, 9)
        perm = list(range(n))
        rng.shuffle(perm)
        obs = orbits(perm)
        f = [F(0)] * n
        for o in obs:                               # orbit-balanced target: orbit o keeps P-mass len(o)/n
            w = [F(rng.randint(0, 5)) for _ in o]
            if sum(w) == 0:
                w[0] = F(1)
            s = sum(w)
            for x, wx in zip(o, w):
                f[x] = wx * len(o) / s
        acc, rb, ra = fill_perm(perm, f, n)
        assert acc == f and rb == 0 and ra == 0, (perm, f)
        ok_bal += 1
        if len(obs) >= 2:                           # move mass between two orbits: a residual must remain
            g = list(f)
            x, y = obs[0][0], obs[1][0]
            d = min(g[x], F(1, 2))
            if d > 0:
                g[x] -= d
                g[y] += d
                acc, rb, ra = fill_perm(perm, g, 4 * n)
                assert rb > 0 and rb == ra
                ok_unbal += 1
    print(f"A  permutations: {ok_bal} orbit-balanced targets filled exactly within |E| steps; "
          f"{ok_unbal} unbalanced targets leave a positive residual")


def targets(rng):
    yield 1, {(0,): F(0), (1,): F(2)}, "f = 2 1{x_0 = 1}"
    yield 2, {(0, 0): F(0), (0, 1): F(0), (1, 0): F(0), (1, 1): F(4)}, "f = 4 1{x_0 = x_1 = 1}"
    for t in range(2):
        k = 3
        ws = list(itertools.product((0, 1), repeat=k))
        raw = [F(rng.randint(0, 6)) for _ in ws]
        s = sum(raw)
        yield k, {w: r * len(ws) / s for w, r in zip(ws, raw)}, f"random f on 3 bits #{t + 1}"


def part_b(rng):
    for k, f_table, label in targets(rng):
        # at stage n every function lives on the window x_{-n},...,x_{k-1} (a tuple of n + k bits)
        a = {w: F(1) for w in itertools.product((0, 1), repeat=k)}
        b = {w: f_table[w] for w in a}
        rs, hs = [], []
        acc_proj = {w: F(0) for w in f_table}        # accepted mass, as a law of the window x_0..x_{k-1}
        for n in range(NSTEPS):
            size = 2 ** (n + k)
            m = {w: min(a[w], b[w]) for w in a}
            hs.append({w: (m[w] / a[w] if a[w] > 0 else F(0)) for w in a})
            for w in m:
                acc_proj[w[-k:]] += m[w] / size
            rs.append(sum(a.values()) / size)
            assert rs[-1] == sum(b.values()) / size  # the two remaining masses agree exactly
            # a_{n+1}(x) = (a_n - m_n)(T^{-1} x), (T^{-1} x)_i = x_{i-1}: on the window -(n+1)..k-1 it reads
            # the coordinates -(n+1)..k-2; b_{n+1} = b_n - m_n reads -n..k-1
            na, nb = {}, {}
            for w in itertools.product((0, 1), repeat=n + 1 + k):
                na[w] = a[w[:-1]] - m[w[:-1]]
                nb[w] = b[w[1:]] - m[w[1:]]
            a, b = na, nb
        r_last = sum(a.values()) / 2 ** (NSTEPS + k)
        print(f"B  {label}: r_n (n = 0..{NSTEPS}) = "
              + ", ".join(f"{float(r):.4g}" for r in rs + [r_last]))
        assert all(rs[i + 1] <= rs[i] for i in range(len(rs) - 1)) and r_last <= rs[-1]
        if k == 1:                                  # r_{2j} = r_{2j+1} = binom(2j, j) / 2^(2j+1)
            from math import comb
            full = rs + [r_last]
            assert all(full[n] == F(comb(2 * (n // 2), n // 2), 2 ** (2 * (n // 2) + 1))
                       for n in range(1, len(full)))
            print("   r_n = binom(2j, j) / 2^(2j+1) with j = floor(n/2), exactly, for 1 <= n <= 13")
        assert all(acc_proj[w] <= f_table[w] / 2 ** k for w in f_table)
        assert sum(acc_proj.values()) == 1 - r_last
        # Monte Carlo of the randomized rule: stage n tests h_n at T^n x, which reads x_0..x_{n+k-1}
        cnt = {w: 0 for w in f_table}
        runs = 200000
        for _ in range(runs):
            x = [rng.randint(0, 1) for _ in range(NSTEPS + k)]
            for n in range(NSTEPS):
                if rng.random() < hs[n][tuple(x[0:n + k])]:
                    cnt[tuple(x[n:n + k])] += 1
                    break
        dev = max(abs(cnt[w] / runs - float(acc_proj[w])) for w in f_table)
        print(f"   accepted by stage {NSTEPS - 1}: {float(1 - r_last):.4f}; Monte Carlo {runs} runs, "
              f"largest deviation from the exact accepted sub-law {dev:.4f}")
        assert dev < 0.005


def part_c():
    count = 0
    for n in range(1, 7):
        for rule in itertools.product(range(n), repeat=n):  # T(x) = x + 1 mod n, shift z by rule[z]
            dens = [0] * n
            for z in range(n):
                dens[(z + rule[z]) % n] += 1      # n times the law of T^{n(Z)} Z
            assert sum(dens) == n
            count += 1
    print(f"C  {count} deterministic shift rules on cycles of length 1..6: every density is integer-valued")


if __name__ == "__main__":
    rng = random.Random(20261016)
    part_a(rng)
    part_b(rng)
    part_c()
    print("all checks passed")
