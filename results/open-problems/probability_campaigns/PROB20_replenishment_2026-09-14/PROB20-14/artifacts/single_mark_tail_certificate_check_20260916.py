from fractions import Fraction
import math

# Critical finite-support test law: E xi = 1.
PI = {0: Fraction(1, 2), 1: Fraction(1, 4), 3: Fraction(1, 4)}
Q = 1.5
SOFT_G = {0: 0.0, 1: 0.2, 3: 0.8}

_CACHE = {}


def conv(n):
    d = {0: Fraction(1)}
    for _ in range(n):
        nd = {}
        for s, p in d.items():
            for x, px in PI.items():
                nd[s + x] = nd.get(s + x, Fraction(0)) + p * px
        d = nd
    return d


def dist(n):
    if n not in _CACHE:
        _CACHE[n] = conv(n)
    return _CACHE[n]


def central_atom(n):
    return float(dist(n).get(n - 1, Fraction(0)))


def conditioned_marginal(n, x):
    den = dist(n)[n - 1]
    num = PI.get(x, Fraction(0)) * dist(n - 1).get(n - 1 - x, Fraction(0))
    return float(num / den)


def Lambda(theta):
    return math.log(
        sum(float(p) * math.exp(-theta * (x - 1)) for x, p in PI.items())
    )


def soft_M(theta):
    return sum(
        float(PI[x]) * SOFT_G.get(x, 0.0) * math.exp(-theta * (x - 1))
        for x in PI
    )


def run():
    p_g = sum(float(PI[x]) * SOFT_G.get(x, 0.0) for x in PI)
    rows = []

    # Check the unoptimized single-mark inequality at several theta values.
    for n in (8, 14, 20):
        lam = -math.log(central_atom(n))
        q_g = sum(SOFT_G.get(x, 0.0) * conditioned_marginal(n, x) for x in PI)
        for theta in (0.0, 0.1, 0.3, 0.7, 1.2):
            rhs = math.exp(lam - theta + (n - 1) * Lambda(theta)) * soft_M(theta)
            assert q_g <= rhs + 1e-12, (n, theta, q_g, rhs)

        # Check the whole-tail hard-support consequence before optimizing theta.
        for K in (0, 1, 2):
            actual = sum(
                (x ** Q) * conditioned_marginal(n, x) for x in PI if x > K
            )
            ordinary_tail = sum(
                (x ** Q) * float(p) for x, p in PI.items() if x > K
            )
            for theta in (0.05, 0.2, 0.6, 1.0):
                rate_candidate = theta * (K + 1) - (n - 1) * Lambda(theta)
                rhs = ordinary_tail * math.exp(lam - rate_candidate)
                assert actual <= rhs + 1e-10, (n, K, theta, actual, rhs)
        rows.append((n, q_g, lam))

    # Check the pre-optimization factorial denominator certificate in a regime
    # where the expected marked multiplicity exceeds 8.
    n = 60
    K = 0
    D = 3
    lam = -math.log(central_atom(n))
    w = sum(
        min(x ** Q, D ** Q) * conditioned_marginal(n, x)
        for x in PI
        if x > K
    )
    w_p = sum(
        min(x ** Q, D ** Q) * float(p) for x, p in PI.items() if x > K
    )
    multiplicity = n * w / (D ** Q)
    assert multiplicity >= 8.0
    m = math.floor(n * w / (4 * D ** Q))
    log_ratio = math.log(w / (2 * w_p))
    for theta in (0.0, 0.02, 0.05, 0.1, 0.2):
        lower_certificate = (
            m * log_ratio
            + theta * (m * K + 1)
            - (n - m) * Lambda(theta)
        )
        assert lower_certificate <= lam + 1e-10, (
            theta,
            lower_certificate,
            lam,
        )

    print("single-mark direct inequalities: PASS")
    for n, q_g, lam in rows:
        print(f"n={n}: q_g={q_g:.12f}, lambda_n={lam:.12f}")
    print(
        "factorial pre-optimization certificate: PASS; "
        f"multiplicity={multiplicity:.12f}, m={m}, lambda_n={lam:.12f}"
    )


if __name__ == "__main__":
    run()
