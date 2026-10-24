from fractions import Fraction
from math import comb, factorial

ASSERTIONS = 0


def check(cond, msg):
    global ASSERTIONS
    ASSERTIONS += 1
    if not cond:
        raise AssertionError(msg)


def trim(p):
    q = list(p)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return tuple(q)


def padd(a, b):
    n = max(len(a), len(b))
    out = [Fraction(0) for _ in range(n)]
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    return trim(out)


def pscale(a, c):
    return trim([c * x for x in a])


def pmul(a, b):
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(out)


def ppow(a, n):
    out = (Fraction(1),)
    for _ in range(n):
        out = pmul(out, a)
    return out


def pintegral(a):
    return (Fraction(0),) + tuple(a[i] / Fraction(i + 1) for i in range(len(a)))


def monomial(k):
    return (Fraction(0),) * k + (Fraction(1),)


ONE = (Fraction(1),)
ONE_MINUS = (Fraction(1), Fraction(-1))


def beta(i, j):
    return Fraction(factorial(i - 1) * factorial(j - 1), factorial(i + j - 1))


def delta_poly(i, j):
    integrand = padd(
        pmul(ppow(ONE_MINUS, i - 1), monomial(j)),
        pmul(ppow(ONE_MINUS, j - 1), monomial(i)),
    )
    return trim(pintegral(integrand))


def ratio_poly(i, j):
    B = beta(i, j)
    return padd(ONE, pscale(delta_poly(i, j), -Fraction(1, 1) / B))


def peval(p, x):
    total = Fraction(0)
    power = Fraction(1)
    for a in p:
        total += a * power
        power *= x
    return total


# U063: exact polynomial rigidity / the theta=1/3 five-leaf mirage.
check(ratio_poly(1, 1) == (Fraction(1), Fraction(0), Fraction(-1)), "R11")
expected_r13 = (
    Fraction(1), Fraction(0), Fraction(-3, 2), Fraction(2), Fraction(-3, 2)
)
expected_r22 = (
    Fraction(1), Fraction(0), Fraction(0), Fraction(-4), Fraction(3)
)
check(ratio_poly(1, 3) == expected_r13, "R13")
check(ratio_poly(2, 2) == expected_r22, "R22")
factor_poly = pscale(
    pmul(pmul(monomial(2), (Fraction(-1), Fraction(1))),
         (Fraction(-1), Fraction(3))),
    Fraction(-3, 2),
)
check(
    padd(expected_r13, pscale(expected_r22, -1)) == factor_poly,
    "R13-R22 factorization",
)

theta = Fraction(1, 3)
for m in range(2, 6):
    for i in range(1, m):
        j = m - i
        check(
            peval(ratio_poly(i, j), theta) == Fraction(8, 9),
            f"five-leaf mirage m={m},i={i}",
        )
r33 = peval(ratio_poly(3, 3), theta)
check(r33 == Fraction(656, 729), "R33 at theta=1/3")
check(r33 - Fraction(8, 9) == Fraction(8, 729), "first six-leaf break")
check(peval(delta_poly(3, 3), theta) == Fraction(73, 21870), "Delta33")
for t in [Fraction(0), Fraction(1, 3), Fraction(1)]:
    check(
        peval(padd(expected_r13, pscale(expected_r22, -1)), t) == 0,
        f"candidate common-scale root theta={t}",
    )


def bias(N, s, c):
    c = Fraction(c)
    x = Fraction(s, N)
    return c * x / (1 - x + c * x)


def lam(N, s):
    return Fraction(N, 2 * s * (N - s))


def harmonic(n):
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction(0))


def q_direct(N, i, j, c):
    out = Fraction(0)
    for s in range(1, N):
        p = bias(N, s, c)
        out += lam(N, s) * (p ** i * (1 - p) ** j + p ** j * (1 - p) ** i)
    return out


def F_grid(N, s, i, j, c):
    c = Fraction(c)
    x = Fraction(s, N)
    D = 1 + (c - 1) * x
    return (
        c ** i * x ** (i - 1) * (1 - x) ** (j - 1)
        + c ** j * x ** (j - 1) * (1 - x) ** (i - 1)
    ) / (2 * D ** (i + j))


