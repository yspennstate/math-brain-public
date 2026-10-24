from functools import lru_cache
from itertools import combinations

names = ["p", "q", "r1", "r2", "a", "b", "c"]
n = len(names)
covers = [
    (0, 2),  # p<r1
    (0, 3),  # p<r2
    (0, 4),  # p<a
    (1, 4),  # q<a
    (2, 5),  # r1<b
    (2, 6),  # r1<c
    (4, 6),  # a<c
]

lt = [[False] * n for _ in range(n)]
for x, y in covers:
    lt[x][y] = True
for k in range(n):
    for i in range(n):
        if lt[i][k]:
            for j in range(n):
                if lt[k][j]:
                    lt[i][j] = True

pred = [0] * n
for y in range(n):
    for x in range(n):
        if lt[x][y]:
            pred[y] |= 1 << x

@lru_cache(None)
def dp(mask):
    if mask == (1 << n) - 1:
        return 1
    ans = 0
    for v in range(n):
        if not ((mask >> v) & 1) and pred[v] & ~mask == 0:
            ans += dp(mask | (1 << v))
    return ans

E = dp(0)

def count_with_before(x, y):
    @lru_cache(None)
    def f(mask):
        if mask == (1 << n) - 1:
            return 1
        ans = 0
        for v in range(n):
            if (mask >> v) & 1 or pred[v] & ~mask:
                continue
            if v == y and not ((mask >> x) & 1):
                continue
            ans += f(mask | (1 << v))
        return ans
    return f(0)

def width():
    best = 0
    for mask in range(1 << n):
        vs = [v for v in range(n) if (mask >> v) & 1]
        if all(not lt[i][j] and not lt[j][i] for i, j in combinations(vs, 2)):
            best = max(best, len(vs))
    return best

def is_cover(x, y):
    return lt[x][y] and not any(
        z != x and z != y and lt[x][z] and lt[z][y] for z in range(n)
    )

cover_check = [
    (names[x], names[y])
    for x in range(n)
    for y in range(n)
    if is_cover(x, y)
]
pairs = [
    ("p", "q", 0, 1),
    ("q", "r1", 1, 2),
    ("q", "r2", 1, 3),
    ("r1", "r2", 2, 3),
    ("r2", "a", 3, 4),
    ("r2", "b", 3, 5),
    ("b", "c", 5, 6),
]

print("POS3_CANONICAL_TWO_FORK_GUARD")
print("extensions", E)
print("width", width())
print("covers", cover_check)
for a, b, x, y in pairs:
    count = count_with_before(x, y)
    print(f"{a}<{b}", count, f"/{E}")

assert E == 79
assert width() == 3
assert count_with_before(0, 1) == 54
assert count_with_before(1, 2) == 55
assert count_with_before(1, 3) == 65
assert count_with_before(2, 3) == 56
assert all(
    count_with_before(x, y) * 3 > 2 * E
    for x, y in [(0, 1), (1, 2), (1, 3), (2, 3)]
)
assert count_with_before(3, 4) == 37
assert E <= 3 * count_with_before(3, 4) <= 2 * E
print("escape_balanced_pair", "r2<a", count_with_before(3, 4), f"/{E}")
print("POS3_CANONICAL_TWO_FORK_GUARD_PASS")
