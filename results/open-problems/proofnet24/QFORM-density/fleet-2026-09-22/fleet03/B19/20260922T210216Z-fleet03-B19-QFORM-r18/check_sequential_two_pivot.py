#!/usr/bin/env python3
import math

m=3501/8000
d0=1/8
s=1.0
K0=(5/math.sqrt(2))*(d0/s)**0.25
bracket=2+math.log(K0)
C=4*math.sqrt(2)/math.sqrt(m*d0)*bracket
assert K0>1
assert C<67

# Analytic derivative sign for F(d)=const*d^{-1/2}[2+log(C0*d^{1/4})]
# throughout d>=d0: the bracket is increasing, so it suffices to test d0.
deriv_core=0.25-0.5*bracket
assert deriv_core<0

# Deterministic grid regression for the two level-set estimates in Lemma 2.1.
def m_level(v,t):
    delta=t**-2
    return 2*(math.sqrt(v+delta)-math.sqrt(max(v-delta,0.0)))

worst1=0.0
worst2=0.0
for iv in range(-80,81):
    v=10.0**(iv/10)
    for it in range(-80,81):
        t=10.0**(it/10)
        ml=m_level(v,t)
        r1=ml/(2*math.sqrt(2)/t)
        worst1=max(worst1,r1)
        if t**-2 < v:
            r2=ml/(4/(t*t*math.sqrt(v)))
            worst2=max(worst2,r2)
assert worst1<=1+1e-12
assert worst2<=1+1e-12

print(f"m={m:.15f}")
print(f"D_min={m*d0:.15f}")
print(f"K0={K0:.15f}")
print(f"bracket={bracket:.15f}")
print(f"C_B20={C:.15f}")
print(f"derivative_core_at_d0={deriv_core:.15f}")
print(f"level_set_bound1_worst_grid={worst1:.15f}")
print(f"level_set_bound2_worst_grid={worst2:.15f}")
print("QFORM_B19_SEQUENTIAL_TWO_PIVOT_CHECK_PASS")
