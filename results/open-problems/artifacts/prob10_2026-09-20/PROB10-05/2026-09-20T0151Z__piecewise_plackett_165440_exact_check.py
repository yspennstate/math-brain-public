from fractions import Fraction as F

# PROB10-05 final exact self-check for this run.
# All theorem-deciding finite inequalities are exact rational/integer arithmetic.

a = F(168557580,170952323)
b = F(167065920,170952323)
r = F(7,8)
N = 16

def q(c):
    D = 1+c-2*a*a
    assert D > 0
    return (c*(1+c)-2*a*a)/D

assert F(0) < b < a < 1
assert q(b) > -F(3,8)
assert (1-b)**2 + 4*b*(1-a*a) > 0
assert F(55,64) > F(37,40)**2

sqrt_caps = [
    F(2121,10000), F(419,2000), F(207,1000), F(511,2500),
    F(2017,10000), F(1991,10000), F(491,2500), F(121,625),
    F(477,2500), F(47,250), F(463,2500), F(911,5000),
    F(1793,10000), F(881,5000), F(433,2500), F(17,100)
]

def B(qq):
    if qq < 0:
        return max(F(3,16), F(1,4)+F(20,111)*qq)
    return F(1,4)+F(7,44)*qq

delta_lb = F(0)
for j in range(N):
    c = b + (a-b)*F(j,N)
    cap = sqrt_caps[j]
    assert cap*cap > 1-c*c
    delta_lb += (a-b)*F(1,N)*F(7,22)/cap*B(q(c))

delta_target = F(723,200000)  # 0.003615
assert delta_lb > delta_target

trace_old = F(273011,250000)
trace_upper = trace_old - delta_target/(1-r**4)
trace_cap = F(108331,100000)
assert trace_upper < trace_cap

# Stronger target extracted after the 0.1654 feasibility check:
# theta*=517/3125=0.16544, so 4 theta*=2068/3125.
theta_before = F(3307,20000)
theta_target = F(517,3125)
x = F(457713,500000)          # 0.915426
beta = F(196421,250000)       # 0.785684

exp = 4*theta_target
assert exp == F(2068,3125)
power_ok = ((x.numerator**exp.denominator)*(r.denominator**exp.numerator)
            < (x.denominator**exp.denominator)*(r.numerator**exp.numerator))
assert power_ok

mu_lo = F(9116948312,10_000_000_000)
mu_hi = F(9116948313,10_000_000_000)
eps2_hi = F(47004495,100_000_000_000)

tail_margin = beta**4 - (trace_cap-x**4)
assert tail_margin > 0
assert beta < mu_lo < mu_hi < x

temple_lower = (x-mu_hi)*(mu_lo-beta)
temple_margin = temple_lower-eps2_hi
assert temple_margin > 0

width_before = F(1,4)-theta_before
width_after = F(1,4)-theta_target
assert width_after < width_before

print("N =", N)
print("delta_lower >", delta_target, "actual_exact =", delta_lb, "decimal =", float(delta_lb))
print("trace_upper =", trace_upper, float(trace_upper))
print("trace_cap =", trace_cap, float(trace_cap), "margin =", float(trace_cap-trace_upper))
print("theta_before =", theta_before, float(theta_before))
print("theta_target =", theta_target, float(theta_target))
print("x =", x, float(x), "power_check =", power_ok)
print("beta =", beta, float(beta))
print("spectral_tail_margin =", tail_margin, float(tail_margin))
print("Temple_margin =", temple_margin, float(temple_margin))
print("width_before =", width_before, float(width_before))
print("width_after =", width_after, float(width_after))
print("metric_improvement =", theta_target-theta_before, float(theta_target-theta_before))
print("ALL_EXACT_CHECKS_PASS = True")
