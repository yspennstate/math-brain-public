from fractions import Fraction as F

# PROB10-05 exact checker: 16-block Plackett lower quadrature,
# improved fourth-trace cap, and the inherited spectral-tail/Temple transfer.

a = F(168557580, 170952323)
b = F(167065920, 170952323)
r = F(7, 8)
N = 16

assert F(0) < b < a < F(1)

def q(c):
    D = 1 + c - 2*a*a
    assert D > 0
    return (c*(1+c) - 2*a*a) / D

# q is increasing on [b,a]: after clearing its positive squared denominator,
# q'(c) has numerator (1-c)^2 + 4*c*(1-a^2) > 0.
assert (1-b)**2 + 4*b*(1-a*a) > 0
assert q(b) > -F(3,8)

# Exact rational upper caps for sqrt(1-c_j^2), j=0,...,15.
sqrt_caps = [
    F(2121,10000), F(419,2000), F(207,1000), F(511,2500),
    F(2017,10000), F(1991,10000), F(491,2500), F(121,625),
    F(477,2500), F(47,250), F(463,2500), F(911,5000),
    F(1793,10000), F(881,5000), F(433,2500), F(17,100)
]

# Rational bracket lower envelope for 1/4 + asin(q)/(2*pi).
# For -3/8 <= q < 0:
# asin(u) <= u/sqrt(1-u^2) <= (40/37)u for 0<=u<=3/8,
# because sqrt(55)/8 > 37/40; and pi>3.
# Also retain the older uniform 3/16 bound.
# For q>=0: asin(q)>=q and pi<22/7, hence 1/(2*pi)>7/44.
assert F(55,64) > F(37,40)**2

def bracket_lb(qq):
    if qq < 0:
        linear = F(1,4) + F(20,111)*qq
        return max(F(3,16), linear)
    return F(1,4) + F(7,44)*qq

delta_lb = F(0)
rows = []
for j in range(N):
    c = b + (a-b)*F(j,N)
    qq = q(c)
    cap = sqrt_caps[j]
    # exact certificate of cap > sqrt(1-c^2)
    assert cap*cap > 1-c*c

    # q(c) is increasing and c>0, so over [c_j,c_{j+1}]
    # both the bracket lower envelope and 1/sqrt(1-c^2) are
    # bounded below by their left-endpoint certificates.
    Bj = bracket_lb(qq)
    term = (a-b)*F(1,N) * F(7,22) / cap * Bj
    delta_lb += term
    rows.append((j,c,qq,Bj,cap,term))

delta_target = F(3615,1_000_000)
assert delta_lb > delta_target

# Inherited equicorrelation fourth-trace cap minus certified cyclic decrement.
trace_old = F(273011,250000)
trace_improved_upper = trace_old - delta_target/(1-r**4)
trace_cap = F(108331,100000)
assert trace_improved_upper < trace_cap

# New source target theta*=827/5000=0.1654.
# 4*theta*=827/1250, so x^1250<r^827 proves x<r^(4 theta*).
theta_before = F(3307,20000)
theta_target = F(827,5000)
x = F(11443,12500)
power_ok = ((x.numerator**1250)*(r.denominator**827)
            < (x.denominator**1250)*(r.numerator**827))
assert power_ok

# Inherited exact degree-18 quasimode enclosure.
mu_lo = F(9116948312,10_000_000_000)
mu_hi = F(9116948313,10_000_000_000)
eps2_hi = F(47004495,100_000_000_000)

# Spectral separation + Temple contradiction.
beta = F(7857,10000)
tail_margin = beta**4 - (trace_cap - x**4)
assert tail_margin > 0
assert beta < mu_lo < mu_hi < x

temple_lower = (x-mu_hi)*(mu_lo-beta)
temple_margin = temple_lower - eps2_hi
assert temple_margin > 0

width_before = F(1,4)-theta_before
width_after = F(1,4)-theta_target
assert width_after < width_before

print("N =", N)
print("q(b) =", q(b), float(q(b)))
for j,c,qq,Bj,cap,term in rows:
    print("row", j,
          "q =", qq, float(qq),
          "B =", Bj, float(Bj),
          "sqrt_cap =", cap, float(cap),
          "term =", term, float(term))
print("delta lower =", delta_lb, float(delta_lb))
print("delta target =", delta_target, float(delta_target))
print("delta margin =", delta_lb-delta_target, float(delta_lb-delta_target))
print("old trace cap =", trace_old, float(trace_old))
print("improved trace upper =", trace_improved_upper, float(trace_improved_upper))
print("new trace cap =", trace_cap, float(trace_cap))
print("trace cap margin =", trace_cap-trace_improved_upper, float(trace_cap-trace_improved_upper))
print("x =", x, float(x), "power check =", power_ok)
print("beta =", beta, float(beta))
print("spectral-tail margin =", tail_margin, float(tail_margin))
print("Temple lower =", temple_lower, float(temple_lower))
print("Temple contradiction margin =", temple_margin, float(temple_margin))
print("old lower =", theta_before, float(theta_before))
print("new lower =", theta_target, float(theta_target))
print("old width =", width_before, float(width_before))
print("new width =", width_after, float(width_after))
print("metric improvement =", theta_target-theta_before, float(theta_target-theta_before))
print("ALL_EXACT_CHECKS_PASS = True")
