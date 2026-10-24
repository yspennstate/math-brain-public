#!/usr/bin/env python3
"""Independent deterministic audit of B05's retained-difference telescope.

This checker does not import the author's code.  Walsh coefficients and
upper-set masses are exact Fractions; only logarithms are evaluated with
70-digit Decimal arithmetic.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
import itertools

getcontext().prec = 70
LN2 = Decimal(2).ln()
C = Decimal(3) / LN2
EPS = Decimal("1e-55")


def D(q: Fraction) -> Decimal:
    return Decimal(q.numerator) / Decimal(q.denominator)


def log2(x: Fraction) -> Decimal:
    return D(x).ln() / LN2


def walsh(values):
    n = len(values)
    out = []
    for mask in range(n):
        total = 0
        for x, value in enumerate(values):
            total += value * (-1 if ((mask & x).bit_count() & 1) else 1)
        out.append(Fraction(total, n))
    return out


def raw_entropy(coeff):
    ans = Decimal(0)
    for x in coeff:
        p = x * x
        if p:
            ans += D(p) * (-log2(p))
    return ans


def upper_u(coeff):
    p = [x * x for x in coeff]
    pi = p[:]
    bits = (len(p) - 1).bit_length()
    for b in range(bits):
        bit = 1 << b
        for s in range(len(p)):
            if not (s & bit):
                pi[s] += pi[s | bit]
    ans = Decimal(0)
    for mass, cap in zip(p, pi):
        if mass:
            ans += D(mass) * log2(cap / mass)
    return ans


def hu_from_coeff(coeff):
    return raw_entropy(coeff), upper_u(coeff)


def node_from_coeff(a, b):
    u = [(x + y) / 2 for x, y in zip(a, b)]
    v = [(x - y) / 2 for x, y in zip(a, b)]
    parent = u + v
    hg, ug = hu_from_coeff(a)
    hh, uh = hu_from_coeff(b)
    hp, up = hu_from_coeff(parent)
    q = sum((x * x for x in v), Fraction(0))
    ld = raw_entropy(v)
    m = [x * x + y * y for x, y in zip(u, v)]
    hm = Decimal(0)
    pair = Decimal(0)
    for x, y, mass in zip(u, v, m):
        if not mass:
            continue
        hm += D(mass) * (-log2(mass))
        xu, yv = x * x, y * y
        if xu:
            pair += D(xu) * log2(mass / xu)
        if yv:
            pair += D(yv) * log2(mass / yv)
    js = hm - (hg + hh) / 2
    ent_err = (hp - (hg + hh) / 2) - (js + pair)
    vparent, vg, vh = hp - up, hg - ug, hh - uh
    lhs = up - (ug + uh) / 2
    rhs = -vparent + (vg + vh) / 2 + ld + C * D(q)
    return {
        "q": q, "ld": ld, "lhs": lhs, "rhs": rhs,
        "ent_err": ent_err,
        "js_slack": Decimal(2) * D(q) / LN2 - js,
        "pair_slack": ld + D(q) / LN2 - pair,
        "local_slack": rhs - lhs,
    }


def bool_functions(n):
    size = 1 << n
    for code in range(1 << size):
        yield [1 if (code >> i) & 1 else -1 for i in range(size)]


def exhaustive_nodes():
    count = 0
    min_js = min_pair = min_local = None
    max_err = Decimal(0)
    for n in range(4):
        coeffs = [walsh(f) for f in bool_functions(n)]
        # Full high-precision enumeration through two bits.  At three bits,
        # take a deterministic phase/bias-spanning 32-function slice; the
        # author's separate float checker exhausts all 65,536 pairs.
        if n == 3:
            coeffs = coeffs[::8]
        for a in coeffs:
            for b in coeffs:
                z = node_from_coeff(a, b)
                count += 1
                max_err = max(max_err, abs(z["ent_err"]))
                min_js = z["js_slack"] if min_js is None else min(min_js, z["js_slack"])
                min_pair = z["pair_slack"] if min_pair is None else min(min_pair, z["pair_slack"])
                min_local = z["local_slack"] if min_local is None else min(min_local, z["local_slack"])
                assert abs(z["ent_err"]) < EPS
                assert z["js_slack"] > -EPS
                assert z["pair_slack"] > -EPS
                assert z["local_slack"] > -EPS
    return count, max_err, min_js, min_pair, min_local


def eval_full_tree(leaves):
    # data bit 0; z0,z1,z2 are bits 1,2,3.  Both subtrees share the data bit.
    vals = []
    for x in range(16):
        data = x & 1
        z0, z1, z2 = (x >> 1) & 1, (x >> 2) & 1, (x >> 3) & 1
        idx = (2 + z2) if z0 else z1
        vals.append(leaves[idx][data])
    return vals


def extend_leaf(leaf):
    return [leaf[x & 1] for x in range(16)]


def eval_child(leaves, right):
    vals = []
    for x in range(16):
        data = x & 1
        z = ((x >> 3) & 1) if right else ((x >> 2) & 1)
        base = 2 if right else 0
        vals.append(leaves[base + z][data])
    return vals


def full_tree_audit():
    funcs = list(bool_functions(1))
    count = 0
    min_slack = None
    max_tel = Decimal(0)
    for leaves in itertools.product(funcs, repeat=4):
        root = eval_full_tree(leaves)
        left, right = eval_child(leaves, False), eval_child(leaves, True)
        ext = [extend_leaf(x) for x in leaves]
        hr, ur = hu_from_coeff(walsh(root))
        child_hu = [hu_from_coeff(walsh(x)) for x in (left, right)]
        leaf_hu = [hu_from_coeff(walsh(x)) for x in ext]
        root_node = node_from_coeff(walsh(left), walsh(right))
        left_node = node_from_coeff(walsh(ext[0]), walsh(ext[1]))
        right_node = node_from_coeff(walsh(ext[2]), walsh(ext[3]))
        node_sum = root_node["lhs"] + (left_node["lhs"] + right_node["lhs"]) / 2
        terminal_u = sum((u for h, u in leaf_hu), Decimal(0)) / 4
        terminal_v = sum((h - u for h, u in leaf_hu), Decimal(0)) / 4
        isel = D(root_node["q"]) + (D(left_node["q"]) + D(right_node["q"])) / 2
        lsum = root_node["ld"] + (left_node["ld"] + right_node["ld"]) / 2
        rhs = terminal_v - (hr - ur) + lsum + C * isel
        lhs = ur - terminal_u
        tel = abs(node_sum - lhs)
        slack = rhs - lhs
        count += 1
        max_tel = max(max_tel, tel)
        min_slack = slack if min_slack is None else min(min_slack, slack)
        assert tel < EPS
        assert slack > -EPS
    return count, max_tel, min_slack


def scalar_grid():
    count = 0
    min_slack = None
    for i in range(-50, 51):
        for j in range(-50, 51):
            x, y = Fraction(i, 17), Fraction(j, 19)
            s = x * x + y * y
            if not s:
                continue
            lhs = Decimal(0)
            if x:
                lhs += D(x * x) * log2(2 * x * x / s) / 2
            if y:
                lhs += D(y * y) * log2(2 * y * y / s) / 2
            rhs = D((x - y) * (x - y)) / (2 * LN2)
            slack = rhs - lhs
            count += 1
            min_slack = slack if min_slack is None else min(min_slack, slack)
            assert slack > -EPS
    return count, min_slack


def repeated_selector_control():
    # Root queries z.  On z=0 return -1.  On z=1 a child formally queries z
    # again, with branches +1 and -1.  On consistent assignments the function
    # is constant -1, hence physical influence is zero, while the formal child
    # ledger charges reach*(disagreement)=1/2.
    physical_influence = Fraction(0)
    formal_node_sum = Fraction(1, 2)
    assert physical_influence != formal_node_sum
    return physical_influence, formal_node_sum


def main():
    sc, ss = scalar_grid()
    nc, err, js, pair, local = exhaustive_nodes()
    tc, terr, tslack = full_tree_audit()
    phys, formal = repeated_selector_control()
    print("independent retained-difference telescope review")
    print(f"precision_digits={getcontext().prec}")
    print(f"scalar_rational_pairs={sc} min_slack={ss}")
    print(f"boolean_node_pairs={nc} max_entropy_identity_error={err}")
    print(f"min_js_slack={js}")
    print(f"min_pair_slack={pair}")
    print(f"min_local_U_slack={local}")
    print(f"shared-data_full_binary_trees={tc} max_telescope_error={terr}")
    print(f"min_tree_slack={tslack}")
    print(f"reused_selector_control physical={phys} formal_node_sum={formal}")
    print("PASS")


if __name__ == "__main__":
    main()
