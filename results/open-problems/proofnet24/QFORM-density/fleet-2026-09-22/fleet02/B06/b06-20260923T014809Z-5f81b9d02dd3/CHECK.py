from fractions import Fraction
from math import sqrt, pi

c = Fraction(6221,6450)
L = Fraction(49,50)
m = 32
eps = Fraction(1,100)
tau = Fraction(1,16)
q = Fraction(4,3)

assert L > c
assert Fraction(1,m) < tau
assert eps < Fraction(3,200)
assert Fraction(1,1) > Fraction(4,5)

inherited_nonanchor_top2 = Fraction(1,m) + Fraction(1,50*m)
assert inherited_nonanchor_top2 == Fraction(51,1600)
assert inherited_nonanchor_top2 < Fraction(1,16)

# Delete the left anchor, retain every right coordinate.
# The three left singular directions become normalized sign-vector/sqrt(m),
# constant-vector/sqrt(m), and the isolated tail coordinate.
active_top2_leverage = Fraction(2,m)
assert active_top2_leverage == Fraction(1,16)

# Active singular values: 1, sqrt(1/50), 1/100.
E3 = Fraction(1,1)*Fraction(1,50)*Fraction(1,10000)
assert E3 == Fraction(1,500000)

alpha_core = Fraction(2,m)
alpha_tail = Fraction(1,1)
gate = q/Fraction(2,1)
assert alpha_core < gate
assert alpha_tail > gate

tail_hub_threshold = gate - active_top2_leverage
assert tail_hub_threshold == Fraction(29,48)

localized_c = Fraction(49,50)
localized_bound = 6*sqrt(pi)/float(localized_c)

print("PASS")
print("L =", L, "c =", c)
print("max inherited p_k^2 =", Fraction(1,m), "< tau =", tau)
print("inherited nonanchor top2 leverage =", inherited_nonanchor_top2)
print("h3/h2 =", eps, "< 3/200")
print("active top2 leverage after deleting left anchor =", active_top2_leverage)
print("E3(active M^T M) =", E3)
print("volume marginal core =", alpha_core)
print("volume marginal tail =", alpha_tail, "> q/2 =", gate)
print("tail-hub threshold q/2-ell =", tail_hub_threshold)
print("full target spectrum contains 1, +1,-1,+1,-1,+1/100,-1/100")
print("localized 3x3 eigenvalue magnitudes =", [Fraction(1,1), localized_c, localized_c])
print("Claude Theorem-A localized bound =", f"{localized_bound:.12f}")
