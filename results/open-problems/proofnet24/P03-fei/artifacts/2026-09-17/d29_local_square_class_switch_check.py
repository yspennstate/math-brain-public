#!/usr/bin/env python3
"""Exact arithmetic checker for P03-I0098-D29-LOCAL-SQUARE-CLASS-SWITCH-262.

This checker verifies only the finite algebra/discriminant arithmetic used in the
written proof. It does not prove Stark-unit existence, Kopp Conjecture 5.1, or a
dimension-29 SIC.
"""
p = 29
rad = 195

def kmul(x, y):
    a,b=x; c,d=y
    return (a*c + rad*b*d, a*d + b*c)

eps = (14,1)       # 14 + sqrt(195)
theta = (15,1)     # 15 + sqrt(195)
assert kmul(theta,theta) == (30*eps[0], 30*eps[1])
assert kmul(eps,(14,-1)) == (1,0)

D = rad % p
assert pow(D,(p-1)//2,p) == p-1  # 195 is nonsquare mod 29, hence (29) inert

def fmul(x,y):
    a,b=x; c,d=y
    return ((a*c + D*b*d) % p, (a*d+b*c) % p)

def fpow(x,n):
    r=(1,0); a=x
    while n:
        if n & 1:
            r=fmul(r,a)
        a=fmul(a,a); n//=2
    return r

epsbar=(14,1)
assert fpow(epsbar,3)==(1,0)
assert epsbar != (1,0)
assert fpow(epsbar,1)!=(1,0)
# one-real-place ray kernel:
# ((F_{29^2}^x) x {+/-}) / <(eps,+),(-1,-)> has size 280.
residue_units = p*p-1
assert residue_units == 840
assert residue_units*2//6 == 280
# The finite-prime inertia image (a,+) intersects global units in <eps>, order 3.
assert residue_units//3 == 280
# For modulus (29) without an infinite place, the kernel has size 140.
assert residue_units//6 == 140

# Kummer switch: theta^2 = 30 eps, hence 30 x^2 = alpha iff
# (theta*x)^2 = alpha*eps.  The following discriminant identities verify the
# d=29 versus d=23 ramification switch.
D_K29, D_Qsqrt30, D_Qsqrt26 = 780,120,104
disc_biquad29 = D_K29*D_Qsqrt30*D_Qsqrt26
assert disc_biquad29 % (D_K29*D_K29) == 0
rel_disc_norm_29 = disc_biquad29 // (D_K29*D_K29)
assert rel_disc_norm_29 == 16

# d=23 analogue: K=Q(sqrt30), K(sqrt24)=K(sqrt6), third quadratic Q(sqrt5).
D_K23, D_Qsqrt6, D_Qsqrt5 = 120,24,5
disc_biquad23 = D_K23*D_Qsqrt6*D_Qsqrt5
assert disc_biquad23 == D_K23*D_K23
rel_disc_norm_23 = 1

# Hensel sign gate at p=29: if alpha == 1 mod P then f(x)=30x^2-alpha
# has f(1)==0 mod P and f'(1)=60==2 mod 29, a unit.
assert 30 % 29 == 1
assert 60 % 29 == 2

print("P03-I0098-D29-LOCAL-SQUARE-CLASS-SWITCH-262=PASS")
print("theta_squared_equals_30_epsilon=PASS")
print("29_inert_in_Qsqrt195=PASS")
print("epsilon_residue_order=3")
print("one_infinite_ray_kernel_order=280")
print("finite_prime_inertia_order=280")
print("no_infinite_ray_kernel_order=140")
print("d29_Kummer_relative_discriminant_norm=16")
print("d23_Kummer_relative_discriminant_norm=1")
print("hensel_fprime_at_1_mod_29=2")
print("ALL_EXACT_CHECKS_PASS=True")
