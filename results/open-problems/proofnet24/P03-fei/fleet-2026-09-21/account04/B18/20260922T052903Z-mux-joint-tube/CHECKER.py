from fractions import Fraction as F


def V(x):
    return 4*x*(1-x)


def mux_data(t, q0, q1):
    r = (1-t)*q0 + t*q1
    vt, v0, v1 = V(t), V(q0), V(q1)
    w = [
        (1-2*r)**2,
        vt*(q1-q0)**2,
        (1-t)**2*v0,
        t*t*v1,
        vt*v0/F(4),
        vt*v1/F(4),
    ]
    d = q0 + q1 - 2*q0*q1
    I = vt*d + v0*(1-t) + v1*t
    W = I/F(4) - r*(1-r)
    W_formula = t*(1-t)*(q0*(1-q0) + q1*(1-q1))
    return w, W, W_formula


# Exact rational regression of the six-mass formula and Poincare currency.
cases = 0
for den in (7, 10, 13):
    for ti in range(1, den):
        t = F(ti, den)
        for i in range(1, den):
            q0 = F(i, den)
            for j in range(1, den):
                q1 = F(j, den)
                w, W, W_formula = mux_data(t, q0, q1)
                assert sum(w) == 1
                assert all(x >= 0 for x in w)
                assert W == W_formula
                assert W >= 0
                cases += 1

# Constants used in the analytic tube proof.
assert F(203, 2*262144) < F(1, 2500)
assert F(89, 4096) - F(1, 2500) > F(1, 48)
reserve_gap = F(89, 4096) - F(1, 2500) - F(1, 48)
assert reserve_gap == F(3803, 7680000)

# 0.268204856 exactly as a terminating decimal.
a = F(33525607, 125000000)
margin_upper = a - F(1, 27)
assert margin_upper < a

print("PASS")
print("exact_bias_cases", cases)
print("tube_loss_bound", "203/524288", float(F(203, 524288)))
print("tube_loss_target", "1/2500", float(F(1, 2500)))
print("reserve_gap_over_1_48", f"{reserve_gap.numerator}/{reserve_gap.denominator}", float(reserve_gap))
print("margin_upper_exact", f"{margin_upper.numerator}/{margin_upper.denominator}")
print("margin_upper_decimal", float(margin_upper))
