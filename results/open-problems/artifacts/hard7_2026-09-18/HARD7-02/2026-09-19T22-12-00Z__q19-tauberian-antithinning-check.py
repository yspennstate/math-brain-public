import sympy as sp

alpha, A, M, r, delta, L, t = sp.symbols(
    "alpha A M r delta L t", positive=True
)

p = alpha * (2 + delta) / (2 * (1 + delta))
R = r ** (1 + delta)

gap_below_alpha = sp.simplify(alpha - p)
gap_above_cutoff = sp.simplify(p - alpha/(1 + delta))
remote_excess = sp.simplify((1 + delta)*p - alpha)
remote_ratio = sp.simplify((M/p) * R**(-p) / r**(-alpha))
annulus_log = sp.simplify(sp.expand_log(sp.log(R/r), force=True))
threshold_power = sp.simplify(2*M/(A*p))
pointwise_coefficient = sp.simplify((A - A/2)/delta)
delta_for_L = A/(4*L)
coefficient_at_delta_L = sp.simplify(pointwise_coefficient.subs(delta, delta_for_L))
critical_integral = sp.integrate(alpha*L/(t*sp.log(t)), t)

assert sp.simplify(gap_below_alpha - alpha*delta/(2*(1+delta))) == 0
assert sp.simplify(gap_above_cutoff - alpha*delta/(2*(1+delta))) == 0
assert sp.simplify(remote_excess - alpha*delta/2) == 0
assert sp.simplify(
    remote_ratio -
    2*M*(1+delta)/(alpha*(2+delta)*r**(alpha*delta/2))
) == 0
assert sp.simplify(annulus_log - delta*sp.log(r)) == 0
assert sp.simplify(
    threshold_power -
    4*M*(1+delta)/(A*alpha*(2+delta))
) == 0
assert sp.simplify(pointwise_coefficient - A/(2*delta)) == 0
assert sp.simplify(coefficient_at_delta_L - 2*L) == 0
assert sp.simplify(critical_integral - alpha*L*sp.log(sp.log(t))) == 0

print("HARD7-02 Tauberian anti-thinning exact algebra self-check")
print("p_delta =", p)
print("alpha - p_delta =", gap_below_alpha)
print("p_delta - alpha/(1+delta) =", gap_above_cutoff)
print("(1+delta)*p_delta - alpha =", remote_excess)
print("remote_tail_ratio_to_r^-alpha =", remote_ratio)
print("annulus_log =", annulus_log)
print("threshold for r^(alpha*delta/2) >=", threshold_power)
print("pointwise coefficient after half-signal localization =", pointwise_coefficient)
print("with delta=A/(4L), coefficient =", coefficient_at_delta_L)
print("critical truncated-moment antiderivative =", critical_integral)
print("ALL_EXACT_CHECKS_PASS = True")
