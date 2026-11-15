"""Section 5 of arXiv 2610.28208 (Chen, Huang: the linear MDS conjecture in even characteristic) on real arcs.

Setting of Lemma 5.1 and Proposition 5.2: q = 2m, 1 <= h <= m - 2, lines L_a (a in a set of size q + 2 - h) in
PG(2, q) with no three concurrent, J = product of the L_a, I = (X1^m, X2^m, X3^m), G = F_q[X1, X2, X3]/(I : J).
Claims tested:
  (i)   (I : J)_r = 0 for 0 <= r <= h - 3                       (Lemma 5.1)
  (ii)  kappa = dim (I : J)_{h-2} <= h - 1                      (Proposition 5.2)
  (iii) the Hilbert function of G is symmetric about s/2, s = m + h - 5, and unimodal (q = 8, 16 only)
The lines are sub-families of dual hyperovals: the conic (1, t, t^2) with (0, 0, 1) and the nucleus (0, 1, 0),
and for q = 32 also the translation hyperoval (1, t, t^4).  Control: with three concurrent lines put into the
family, and with a pencil of lines.  h runs over 1..m-1 (the range of Lemma 5.1; the main proof uses h <= m-2).
"""
import random
import sys
import time


class GF2e:
    def __init__(self, e, poly):
        self.q = 1 << e
        self.exp = [0] * (2 * self.q)
        self.log = [0] * self.q
        x = 1
        for i in range(self.q - 1):
            self.exp[i] = x
            self.log[x] = i
            x <<= 1
            if x & self.q:
                x ^= poly
        assert x == 1, "polynomial not primitive"
        for i in range(self.q - 1, 2 * self.q):
            self.exp[i] = self.exp[i - (self.q - 1)]

    def mul(self, a, b):
        return 0 if a == 0 or b == 0 else self.exp[self.log[a] + self.log[b]]

    def inv(self, a):
        return self.exp[self.q - 1 - self.log[a]]

    def pw(self, a, n):
        return 0 if a == 0 else self.exp[(self.log[a] * n) % (self.q - 1)]


def det3(F, a, b, c):
    m = F.mul
    return (m(a[0], m(b[1], c[2]) ^ m(b[2], c[1])) ^ m(a[1], m(b[0], c[2]) ^ m(b[2], c[0])) ^ m(a[2], m(b[0], c[1]) ^ m(b[1], c[0])))


def is_arc(F, pts):
    n = len(pts)
    return all(det3(F, pts[i], pts[j], pts[k]) for i in range(n) for j in range(i + 1, n) for k in range(j + 1, n))


def product_of_lines(F, lines):
    J = {(0, 0, 0): 1}
    for (a, b, c) in lines:
        N = {}
        for (i, j, k), v in J.items():
            for co, mon in ((a, (i + 1, j, k)), (b, (i, j + 1, k)), (c, (i, j, k + 1))):
                if co:
                    N[mon] = N.get(mon, 0) ^ F.mul(co, v)
        J = {k: v for k, v in N.items() if v}
    return J


def monos(d, cap=None):
    out = []
    for i in range(d + 1):
        for j in range(d - i + 1):
            k = d - i - j
            if cap is None or (i < cap and j < cap and k < cap):
                out.append((i, j, k))
    return out


def rank(F, rows):
    rows = [r[:] for r in rows]
    rk = 0
    ncol = len(rows[0]) if rows else 0
    for c in range(ncol):
        piv = next((i for i in range(rk, len(rows)) if rows[i][c]), None)
        if piv is None:
            continue
        rows[rk], rows[piv] = rows[piv], rows[rk]
        inv = F.inv(rows[rk][c])
        pr = [F.mul(inv, x) for x in rows[rk]]
        rows[rk] = pr
        for i in range(len(rows)):
            if i != rk and rows[i][c]:
                f = rows[i][c]
                ri = rows[i]
                rows[i] = [x ^ F.mul(f, y) for x, y in zip(ri, pr)]
        rk += 1
        if rk == len(rows):
            break
    return rk


def colon_dim(F, J, degJ, m, r):
    """dim of {T in R_r : J T in (X1^m, X2^m, X3^m)}."""
    src = monos(r)
    tgt = monos(degJ + r, cap=m)
    if not tgt:
        return len(src)
    rows = []
    for (u1, u2, u3) in src:
        rows.append([J.get((w1 - u1, w2 - u2, w3 - u3), 0) if w1 >= u1 and w2 >= u2 and w3 >= u3 else 0 for (w1, w2, w3) in tgt])
    return len(src) - rank(F, rows)


