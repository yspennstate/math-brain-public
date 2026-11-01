#!/usr/bin/env python3
from fractions import Fraction as Q

# Intervals A=[0,1/6), B=[1/6,1/2), C=[1/2,1].
lengths = [Q(1,6), Q(1,3), Q(1,2)]
first_moments = [Q(1,72), Q(1,9), Q(3,8)]

# Heights h_i(r)=a_i+b_i r for f_r=(5r, 3-4r, r).
heights = [(Q(0),Q(5)), (Q(3),Q(-4)), (Q(0),Q(1))]

mass = (
    sum(a*L for (a,b),L in zip(heights,lengths)),
    sum(b*L for (a,b),L in zip(heights,lengths)),
)
mean = (
    sum(a*M for (a,b),M in zip(heights,first_moments)),
    sum(b*M for (a,b),M in zip(heights,first_moments)),
)

# r_*=3/5 is the right endpoint of the maximal unimodal parameter range.
rstar = Q(3,5)
h0 = [a for a,b in heights]
hstar = [a+b*rstar for a,b in heights]

# f_r=(1-lambda) f_0 + lambda f_{3/5}, lambda=5r/3.
lam_coeff = Q(5,3)
mix = []
for u,v in zip(h0,hstar):
    mix.append((u, lam_coeff*(v-u)))

print('mass affine =', mass)
print('mean affine =', mean)
print('rstar =', rstar)
print('h(0) =', h0)
print('h(3/5) =', hstar)
print('mixture affine coefficients =', mix)
print('target affine coefficients =', heights)
print('unimodality differences:')
print('h2-h1 = 3 - 9 r')
print('h2-h3 = 3 - 5 r')
print('h1-h2 = -3 + 9 r')
print('density range: h2>=0 iff r<=3/4; h1,h3>=0 iff r>=0')
print('unimodal range within density range: 0<=r<=3/5')

assert mass == (Q(1),Q(0))
assert mean == (Q(1,3),Q(0))
assert mix == heights
assert h0 == [Q(0),Q(3),Q(0)]
assert hstar == [Q(3),Q(3,5),Q(3,5)]

print('ALL_EXACT_CHECKS_PASS')
