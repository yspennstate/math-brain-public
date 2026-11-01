import math


def f(p):
    if p == 1.0:
        return 1.0
    return p + (1.0-p)*math.log1p(-p)


print("P20-T10-SINGLE-EDGE-RESIDUAL-CLOCK-SANITY")
print("analytic:")
print("  f(p)=p+(1-p)log(1-p)")
print("  f'(p)=-log(1-p)")
print("  (f(p)-p^2/2)'=-log(1-p)-p")
print("  derivative again = p/(1-p) >= 0")
print("  hence f(p)>=p^2/2 on [0,1)")
print()

# For a shifted residual-clock interval (alpha, alpha+L), compute exactly
# up to floating evaluation the disagreement mass and the integrated
# distance from the lower threshold.  This is only a sanity check; the
# report proves the inequality analytically by layer cake.
cases = [
    (0.0, 0.10), (0.0, 0.50), (0.0, 1.00),
    (0.25, 0.25), (0.25, 1.00),
    (1.25, 0.70), (2.00, 2.00),
]
for alpha, L in cases:
    p = math.exp(-alpha)*(1.0-math.exp(-L))
    charge = math.exp(-alpha)*(1.0-(L+1.0)*math.exp(-L))
    assert charge + 1e-14 >= f(p)
    assert f(p) + 1e-14 >= p*p/2.0
    print(
        f"alpha={alpha:.2f} L={L:.2f} p={p:.12g} "
        f"charge={charge:.12g} f(p)={f(p):.12g} p^2/2={p*p/2:.12g}"
    )

print()
print("factor comparison:")
for p in (0.01, 0.05, 0.10, 0.25, 0.50):
    old = f(p)/3.0
    new = f(p)
    print(
        f"p={p:.2f} old_four_star_g={old:.12g} "
        f"new_one_edge_f={new:.12g} ratio={new/old:.1f}"
    )

print("P20-T10-SINGLE-EDGE-RESIDUAL-CLOCK-SANITY: ALL_CHECKS_PASS")
