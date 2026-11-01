from fractions import Fraction as F

# NM13-05 T06 exact arithmetic checker:
# rare extra-child stability for P(nu=3)=1-p, P(nu=4)=p.
L = F(299, 100)
eps = F(1, 200)

D = (F(3)-L)*(F(9)-L)
Abar = F(6)*L / D

delta_small = D / (F(2)*L)
delta_large = F(4)*D / (F(10)*L - D)

theta_defect_large = F(5)*eps / (F(4)+eps)

gap_small = F(3) - Abar*eps
gap_large = F(3) - Abar*theta_defect_large

denom = (F(4)+L)**2
margin_small = F(2)*gap_small/denom
margin_large = F(2)*gap_large/denom

beta_min = F(1)/L
baseline_adjacent = F(11,4)
gain = L-baseline_adjacent

checks = [
    ("L<3", L < 3),
    ("eps below parametric small-tail threshold", eps < delta_small),
    ("eps below parametric large-tail threshold", eps < delta_large),
    ("small-tail numerator gap positive", gap_small > 0),
    ("large-tail numerator gap positive", gap_large > 0),
    ("small-tail derivative margin positive", margin_small > 0),
    ("large-tail derivative margin positive", margin_large > 0),
    ("strict gain over inherited all-mixture d-1/4 endpoint", gain > 0),
]

print("T06 rare-extra-child exact checker")
print("family: P(nu=3)=1-p, P(nu=4)=p")
print("parent-bias endpoint L =", L, float(L))
print("tail width eps =", eps, float(eps))
print("D=(3-L)(9-L) =", D, float(D))
print("Abar=6L/D =", Abar, float(Abar))
print("parametric small-tail threshold delta_- =", delta_small, float(delta_small))
print("parametric large-tail threshold delta_+ =", delta_large, float(delta_large))
print("large-tail bound on 1-theta =", theta_defect_large, float(theta_defect_large))
print("small-tail numerator gap =", gap_small, float(gap_small))
print("large-tail numerator gap =", gap_large, float(gap_large))
print("uniform -ell' margin, small tail =", margin_small, float(margin_small))
print("uniform -ell' margin, large tail =", margin_large, float(margin_large))
print("child-bias beta lower endpoint =", beta_min, float(beta_min))
print("gain over inherited all-mixture lambda<=11/4 =", gain, float(gain))
for name, ok in checks:
    print(name + ":", "PASS" if ok else "FAIL")
assert all(ok for _,ok in checks)
print("ALL_EXACT_CHECKS_PASS")
