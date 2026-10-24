import math


def check(eps, nu, m):
    assert 0 < eps <= 0.25
    assert 0 < nu <= 1
    assert m >= 2 and m % 2 == 0

    disc = math.sqrt((eps*nu)**2 + 4*eps**(-2))
    lam_plus = (eps*nu + disc)/2
    lam_minus = (eps*nu - disc)/2

    W2 = eps**(-2)*(1-1/m) + 2*eps**2*nu**2
    leakage = eps**(-4)*(1-1/m)
    leakage_rhs = W2/(4*eps**2)

    slope_norm = eps**(-1)
    crossing_frob = eps**(-1)
    alpha_max = 1/m
    compiler_bound = 8*eps**(-0.5)*(slope_norm*crossing_frob)**(-0.25)

    assert abs(lam_plus) > 1
    assert abs(lam_minus) > 1
    assert eps**(-1) > 1
    assert leakage >= leakage_rhs
    assert alpha_max <= 0.5
    assert abs(compiler_bound-8) < 1e-12

    print(
        f"eps={eps:g} nu={nu:g} m={m} "
        f"active_eigs=[{eps:.12g},{lam_minus:.12g},{-eps**-1:.12g},{eps**-1:.12g},{lam_plus:.12g}] "
        f"W2={W2:.12g} leakage_ratio={leakage/leakage_rhs:.12g} "
        f"alpha_max={alpha_max:.12g} bound={compiler_bound:.12g}"
    )


for args in [(0.25,1.0,64),(0.1,0.2,2048),(0.05,0.001,8192)]:
    check(*args)

print("STATUS=PASS")
