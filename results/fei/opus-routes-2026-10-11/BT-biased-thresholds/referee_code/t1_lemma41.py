"""Lemma 4.1 (least-element decomposition), exact check for ANY Boolean T, any product law, any order.

Claim: for S = B u {i}, i the last element of S in the order, B subset U_i (= coordinates before i):
   fhat(S) = sigma_i * ehat_i(B),  e_i = E[d_i | y_{U_i}],
so P(S) = sigma_i^2 ehat_i(B)^2 and ln(sigma_S^2/P(S)) = ln(sigma_B^2/ehat_i(B)^2) termwise, and
   Delta = sum_i sigma_i^2 I_mu(e_i).
In G-coordinates (fhat(S) = sigma_S G_f[S], ehat(B) = sigma_B G_e[B]) the termwise claim is
   G_f[B u {i}] == G_{e_i}[B]  exactly.
"""
import random
import sys
import time
from fractions import Fraction as Fr
from bfcore import *


def check(T, qs, order):
    n = len(qs)
    f = [2 * t - 1 for t in T]
    Gf = gtrans([Fr(v) for v in f], qs)
    P = [sigS2(S, qs) * Gf[S] ** 2 for S in range(1 << n)]
    Delta = sum((popcount(S) - 1) * P[S] for S in range(1 << n) if popcount(S) >= 2)
    Dsum = Fr(0)
    w = mu_weights(qs)
    for k, i in enumerate(order):
        U = order[:k]
        R = [c for c in range(n) if c != i and c not in U]
        d = pivotal(T, n, i)
        m = len(U)
        e = [Fr(0)] * (1 << m)
        # e(z) = sum_{y_R} mu_R(y_R) d(z, y_R)  (d independent of y_i)
        for z in range(1 << m):
            base = 0
            for b in range(m):
                if (z >> b) & 1:
                    base |= 1 << U[b]
            acc = Fr(0)
            for r in range(1 << len(R)):
                y = base
                pr = Fr(1)
                for b in range(len(R)):
                    if (r >> b) & 1:
                        y |= 1 << R[b]
                        pr *= qs[R[b]]
                    else:
                        pr *= 1 - qs[R[b]]
                acc += pr * d[y]
            e[z] = acc
        Ge = gtrans(e, [qs[c] for c in U])
        Ie = Fr(0)
        for Bl in range(1 << m):
            Bg = 0
            for b in range(m):
                if (Bl >> b) & 1:
                    Bg |= 1 << U[b]
            if Gf[Bg | (1 << i)] != Ge[Bl]:
                return False, ("termwise", i, Bg)
            Ie += popcount(Bl) * sigS2(Bg, qs) * Ge[Bl] ** 2
        Dsum += sig2(qs[i]) * Ie
    if Dsum != Delta:
        return False, ("Delta", Dsum, Delta)
    return True, None


def rq(extreme=False):
    if extreme and random.random() < 0.3:
        return random.choice([Fr(1, 10 ** 6), Fr(10 ** 6 - 1, 10 ** 6), Fr(1, 997), Fr(996, 997)])
    return Fr(random.randint(1, 999), 1000)


if __name__ == "__main__":
    random.seed(41)
    t0 = time.time()
    tot = 0
    fails = []
    # n <= 3: every function, every order, 6 bias vectors each
    for n in range(1, 4):
        orders = list(itertools.permutations(range(n)))
        for code in range(1 << (1 << n)):
            T = [(code >> y) & 1 for y in range(1 << n)]
            for rep in range(6):
                qs = [rq(True) for _ in range(n)]
                order = list(random.choice(orders))
                ok, info = check(T, qs, order)
                tot += 1
                if not ok:
                    fails.append((n, code, qs, order, info))
    print("n<=3 all functions:", tot, "cases, fails", len(fails), "time", round(time.time() - t0, 1))
    # n = 4: every one of the 65536 functions, one random (bias, order) each
    n = 4
    orders = list(itertools.permutations(range(n)))
    c4 = 0
    for code in range(1 << 16):
        T = [(code >> y) & 1 for y in range(16)]
        qs = [rq(True) for _ in range(n)]
        order = list(random.choice(orders))
        ok, info = check(T, qs, order)
        c4 += 1
        if not ok:
            fails.append((n, code, qs, order, info))
    print("n=4 all 65536 functions:", c4, "cases, total fails", len(fails), "time", round(time.time() - t0, 1))
    if fails:
        print("FIRST FAILS", fails[:5])
    sys.stdout.flush()
