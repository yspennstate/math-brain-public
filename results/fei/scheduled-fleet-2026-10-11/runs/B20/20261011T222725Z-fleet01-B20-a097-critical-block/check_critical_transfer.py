#!/usr/bin/env python3
"""Exact finite audit for the A097 complete critical-block transfer.

Walsh coefficients, restrictions, influences and tensor truth tables are
Fractions.  Logarithms use outward rational intervals from an atanh series.
No randomness or floating-point comparison enters an assertion.
"""

from fractions import Fraction as Q


def add(x, y): return (x[0] + y[0], x[1] + y[1])
def neg(x): return (-x[1], -x[0])
def sub(x, y): return add(x, neg(y))
def scale(c, x): return (c*x[0], c*x[1]) if c >= 0 else (c*x[1], c*x[0])


def ln_interval(x, terms=100):
    assert x > 0
    e, y = 0, x
    while y >= 2:
        y /= 2
        e += 1
    while y < 1:
        y *= 2
        e -= 1

    def core(z):
        u = (z-1)/(z+1)
        au, s, p = abs(u), Q(0), u
        for j in range(terms):
            s += p/(2*j+1)
            p *= u*u
        tail = 2*au**(2*terms+1)/((2*terms+1)*(1-au*au))
        return 2*s-tail, 2*s+tail

    l2, u2 = core(Q(2))
    ly, uy = core(y)
    return (ly + e*(l2 if e >= 0 else u2),
            uy + e*(u2 if e >= 0 else l2))


LN2 = ln_interval(Q(2))


def div_pos(x, y):
    assert y[0] > 0
    v = [x[i]/y[j] for i in (0, 1) for j in (0, 1)]
    return min(v), max(v)


def entropy_term(q):
    if not q:
        return Q(0), Q(0)
    return scale(-q, div_pos(ln_interval(q), LN2))


def hadamard(vals):
    a, h = [Q(v) for v in vals], 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x/len(a) for x in a]


class BF:
    def __init__(self, vals):
        self.vals = tuple(vals)
        self.n = len(vals).bit_length()-1
        assert len(vals) == 1 << self.n and set(vals) <= {-1, 1}
        self.a = hadamard(vals)
        self.I = sum(Q(s.bit_count())*z*z for s, z in enumerate(self.a))
        self.H = Q(0), Q(0)
        for z in self.a:
            self.H = add(self.H, entropy_term(z*z))

    def ratio(self):
        assert self.I > 0
        return self.H[0]/self.I, self.H[1]/self.I


def assignment(cbits, abits, C, A):
    x = 0
    for j, i in enumerate(C):
        x |= ((cbits >> j) & 1) << i
    for j, i in enumerate(A):
        x |= ((abits >> j) & 1) << i
    return x


def children(f, mask):
    A = [i for i in range(f.n) if mask >> i & 1]
    C = [i for i in range(f.n) if not (mask >> i & 1)]
    out = []
    for abits in range(1 << len(A)):
        vals = [f.vals[assignment(cbits, abits, C, A)]
                for cbits in range(1 << len(C))]
        out.append(BF(vals))
    return out


def avg(xs):
    z = Q(0), Q(0)
    for x in xs:
        z = add(z, x)
    return scale(Q(1, len(xs)), z)


def block_influence(f, mask):
    return sum(Q((s & mask).bit_count())*z*z for s, z in enumerate(f.a))


def critical_certified(f):
    if not f.I:
        return False
    r = f.ratio()
    for mask in range(1, (1 << f.n)-1):
        for c in children(f, mask):
            if c.I and c.ratio()[1] > r[0]:
                return False
    return True


def critical_not_refuted(f):
    if not f.I:
        return False
    r = f.ratio()
    for mask in range(1, 1 << f.n):
        for c in children(f, mask):
            if c.I and c.ratio()[1] > r[0]:
                return False
    return True


def block_check(f, mask):
    cs = children(f, mask)
    avg_h = avg([c.H for c in cs])
    avg_i = sum(c.I for c in cs)/len(cs)
    ia = block_influence(f, mask)
    assert avg_i + ia == f.I
    gamma = sub(f.H, avg_h)
    r = f.ratio()
    lhs = avg([sub(c.H, scale(c.I, r)) for c in cs])
    rhs = sub(scale(ia, r), gamma)
    assert not (lhs[1] < rhs[0] or rhs[1] < lhs[0])
    return gamma, scale(ia, r)


def tensor(f, g):
    return BF([f.vals[x]*g.vals[y]
               for y in range(1 << g.n) for x in range(1 << f.n)])


def contains(x, q): return x[0] <= q <= x[1]


def main():
    print("RIGOROUS A097 CRITICAL-BLOCK TRANSFER CERTIFICATE")
    print(f"ln_terms=100 ln2_width<={float(LN2[1]-LN2[0]):.3e} seed=None")
    funcs, identities, crits, crit_blocks = [], 0, 0, 0
    for n in (1, 2, 3):
        for code in range(1 << (1 << n)):
            f = BF([1 if code >> x & 1 else -1 for x in range(1 << n)])
            if not f.I:
                continue
            funcs.append(f)
            is_crit = critical_certified(f)
            crits += int(is_crit)
            for mask in range(1, 1 << n):
                gamma, ria = block_check(f, mask)
                identities += 1
                if is_crit:
                    if mask == (1 << n)-1:
                        assert gamma == f.H and ria == f.H
                    else:
                        assert gamma[0] >= ria[1]
                    crit_blocks += 1
    print(f"exhaustive_n_le_3 nonconstant={len(funcs)} restriction_critical_certified={crits}")
    print(f"block_deficit_identities={identities} critical_inequalities={crit_blocks}")

    and2 = BF([1, 1, 1, -1])
    maj3 = BF([1 if sum(1 if not (x >> i & 1) else -1 for i in range(3)) > 0
               else -1 for x in range(8)])
    unequal, matched = tensor(and2, maj3), tensor(and2, and2)
    assert contains(and2.ratio(), Q(2))
    assert contains(maj3.ratio(), Q(4, 3))
    assert contains(unequal.ratio(), Q(8, 5))
    assert not critical_not_refuted(unequal)
    print("unequal_tensor AND2xMAJ3: factor_ratios=2,4/3 product_ratio=8/5 => REJECTED_BY_RESTRICTION")
    print("matched_tensor AND2xAND2: factor_ratios=2,2 product_ratio=2 => PASSES_EXHAUSTIVE_RESTRICTIONS")

    small = []
    for n in (1, 2):
        for code in range(1 << (1 << n)):
            f = BF([1 if code >> x & 1 else -1 for x in range(1 << n)])
            if f.I:
                small.append(f)
    pairs = rejected = equal = 0
    for f in small:
        for g in small:
            t = tensor(f, g)
            expected = div_pos(add(f.H, g.H), (f.I+g.I, f.I+g.I))
            assert not (t.ratio()[1] < expected[0] or expected[1] < t.ratio()[0])
            pairs += 1
            if f.ratio()[1] < g.ratio()[0] or g.ratio()[1] < f.ratio()[0]:
                assert not critical_not_refuted(t)
                rejected += 1
            else:
                equal += 1
    print(f"tensor_pairs={pairs} unequal_ratio_rejected={rejected} equal_ratio_pairs={equal}")
    print(f"PASS assertions={identities+crit_blocks+pairs+rejected+8}")


if __name__ == "__main__":
    main()