def run_family(F, name, lines, m, h, full):
    q = 2 * m
    assert len(lines) == q + 2 - h
    J = product_of_lines(F, lines)
    degJ = q + 2 - h
    s = m + h - 5
    top = s if full else h - 2
    cd = [colon_dim(F, J, degJ, m, r) for r in range(0, max(top, -1) + 1)]
    inj = all(cd[r] == 0 for r in range(0, h - 2)) if h >= 3 else True
    kappa = cd[h - 2] if h >= 2 else 0
    line = "%-26s q %2d h %2d: (I:J)_r = 0 for r <= h-3: %s; kappa %d (bound %d): %s" % (name, q, h, inj, kappa, h - 1, kappa <= h - 1)
    if full and s >= 0:
        H = [len(monos(r)) - cd[r] for r in range(s + 1)]
        sym = H == H[::-1]
        peak = H.index(max(H))
        uni = all(H[i] <= H[i + 1] for i in range(peak)) and all(H[i] >= H[i + 1] for i in range(peak, s))
        line += "; H_G %s symmetric %s unimodal %s" % (H, sym, uni)
    print(line)
    return inj and kappa <= h - 1


def main():
    t0 = time.time()
    rng = random.Random(7)
    ok = True
    for e, poly in ((3, 0b1011), (4, 0b10011), (5, 0b100101)):
        F = GF2e(e, poly)
        q, m = F.q, F.q // 2
        fams = {"conic+nucleus": [(1, t, F.mul(t, t)) for t in range(q)] + [(0, 0, 1), (0, 1, 0)]}
        if e == 5:
            fams["translation t^4"] = [(1, t, F.pw(t, 4)) for t in range(q)] + [(0, 0, 1), (0, 1, 0)]
        for name, hyp in fams.items():
            assert len(hyp) == q + 2 and is_arc(F, hyp), "not a hyperoval"
            for h in range(1, m):
                ok &= run_family(F, name + " first", hyp[: q + 2 - h], m, h, full=(e <= 4))
                sub = rng.sample(hyp, q + 2 - h)
                ok &= run_family(F, name + " random", sub, m, h, full=False)
        # arcs grown point by point in random order (not chosen inside a hyperoval)
        allpts = [(1, x, y) for x in range(q) for y in range(q)] + [(0, 1, x) for x in range(q)] + [(0, 0, 1)]
        best = {}
        for trial in range(40 if e <= 4 else 12):
            order = allpts[:]
            rng.shuffle(order)
            arc = []
            for pt in order:
                if all(det3(F, arc[i], arc[j], pt) for i in range(len(arc)) for j in range(i + 1, len(arc))):
                    arc.append(pt)
            for h in range(1, m):
                if len(arc) >= q + 2 - h and h not in best:
                    best[h] = arc[: q + 2 - h]
        print("grown arcs, q %d: sizes needed %d..%d, found for h in %s" % (q, q + 3 - m, q + 1, sorted(best)))
        for h in sorted(best):
            ok &= run_family(F, "grown arc", best[h], m, h, full=(e <= 4))
        # control: three concurrent lines (all through the point (0, 0, 1), i.e. third coefficient 0)
        if e == 4:
            for h in (4, 5, 6):
                bad = [(1, 0, 0), (0, 1, 0), (1, 1, 0)] + fams["conic+nucleus"][3: q + 2 - h]
                J = product_of_lines(F, bad)
                cd = [colon_dim(F, J, q + 2 - h, m, r) for r in range(0, h - 1)]
                print("control, three concurrent lines, q %d h %d: dim (I:J)_r for r = 0..h-2: %s (bound for the last %d)" % (q, h, cd, h - 1))
            # control: every line through one point (a pencil); J is then a binary form of degree q + 2 - h
            for h in (3, 4, 5):
                pencil = ([(1, t, 0) for t in range(q)] + [(0, 1, 0)])[: q + 2 - h]
                J = product_of_lines(F, pencil)
                cd = [colon_dim(F, J, q + 2 - h, m, r) for r in range(0, h - 1)]
                print("control, pencil of %d lines, q %d h %d: dim (I:J)_r for r = 0..h-2: %s (Lemma 5.1 would give 0 for r <= %d)" % (len(pencil), q, h, cd, h - 3))
    print("all tested families satisfy (i) and (ii): %s" % ok)
    print("time %.1f s" % (time.time() - t0))


if __name__ == "__main__":
    main()
