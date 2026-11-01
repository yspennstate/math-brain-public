import math
import numpy as np

alpha = 0.25
alpha0 = 1/(2*math.sqrt(2))

def pair_constant(a):
    outer = 2**(a + 1.5)
    if a >= alpha0:
        inner = outer
    else:
        inner = 2**a * math.exp(-1 + 2*math.sqrt(2)*a) / a
    return max(inner, outer)

cp = pair_constant(alpha)
csq = 2**(3*alpha)/(1-2*alpha)
ccomp = cp*csq
partner_h14 = 4.0
cpartner = cp*partner_h14

print(f"alpha={alpha:.17g}")
print(f"pair_constant={cp:.15f}")
print(f"square_H14_constant={csq:.15f}")
print(f"pair_square_constant={ccomp:.15f}")
print(f"pair_square_closed_form={16*math.exp(1/math.sqrt(2)-1):.15f}")
print(f"partner_H14_multiplier={partner_h14:.15f}")
print(f"pair_partner_constant={cpartner:.15f}")

# Regression of the inner pair-envelope optimization.
for a in [0.10, 0.20, 0.25, alpha0, 0.40, 0.49, 0.50]:
    ys = np.linspace(0.0, 50.0, 200001)
    vals = 2**a*np.exp(-a*ys)*(2*math.sqrt(2)+ys)
    assert vals.max() <= pair_constant(a) + 2e-9

# Unit-scale exact sublevel-length regression for |x^2-s|<1.
ss = np.linspace(-2.0, 10.0, 100000)
mx = 0.0
for s in ss:
    lo, hi = s-1.0, s+1.0
    if hi <= 0:
        ell = 0.0
    elif lo <= 0:
        ell = 2*math.sqrt(hi)
    else:
        ell = 2*(math.sqrt(hi)-math.sqrt(lo))
    mx = max(mx, ell)
print(f"square_sublevel_grid_max={mx:.15f}")
print(f"square_sublevel_exact_cap={2*math.sqrt(2):.15f}")
assert mx <= 2*math.sqrt(2) + 1e-12
print("STATUS=PASS")
