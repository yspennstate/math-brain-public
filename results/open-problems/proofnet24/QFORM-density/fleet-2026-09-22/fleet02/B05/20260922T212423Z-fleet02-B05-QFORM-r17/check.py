from math import sqrt

samples = [0.0, 0.1, 1/3, 1.0, 4.0, 10.0, 100.0]

for a in samples:
    r = sqrt(a + 1.0)

    # Unnormalized star [[a,r],[r,0]] at the sharp target threshold r^2=a+1.
    disc_star = sqrt(a*a + 4*r*r)
    lam_plus = (a + disc_star)/2
    lam_minus = (a - disc_star)/2
    assert lam_plus >= 1.0 - 1e-12
    assert lam_minus <= -1.0 + 1e-12

    # Ball-normalized aggregate pair [[a,r/sqrt(2)],[r/sqrt(2),0]].
    D = r*r/2
    disc_norm = sqrt(a*a + 2*r*r)
    mu_plus = (a + disc_norm)/2
    mu_minus = (a - disc_norm)/2
    kappa = min(abs(mu_plus), abs(mu_minus))
    assert D >= 0.5 - 1e-12
    assert kappa >= 0.5 - 1e-12
    assert D*kappa >= 0.25 - 1e-12

    print(
        f"a={a:.12g} r={r:.12g} "
        f"star=({lam_plus:.12g},{lam_minus:.12g}) "
        f"D={D:.12g} kappa={kappa:.12g} Dk={D*kappa:.12g}"
    )

C = 8 * 2**(3/4)
print(f"universal_star_bound={C:.12f}")
assert C < 13.455
print("QFORM_B05_DIFFUSE_STAR_AGGREGATE_CHECK_PASS")
