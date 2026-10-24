from fractions import Fraction as F

# Exact constants inherited from the proved softened-edge four-cycle certificate.
a = F(168557580, 170952323)
b = F(167065920, 170952323)
r = F(7, 8)

assert F(0) < b < a < F(1)

# Along Sigma(c)=circ(1,a,c,a), the conditional correlation of the
# remaining opposite pair given one opposite pair equal to zero is
# q(c)=[c(1+c)-2a^2]/[1+c-2a^2].  The denominator is increasing in c,
# so positivity at b pays it on [b,a].  The report proves q'(c)>0 by
# q'(c) numerator=(1-c)^2+4c(1-a^2)>0.
D_b = 1 + b - 2*a*a
N_b = b*(1+b) - 2*a*a
assert D_b > 0
q_b = N_b / D_b
assert q_b > -F(3, 8)

# For the Plackett decrement, use pi<22/7 and
# sqrt(1-b^2)<213/1000.  The second inequality is exact by squaring.
sqrt_cap = F(213, 1000)
assert sqrt_cap*sqrt_cap > 1 - b*b
pi_cap = F(22, 7)
delta_lb = 3*(a-b) / (16*pi_cap*sqrt_cap)
delta_target = F(243, 100000)
assert delta_lb > delta_target

# Previous PROB10-05 certified equicorrelation fourth-trace cap.
trace_old = F(273011, 250000)
trace_improved_upper = trace_old - delta_target/(1-r**4)
trace_cap = F(5431, 5000)
assert trace_improved_upper < trace_cap

# New source-level target theta*=1653/10000.  Since 4 theta*=1653/2500,
# x^2500 < r^1653 proves x<r^(4 theta*).
theta_before = F(413, 2500)
theta_target = F(1653, 10000)
x = F(91549, 100000)
power_ok = ((x.numerator**2500)*(r.denominator**1653)
            < (x.denominator**2500)*(r.numerator**1653))
assert power_ok

# Inherited degree-18 quasimode certificate.
mu_lo = F(9116948312, 10_000_000_000)
mu_hi = F(9116948313, 10_000_000_000)
eps2_hi = F(47004495, 100_000_000_000)

# If lambda_1 >= r^(4 theta*), then lambda_1>x.  The trace cap makes all
# non-Perron spectral values smaller than beta in modulus.
beta = F(7871, 10000)
tail_margin = beta**4 - (trace_cap - x**4)
assert tail_margin > 0
assert beta < mu_lo < mu_hi < x

# Temple contradiction.
temple_lower = (x-mu_hi)*(mu_lo-beta)
temple_margin = temple_lower - eps2_hi
assert temple_margin > 0

width_before = F(1,4) - theta_before
width_after = F(1,4) - theta_target
assert width_after < width_before

print('a =', a, float(a))
print('b =', b, float(b))
print('D_b =', D_b, float(D_b))
print('q(b) =', q_b, float(q_b))
print('q(b)+3/8 =', q_b+F(3,8), float(q_b+F(3,8)))
print('(213/1000)^2-(1-b^2) =', sqrt_cap*sqrt_cap-(1-b*b), float(sqrt_cap*sqrt_cap-(1-b*b)))
print('Plackett decrement lower bound =', delta_lb, float(delta_lb))
print('decrement target =', delta_target, float(delta_target))
print('decrement margin =', delta_lb-delta_target, float(delta_lb-delta_target))
print('old trace cap =', trace_old, float(trace_old))
print('improved trace upper =', trace_improved_upper, float(trace_improved_upper))
print('new trace cap =', trace_cap, float(trace_cap))
print('trace cap margin =', trace_cap-trace_improved_upper, float(trace_cap-trace_improved_upper))
print('x =', x, float(x), 'power check =', power_ok)
print('beta =', beta, float(beta))
print('spectral-tail margin =', tail_margin, float(tail_margin))
print('Temple lower =', temple_lower, float(temple_lower))
print('Temple contradiction margin =', temple_margin, float(temple_margin))
print('old lower =', theta_before, float(theta_before))
print('new lower =', theta_target, float(theta_target))
print('old width =', width_before, float(width_before))
print('new width =', width_after, float(width_after))
print('metric improvement =', theta_target-theta_before, float(theta_target-theta_before))
print('ALL_EXACT_CHECKS_PASS = True')
