from itertools import combinations, permutations
from fractions import Fraction


def closure(n, mask):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    R = [[False] * n for _ in range(n)]
    for bit, (i, j) in enumerate(pairs):
        if (mask >> bit) & 1:
            R[i][j] = True
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    if R[k][j]:
                        R[i][j] = True
    bits = sum((1 << bit) for bit, (i, j) in enumerate(pairs) if R[i][j])
    return bits, R


def width_at_most_three(n, R):
    for S in combinations(range(n), 4):
        if all(
            not ((i < j and R[i][j]) or (j < i and R[j][i]))
            for i, j in combinations(S, 2)
        ):
            return False
    return True


def linear_extensions(n, R):
    ans = []
    for p in permutations(range(n)):
        pos = {x: i for i, x in enumerate(p)}
        if all(
            (not R[i][j]) or pos[i] < pos[j]
            for i in range(n)
            for j in range(i + 1, n)
        ):
            ans.append(p)
    return ans


def qualifying_checks(n, R, exts):
    E = len(exts)

    def p_before(a, b):
        return Fraction(sum(p.index(a) < p.index(b) for p in exts), E)

    checked = endpoint = 0
    endpoint_atoms = []
    endpoint_mus = []

    for x in range(n):
        inc = [
            y
            for y in range(n)
            if y != x
            and not ((y < x and R[y][x]) or (x < y and R[x][y]))
        ]
        if not inc:
            continue
        if any(Fraction(1, 3) <= p_before(x, y) <= Fraction(2, 3) for y in inc):
            continue

        D = {y for y in range(n) if y != x and p_before(y, x) > Fraction(2, 3)}
        U = {y for y in range(n) if y != x and p_before(x, y) > Fraction(2, 3)}
        assert D | U == set(range(n)) - {x}
        assert not (D & U)

        qexts = set(tuple(z for z in p if z != x) for p in exts)
        sumW = sumC = sumW2 = sumFact = 0
        is_endpoint = (not D) or (not U)

        for tau in qexts:
            pos = {z: i + 1 for i, z in enumerate(tau)}
            preds = [y for y in tau if y < x and R[y][x]]
            succs = [y for y in tau if x < y and R[x][y]]
            a = max((pos[y] for y in preds), default=0)
            b = min((pos[y] - 1 for y in succs), default=n - 1)
            W = b - a + 1
            corridor = list(tau[a:b])

            base = sum(1 for y in inc if y in U and pos[y] <= a)
            base += sum(1 for y in inc if y in D and pos[y] > b)
            C = W * base
            for t, y in enumerate(corridor, 1):
                assert y in inc
                C += t if y in D else W - t

            assert C >= (W * W) // 4
            if is_endpoint:
                assert C == W * (W - 1) // 2

            sumW += W
            sumC += C
            sumW2 += W * W
            sumFact += W * (W - 1)

        assert sumW == E
        minority_mass = sum(
            p_before(x, y) if y in D else p_before(y, x) for y in inc
        )
        assert minority_mass == Fraction(sumC, sumW)

        m = len(inc)
        NQ = len(qexts)
        mu = Fraction(sumW, NQ)
        assert Fraction(sumC, NQ) < Fraction(m, 3) * mu
        assert Fraction(sumW2, NQ) < Fraction(4 * m, 3) * mu + 1

        if is_endpoint:
            atom = Fraction(NQ, E)
            assert atom > Fraction(4, 9)
            assert mu < Fraction(9, 4)
            assert Fraction(sumFact, NQ) < Fraction(2 * m, 3) * mu
            assert Fraction(sumW2, NQ) < Fraction(3 * m, 2) + Fraction(9, 4)
            endpoint_atoms.append(atom)
            endpoint_mus.append(mu)
            endpoint += 1

        checked += 1

    return checked, endpoint, endpoint_atoms, endpoint_mus


grand_posets = grand_cases = grand_endpoints = 0
all_endpoint_atoms = []
all_endpoint_mus = []

for n in range(1, 7):
    pairs = n * (n - 1) // 2
    seen = {}
    for mask in range(1 << pairs):
        bits, R = closure(n, mask)
        seen.setdefault(bits, R)

    width3 = cases = endpoints = 0
    for R in seen.values():
        if not width_at_most_three(n, R):
            continue
        width3 += 1
        c, e, atoms, mus = qualifying_checks(n, R, linear_extensions(n, R))
        cases += c
        endpoints += e
        all_endpoint_atoms.extend(atoms)
        all_endpoint_mus.extend(mus)

    grand_posets += width3
    grand_cases += cases
    grand_endpoints += endpoints
    print(f"n={n} width_le_3={width3} qualifying_x={cases} endpoint_x={endpoints}")

print(
    f"TOTAL width_le_3={grand_posets} qualifying_x={grand_cases} "
    f"endpoint_x={grand_endpoints}"
)
print(f"MIN_ENDPOINT_ATOM={min(all_endpoint_atoms) if all_endpoint_atoms else 'NA'}")
print(f"MAX_ENDPOINT_MEAN_W={max(all_endpoint_mus) if all_endpoint_mus else 'NA'}")
print("POS3_INSERTION_MOMENT_CHECK_PASS")
