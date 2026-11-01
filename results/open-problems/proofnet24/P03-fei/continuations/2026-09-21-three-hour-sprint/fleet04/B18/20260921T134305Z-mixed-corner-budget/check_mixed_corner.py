from itertools import combinations
from math import log2, log


def fwht(a):
    a = [float(x) for x in a]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    N = len(a)
    return [x / N for x in a]


def influences(vals):
    N = len(vals)
    n = N.bit_length() - 1
    ans = []
    for i in range(n):
        c = sum(vals[x] != vals[x ^ (1 << i)]
                for x in range(N) if not (x >> i) & 1)
        ans.append(c / (N // 2))
    return ans


def pivotal(vals, i):
    N = len(vals)
    n = N.bit_length() - 1
    others = [j for j in range(n) if j != i]
    out = []
    for z in range(1 << (n - 1)):
        x = sum(((z >> k) & 1) << j for k, j in enumerate(others))
        out.append(int(vals[x] != vals[x ^ (1 << i)]))
    return out


def total_inf01(vals):
    if len(vals) == 1:
        return 0.0
    N = len(vals)
    n = N.bit_length() - 1
    s = 0.0
    for j in range(n):
        c = sum(vals[x] != vals[x ^ (1 << j)]
                for x in range(N) if not (x >> j) & 1)
        s += c / (N // 2)
    return s


def h2(p):
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * log2(p) - (1 - p) * log2(1 - p)


def Bi(vals, i):
    c = fwht(vals)
    p = [x * x for x in c]
    N = len(vals)
    bit = 1 << i
    z = 0.0
    for T in range(N):
        if T & bit:
            continue
        w = p[T] + p[T | bit]
        if w:
            z += w * h2(p[T | bit] / w)
    return z


def beta(vals, i, j):
    N = len(vals)
    m = (1 << i) | (1 << j)
    tot = hit = 0
    for x in range(N):
        if x & m:
            continue
        hit += vals[x] * vals[x ^ (1 << i)] * vals[x ^ (1 << j)] * vals[x ^ m] == -1
        tot += 1
    return hit / tot


def gamma(vals):
    n = len(vals).bit_length() - 1
    return sum(beta(vals, i, j) for i, j in combinations(range(n), 2))


def restrict(vals, i, b):
    n = len(vals).bit_length() - 1
    others = [j for j in range(n) if j != i]
    out = []
    for z in range(1 << (n - 1)):
        x = sum(((z >> k) & 1) << j for k, j in enumerate(others))
        out.append(vals[x | (b << i)])
    return out


def tree_budget(vals, order):
    def rec(vs, labels, pos):
        if pos == len(order) or not labels:
            return 0.0
        t = order[pos]
        if t not in labels:
            return rec(vs, labels, pos + 1)
        i = labels.index(t)
        local = total_inf01(pivotal(vs, i))
        nl = labels[:i] + labels[i + 1:]
        return (local
                + 0.5 * rec(restrict(vs, i, 0), nl, pos + 1)
                + 0.5 * rec(restrict(vs, i, 1), nl, pos + 1))
    return rec(vals, list(range(len(order))), 0)


tests = 0
for n in range(1, 5):
    N = 1 << n
    min_slack = 10.0
    max_tree_err = 0.0
    for code in range(1 << (N - 1)):
        vals = [1] + [1 if (code >> (x - 1)) & 1 else -1 for x in range(1, N)]
        inf = influences(vals)
        for i, a in enumerate(inf):
            if a:
                rhs = 0.5 * total_inf01(pivotal(vals, i)) + a / log(2)
                min_slack = min(min_slack, rhs - Bi(vals, i))
                tests += 1
        if n >= 2:
            max_tree_err = max(max_tree_err,
                               abs(tree_budget(vals, list(range(n))) - gamma(vals)))
    print("n", n,
          "min_local_slack", format(min_slack, ".15g"),
          "max_tree_err", format(max_tree_err, ".15g"))

print("local_relevant_coordinate_tests", tests)

for n in range(2, 9):
    vals = [-1] + [1] * ((1 << n) - 1)
    I = sum(influences(vals))
    G = gamma(vals)
    print("one_point", n,
          "I", format(I, ".15g"),
          "Gamma2", format(G, ".15g"),
          "ratio", format(G / I, ".15g"))
