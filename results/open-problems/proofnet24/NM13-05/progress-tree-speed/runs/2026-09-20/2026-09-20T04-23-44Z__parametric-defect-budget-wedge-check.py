from fractions import Fraction as F

# Exact self-check for the analytic identities used in
# 2026-09-20T04-23-44Z__parametric-defect-budget-wedge.md.
# This is a sanity check only; the theorem is proved algebraically in the report.

def A(d, delta):
    d = F(d, 1)
    return d * (d - 1) * (d - delta) / (delta * (d * (d - 1) + delta))


def verify_grid():
    deltas = [F(1,1000), F(1,100), F(1,20), F(1,10), F(1,4), F(1,2), F(1,1)]
    count = 0
    for di in range(2, 101):
        d = F(di, 1)
        for delta in deltas:
            a = A(di, delta)

            g_small = d - a * delta
            g_small_expected = d*d*delta / (d*(d-1) + delta)
            assert g_small == g_small_expected
            assert g_small > 0

            eta = (d + 2) * delta / (d + 1 + delta)
            g_high = d + 1 - (a + 1) * eta
            g_high_expected = (
                d*(d-1) + delta*(d+1)*(d*d+1) - delta*delta
            ) / ((d+1+delta) * (d*(d-1)+delta))
            assert g_high == g_high_expected
            assert g_high > 0
            count += 1
    return count


count = verify_grid()
print('exact identity cases:', count)

for delta in [F(1,10), F(1,20), F(1,100)]:
    d = 3
    a = A(d, delta)
    g_small = F(d,1) - a*delta
    eta = F(d+2,1)*delta / (F(d+1,1)+delta)
    g_high = F(d+1,1) - (a+1)*eta
    denom = (F(2*d+1,1)-delta)**2
    deriv_small = 2*g_small/denom
    deriv_high = 2*g_high/denom
    print(
        f'd=3 delta={delta}: A={a}, Gsmall={g_small}, Ghigh={g_high}, '
        f'deriv_small={deriv_small}, deriv_high={deriv_high}'
    )

print('ALL_EXACT_CHECKS_PASS')
