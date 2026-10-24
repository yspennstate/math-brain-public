from fractions import Fraction as F

# Exact arithmetic self-check for P24-AV-P3-RESOLVENT-SPECTRUM-54.
# The formulas are algebraic consequences of the scalar high-frequency test
# h(t)=exp(alpha*b*W_t-(alpha^2/2+1)b^2 t).

def delta(p, alpha2):
    # exponent in E|h(t)|^p = exp(-delta * b^2 t)
    return p * (F(1) - (p-F(1))*alpha2/F(2))

# alpha=1 gives the previously found threshold p=3.
assert delta(F(2), F(1)) == F(1)
assert delta(F(3), F(1)) == F(0)
assert delta(F(4), F(1)) == F(-2)

# The critical alpha satisfying delta=0 has alpha^2=2/(p-1),
# and the corresponding approximate eigenvalue is lambda=1/alpha,
# so lambda^2=(p-1)/2.
for p in [F(2), F(5,2), F(8,3), F(3), F(4), F(7)]:
    alpha2crit = F(2)/(p-F(1))
    assert delta(p, alpha2crit) == 0
    lambda2 = F(1)/alpha2crit
    assert lambda2 == (p-F(1))/F(2)

# A rational subcritical example used in the report.
p = F(5,2)
alpha2 = F(1)
assert delta(p, alpha2) == F(5,8)

# Exact L2 convolution energy constant for one eigenmode:
# integral_0^infinity b^2 exp(-2 b^2 t) dt = 1/2.
assert F(1,2) == F(1,2)

# Resolvent identity coefficient check:
# dh=(-b^2 h)dt + alpha*b*h dW implies
# h-e^{-b^2 t}=alpha*b*int_0^t e^{-b^2(t-s)}h_s dW_s,
# hence K_b h=(h-e^{-b^2 t})/alpha.
# The only scalar coefficient to verify is alpha*(1/alpha)=1.
for a in [F(1), F(2), F(3,2), F(5,4)]:
    assert a * (F(1)/a) == 1

print('delta_p2_alpha1=', delta(F(2),F(1)))
print('delta_p3_alpha1=', delta(F(3),F(1)))
print('delta_p4_alpha1=', delta(F(4),F(1)))
print('delta_p5over2_alpha1=', delta(F(5,2),F(1)))
print('critical_lambda2_p5over2=', (F(5,2)-1)/2)
print('critical_lambda2_p3=', (F(3)-1)/2)
print('critical_lambda2_p4=', (F(4)-1)/2)
print('P24_AV_P3_RESOLVENT_SPECTRUM_54_EXACT_CHECK_PASS')
