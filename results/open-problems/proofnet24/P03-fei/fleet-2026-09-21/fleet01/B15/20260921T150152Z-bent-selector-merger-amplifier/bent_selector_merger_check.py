from collections import Counter
from fractions import Fraction


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def nu2(x):
    x = abs(x)
    assert x
    return (x & -x).bit_length() - 1


def bent_values(r):
    n = 2*r
    out = []
    for x in range(1 << n):
        q = 0
        for j in range(r):
            q ^= ((x >> (2*j)) & 1) & ((x >> (2*j+1)) & 1)
        out.append(1 if q == 0 else -1)
    return out


def packet_depth(walsh, mag):
    sign_coeff = [0 if abs(c) != mag else (1 if c > 0 else -1) for c in walsh]
    vals = fwht(sign_coeff)
    return min(nu2(v) for v in vals if v)


def check(r):
    M = 1 << (2*r)
    rootM = 1 << r
    g = bent_values(r)
    Wg = fwht(g)
    assert set(abs(c) for c in Wg) == {rootM}
    assert Wg[0] == rootM

    # Selector coordinate t: t=0 gives g; t=1 gives the constant -1.
    F = g + [-1]*M
    WF = fwht(F)

    expected = Counter({
        rootM: 2*(M-1),
        rootM*(rootM-1): 1,
        rootM*(rootM+1): 1,
    })
    actual = Counter(abs(c) for c in WF if c)
    assert actual == expected

    depths = {mag: packet_depth(WF, mag) for mag in actual}
    assert depths[rootM] == 1
    assert depths[rootM*(rootM-1)] == 0
    assert depths[rootM*(rootM+1)] == 0

    # On the t=0 branch the child is g. Its only magnitude packet has carry depth r.
    child_signs = [1 if c > 0 else -1 for c in Wg]
    child_vals = fwht(child_signs)
    child_depth = min(nu2(v) for v in child_vals if v)
    assert child_depth == r

    # Split the child packet by parent-pair ancestry. T != empty comes from the
    # repeated small parent magnitude; T = empty comes from the two unequal
    # exceptional magnitudes. Both source groups separately have depth zero.
    bulk = list(child_signs)
    bulk[0] = 0
    singleton = [0]*M
    singleton[0] = child_signs[0]
    bulk_depth = min(nu2(v) for v in fwht(bulk) if v)
    singleton_depth = min(nu2(v) for v in fwht(singleton) if v)
    assert bulk_depth == 0
    assert singleton_depth == 0
    assert [bulk[i] + singleton[i] for i in range(M)] == child_signs

    influence_t = Fraction(sum(v == 1 for v in g), M)
    assert influence_t == Fraction(rootM+1, 2*rootM)

    p_small = Fraction(M-1, 2*M)
    avg_child_R = Fraction(r, 2)
    raw_valuation_gain = avg_child_R - p_small
    assert raw_valuation_gain == Fraction((r-1)*M+1, 2*M)

    return {
        "r": r,
        "parent_magnitude_numerators": dict(sorted(actual.items())),
        "parent_packet_depths": dict(sorted(depths.items())),
        "child_depth": child_depth,
        "ancestry_depths": (bulk_depth, singleton_depth),
        "ancestry_counts": (M-1, 1),
        "influence_t": str(influence_t),
        "raw_avg_valuation_gain": str(raw_valuation_gain),
    }


def main():
    print("B15_BENT_SELECTOR_MERGER_CHECK")
    for r in range(2, 7):
        print(check(r))
    print("PASS")


if __name__ == "__main__":
    main()
