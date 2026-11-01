"""Exact-rational checks for the frozen two-input Euler entrance theorem."""

from fractions import Fraction as Q
from itertools import product


def ceil_q(t):
    return -(-t.numerator // t.denominator)


def formula(x, y, A, B, rho, gamma):
    assert A < 0 < B and -1 < rho < 0 and gamma > 0
    a, k = -A, -rho
    if x <= 0:
        return "escape" if y > 0 else "dead"
    if y > 0:
        return "escape"
    nx = ceil_q(x / (gamma * a))
    return "escape" if y + nx * gamma * k * a > 0 else "dead"


def iterate(x, y, A, B, rho, gamma, max_steps=1000):
    path = [(x, y)]
    for _ in range(max_steps):
        if x <= 0:
            return ("escape" if y > 0 else "dead"), path
        if y > 0:
            dx, dy = A + rho * B, rho * A + B
        else:
            dx, dy = A, rho * A
        x, y = x + gamma * dx, y + gamma * dy
        path.append((x, y))
    raise AssertionError("sector not resolved")


if __name__ == "__main__":
    A, B, rho = Q(-1), Q(1), Q(-1, 2)
    x, y = Q(14, 100), Q(-12, 100)
    for gamma in (Q(1), Q(1, 10), Q(13, 100), Q(14, 100)):
        result, path = iterate(x, y, A, B, rho, gamma)
        print(f"gamma={gamma}: {result}; path={path}; ray="
              f"{(rho * B, B) if result == 'escape' else (Q(0), Q(0))}")

    tx, ty = x / (-A), (-y) / (rho * A)
    assert ty > tx
    intervals = []
    n = 1
    while n * (ty - tx) < ty:
        intervals.append((ty / n, None if n == 1 else tx / (n - 1)))
        n += 1
    print(f"exact open escape intervals in gamma: {intervals}")

    # Formula versus direct recurrence across both interior start sectors.
    tested = 0
    vals = (Q(1, 10), Q(1, 4), Q(1, 2), Q(1), Q(3, 2))
    for xx, yy, aa, bb, kk, gg in product(vals, vals, vals, vals, (Q(1, 4), Q(1, 2)), vals):
        for sign_x, sign_y in product((-1, 1), repeat=2):
            px, py = sign_x * xx, sign_y * yy
            predicted = formula(px, py, -aa, bb, -kk, gg)
            observed, _ = iterate(px, py, -aa, bb, -kk, gg)
            assert predicted == observed, (px, py, aa, bb, kk, gg, predicted, observed)
            tested += 1
    print(f"exhaustive exact-rational sector checks: {tested} passed")

    # Uniform interval bounds at fixed gamma=1 and gamma=1/10.
    # x in (.13,.15), y in (-.13,-.11), A in (-1.02,-.98),
    # B in (.98,1.02), rho in (-.51,-.49).
    xlo, xhi = Q(13, 100), Q(15, 100)
    ylo, yhi = Q(-13, 100), Q(-11, 100)
    alo, ahi = Q(-102, 100), Q(-98, 100)
    klo, khi = Q(49, 100), Q(51, 100)
    gamma = Q(1)
    x1hi = xhi + gamma * ahi
    y1lo = ylo + gamma * klo * (-ahi)
    assert x1hi < 0 < y1lo
    print(f"gamma=1 robust margins: x1<{x1hi}, y1>{y1lo}")
    gamma = Q(1, 10)
    x1lo = xlo + gamma * alo
    y1hi = yhi + gamma * khi * (-alo)
    x2hi = xhi + 2 * gamma * ahi
    y2hi = yhi + 2 * gamma * khi * (-alo)
    assert x1lo > 0 and y1hi < 0 and x2hi < 0 and y2hi < 0
    print(f"gamma=1/10 robust margins: x1>{x1lo}, y1<{y1hi}, "
          f"x2<{x2hi}, y2<{y2hi}")
