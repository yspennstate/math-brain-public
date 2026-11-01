from fractions import Fraction
from itertools import combinations, permutations, product


def count_pattern(seq, I, J):
    # x,y,b use I; z uses J. Equal external gaps are allowed; seq fixes tie order.
    total = 0
    for gx, gy, gb, gz in product(I, I, I, J):
        g = {'x': gx, 'y': gy, 'b': gb, 'z': gz}
        if all(g[u] <= g[v] for u, v in zip(seq, seq[1:])):
            total += 1
    return total


def interval_regression():
    n2 = n3 = 0
    # Pattern II: x<y<z; b||z.  I=[0,m-1], J=[d,m-1+e].
    for m in range(1, 9):
        I = range(0, m)
        for d in range(0, m + 1):
            for e in range(0, 5):
                J = range(d, m + e)
                if not list(J):
                    continue
                seqs = ['bxyz', 'xbyz', 'xybz', 'xyzb']
                A = [count_pattern(s, I, J) for s in seqs]
                assert A[0] == A[1] == A[2]
                assert A[3] <= A[2]
                den = sum(A)
                p = Fraction(A[2] + A[3], den)  # y<b
                assert Fraction(1, 3) <= p <= Fraction(1, 2)
                n2 += 1

    # Pattern III: x<y and z<b; z||x,y. I=[0,m-1], J=[-e,m-1-d].
    for m in range(1, 9):
        I = range(0, m)
        for e in range(0, 5):
            for d in range(0, m):
                J = range(-e, m - d)
                seqs = ['xyzb', 'xzyb', 'xzby', 'zxyb', 'zxby', 'zbxy']
                A = [count_pattern(s, I, J) for s in seqs]
                assert A[1] == A[2]
                assert A[3] == A[4] == A[5]
                assert A[0] <= A[3]
                den = sum(A)
                p = Fraction(A[0] + A[1] + A[3], den)  # y<b
                assert Fraction(1, 3) <= p <= Fraction(1, 2)
                n3 += 1
    return n2, n3


def transitive_closure(n, edges):
    R = set(edges)
    changed = True
    while changed:
        changed = False
        add = set()
        for a, b in R:
            for c, d in R:
                if b == c and (a, d) not in R:
                    add.add((a, d))
        if add:
            R |= add
            changed = True
    return frozenset(R)


