from fractions import Fraction
from itertools import combinations, product
from collections import Counter


def rank_cols(cols):
    if not cols:
        return 0
    m = len(cols[0]); n = len(cols)
    A = [[Fraction(cols[j][i]) for j in range(n)] for i in range(m)]
    row = col = 0
    while row < m and col < n:
        pivot = next((i for i in range(row, m) if A[i][col]), None)
        if pivot is None:
            col += 1
            continue
        A[row], A[pivot] = A[pivot], A[row]
        p = A[row][col]
        A[row] = [x / p for x in A[row]]
        for i in range(m):
            if i != row and A[i][col]:
                f = A[i][col]
                A[i] = [A[i][j] - f * A[row][j] for j in range(n)]
        row += 1; col += 1
    return row


def dissociated(V, idxs):
    zero = (0,) * len(V[0])
    sums = {zero}
    for i in idxs:
        v = V[i]
        shifted = {tuple(a + b for a, b in zip(s, v)) for s in sums}
        if sums & shifted:
            return False
        sums |= shifted
    return True


def maximal_sets(V):
    N = len(V); out = []
    for mask in range(1 << N):
        S = [i for i in range(N) if (mask >> i) & 1]
        if not dissociated(V, S):
            continue
        if all((mask >> j) & 1 or not dissociated(V, S + [j]) for j in range(N)):
            out.append(tuple(S))
    return out


def neg_width(V, S, target):
    m = len(V[0]); best = None
    for coeff in product((-1, 0, 1), repeat=len(S)):
        vec = [0] * m
        for c, i in zip(coeff, S):
            if c:
                for d in range(m):
                    vec[d] += c * V[i][d]
        if tuple(vec) == V[target]:
            b = sum(c == -1 for c in coeff)
            if best is None or b < best:
                best = b
    assert best is not None
    return best


def full_profile(V):
    r = rank_cols(V)
    MS = maximal_sets(V)
    widths = {}
    for S in MS:
        widths[S] = {i: (0 if i in S else neg_width(V, S, i)) for i in range(len(V))}
    maxw = max(max(w.values()) for w in widths.values())
    rho = {}
    for k in range(maxw + 2):
        best = r + 1
        for S, w in widths.items():
            H = [i for i, z in w.items() if z > k]
            hr = rank_cols([V[i] for i in H]) if H else 0
            best = min(best, hr)
        rho[k] = best
    return rho, MS, widths


def minimum_support_relation(V):
    N = len(V); m = len(V[0]); best = None
    for coeff in product((-1, 0, 1), repeat=N):
        if not any(coeff):
            continue
        total = [0] * m
        for c, v in zip(coeff, V):
            if c:
                for d in range(m):
                    total[d] += c * v[d]
        if any(total):
            continue
        support = {i for i, c in enumerate(coeff) if c}
        candidate = (len(support), tuple(coeff), support)
        if best is None or candidate[0] < best[0]:
            best = candidate
    return best


def theorem_construction(V):
    r = rank_cols(V)
    relation = minimum_support_relation(V)
    assert relation is not None
    _, coeff, support = relation
    P = [i for i, c in enumerate(coeff) if c == 1]
    N = [i for i, c in enumerate(coeff) if c == -1]
    assert P and N
    side = P if len(P) <= len(N) else N
    t = side[0]
    S = [i for i in support if i != t]
    assert dissociated(V, S)
    for j in range(len(V)):
        if j == t or j in S:
            continue
        if dissociated(V, S + [j]):
            S.append(j)
    S = tuple(sorted(S))
    assert t not in S
    assert all(j in S or not dissociated(V, list(S) + [j]) for j in range(len(V)))
    width_t = neg_width(V, S, t)
    assert width_t <= r // 2
    assert len(V) - len(S) <= 2
    return S, t, width_t


def main():
    config_count = 0
    profile_checks = 0
    construction_checks = 0
    omission_checks = 0
    profile_shapes = Counter()
    max_maximal_sets = 0
    max_ratio = Fraction(0)
    max_ratio_witness = None

    for m in range(1, 5):
        universe = [tuple((x >> i) & 1 for i in range(m)) for x in range(1, 2 ** m)]
        local = 0
        for N in range(1, min(len(universe), m + 2) + 1):
            for V in combinations(universe, N):
                r = rank_cols(V)
                if N - r != 2:
                    continue
                local += 1; config_count += 1
                rho, MS, widths = full_profile(V)
                max_maximal_sets = max(max_maximal_sets, len(MS))

                # Lemma 3.1 and high-threshold width statement.
                for S in MS:
                    assert len(V) - len(S) <= 2
                    omission_checks += 1
                    for i, w in widths[S].items():
                        if i not in S:
                            assert w <= len(S) - 1

                # The full candidate inequality on every exact profile value.
                for k, z in rho.items():
                    assert (k + 1) * z <= r
                    ratio = Fraction((k + 1) * z, r)
                    if ratio > max_ratio:
                        max_ratio = ratio
                        max_ratio_witness = (m, V, r, k, z, dict(rho))
                    profile_checks += 1
                profile_shapes[(r, tuple(rho[k] for k in sorted(rho)))] += 1

                # The proof's support-minimal-relation construction.
                theorem_construction(V)
                construction_checks += 1
        print(f"dimension {m}: nullity-two configurations = {local}")

    print(f"TOTAL_CONFIGURATIONS={config_count}")
    print(f"MAXIMAL_SET_OMISSION_CHECKS={omission_checks}")
    print(f"PROFILE_INEQUALITY_CHECKS={profile_checks}")
    print(f"THEOREM_CONSTRUCTION_CHECKS={construction_checks}")
    print(f"MAX_MAXIMAL_DISSOCIATED_SETS_IN_ONE_CONFIGURATION={max_maximal_sets}")
    print(f"DISTINCT_PROFILE_SHAPES={len(profile_shapes)}")
    print(f"MAX_OBSERVED_RATIO={(float(max_ratio)):.6f} = {max_ratio}")
    print(f"MAX_RATIO_WITNESS={max_ratio_witness}")
    print("PROFILE_SHAPES:")
    for key, count in sorted(profile_shapes.items()):
        print(count, key)
    print("ALL_CHECKS_PASSED")


if __name__ == "__main__":
    main()
