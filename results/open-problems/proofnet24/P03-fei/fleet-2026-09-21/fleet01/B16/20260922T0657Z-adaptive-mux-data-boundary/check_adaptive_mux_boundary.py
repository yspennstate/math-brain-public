import math, random
from fractions import Fraction

# Analytic constants in REPORT.md.
assert Fraction(21,88) < Fraction(1,4)
assert 0.25 < 0.258204856
assert Fraction(31,176)+Fraction(11,176)==Fraction(21,88)

# The only calculus auxiliary used in the entropy estimate:
# 5+log_2 L <= L for L>=8.  Its derivative difference is
# 1 - 1/(L ln 2) > 0 for L>=8, so checking L=8 is enough.
assert abs((5+math.log2(8))-8) < 1e-15
assert 1 - 1/(8*math.log(2)) > 0

# Diagnostics only: sample the exact six MUX masses to stress the two
# coarse inequalities used in the analytic proof.  The theorem does not
# rely on this finite sampling.
rng=random.Random(160922)
max_l1_ratio=0.0
min_sym_ratio=float('inf')
N=100000
for _ in range(N):
    p=max(min(rng.random(),1-1e-12),1e-12)
    x=max(min(rng.random(),1-1e-12),1e-12)
    Q=p*(1-p)*x*(1-x)
    L=math.log2(16/Q)
    assert L >= 8-1e-12
    y=Q/(176*L)*rng.random()

    r0=(1-p)*x
    r=r0+p*y
    Vp=4*p*(1-p)
    Vy=4*y*(1-y)
    Vx=4*x*(1-x)
    w0=((1-2*r0)**2, Vp*x*x, (1-p)**2*Vx, 0.0,
        p*(1-p)*Vx, 0.0)
    w=((1-2*r)**2, Vp*(y-x)**2, (1-p)**2*Vx, p*p*Vy,
       p*(1-p)*Vx, p*(1-p)*Vy)
    l1=sum(abs(a-b) for a,b in zip(w,w0))
    if y>0:
        max_l1_ratio=max(max_l1_ratio,l1/y)
    min_sym_ratio=min(min_sym_ratio,min(r0,1-r0)/Q,min(r,1-r)/Q)
    assert l1 < 11*y + 1e-14
    assert min(r0,1-r0) >= Q - 1e-15
    assert min(r,1-r) >= Q - 1e-12

    theta0=11*Q/(352*L)
    # e<3 and 5+log_2 L<=L yield the analytic 2L bound.
    assert math.log2(5*math.e/theta0) < 2*L + 1e-12

print('PASS')
print('samples',N)
print('max_exact_l1_over_y',format(max_l1_ratio,'.15f'))
print('min_exact_segment_symmetric_distance_over_Q',format(min_sym_ratio,'.15f'))
print('analytic_residual_loss_fraction',f'{Fraction(21,88)}',float(Fraction(21,88)))
print('cross_deficit_floor',0.258204856)
