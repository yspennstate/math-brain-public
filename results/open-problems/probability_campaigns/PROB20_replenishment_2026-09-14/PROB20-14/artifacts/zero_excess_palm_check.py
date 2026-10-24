from fractions import Fraction
from collections import defaultdict

# Critical test law: E xi = 1.
PI = {
    0: Fraction(11, 20),
    1: Fraction(1, 5),
    2: Fraction(3, 20),
    5: Fraction(1, 10),
}
assert sum(PI.values()) == 1
assert sum(x * p for x, p in PI.items()) == 1
PI0 = PI[0]


def sum_prob(N, target):
    dp = {0: Fraction(1)}
    for _ in range(N):
        nxt = defaultdict(Fraction)
        for s, p in dp.items():
            for x, px in PI.items():
                if s + x <= target:
                    nxt[s + x] += p * px
        dp = dict(nxt)
    return dp.get(target, Fraction(0))


def palm_joint(N, target):
    """Exact unconditioned mass indexed by (zero_count, positive_excess_sum),
    restricted to residual sum == target."""
    dp = {(0, 0, 0): Fraction(1)}
    for _ in range(N):
        nxt = defaultdict(Fraction)
        for (s, z, y), p in dp.items():
            for x, px in PI.items():
                ns = s + x
                if ns <= target:
                    nxt[(ns, z + (x == 0), y + max(x - 1, 0))] += p * px
        dp = dict(nxt)
    return {(z, y): p for (s, z, y), p in dp.items() if s == target}


def renewal_probs(d, smax):
    dist = {0: Fraction(1)}
    ans = []
    for _s in range(1, smax + 1):
        nxt = defaultdict(Fraction)
        for total, p in dist.items():
            for x, px in PI.items():
                nt = total + x
                if nt <= d:
                    nxt[nt] += p * px
        dist = dict(nxt)
        ans.append(dist.get(d, Fraction(0)))
    return ans


def falling(z, m):
    out = 1
    for j in range(m):
        out *= z - j
    return out


def H(n, d, z):
    vals = renewal_probs(d, n)
    out = Fraction(0)
    for s, nu in enumerate(vals, start=1):
        if nu == 0 or s - 1 > z:
            continue
        out += (
            nu
            * Fraction(falling(z, s - 1), 1)
            / (PI0 ** (s - 1) * Fraction(falling(n, s), 1))
        )
    return out


# Exact Palm residual check for n=18, selected degree d=5.
n = 18
d = 5
N = n - 1
a_n = sum_prob(n, n - 1)
shifted = sum_prob(N, N - d)
R = shifted / a_n
joint = palm_joint(N, N - d)

assert sum(joint.values()) == shifted
# Deterministic identity under the degree-d Palm event: N0 = d + sum (xi_i-1)_+.
assert all(z == d + y for (z, y) in joint)

# Criticality identity E (xi-1)_+ = pi_0.
EY = sum(max(x - 1, 0) * p for x, p in PI.items())
assert EY == PI0

# Check the factorial factor from the new proof on Palm states satisfying
# Y >= pi_0*N - (pi_0/4)d, using central renewal lengths |s-d| <= d/4.
eta = PI0 / 4
for (z, y), mass in joint.items():
    if Fraction(y, 1) < PI0 * N - eta * d:
        continue
    for s in range(max(1, (3 * d + 3) // 4), (5 * d) // 4 + 1):
        if s - 1 > z:
            continue
        factor = (
            Fraction(falling(z, s - 1), 1)
            / (PI0 ** (s - 1) * Fraction(falling(N, s - 1), 1))
        )
        assert factor >= 1

# Numerical renewal-localization certificate: for this span-one law the full
# renewal mass tends to 1 and an increasing fraction lies at s approximately d.
rows = []
for D in (10, 20, 40, 80):
    vals = renewal_probs(D, 3 * D)
    total = sum(vals)
    lo = max(1, (3 * D) // 4)
    hi = min(len(vals), (5 * D) // 4)
    central = sum(vals[s - 1] for s in range(lo, hi + 1))
    rows.append((D, float(total), float(central), float(central / total)))

print("a_n =", a_n)
print("shifted atom =", shifted)
print("R_{n,d} =", R, "~=", float(R))
print("Palm zero/excess states:", len(joint), "identity verified")
print("E[(xi-1)_+] = pi_0 =", PI0)
print("central renewal localization rows (d, total U, central mass, fraction):")
for row in rows:
    print(row)
print("all exact assertions passed")
