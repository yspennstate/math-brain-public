from fractions import Fraction as F

# Exact-arithmetic self-check for the symbolic margin used in the report.
# This is not a simulation proof: the theorem proof is written symbolically
# in the accompanying report.  The finite grid below checks the algebra and
# the displayed concrete corollaries using rational arithmetic only.


def A(d, delta):
    return F(d * (d - 1), 1) * (F(d, 1) - delta) / (
        delta * (F(d * (d - 1), 1) + delta)
    )


def gap(d, delta):
    return F(d, 1) - A(d, delta) * delta


def closed_gap(d, delta):
    return F(d * d, 1) * delta / (F(d * (d - 1), 1) + delta)


def derivative_margin(d, delta):
    # From -ell' >= 2*gap/(M+lambda)^2 and M+lambda <= 2d.
    return delta / (2 * (F(d * (d - 1), 1) + delta))


DELTAS = [F(1, 1), F(1, 2), F(7, 20), F(1, 10), F(1, 20), F(1, 100), F(1, 1000)]

count = 0
for d in range(2, 101):
    for delta in DELTAS:
        assert F(0, 1) < delta <= 1
        assert gap(d, delta) == closed_gap(d, delta)
        assert gap(d, delta) > 0
        assert F(2, 1) * gap(d, delta) / F((2 * d) ** 2, 1) == derivative_margin(d, delta)
        count += 1

print(f"symbolic-rational identity grid: {count} cases PASS")
for d, delta in [
    (3, F(1, 10)),
    (3, F(1, 20)),
    (2, F(1, 20)),
    (10, F(1, 100)),
]:
    print(
        f"d={d} delta={delta} A={A(d, delta)} "
        f"gap={gap(d, delta)} derivative_margin={derivative_margin(d, delta)}"
    )

assert derivative_margin(3, F(1, 10)) == F(1, 122)
print("d=3 delta=1/10 concrete derivative margin = 1/122 PASS")
print("ALL_EXACT_CHECKS_PASS")
