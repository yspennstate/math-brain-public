from itertools import combinations, permutations
from fractions import Fraction


def natural_closures(n):
    pairs = list(combinations(range(n), 2))
    seen = {}
    for mask in range(1 << len(pairs)):
        rel = [[False] * n for _ in range(n)]
        for k, (i, j) in enumerate(pairs):
            if (mask >> k) & 1:
                rel[i][j] = True
        for k in range(n):
            for i in range(n):
                if rel[i][k]:
                    for j in range(n):
                        if rel[k][j]:
                            rel[i][j] = True
        canon = 0
        for k, (i, j) in enumerate(pairs):
            if rel[i][j]:
                canon |= 1 << k
        if canon not in seen:
            seen[canon] = rel
    return seen


def extension_positions(rel):
    n = len(rel)
    ans = []
    for word in permutations(range(n)):
        pos = [0] * n
        for i, v in enumerate(word):
            pos[v] = i
        good = True
        for i in range(n):
            for j in range(n):
                if rel[i][j] and pos[i] > pos[j]:
                    good = False
                    break
            if not good:
                break
        if good:
            ans.append(pos)
    return ans


closures_total = 0
starts = 0
terminal_tests = 0
failures = 0
minimum_slack = None

for n in range(3, 7):
    closures = natural_closures(n)
    closures_total += len(closures)
    for rel in closures.values():
        pred = [{i for i in range(n) if rel[i][v]} for v in range(n)]
        succ = [{j for j in range(n) if rel[v][j]} for v in range(n)]
        exts = extension_positions(rel)
        E = len(exts)

        # q[x][y] = Pr(y<x), stored as exact numerator.
        qnum = [[0] * n for _ in range(n)]
        for pos in exts:
            for x in range(n):
                for y in range(n):
                    if x != y and pos[y] < pos[x]:
                        qnum[x][y] += 1

        covers = []
        for a in range(n):
            for b in range(n):
                if not rel[a][b]:
                    continue
                if not any(rel[a][z] and rel[z][b]
                           for z in range(n) if z not in (a, b)):
                    covers.append((a, b))

        for x in range(n):
            for y0 in range(n):
                if x == y0 or rel[x][y0] or rel[y0][x]:
                    continue
                if not pred[x].issubset(pred[y0]):
                    continue
                if succ[y0].issubset(succ[x]):
                    continue
                starts += 1

                T = [z for z in range(n)
                     if (z == y0 or rel[y0][z])
                     and z != x and not rel[x][z] and not rel[z][x]]
                maximal = [z for z in T
                           if not any(rel[z][w] for w in T)]

                for ym in maximal:
                    assert ym != y0
                    assert succ[ym].issubset(succ[x])
                    assert pred[x].issubset(pred[ym])

                    previous = [d for d, z in covers
                                if z == ym and d in T
                                and (d == y0 or rel[y0][d])]
                    assert previous

                    q0 = Fraction(qnum[x][y0], E)
                    qm = Fraction(qnum[x][ym], E)
                    for d in previous:
                        terminal_tests += 1
                        qd = Fraction(qnum[x][d], E)
                        slack = qd / 2 - qm
                        if minimum_slack is None or slack < minimum_slack:
                            minimum_slack = slack
                        if slack < 0 or q0 - qm < q0 / 2:
                            failures += 1

print("naturally_labelled_transitive_closures", closures_total)
print("noncrossed_successor_starts", starts)
print("terminal_cover_tests", terminal_tests)
print("terminal_or_charge_failures", failures)
print("minimum_terminal_halving_slack", minimum_slack)
assert closures_total == 5228
assert starts == 18967
assert terminal_tests == 23323
assert failures == 0
assert minimum_slack == 0
print("POS3_SUCCESSOR_STAIRCASE_HALF_CHARGE_PASS")
