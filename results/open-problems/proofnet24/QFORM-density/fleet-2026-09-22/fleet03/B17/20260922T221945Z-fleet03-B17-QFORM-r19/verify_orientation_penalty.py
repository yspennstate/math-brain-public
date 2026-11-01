from fractions import Fraction as F


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def eye(n):
    return [[F(int(i == j), 1) for j in range(n)] for i in range(n)]


partner = F(5295, 21952)
base = F(69, 320)


def witness(N):
    d = N * N + 2
    u = [F(2 * N, d), F(2 * N, d), F(N * N - 2, d)]
    assert sum(x * x for x in u) == 1

    B = [[F(int(i == j), 1) - 2 * u[i] * u[j]
          for j in range(3)] for i in range(3)]
    assert matmul(B, B) == eye(3)
    assert all(B[i][j] != 0 for i in range(3) for j in range(3))

    S4 = sum(x ** 4 for x in u)
    c = F(177, 640) - F(39, 640) * S4
    mix = sum(B[i][j] ** 2 for i in range(3) for j in range(i + 1, 3))
    assert c == base + F(39, 1280) * mix

    explicit = base + F(39, 40) * F(
        N * N * (N ** 4 - 2 * N * N + 4), (N * N + 2) ** 4
    )
    assert c == explicit
    return u, B, c


for N in [2, 3, 4, 6, 10, 20]:
    u, B, c = witness(N)
    assert c > base
    print(N, c, float(c), "partner_diff", float(partner - c))

u6, B6, c6 = witness(6)
u10, B10, c10 = witness(10)
assert c6 == F(1970841, 8340544)
assert c10 == F(53990741, 240540480)
assert partner - c6 == F(439101, 89400206)
assert partner - c10 == F(43191941, 2578293270)

print("u6", u6)
print("B6", B6)
print("u10", u10)
print("B10", B10)
print("partner", partner, float(partner))
print("base", base, float(base))
print("PASS orientation penalty exact arithmetic")
