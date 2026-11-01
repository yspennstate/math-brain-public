from fractions import Fraction as F

W = (1, 4, 2, 2, 4, 1)


def norm(t):
    return sum(F(w) * x for w, x in zip(W, t))


def L(t, base):
    s, a, b, g, d, e = t
    return (
        s
        + 2 * (1 + base) * a
        + (1 + base) * b
        + 2 * base * g
        + (1 + 3 * base * base) * d
        + base**3 * e
    )


def bracket(t, p):
    q = 1 - p
    s, a, b, g, d, e = t
    return (
        p * s
        + 2 * p * (3 - 2 * p) * a
        + (2 * p - 1) * b
        + 2 * p * q * (2 - p) * g
        + (2 * p**3 - 7 * p**2 + 8 * p - 2) * d
        - q**3 * e
    )


def T(t):
    return t[2] + 2 * t[4] + t[5]


p = F(1, 3)
q = F(2, 3)

theta_p = (F(1, 4), F(0), F(7, 40), F(0), F(3, 80), F(1, 4))
theta_q = (
    F(0),
    F(0),
    F(0),
    F(14989, 34560),
    F(79, 34560),
    F(79, 640),
)

assert norm(theta_p) == 1
assert norm(theta_q) == 1

Lp = L(theta_p, q)
Lq = L(theta_q, p)
assert Lp == F(1519, 2160)
assert Lq == F(641, 2160)
assert Lp + Lq == 1

Dp = 1 - Lp
Dq = 1 - Lq
assert Dp == F(641, 2160) < p
assert Dq == F(1519, 2160) > q
assert Dp + Dq == 1

Fp = bracket(theta_p, p)
Fq = bracket(theta_q, q)
assert Fp == F(-109, 2160) < 0
assert Fq == F(14831, 58320) > 0

Tp = T(theta_p)
Tq = T(theta_q)
assert theta_p[5] - Tp * Tp == 0
assert theta_q[5] - Tq * Tq == F(1997831, 18662400) > 0

leaf_p = theta_p[4] - q**3 * theta_p[5] / 2
leaf_q = theta_q[4] - p**3 * theta_q[5] / 2
assert leaf_p == F(1, 2160) > 0
assert leaf_q == 0

for name, val in [
    ("norm_p", norm(theta_p)),
    ("norm_q", norm(theta_q)),
    ("L_p(q)", Lp),
    ("L_q(p)", Lq),
    ("L_sum", Lp + Lq),
    ("D_p", Dp),
    ("D_q", Dq),
    ("F_p", Fp),
    ("F_q", Fq),
    ("T_p", Tp),
    ("eps_p_minus_Tp2", theta_p[5] - Tp * Tp),
    ("leaf_p_slack", leaf_p),
    ("T_q", Tq),
    ("eps_q_minus_Tq2", theta_q[5] - Tq * Tq),
    ("leaf_q_slack", leaf_q),
]:
    print(f"{name}={val}")

print("ALL_EXACT_CHECKS_PASS")