def naturally_labeled_posets(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    seen = set()
    for mask in range(1 << len(pairs)):
        edges = [pairs[k] for k in range(len(pairs)) if (mask >> k) & 1]
        seen.add(transitive_closure(n, edges))
    return sorted(seen, key=lambda x: (len(x), tuple(sorted(x))))


def comparable(R, a, b):
    return (a, b) in R or (b, a) in R


def width(n, R):
    best = 1
    for mask in range(1, 1 << n):
        elems = [i for i in range(n) if (mask >> i) & 1]
        if len(elems) <= best:
            continue
        if all(not comparable(R, a, b) for a, b in combinations(elems, 2)):
            best = len(elems)
    return best


def is_cover(R, x, y):
    if (x, y) not in R:
        return False
    return not any((x, z) in R and (z, y) in R
                   for z in range(max(y + 1, 1)) if z not in (x, y))


def linear_extensions(n, R):
    preds = [0] * n
    for a, b in R:
        preds[b] |= 1 << a
    out = []

    def rec(mask, cur):
        if len(cur) == n:
            out.append(tuple(cur))
            return
        for v in range(n):
            if (mask >> v) & 1:
                continue
            if preds[v] & ~mask == 0:
                rec(mask | (1 << v), cur + [v])

    rec(0, [])
    return out


def rel(R, z, a):
    if (z, a) in R:
        return -1
    if (a, z) in R:
        return 1
    return 0


def distinguishers(n, R, a, b):
    return {z for z in range(n)
            if z not in (a, b) and rel(R, z, a) != rel(R, z, b)}


def before_count(exts, a, b):
    return sum(e.index(a) < e.index(b) for e in exts)


def exhaustive_regression():
    unique = {}
    w3 = {}
    cover_configs = 0
    hyp_cases = 0
    strong_flips = 0
    min_union = None

    for n in range(3, 7):
        Ps = naturally_labeled_posets(n)
        unique[n] = len(Ps)
        good = [R for R in Ps if width(n, R) <= 3]
        w3[n] = len(good)
        for R in good:
            exts = linear_extensions(n, R)
            E = len(exts)
            for x in range(n):
                for y in range(n):
                    if not is_cover(R, x, y):
                        continue
                    for b in range(n):
                        if b in (x, y) or comparable(R, b, x) or comparable(R, b, y):
                            continue
                        cover_configs += 1
                        Dx = distinguishers(n, R, x, b) - {y}
                        Dy = distinguishers(n, R, y, b) - {x}
                        u = Dx | Dy
                        Nx = before_count(exts, x, b)
                        Ny = before_count(exts, y, b)
                        balx = 3 * Nx >= E and 3 * Nx <= 2 * E
                        baly = 3 * Ny >= E and 3 * Ny <= 2 * E
                        if len(u) <= 1:
                            hyp_cases += 1
                            assert balx or baly
                        if 3 * Nx > 2 * E and 3 * Ny < E:
                            strong_flips += 1
                            min_union = len(u) if min_union is None else min(min_union, len(u))
                            assert len(u) >= 2
    return unique, w3, cover_configs, hyp_cases, strong_flips, min_union


def sharp_witness():
    n = 5
    R = transitive_closure(n, [(0, 2), (0, 3), (1, 2)])
    exts = linear_extensions(n, R)
    E = len(exts)
    x, y, b = 0, 2, 4
    Nx = before_count(exts, x, b)
    Ny = before_count(exts, y, b)
    gap = sum(e.index(x) < e.index(b) < e.index(y) for e in exts)
    Dx = distinguishers(n, R, x, b) - {y}
    Dy = distinguishers(n, R, y, b) - {x}
    probs = {}
    for a, c in combinations(range(n), 2):
        if not comparable(R, a, c):
            probs[(a, c)] = Fraction(before_count(exts, a, c), E)

    assert E == 25 and Nx == 18 and Ny == 7 and gap == 11
    assert Dx == {3} and Dy == {1}
    assert probs == {
        (0, 1): Fraction(3, 5), (0, 4): Fraction(18, 25),
        (1, 3): Fraction(4, 5), (1, 4): Fraction(16, 25),
        (2, 3): Fraction(2, 5), (2, 4): Fraction(7, 25),
        (3, 4): Fraction(9, 25)
    }
    return E, Nx, Ny, gap, Dx, Dy, probs


if __name__ == '__main__':
    n2, n3 = interval_regression()
    unique, w3, cfg, hyp, strong, minu = exhaustive_regression()
    E, Nx, Ny, gap, Dx, Dy, probs = sharp_witness()
    print('pattern_II_interval_cases', n2)
    print('pattern_III_interval_cases', n3)
    print('unique_transitive_closures_by_n', ' '.join(f'{n}:{unique[n]}' for n in sorted(unique)))
    print('width_le3_closures_by_n', ' '.join(f'{n}:{w3[n]}' for n in sorted(w3)))
    print('cover_configs_checked', cfg)
    print('cover_two_witness_hypothesis_cases', hyp)
    print('strong_flip_cases', strong)
    print('minimum_external_union_on_strong_flip', minu)
    print('sharp_witness', 'E', E, 'px', f'{Nx}/{E}', 'py', f'{Ny}/{E}', 'gap', f'{gap}/{E}',
          'Dx_extra', sorted(Dx), 'Dy_extra', sorted(Dy))
    print('sharp_incomparable_probabilities', ' '.join(f'{a}-{b}:{p}' for (a, b), p in sorted(probs.items())))
    print('POS3_COVER_FLUX_TWO_WITNESS_REGRESSION_PASS')
