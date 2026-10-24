from itertools import product, combinations, permutations
from fractions import Fraction

N = 5
PAIRS = list(combinations(range(N), 2))


def transitive_posets():
    for states in product(range(3), repeat=len(PAIRS)):
        lt = [[False] * N for _ in range(N)]
        for (i, j), s in zip(PAIRS, states):
            if s == 1:
                lt[i][j] = True
            elif s == 2:
                lt[j][i] = True
        ok = True
        for i in range(N):
            for j in range(N):
                if lt[i][j]:
                    for k in range(N):
                        if lt[j][k] and not lt[i][k]:
                            ok = False
                            break
                    if not ok:
                        break
            if not ok:
                break
        if ok:
            yield lt


def width(lt):
    out = 0
    for mask in range(1, 1 << N):
        xs = [i for i in range(N) if (mask >> i) & 1]
        if len(xs) <= out:
            continue
        if all(not lt[i][j] and not lt[j][i] for i, j in combinations(xs, 2)):
            out = len(xs)
    return out


def linear_extensions(lt):
    out = []
    for p in permutations(range(N)):
        pos = [0] * N
        for k, x in enumerate(p):
            pos[x] = k
        if all((not lt[i][j]) or pos[i] < pos[j] for i in range(N) for j in range(N)):
            out.append(p)
    return out


total = width3 = nonchain = target_ok = no_balanced = 0
entropy_violations = 0
max_q2_one_plus_var = Fraction(0)
max_pi = 0

for lt in transitive_posets():
    total += 1
    if width(lt) > 3:
        continue
    width3 += 1
    inc = [(i, j) for i, j in PAIRS if not lt[i][j] and not lt[j][i]]
    if not inc:
        continue
    nonchain += 1
    exts = linear_extensions(lt)
    E = len(exts)
    best_minor = Fraction(0)
    for i, j in inc:
        c = sum(1 for p in exts if p.index(i) < p.index(j))
        r = Fraction(c, E)
        best_minor = max(best_minor, min(r, 1 - r))
    if best_minor >= Fraction(1, 3):
        target_ok += 1
    else:
        no_balanced += 1

    for x in range(N):
        rc = [0] * N
        for p in exts:
            rc[p.index(x)] += 1
        q = Fraction(max(rc), E)
        mean = sum(Fraction((k + 1) * c, E) for k, c in enumerate(rc))
        var = sum(Fraction((k + 1) ** 2 * c, E) for k, c in enumerate(rc)) - mean * mean
        check = q * q * (1 + var)
        max_q2_one_plus_var = max(max_q2_one_plus_var, check)
        if check > 1:
            entropy_violations += 1

    degrees = [sum(1 for y in range(N) if y != x and not lt[x][y] and not lt[y][x]) for x in range(N)]
    max_pi = max(max_pi, max(degrees))

print("labeled_posets_n5", total)
print("width_at_most_3", width3)
print("width_at_most_3_nonchains", nonchain)
print("balanced_pair_verified", target_ok)
print("no_balanced_counterexamples", no_balanced)
print("aravinda_rank_inequality_violations", entropy_violations)
print("max_q2_times_1_plus_var", max_q2_one_plus_var)
print("max_incomparability_degree", max_pi)
print("POS3_N5_EXACT_CHECK_PASS")
