from fractions import Fraction as F
import math

h=F(17,20)
tau=F(3,20)
d=F(53,500)
off=F(3,10)
assert h*h-off*off == F(253,400)
assert h*d-off*off == F(1,10000)
L=h-d
assert L == F(93,125)
u=tau/L
assert u == F(25,124)
R2=1-2*u
assert R2 == F(37,62)
F2=2/h**2 + 4*u/(h**2*R2) + ((1/L+2*u/h)/R2)**2
assert F2 == F(49579300,3560769)
assert F2 < F(1000,267)**2
pert=tau+d
assert pert == F(32,125)
delta=F(267,1000)-pert
assert delta == F(11,1000)
sigma=3*delta/F(8,1)
assert sigma == F(33,8000)
entry=F(27,64)*sigma
assert entry == F(891,512000)

alpha=0.4
I=2**(-(alpha+1)/2)*math.gamma((1-alpha)/2)
C=math.exp(0.5)*math.sqrt(2/math.pi)*(1+I)
m=float(h)
K0=2*m**(-0.75)
sig=float(sigma)
tq2=8*math.pi*math.e/sig
tq1=math.pi*math.e*math.sqrt(2)/sig
bq2=K0*(1+C*tq2**alpha/(4*alpha-1))
bq1=K0*(1+C*tq1**alpha/(4*alpha-1))
am=3/8
Lm=2*(2/float(entry))**am
bm=K0*(1+Lm/(4*am-1))
eta=float(F(11,4000))
Ldiag=2*math.sqrt(2/eta)
bdiag=4*m**(-0.75)*math.sqrt(Ldiag)
assert bq2 < 688
assert bq1 < 346
assert bm < 130
assert bdiag < 34
print('QFORM_B19_S2_3OVER20_CLOSURE_CHECK_PASS')
print('same_sign_det=', F(253,400))
print('third_diag_det=', F(1,10000))
print('lambda_floor=', L)
print('coordinate_mass_cap=', u)
print('outside_mass_floor=', R2)
print('inverse_frobenius_sq=', F2, float(F2))
print('compression_gap=', delta)
print('forced_cross_s1=', sigma)
print('localized_cross_entry=', entry)
print('C_2over5=', C)
print('q2_bound=', bq2)
print('q1_bound=', bq1)
print('mixed_bound=', bm)
print('diag_bound=', bdiag)
