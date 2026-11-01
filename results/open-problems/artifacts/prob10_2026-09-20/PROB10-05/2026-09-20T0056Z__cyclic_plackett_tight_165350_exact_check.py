from fractions import Fraction as F

# Exact cyclic four-cycle constants.
a = F(168557580, 170952323)
b = F(167065920, 170952323)
r = F(7, 8)
assert F(0) < b < a < F(1)

# Conditional correlation q(c) for the remaining opposite pair after
# conditioning one opposite pair at zero.  The report proves q'(c)>0 on
# [b,a] because its numerator is (1-c)^2+4c(1-a^2)>0.
D_b = 1 + b - 2*a*a
q_b = (b*(1+b) - 2*a*a) / D_b
assert D_b > 0
assert q_b > -F(3,8)

# Plackett decrement.  pi<22/7 and sqrt(1-b^2)<213/1000.
sqrt_cap = F(213,1000)
assert sqrt_cap**2 > 1-b*b
pi_cap = F(22,7)
delta_lb = 3*(a-b)/(16*pi_cap*sqrt_cap)
delta_target = F(243,100000)
assert delta_lb > delta_target

# Certified equicorrelation trace cap from the preceding PROB10-05 run,
# minus the rigorous cyclic decrement.
trace_old = F(273011,250000)
trace_improved_upper = trace_old - delta_target/(1-r**4)
trace_cap = F(5431,5000)
assert trace_improved_upper < trace_cap

# Tight source target theta*=3307/20000=0.16535.
# Since 4 theta*=3307/5000, x^5000<r^3307 proves x<r^(4 theta*).
theta_before = F(413,2500)
theta_target = F(3307,20000)
x = F(91547,100000)
power_ok = ((x.numerator**5000)*(r.denominator**3307)
            < (x.denominator**5000)*(r.numerator**3307))
assert power_ok

# Inherited exact degree-18 quasimode enclosure.
mu_lo = F(9116948312,10_000_000_000)
mu_hi = F(9116948313,10_000_000_000)
eps2_hi = F(47004495,100_000_000_000)

# Trace separation and Temple contradiction.
beta = F(787101,1_000_000)
tail_margin = beta**4 - (trace_cap - x**4)
assert tail_margin > 0
assert beta < mu_lo < mu_hi < x

temple_lower = (x-mu_hi)*(mu_lo-beta)
temple_margin = temple_lower - eps2_hi
assert temple_margin > 0

width_before = F(1,4)-theta_before
width_after = F(1,4)-theta_target
assert width_after < width_before

print('a =', a, float(a))
print('b =', b, float(b))
print('D_b =', D_b, float(D_b))
print('q(b) =', q_b, float(q_b))
print('q(b)+3/8 =', q_b+F(3,8), float(q_b+F(3,8)))
print('(213/1000)^2-(1-b^2) =', sqrt_cap**2-(1-b*b), float(sqrt_cap**2-(1-b*b)))
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
