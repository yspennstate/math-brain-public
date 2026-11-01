from math import gamma

def moment(m, alpha):
    if alpha >= 2:
        return float("inf")
    k = m**(-alpha/2) * gamma(m+1) * gamma(2-alpha) / gamma(m+1-alpha)
    return k*k

for alpha in (2/3, 1.0, 1.5):
    vals = [moment(m, alpha) / (m**alpha) for m in (2, 5, 10, 50, 100)]
    target = gamma(2-alpha)**2
    print(alpha, vals, "target", target)

for m in (2, 3, 10):
    assert abs(moment(m, 1.0)-m) < 1e-9

print("PASS QFORM-CONDITIONAL-PROJECTION-ALL-POSITIVE-MOMENTS-FALSE-v1")
