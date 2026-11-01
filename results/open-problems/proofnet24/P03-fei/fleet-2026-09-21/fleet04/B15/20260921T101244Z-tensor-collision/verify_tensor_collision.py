from fractions import Fraction
import json


def walsh_int(values):
    a = [int(x) for x in values]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def v2(z):
    z = abs(int(z))
    if not z:
        raise ValueError("v2(0)")
    return (z & -z).bit_length() - 1


def profile(values):
    N = len(values)
    W = walsh_int(values)
    groups = {}
    for s, w in enumerate(W):
        if w:
            groups.setdefault(abs(w), []).append((s, 1 if w > 0 else -1))
    out = {}
    for m, entries in groups.items():
        eps = [0] * N
        for s, sign in entries:
            eps[s] = sign
        V = walsh_int(eps)
        r = min(v2(z) for z in V if z)
        out[m] = {"N": len(entries), "r": r}
    return out


def tensor(f, g):
    return [x*y for x in f for y in g]


def vals_from_positive_mask(n, mask):
    return [1 if ((mask >> i) & 1) else -1 for i in range(1 << n)]


def collision_defect(f, g):
    Nf, Ng = len(f), len(g)
    Nh = Nf * Ng
    pf, pg, ph = profile(f), profile(g), profile(tensor(f, g))
    pairs = {}
    for a, A in pf.items():
        for b, B in pg.items():
            c = a*b
            z = pairs.setdefault(c, {"N": 0, "weighted_rsum": 0, "min_rsum": None, "max_rsum": None})
            multiplicity = A["N"] * B["N"]
            rs = A["r"] + B["r"]
            z["N"] += multiplicity
            z["weighted_rsum"] += multiplicity * rs
            z["min_rsum"] = rs if z["min_rsum"] is None else min(z["min_rsum"], rs)
            z["max_rsum"] = rs if z["max_rsum"] is None else max(z["max_rsum"], rs)
    total = Fraction(0, 1)
    fibers = {}
    for c, z in sorted(pairs.items()):
        assert c in ph
        assert z["N"] == ph[c]["N"]
        rc = ph[c]["r"]
        term = Fraction(c*c, Nh*Nh) * (z["weighted_rsum"] - z["N"]*rc)
        total += term
        fibers[str(c)] = {
            **z,
            "merged_r": rc,
            "defect_num": term.numerator,
            "defect_den": term.denominator,
        }
    return total, pf, pg, ph, fibers


def exhaustive_3x3():
    funcs = [vals_from_positive_mask(3, mask) for mask in range(1 << (1 << 3))]
    positive = 0
    max_defect = Fraction(-10**9, 1)
    argmax = None
    for i, f in enumerate(funcs):
        for j, g in enumerate(funcs):
            d, *_ = collision_defect(f, g)
            if d > 0:
                positive += 1
                if positive <= 3:
                    raise AssertionError(("unexpected positive 3x3 defect", i, j, d))
            if d > max_defect:
                max_defect = d
                argmax = (i, j)
    return {
        "pairs": len(funcs)**2,
        "positive_defects": positive,
        "max_defect_num": max_defect.numerator,
        "max_defect_den": max_defect.denominator,
        "argmax": argmax,
    }


def main():
    f = vals_from_positive_mask(3, 0x37)
    g = vals_from_positive_mask(4, 0x5f75)
    d, pf, pg, ph, fibers = collision_defect(f, g)
    assert d == Fraction(27, 128), d
    assert fibers["12"]["defect_num"] == 27 and fibers["12"]["defect_den"] == 128
    assert sum(1 for z in fibers.values() if Fraction(z["defect_num"], z["defect_den"]) > 0) == 1
    small = exhaustive_3x3()
    out = {
        "counterexample": {
            "f_n": 3,
            "f_positive_mask_hex": "0x37",
            "g_n": 4,
            "g_positive_mask_hex": "0x5f75",
            "defect_num": d.numerator,
            "defect_den": d.denominator,
            "defect_float": float(d),
            "f_profile": pf,
            "g_profile": pg,
            "product_profile": ph,
            "collision_fibers": fibers,
        },
        "exhaustive_3x3": small,
        "status": "PASS",
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
