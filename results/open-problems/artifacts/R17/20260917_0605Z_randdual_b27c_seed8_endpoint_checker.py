#!/usr/bin/env python3
"""
R17-C024 exact endpoint compiler and dual Collatz bracket.

Dependency (already archived and exact-scanned):
  artifacts/R17/20260917_0605Z_randdual_b27c_seed8_cone_checker_output.txt

At z = 256717/800000, that file gives exact min/max component ratios
for a positive integer vector V on all 6,419,109 states.  By
Collatz--Wielandt,
    lambda_min <= rho(A_z) <= lambda_max.
Lueker's h=8 machine upper-bound functional is
    B(rho) = 2*(-log(2z))/(-log rho).
Since B is increasing on rho in (0,1), the same min/max ratios give
a rigorous two-sided bracket on the *intrinsic fixed-z machine bound*.
Only the upper side is a bound on gamma_2.

No floating-point arithmetic enters any theorem check. Decimal is display-only.
"""
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec = 120

z = Fraction(256717, 800000)
twoz = 2*z

lambda_min = Fraction(
    46182529968584060234521168602239065761790673471223158882302752058496559,
    135106723009294825124746869342208000000000000000000000000000000000000000,
)
lambda_max = Fraction(
    4785233721031882526591346223710818319327971859767342104653786449393161,
    13999173439003619880786492129280000000000000000000000000000000000000000,
)
assert 0 < lambda_min <= lambda_max < 1
assert 0 < twoz < 1

def neglog_bounds(x: Fraction, terms: int):
    # u=(1-x)/(1+x), -log x = 2 sum_{k>=0} u^(2k+1)/(2k+1).
    # The positive tail after `terms` terms is bounded by
    # 2*u^(2m+1)/((2m+1)*(1-u^2)).
    u=(1-x)/(1+x)
    s=Fraction(0)
    p=u
    for k in range(terms):
        s += p/Fraction(2*k+1)
        p *= u*u
    lo=2*s
    hi=lo + 2*p/Fraction(2*terms+1)/(1-u*u)
    return lo,hi

A_lo,A_hi = neglog_bounds(twoz, 100)
Lm_lo,Lm_hi = neglog_bounds(lambda_min, 200)
LM_lo,LM_hi = neglog_bounds(lambda_max, 200)

# B(rho)=2*(-log(2z))/(-log rho) is increasing for 0<rho<1.
B_machine_lo = 2*A_lo/Lm_hi
B_machine_hi = 2*A_hi/LM_lo
assert B_machine_lo < B_machine_hi

# Previous certified endpoint C023 and new rational endpoint.
U_prev = Fraction(82627917854239849, 10**17)
U_new  = Fraction(826279178542398483045, 10**21)
L      = Fraction(792665992, 10**9)

assert B_machine_hi < U_new < U_prev
improvement = U_prev-U_new
width = U_new-L

def dec(q: Fraction):
    return Decimal(q.numerator)/Decimal(q.denominator)

print("R17-C024 exact seed-8 dual Collatz / endpoint compiler")
print("z =", z)
print("lambda_min =", lambda_min)
print("lambda_max =", lambda_max)
print("EXACT_DUAL_COLLATZ_ORDER=PASS")
print("fixed_z_machine_lower_decimal =", dec(B_machine_lo))
print("fixed_z_machine_upper_decimal =", dec(B_machine_hi))
print("fixed_z_machine_bracket_width_decimal =", dec(B_machine_hi-B_machine_lo))
print("CERTIFIED_NEW_UPPER =", U_new)
print("CERTIFIED_NEW_UPPER_DECIMAL =", dec(U_new))
print("ENDPOINT_MARGIN_DECIMAL =", dec(U_new-B_machine_hi))
print("PREVIOUS_UPPER =", U_prev)
print("UPPER_DECREASE =", improvement)
print("UPPER_DECREASE_DECIMAL =", dec(improvement))
print("CERTIFIED_NEW_WIDTH =", width)
print("CERTIFIED_NEW_WIDTH_DECIMAL =", dec(width))
print("ALL_EXACT_CHECKS_PASS")
