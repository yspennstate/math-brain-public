from math import e, log, pi, sqrt


def exact_bound(D, detM=1.0):
    L = log(e / D)
    r = 2.0 + 1.0 / L
    q = r / (r - 1.0)
    B = 1.0 + 2.0 / (2.0 - q)
    A = (
        e
        * pi
        * (2.0 * pi) ** (1.0 / r)
        * B ** (1.0 / q)
        * (2.0 / (q - 1.0)) ** (1.0 / q)
        * D ** (-0.5 + 1.0 / r)
        * detM ** (-1.0 / r)
    )
    return (r + 1.0) / pi * (A / (2.0 * r)) ** (r / (r + 1.0))


crude_constant = (
    (4.0 / pi)
    * (e * pi * sqrt(2.0 * pi)) ** (3.0 / 4.0)
    * sqrt(5.0)
    * e ** (1.0 / 6.0)
)
print("analytic crude constant", crude_constant)
assert crude_constant < 34.0

for k in range(0, 121):
    D = 10.0 ** (-k / 10.0)
    L = log(e / D)
    val = exact_bound(D)
    assert val < 34.0 * sqrt(L)
    if k in (0, 10, 30, 60, 120):
        print(f"D={D:.1e} exact={val:.12g} ratio_sqrtlog={val/sqrt(L):.12g}")

partner = 4.0 * sqrt(2.0 * e) * 768.0 ** (1.0 / 8.0)
print("partner half-Riesz", partner)
print("partner density at |a|=1/4", 2.0 * partner)
assert partner < 21.399
assert 2.0 * partner < 42.798

print("PASS QFORM-NULL-COLOOP-ADAPTIVE-HY-STABILITY-v1")
