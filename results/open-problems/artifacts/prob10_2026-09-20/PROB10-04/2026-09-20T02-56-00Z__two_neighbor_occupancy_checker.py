from math import comb, factorial, log, sqrt, exp
from itertools import combinations, product


def falling(A, h):
    z = 1
    for j in range(h):
        z *= A - j
    return z


def n0_formula(n, L, A):
    B = n - 1 - A
    total = 0
    for s in range(L + 1):
        for t in range(L - s + 1):
            h = 2 * s + t
            if h > A:
                continue
            r = L - s - t
            mult = factorial(L) // (factorial(s) * factorial(t) * factorial(r))
            num = mult * falling(A, h) * (B**t) * (comb(B, 2)**r)
            assert num % (2**s) == 0
            total += num // (2**s)
    return total


def brute_count(n, L, A):
    pairs = list(combinations(range(n - 1), 2))
    count = 0
    for choice in product(pairs, repeat=L):
        occ = [0] * A
        good = True
        for pair in choice:
            for y in pair:
                if y < A:
                    occ[y] += 1
                    if occ[y] >= 2:
                        good = False
                        break
            if not good:
                break
        count += int(good)
    return count, len(pairs)**L


def phi_saddle(ell, a):
    b = 1 - a
    B = 1 - 2 * a + 2 * ell
    q = (-B + sqrt(B * B + 4 * a * b)) / (2 * b)
    r = ell / (1 + q)**2
    v = 2 * ell * q / (1 + q)**2
    u = ell * q * q / (1 + q)**2
    h = 2 * u + v
    Phi = -(u * log(u / ell) + v * log(v / ell) + r * log(r / ell))
    Phi += a * log(a) - (a - h) * log(a - h) - h
    Phi += (2 * r + v) * log(b) + v * log(2)
    return Phi, q, u, v, r, h


def H(x):
    if x <= 0 or x >= 1:
        return 0.0
    return -x * log(x) - (1 - x) * log(1 - x)


def kappa2(alpha, rho):
    lam = 3 * alpha / 7
    ell = rho * lam * exp(-lam)
    a = (1 - rho) * exp(-lam)
    Phi, *_ = phi_saddle(ell, a)
    return -Phi


def first_moment_objective(alpha, rho):
    return H(rho) + alpha * log(7 / 8) - kappa2(alpha, rho)


def maximize_rho(alpha):
    # Numerical evidence only, not interval certification.
    lo, hi = 0.35, 0.65
    gr = (sqrt(5) - 1) / 2
    x1 = hi - gr * (hi - lo)
    x2 = lo + gr * (hi - lo)
    f1 = first_moment_objective(alpha, x1)
    f2 = first_moment_objective(alpha, x2)
    for _ in range(100):
        if f1 < f2:
            lo = x1
            x1 = x2
            f1 = f2
            x2 = lo + gr * (hi - lo)
            f2 = first_moment_objective(alpha, x2)
        else:
            hi = x2
            x2 = x1
            f2 = f1
            x1 = hi - gr * (hi - lo)
            f1 = first_moment_objective(alpha, x1)
    x = (lo + hi) / 2
    return x, first_moment_objective(alpha, x)


def crossing():
    lo, hi = 5.15, 5.20
    for _ in range(80):
        mid = (lo + hi) / 2
        _, f = maximize_rho(mid)
        if f > 0:
            lo = mid
        else:
            hi = mid
    a = (lo + hi) / 2
    return a, maximize_rho(a)


tests = [(8, 3, 2), (9, 2, 3), (7, 3, 1), (10, 2, 4)]
for T in tests:
    exact = n0_formula(*T)
    brute, total = brute_count(*T)
    print("FINITE", T, "formula", exact, "brute", brute, "total", total, "PASS", exact == brute)
    assert exact == brute

alpha = 4.4898
rho = 0.46
lam = 3 * alpha / 7
ell = rho * lam * exp(-lam)
a = (1 - rho) * exp(-lam)
Phi, q, u, v, r, h = phi_saddle(ell, a)
print("alpha", alpha, "rho", rho)
print("lambda", repr(lam))
print("ell", repr(ell))
print("a", repr(a))
print("q", repr(q))
print("u", repr(u), "v", repr(v), "r", repr(r), "h", repr(h))
print("Psi", repr(Phi))
print("kappa2", repr(-Phi))

for n in [100, 200, 500, 1000]:
    L = round(ell * n)
    A = round(a * n)
    exact = n0_formula(n, L, A)
    den = comb(n - 1, 2)**L
    print("FINITE_RATE", n, L, A, repr((log(exact) - log(den)) / n))

cross, rho_data = crossing()
print("NUMERICAL_STANDALONE_CROSSING", repr(cross))
print("NUMERICAL_RHO_AT_CROSSING", repr(rho_data[0]))
print("NUMERICAL_OBJECTIVE_AT_CROSSING", repr(rho_data[1]))
print("NOTE numerical crossing is auxiliary evidence, not interval-certified source progress")
print("ALL_EXACT_FINITE_CHECKS_PASS = True")