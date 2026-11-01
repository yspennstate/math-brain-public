from math import sqrt, e

max_identity_error = 0.0
strict_cases = 0
for i in range(1001):
    r = i / 1000.0
    for j in range(1001):
        s = j / 1000.0
        d1 = r * s
        d2 = (1.0-r) * (1.0-s)
        m = 1.0 - d1 - d2
        err = abs((m*m - 4.0*d1*d2) - (r-s)*(r-s))
        max_identity_error = max(max_identity_error, err)
        if m > 1e-12 and d1 < m/4.0 - 1e-12 and d2 < m/4.0 - 1e-12:
            strict_cases += 1
            if not (m > 2.0/3.0 and abs(r-s) > 1.0/sqrt(3.0)):
                raise AssertionError("strict routing implication failed")

near = (103680.0 ** (1.0/3.0)) * (e ** (2.0/3.0)) * (2.0 ** (1.0/6.0)) * (4096.0 ** (1.0/3.0))
pivot = 16.0 * sqrt(60.0) * (2.0 ** (18.0/4.0))
if not near < 1644.0:
    raise AssertionError("near-null constant")
if not pivot < 2805.0:
    raise AssertionError("pivot constant")
if not 1.0/(64.0*2048.0*2.0) == 2.0**(-18):
    raise AssertionError("threshold identity")

print("max_identity_error", max_identity_error)
print("strict_grid_implication_cases", strict_cases)
print("near_null_constant", near)
print("rankone_pivot_constant", pivot)
print("QFORM_B19_R22_TWORANK2_ROUTING_CHECK_PASS")
