"""Checks for the card-cyclic-to-random lower bound.

1. The pair-order proposition: Q f_ij = Phi(M e_i wedge M e_j) on
   every deck, n = 3..6, in exact arithmetic.
2. The eigenfunction Psi_n built from the two eigenvectors: Q Psi_n = lambda_n Psi_n on every deck,
   n = 5..7, in floating point.
3. The constant a, the root z, z = 1 + W_1(-1/e), the zeros of F_n near 0 and z,
   n log|lambda_n| -> -a, and Psi_n(id)/n^2 -> A (Section 3 and Lemma 4.1).
4. Small decks: exact total variation from every starting deck.

Decks are tuples read from the top; card i is above card j if it comes first.
Requires mpmath.
"""
from fractions import Fraction as Fr
from itertools import permutations
import mpmath as mp

mp.mp.dps = 40


def outcomes(w, label):
    """The n equally likely decks after reinserting `label`."""
    rest = tuple(x for x in w if x != label)
    return [rest[:p] + (label,) + rest[p:] for p in range(len(w))]


def q_outcomes(w):
    """One step of the rotating-frame chain: reinsert card 1, then relabel."""
    n = len(w)
    return [tuple(n if x == 1 else x - 1 for x in v) for v in outcomes(w, 1)]


def f(w, i, j):
    return 1 if w.index(i) < w.index(j) else -1


def wedge_image(n, i, j):
    """Coefficients of M e_i wedge M e_j as a dict {(k, l): c}, k != l."""
    def Me(i):
        return {i + 1: Fr(1)} if i < n else {l: Fr(1, n) for l in range(2, n + 1)}
    out = {}
    for k, ck in Me(i).items():
        for l, cl in Me(j).items():
            if k != l:
                out[(k, l)] = out.get((k, l), 0) + ck * cl
    return out


def check_wedge(n):
    decks = list(permutations(range(1, n + 1)))
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            img = wedge_image(n, i, j)
            for w in decks:
                lhs = Fr(sum(f(v, i, j) for v in q_outcomes(w)), n)
                rhs = sum(c * f(w, k, l) for (k, l), c in img.items())
                if lhs != rhs:
                    return False
    return True


def Fn(s, n):
    return mp.fsum(mp.e ** (-k * s / n) for k in range(1, n)) / n - 1


def vec(s, n):
    return [mp.mpf(0)] + [mp.fsum(mp.e ** (-k * s / n) for k in range(1, j)) / n for j in range(2, n + 1)]


def constants():
    h = lambda b: b * mp.cot(b) - 1 - mp.log(b / mp.sin(b))
    b = mp.findroot(h, 7.46)
    a = mp.log(b / mp.sin(b))
    z = mp.mpc(-a, b)
    return a, b, z


def psi(n, a, z):
    s0 = mp.findroot(lambda s: Fn(s, n), -2.0 / n)
    s1 = mp.findroot(lambda s: Fn(s, n), z)
    u, v = vec(s0, n), vec(s1, n)
    coef = {(i, j): u[i - 1] * v[j - 1] - u[j - 1] * v[i - 1] for i in range(1, n + 1) for j in range(i + 1, n + 1)}
    lam = mp.e ** ((s0 + s1) / n)
    return s0, s1, lam, coef


def psi_value(w, coef):
    return mp.fsum(c * f(w, i, j) for (i, j), c in coef.items())


def tv_profile(n, tmax):
    """Exact worst-start TV of the original chain for t = 0..tmax, and the TV from each start."""
    decks = list(permutations(range(1, n + 1)))
    N = len(decks)
    rows = {}
    for w0 in decks:
        dist = {w0: 1}
        prof = []
        for t in range(tmax + 1):
            den = n ** t
            tv = Fr(sum(abs(Fr(c, den) - Fr(1, N)) for c in dist.values()) + Fr(N - len(dist), N), 2)
            prof.append(tv)
            label = 1 + t % n
            new = {}
            for w, c in dist.items():
                for v in outcomes(w, label):
                    new[v] = new.get(v, 0) + c
            dist = new
        rows[w0] = prof
    return rows


def main():
    bad = 0
    for n in range(3, 7):
        ok = check_wedge(n)
        print("Prop 2.2, n=%d, every deck: %s" % (n, "ok" if ok else "FAIL"))
        bad += not ok

    a, b, z = constants()
    print("a = %s\nb = %s" % (mp.nstr(a, 20), mp.nstr(b, 20)))
    ok = abs(mp.e ** (-z) - (1 - z)) < mp.mpf(10) ** -30 and abs(z - (1 + mp.lambertw(-1 / mp.e, 1))) < mp.mpf(10) ** -30
    print("e^-z = 1-z and z = 1+W_1(-1/e): %s" % ("ok" if ok else "FAIL"))
    bad += not ok
    A = -mp.mpf(2) / (3 * z) - 1 / z ** 2
    print("A = %s,  1/(2a) = %s" % (mp.nstr(A, 12), mp.nstr(1 / (2 * a), 20)))

    for n in (5, 6, 7):
        s0, s1, lam, coef = psi(n, a, z)
        err = max(abs(mp.fsum(psi_value(v, coef) for v in q_outcomes(w)) / n - lam * psi_value(w, coef))
                  for w in permutations(range(1, n + 1)))
        ok = err < mp.mpf(10) ** -25
        print("Q Psi = lambda Psi, n=%d, every deck: max error %s %s" % (n, mp.nstr(err, 3), "ok" if ok else "FAIL"))
        bad += not ok

    print("   n    n*s0      n*(s1-z)         n*log|lambda|+a   n*(n*log|lambda|+a)   Psi(id)/n^2")
    for n in (25, 50, 100, 200, 400):
        s0, s1, lam, coef = psi(n, a, z)
        x = n * mp.log(abs(lam)) + a
        val = psi_value(tuple(range(1, n + 1)), coef) / n ** 2
        print("%4d  %8s  %22s  %12s  %12s  %s" % (n, mp.nstr(n * s0, 6), mp.nstr(n * (s1 - z), 6), mp.nstr(x, 6),
                                                  mp.nstr(n * x, 6), mp.nstr(val, 8)))

    rows = tv_profile(3, 8)
    ok = all(rows[w][t] == Fr(1, 2 * 3 ** (t - 1)) for w in rows for t in range(1, 9))
    print("n=3: d(t) = (1/2) 3^-(t-1) from every deck, t=1..8: %s" % ("ok" if ok else "FAIL"))
    bad += not ok
    thr = []
    for n in range(2, 7):
        rows = tv_profile(n, 8)
        worst = [max(r[t] for r in rows.values()) for t in range(9)]
        thr.append(next(t for t in range(9) if worst[t] <= Fr(1, 4)))
        if n == 4:
            r1, r2 = rows[(1, 2, 3, 4)][5], rows[(1, 2, 4, 3)][5]
            ok = (r1, r2) == (Fr(1, 32), Fr(3, 64))
            print("n=4, t=5: TV from 1234 = %s, from 1243 = %s: %s" % (r1, r2, "ok" if ok else "FAIL"))
            bad += not ok
    ok = thr == [1, 2, 3, 5, 6]
    print("worst-start t_mix(1/4), n=2..6: %s %s" % (thr, "ok" if ok else "FAIL"))
    bad += not ok
    print("all checks passed" if bad == 0 else "%d check(s) failed" % bad)
    return bad


if __name__ == "__main__":
    raise SystemExit(main())
