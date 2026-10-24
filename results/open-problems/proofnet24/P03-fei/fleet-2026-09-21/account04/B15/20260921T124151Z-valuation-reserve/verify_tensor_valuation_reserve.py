from fractions import Fraction


def popcount(x):
    return x.bit_count()


def walsh_from_positive_mask(n, positive_mask):
    vals = [1 if ((positive_mask >> x) & 1) else -1 for x in range(1 << n)]
    W = []
    for s in range(1 << n):
        total = 0
        for x, v in enumerate(vals):
            total += v * (-1 if (popcount(s & x) & 1) else 1)
        W.append(total)
    return vals, W


def nu2(z):
    z = abs(z)
    if z == 0:
        raise ValueError("nu2(0)")
    return (z & -z).bit_length() - 1


def packet_reserve(n, W):
    groups = {}
    for s, w in enumerate(W):
        if w:
            groups.setdefault(abs(w), []).append((s, 1 if w > 0 else -1))
    reserve = Fraction(0)
    for absw, items in groups.items():
        vals = []
        for x in range(1 << n):
            v = sum(
                sgn * (-1 if (popcount(s & x) & 1) else 1)
                for s, sgn in items
            )
            vals.append(v)
        r = min(nu2(v) for v in vals if v)
        p = Fraction(len(items) * absw * absw, 1 << (2 * n))
        reserve += p * r
    return reserve


def influence(n, W):
    return Fraction(
        sum(popcount(s) * w * w for s, w in enumerate(W)),
        1 << (2 * n),
    )


def tensor_positive_mask(n_a, mask_a, n_b, mask_b):
    vals_a, _ = walsh_from_positive_mask(n_a, mask_a)
    vals_b, _ = walsh_from_positive_mask(n_b, mask_b)
    mask = 0
    for xb, vb in enumerate(vals_b):
        for xa, va in enumerate(vals_a):
            if va * vb == 1:
                mask |= 1 << (xa | (xb << n_a))
    return n_a + n_b, mask


def reserve(n, mask):
    _, W = walsh_from_positive_mask(n, mask)
    return packet_reserve(n, W), influence(n, W)


# Previously exhibited positive D-collision defect.
ra, ia = reserve(3, 0x37)
rb, ib = reserve(4, 0x5F75)
nt, mt = tensor_positive_mask(3, 0x37, 4, 0x5F75)
rt, it = reserve(nt, mt)
assert (ra, rb, rt, ra + rb - rt) == (
    Fraction(0),
    Fraction(3, 8),
    Fraction(21, 128),
    Fraction(27, 128),
)
assert it == ia + ib

# A second example with nonzero reserve in both factors.
ra2, ia2 = reserve(4, 0x6094)
rb2, ib2 = reserve(4, 0x0EE7)
nt2, mt2 = tensor_positive_mask(4, 0x6094, 4, 0x0EE7)
rt2, it2 = reserve(nt2, mt2)
assert (ra2, rb2, rt2, ra2 + rb2 - rt2) == (
    Fraction(3, 8),
    Fraction(1),
    Fraction(271, 256),
    Fraction(81, 256),
)
assert it2 == ia2 + ib2

# Finite sanity check: all ordered 3-bit x 3-bit Boolean pairs.
r3 = {}
for mask in range(256):
    r3[mask], _ = reserve(3, mask)
positive = 0
for a in range(256):
    for b in range(256):
        nt, mt = tensor_positive_mask(3, a, 3, b)
        rt, _ = reserve(nt, mt)
        if r3[a] + r3[b] - rt > 0:
            positive += 1
assert positive == 0

print("PASS")
print("known_positive_defect", Fraction(27, 128))
print("known_reserve_before", Fraction(3, 8))
print("known_reserve_after", Fraction(21, 128))
print("both_nonzero_defect", Fraction(81, 256))
print("both_nonzero_reserve_before", Fraction(11, 8))
print("both_nonzero_reserve_after", Fraction(271, 256))
print("ordered_3bit_pairs", 65536)
print("ordered_3bit_positive_defects", positive)
