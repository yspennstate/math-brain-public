from fractions import Fraction
from itertools import product, combinations

def points(n):
    return list(product((0, 1), repeat=n))

def table(mask, n):
    return {x: (1 if (mask >> k) & 1 else -1) for k, x in enumerate(points(n))}

def influence(f, n, i):
    others = [k for k in range(n) if k != i]
    hit = 0
    for z in product((0, 1), repeat=n - 1):
        x0 = [0] * n
        x1 = [0] * n
        for a, k in enumerate(others):
            x0[k] = x1[k] = z[a]
        x0[i], x1[i] = 0, 1
        hit += f[tuple(x0)] != f[tuple(x1)]
    return Fraction(hit, 2 ** (n - 1))

def centered_gauge(f, n):
    flip = {i for i in range(n) if influence(f, n, i) > Fraction(1, 2)}
    out = {}
    for x, v in f.items():
        chi = 1
        for i in flip:
            chi *= (-1 if x[i] == 0 else 1)
        out[x] = v * chi
    return out

def support_change(f, n, i, j):
    others = [k for k in range(n) if k not in (i, j)]
    hit = 0
    for z in product((0, 1), repeat=n - 2):
        vals = []
        for jv in (0, 1):
            x0 = [0] * n
            x1 = [0] * n
            for a, k in enumerate(others):
                x0[k] = x1[k] = z[a]
            x0[j] = x1[j] = jv
            x0[i], x1[i] = 0, 1
            vals.append(int(f[tuple(x0)] != f[tuple(x1)]))
        hit += vals[0] != vals[1]
    return Fraction(hit, 2 ** (n - 2))

def crossing(f, n, target, reveal):
    others = [k for k in range(n) if k not in (target, reveal)]
    post = []
    for rv in (0, 1):
        hit = 0
        for z in product((0, 1), repeat=n - 2):
            x0 = [0] * n
            x1 = [0] * n
            for a, k in enumerate(others):
                x0[k] = x1[k] = z[a]
            x0[reveal] = x1[reveal] = rv
            x0[target], x1[target] = 0, 1
            hit += f[tuple(x0)] != f[tuple(x1)]
        post.append(Fraction(hit, 2 ** (n - 2)))
    a, b = post
    return (max(2 * a - 1, 0) + max(2 * b - 1, 0)) / 2

def derivative_value(f, n, i, j, jv, z):
    others = [k for k in range(n) if k not in (i, j)]
    x0 = [0] * n
    x1 = [0] * n
    for a, k in enumerate(others):
        x0[k] = x1[k] = z[a]
    x0[j] = x1[j] = jv
    x0[i], x1[i] = 0, 1
    return Fraction(f[tuple(x1)] - f[tuple(x0)], 2)

def curvature_and_opposite(f, n, i, j):
    kap = Fraction(0)
    opp = Fraction(0)
    for z in product((0, 1), repeat=n - 2):
        g0 = derivative_value(f, n, i, j, 0, z)
        g1 = derivative_value(f, n, i, j, 1, z)
        kap += (g0 - g1) ** 2
        opp += int(g0 * g1 < 0)
    den = 2 ** (n - 2)
    return kap / den, opp / den

def local_face_check():
    # Every +/-1 labelling of a two-face.
    for mask in range(16):
        f = table(mask, 2)
        p01 = support_change(f, 2, 0, 1)
        p10 = support_change(f, 2, 1, 0)
        k01, o01 = curvature_and_opposite(f, 2, 0, 1)
        k10, o10 = curvature_and_opposite(f, 2, 1, 0)
        assert p01 == p10
        assert k01 == k10
        assert o01 == o10
        assert k01 == p01 + 4 * o01

def exhaustive_centered_check():
    functions = 0
    unordered_pairs = 0
    for n in (2, 3):
        for mask in range(2 ** (2 ** n)):
            f = centered_gauge(table(mask, n), n)
            assert all(influence(f, n, i) <= Fraction(1, 2) for i in range(n))
            for i, j in combinations(range(n), 2):
                p = support_change(f, n, i, j)
                assert p == support_change(f, n, j, i)
                c_ij = crossing(f, n, i, j)
                c_ji = crossing(f, n, j, i)
                assert 2 * c_ij <= p
                assert 2 * c_ji <= p
                zeta = p - c_ij - c_ji
                assert zeta >= 0
                kap, o = curvature_and_opposite(f, n, i, j)
                kap2, o2 = curvature_and_opposite(f, n, j, i)
                assert kap == kap2 and o == o2 and kap == p + 4 * o
                xi = zeta + 4 * o
                omega_ij = p - 2 * c_ij + 4 * o
                omega_ji = p - 2 * c_ji + 4 * o
                assert omega_ij == xi + c_ji - c_ij
                assert omega_ji == xi + c_ij - c_ji
                assert (omega_ij + omega_ji) / 2 == xi
                unordered_pairs += 1
            functions += 1
    return functions, unordered_pairs

if __name__ == "__main__":
    local_face_check()
    fcount, pcount = exhaustive_centered_check()
    print("two_face_labelings", 16)
    print("centered_functions", fcount)
    print("unordered_pair_checks", pcount)
    print("RESULT PASS")
