"""Exact check of Lemma A and Lemma B of FLOW section 11(i) by enumeration of all sign patterns.

R = sum_j w_j eps_j, weights in (0, a].
  Lemma A:  for 0 <= c <= alpha:   P[alpha <= R <= alpha + a] <= 2 P[c - a <= R <= c + a].
  Lemma B:  for t >= 0:            P[R > t + a] <= (16/3) (1 + sigma/a) P[|R - t| <= a].
Candidates for (c, alpha) are aligned to the atoms of R (where the two sides jump), plus random points.

usage: python lemmaA_check.py reps maxn seed
"""
import sys
import numpy as np

EPS = 1e-9


def sums(ws):
    s = np.zeros(1)
    for w in ws:
        s = np.concatenate([s - w, s + w])
    return np.sort(s)


def mass(s, lo, hi):
    """P[lo <= R <= hi] with a tolerance of EPS/10 on both ends (closed interval)."""
    i = np.searchsorted(s, lo - EPS / 10, side='left')
    j = np.searchsorted(s, hi + EPS / 10, side='right')
    return (j - i) / len(s)


def check(ws, a, rng, npts=60):
    s = sums(ws)
    atoms = np.unique(np.round(s, 9))
    sig = float(np.sqrt(sum(w * w for w in ws)))
    top = float(atoms[-1])
    worstA = (0.0, None)
    worstB = (0.0, None)
    # alpha candidates: atoms >= 0 and atoms - a >= 0 (interval ends on an atom), a few random
    ca = np.concatenate([atoms[atoms >= 0], atoms[atoms - a >= 0] - a, rng.random(5) * (top + a)])
    ca = np.unique(ca[ca >= 0])
    if len(ca) > npts:
        ca = rng.choice(ca, npts, replace=False)
    for al in ca:
        num = mass(s, al, al + a)
        if num == 0:
            continue
        # c candidates in [0, al]: window just misses an atom on either side
        cc = np.concatenate([[0.0, al], atoms + a + EPS, atoms - a - EPS, rng.random(5) * al])
        cc = np.unique(cc[(cc >= 0) & (cc <= al)])
        if len(cc) > npts:
            cc = np.concatenate([[0.0, al], rng.choice(cc, npts, replace=False)])
        for c in cc:
            den = mass(s, c - a, c + a)
            r = float('inf') if den == 0 else num / den
            if r > worstA[0]:
                worstA = (r, (float(c), float(al)))
    # Lemma B: t candidates
    ct = np.concatenate([[0.0], atoms + a + EPS, atoms - a - EPS, atoms - a + EPS, rng.random(5) * top])
    ct = np.unique(ct[(ct >= 0) & (ct <= top)])
    if len(ct) > 4 * npts:
        ct = rng.choice(ct, 4 * npts, replace=False)
    for t in ct:
        tail = 1.0 - np.searchsorted(s, t + a + EPS / 10, side='right') / len(s)
        if tail <= 0:
            continue
        den = mass(s, t - a, t + a)
        r = float('inf') if den == 0 else tail / ((1 + sig / a) * den)
        if r > worstB[0]:
            worstB = (r, float(t))
    return worstA, worstB


def main():
    reps, maxn, seed = (int(x) for x in sys.argv[1:4])
    rng = np.random.default_rng(seed)
    topA = 0.0
    topB = 0.0
    for rep in range(reps):
        n = int(rng.integers(1, maxn + 1))
        kind = int(rng.integers(0, 7))
        if kind == 0:
            ws = list(rng.random(n) * 0.999 + 0.001)
        elif kind == 1:
            ws = [float(x) for x in rng.integers(1, 7, n)]
        elif kind == 2:
            ws = [1.0] * n
        elif kind == 3:
            ws = list(0.5 + 0.5 * rng.random(n))            # all steps above half the cap
        elif kind == 4:
            ws = [1.0] * int(rng.integers(1, 4)) + list(rng.random(n) * 0.2 + 0.001)
        elif kind == 5:
            ws = list(rng.random(n) ** 4 + 0.001)
        else:
            ws = [float(2.0 ** (-j)) for j in range(n)]
        ws = ws[:maxn]
        m = max(ws)
        a = float(rng.choice([m, m, m, 1.25 * m, 2 * m]))
        wa, wb = check(ws, a, rng)
        if wa[0] > topA:
            topA = wa[0]
            print('A=%.4f (c, alpha)=%s a=%.3f n=%d kind=%d' % (wa[0], wa[1], a, len(ws), kind))
        if wb[0] > topB:
            topB = wb[0]
            print('B=%.4f t=%s a=%.3f n=%d kind=%d (bound 16/3 = 5.333)' % (wb[0], wb[1], a, len(ws), kind))
        sys.stdout.flush()
    print('max A = %.4f (bound 2)   max B = %.4f (bound 5.3333)   %d weight sets' % (topA, topB, reps))


if __name__ == '__main__':
    main()
