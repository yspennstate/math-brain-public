from fractions import Fraction
from itertools import permutations, combinations
from math import factorial

ASSERTIONS = 0

def check(cond, msg=""):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg or f"assertion {ASSERTIONS} failed")

def is_pow2(m):
    return m > 0 and (m & (m - 1)) == 0

def theta(m):
    return 2 if is_pow2(m) else 1

def cycles_of_perm(p):
    n = len(p)
    seen = [False] * n
    out = []
    for i in range(n):
        if not seen[i]:
            c = []
            j = i
            while not seen[j]:
                seen[j] = True
                c.append(j)
                j = p[j]
            out.append(tuple(c))
    return out

def falling(x, r):
    y = 1
    for k in range(r):
        y *= x - k
    return y

def split_kernel(N, m, i, j):
    if i + j > N:
        return Fraction(0)
    return Fraction(
        falling(m, i) * falling(N - m, j)
        + falling(m, j) * falling(N - m, i),
        falling(N, i + j),
    )

MAXN = 10
f = [Fraction(0)] * (MAXN + 1)
f[0] = Fraction(1)
for n in range(1, MAXN + 1):
    f[n] = sum(Fraction(theta(m)) * f[n - m] for m in range(1, n + 1)) / n
    check(f[n] > 0, f"f[{n}] positive")

# B(z)=int_0^1 exp(t A(z)) dt=(F(z)-1)/A(z).
# From A(z)B(z)=F(z)-1, solve b_n exactly because A_1=theta_1=2.
b = [Fraction(0)] * (MAXN + 1)
b[0] = Fraction(1)
for n in range(1, MAXN + 1):
    if n + 1 <= MAXN:
        rest = sum(Fraction(theta(m), m) * b[n + 1 - m] for m in range(2, n + 2))
        b[n] = (f[n + 1] - rest) / theta(1)
        check(b[n] >= 0, f"b[{n}] nonnegative")

for n in range(1, 9):
    total = 0
    support_weight = {}
    size_weight = {}
    for p in permutations(range(n)):
        cyc = cycles_of_perm(p)
        w = 1
        for c in cyc:
            w *= theta(len(c))
        total += w
        k = len(cyc)
        for c in cyc:
            S = frozenset(c)
            support_weight[S] = support_weight.get(S, Fraction(0)) + Fraction(w, k)
            size_weight[len(c)] = size_weight.get(len(c), Fraction(0)) + Fraction(w, k)

    check(Fraction(total, factorial(n)) == f[n], f"normalization n={n}")
    check(sum(support_weight.values(), Fraction(0)) == total, f"support mass n={n}")
    check(sum(size_weight.values(), Fraction(0)) == total, f"size mass n={n}")

    for m in range(1, n + 1):
        vals = []
        for S in combinations(range(n), m):
            vals.append(support_weight.get(frozenset(S), Fraction(0)))
        check(len(set(vals)) == 1, f"exchangeability n={n},m={m}")

    for m in range(1, n + 1):
        empirical = size_weight.get(m, Fraction(0)) / total
        predicted = Fraction(theta(m), m) * b[n - m] / f[n]
        check(empirical == predicted, f"pointing n={n},m={m}")

    maxvis = min(n, 5)
    for vis in range(2, maxvis + 1):
        for i in range(1, vis):
            j = vis - i
            A = frozenset(range(i))
            B = frozenset(range(i, vis))
            direct = Fraction(0)
            for S, wt in support_weight.items():
                left = S.intersection(range(vis))
                if left == A or left == B:
                    direct += wt
            direct /= total
            mixture = sum(
                (size_weight.get(m, Fraction(0)) / total) * split_kernel(n, m, i, j)
                for m in range(1, n + 1)
            )
            check(direct == mixture, f"split n={n},i={i},j={j}")

n = 4
total = 0
size_weight = {}
for p in permutations(range(n)):
    cyc = cycles_of_perm(p)
    w = 1
    for c in cyc:
        w *= theta(len(c))
    total += w
    for c in cyc:
        size_weight[len(c)] = size_weight.get(len(c), Fraction(0)) + Fraction(w, len(cyc))
p = {m: size_weight.get(m, Fraction(0)) / total for m in range(1, n + 1)}
check(p == {1: Fraction(7, 13), 2: Fraction(7, 26), 3: Fraction(1, 13), 4: Fraction(3, 26)})
P11 = sum(p[m] * split_kernel(4, m, 1, 1) for m in p)
P22 = sum(p[m] * split_kernel(4, m, 2, 2) for m in p)
P13 = sum(p[m] * split_kernel(4, m, 1, 3) for m in p)
check(P11 == Fraction(19, 39))
check(P22 == Fraction(7, 78))
check(P13 == Fraction(2, 13))
check(P22 / P11 == Fraction(7, 38))
check(P13 / P11 == Fraction(6, 19))

for N in range(1, 10001):
    count = sum(1 for m in range(1, N + 1) if is_pow2(m))
    check(2 ** (count - 1) <= N < 2 ** count, f"dyadic count N={N}")

print(f"ASSERTIONS={ASSERTIONS}")
print("N4_SELECTED_SIZE=" + ",".join(f"{m}:{p[m]}" for m in sorted(p)))
print(f"N4_P11={P11}")
print(f"N4_P22={P22}")
print(f"N4_P13={P13}")
print(f"N4_R22={P22 / P11}")
print(f"N4_R13={P13 / P11}")
print("ALL_EXACT_CHECKS_PASS")
