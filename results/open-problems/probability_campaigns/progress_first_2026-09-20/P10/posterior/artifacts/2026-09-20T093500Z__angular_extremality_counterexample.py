#!/usr/bin/env python3
"""
P10/F0119: rigorous interval certificate that the proposed fixed-radius
angular-extremality reduction is false at the binary-tree KS point.

We work at |m|=1/2.  The two reflection-axis representatives in one Weyl
sector are
  p_axis0 = (2/3,1/6,1/6),
  p_axis60 = (1/2,1/2,0).
The genuinely three-distinct interior representative at theta=pi/12 is
written exactly with radicals:
  p_int = ((1+(sqrt(6)+sqrt(2))/4)/3,
           (1+(sqrt(2)-sqrt(6))/4)/3,
           (1-sqrt(2)/2)/3).

For the quartic Lyapunov
  Psi(p)=D(p||u)+(3/2)sum z_i^3-sum z_i^4
and orbit-averaged two-child kernel K_lambda, this checks at
lambda*=1/sqrt(2) that
  H_int := Psi(p_int)-K_*(p_int,p_int)
is strictly smaller than both axis values at the same radius.
Hence the KS gap is not minimized on a reflection axis at fixed radius.

It also checks at lambda=353/500=0.706 (<1/sqrt(2), >0.70237785)
that the same single-orbit seed strictly contracts in expected Psi, so this
explicit angular counterexample is not itself a one-orbit below-KS
reconstruction witness.

All transcendental evaluations use mpmath.iv outward-rounded interval
arithmetic.
"""
import itertools
import mpmath as mp

iv = mp.iv
PERMS = list(itertools.permutations(range(3)))
ONE = iv.mpf(1)
THIRD = ONE / 3

def xlog3x(x):
    if x.a == 0 and x.b == 0:
        return iv.mpf(0)
    if x.a <= 0:
        raise ValueError("unexpected nonpositive interval in x log(3x)")
    return x * iv.log(3*x)

def Psi(p):
    d = iv.mpf(0)
    for x in p:
        d += xlog3x(x)
    z = [x-THIRD for x in p]
    return d + iv.mpf('1.5')*sum((x**3 for x in z), iv.mpf(0)) \
             - sum((x**4 for x in z), iv.mpf(0))

def T(p, lam):
    return [THIRD + lam*(x-THIRD) for x in p]

def K(p, q, lam):
    r = T(p, lam)
    total = iv.mpf(0)
    for perm in PERMS:
        s = T([q[i] for i in perm], lam)
        Z = sum((r[i]*s[i] for i in range(3)), iv.mpf(0))
        post = [r[i]*s[i]/Z for i in range(3)]
        total += 3*Z*Psi(post)
    return total/6

def Hdiag(p, lam):
    return Psi(p)-K(p,p,lam)

s2 = iv.sqrt(2)
s6 = iv.sqrt(6)
p_axis0 = [iv.mpf(2)/3, iv.mpf(1)/6, iv.mpf(1)/6]
p_axis60 = [iv.mpf(1)/2, iv.mpf(1)/2, iv.mpf(0)]
p_int = [
    (ONE + (s6+s2)/4)/3,
    (ONE + (s2-s6)/4)/3,
    (ONE - s2/2)/3,
]

lam_ks = ONE/s2
lam_below = iv.mpf(353)/500

H0 = Hdiag(p_axis0, lam_ks)
Hi = Hdiag(p_int, lam_ks)
H60 = Hdiag(p_axis60, lam_ks)
gap0 = H0-Hi
gap60 = H60-Hi
below_gap = Hdiag(p_int, lam_below)

print("p_int", p_int)
print("H_axis0", H0)
print("H_interior", Hi)
print("H_axis60", H60)
print("axis0_minus_interior", gap0)
print("axis60_minus_interior", gap60)
print("lambda_below", lam_below)
print("belowKS_single_orbit_gap", below_gap)

assert gap0.a > 0
assert gap60.a > 0
assert below_gap.a > 0
print("OVERALL_PASS")