# U064/C083 finite algebra: exact clock normalization, odds-Jacobian identity,
# and equality between the direct split clock calculation and the Riemann-sum form.
for N in range(2, 21):
    check(
        sum((lam(N, s) for s in range(1, N)), Fraction(0)) == harmonic(N - 1),
        f"harmonic normalization N={N}",
    )
    for c in [Fraction(1, 2), Fraction(2), Fraction(3), Fraction(7, 3), Fraction(5)]:
        for s in range(1, N):
            p = bias(N, s, c)
            check(Fraction(0) < p < Fraction(1), f"bias bounds N={N},s={s},c={c}")
            x = Fraction(s, N)
            D = 1 + (c - 1) * x
            deriv = c / (D * D)
            check(
                deriv * x * (1 - x) == p * (1 - p),
                f"odds Jacobian N={N},s={s},c={c}",
            )
        maxm = min(N, 8)
        for m in range(2, maxm + 1):
            for i in range(1, m):
                j = m - i
                sum_f = Fraction(0)
                for s in range(1, N):
                    p = bias(N, s, c)
                    direct_term = lam(N, s) * (
                        p ** i * (1 - p) ** j + p ** j * (1 - p) ** i
                    )
                    fterm = Fraction(1, N) * F_grid(N, s, i, j, c)
                    check(
                        direct_term == fterm,
                        f"split term formula N={N},s={s},m={m},i={i},c={c}",
                    )
                    sum_f += fterm
                check(
                    q_direct(N, i, j, c) == sum_f,
                    f"split rate formula N={N},m={m},i={i},c={c}",
                )
                check(
                    q_direct(N, i, j, c) > 0,
                    f"positive split rate N={N},m={m},i={i},c={c}",
                )

# c=1 collapses exactly to the ordinary iid harmonic-grid comparator.
for N in range(2, 21):
    for m in range(2, min(N, 8) + 1):
        for i in range(1, m):
            j = m - i
            expected = sum(
                (
                    Fraction(1, N)
                    * (
                        Fraction(s, N) ** (i - 1)
                        * (1 - Fraction(s, N)) ** (j - 1)
                        + Fraction(s, N) ** (j - 1)
                        * (1 - Fraction(s, N)) ** (i - 1)
                    )
                    / 2
                    for s in range(1, N)
                ),
                Fraction(0),
            )
            check(
                q_direct(N, i, j, Fraction(1)) == expected,
                f"c=1 comparator N={N},m={m},i={i}",
            )

# C083 exact four-leaf non-equivalence witness, c=3.
N = 4
c = Fraction(3)
biases = [bias(N, s, c) for s in range(1, N)]
rates = [lam(N, s) for s in range(1, N)]
q13 = q_direct(4, 1, 3, c)
q22 = q_direct(4, 2, 2, c)
root = 4 * q13 + 3 * q22
p_bal = 3 * q22 / root
check(biases == [Fraction(1, 2), Fraction(3, 4), Fraction(9, 10)], "C083 biases")
check(rates == [Fraction(2, 3), Fraction(1, 2), Fraction(2, 3)], "C083 clocks")
check(q13 == Fraction(91741, 480000), "C083 q(1|3)")
check(q22 == Fraction(62059, 480000), "C083 q(2|2)")
check(root == Fraction(553141, 480000), "C083 root rate")
check(p_bal == Fraction(186177, 553141), "C083 balanced root probability")
check(p_bal != Fraction(3, 11), "C083 differs from source CTCS(4)")
check(p_bal != Fraction(147, 527), "C083 differs from C082")
check(q13 / q22 != Fraction(2), "C083 rate ratio differs from source")

print("U063_R13_MINUS_R22=-3/2*theta^2*(theta-1)*(3theta-1)")
print("U063_THETA_1_3_RATIO_M_LE_5=8/9")
print(f"U063_R33_THETA_1_3={r33}")
print(f"U063_R33_MINUS_8_9={r33 - Fraction(8,9)}")
print(f"U063_DELTA33_THETA_1_3={peval(delta_poly(3,3),theta)}")
print("C083_BIASES_N4=" + ",".join(map(str, biases)))
print("C083_CLOCKS_N4=" + ",".join(map(str, rates)))
print(f"C083_Q13_N4={q13}")
print(f"C083_Q22_N4={q22}")
print(f"C083_ROOT_RATE_N4={root}")
print(f"C083_BALANCED_ROOT_PROB_N4={p_bal}")
print(f"C083_MINUS_SOURCE_3_11={p_bal - Fraction(3,11)}")
print(f"C083_MINUS_C082_147_527={p_bal - Fraction(147,527)}")
print(f"C083_RATE_RATIO_Q13_OVER_Q22={q13/q22}")
print(f"C083_RATE_RATIO_MINUS_2={q13/q22 - 2}")
print(f"ASSERTIONS={ASSERTIONS}")
print("STATUS=ALL_EXACT_CHECKS_PASS")
