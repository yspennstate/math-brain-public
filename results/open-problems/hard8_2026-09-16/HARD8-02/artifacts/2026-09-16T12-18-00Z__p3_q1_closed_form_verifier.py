#!/usr/bin/env python3


def build_q1(h):
    """Closed-form q=1 absorber from the 2026-09-16T12:18:00Z report.

    Parameters:
      h >= 2,
      k = h-1,
      c = 2h.

    Returns c triples (root, middle, leaf).
    """
    assert h >= 2
    c = 2 * h
    n = 2 * h - 1

    # Leaf-pair permutation on low indices 0,...,2h-1.
    pi = [None] * (2 * h)
    pi[0] = 2 * h - 1
    for i in range(1, 2 * h):
        t = i - 1
        pi[i] = (2 * t + 1) % n
    assert sorted(pi) == list(range(2 * h))

    # Root assignment to the actual middle labels.
    root_for_middle = {2 * h + 1: 5 * h}
    for m in [0] + list(range(2, 2 * h)):
        v = 0 if m == 0 else m - 1
        u = (h * v) % n
        a = u if u < h else u + 1
        root_for_middle[m] = 4 * h + a

    triples = []
    for i in range(2 * h):
        high = 2 * h + pi[i]
        if i == 1:
            middle, leaf = high, i
        else:
            middle, leaf = i, high
        triples.append((root_for_middle[middle], middle, leaf))
    return triples


def verify_q1(h):
    c = 2 * h
    k = h - 1
    triples = build_q1(h)

    roots = sorted(r for r, m, l in triples)
    nonroots = sorted(x for r, m, l in triples for x in (m, l))
    leaf_diffs = sorted(abs(m - l) for r, m, l in triples)
    root_diffs = sorted(r - m for r, m, l in triples)  # every root exceeds its middle
    all_diffs = sorted(leaf_diffs + root_diffs)

    assert roots == list(range(2 * c, 3 * c))
    assert nonroots == list(range(2 * c))

    assert leaf_diffs == list(range(h, 3 * h - 1)) + [4 * h - 1]
    assert root_diffs == list(range(3 * h - 1, 4 * h - 1)) + list(range(4 * h, 5 * h))
    assert all_diffs == list(range(k + 1, k + 2 * c + 1))

    mins = []
    reversed_sum = 0
    reversed_count = 0
    for r, m, l in triples:
        mins.append(min(m, l))
        if m > l:
            reversed_count += 1
            reversed_sum += m - l

    E = sum(mins) - c * (c - 1) // 2
    assert E == 0
    assert reversed_count == 1
    assert reversed_sum == c
    assert c * (c - 2 * k - 1) == 3 * E + reversed_sum

    # General leaf-spectrum sum identity specialized to q=1.
    S_A = sum(leaf_diffs)
    S_0 = sum(range(k + 1, k + c + 1))
    assert S_A - S_0 == c // 2

    return triples


# Large deterministic exact-integer evaluation range.
checks = 0
for h in range(2, 2001):
    verify_q1(h)
    checks += 1
print("Q1_FORMULA_CHECKS", checks)

# Independent symbolic-arithmetic consistency check for the split-spectrum
# identity.  The proof is algebraic and universal; this finite loop merely
# checks the simplified expressions on a broad parameter box.
param_checks = 0
for c in range(1, 201):
    for k in range(0, 100):
        q = c - (2 * k + 1)
        if q < 0:
            continue
        # Twice the step before dividing by 2 in the report:
        # c(2k+c+1) - 2c(2k+1) = c(c-2k-1) = c q.
        lhs = c * (2 * k + c + 1) - 2 * c * (2 * k + 1)
        rhs = c * q
        assert lhs == rhs
        param_checks += 1
print("SPLIT_IDENTITY_PARAMETER_CHECKS", param_checks)

# Display the first three closed-form certificates for reproducibility.
for h in (2, 3, 4):
    print("EXAMPLE_H", h, build_q1(h))

print("ALL_CHECKS_PASSED")
