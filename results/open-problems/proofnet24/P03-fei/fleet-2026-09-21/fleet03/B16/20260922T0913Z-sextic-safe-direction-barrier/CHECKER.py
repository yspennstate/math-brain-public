#!/usr/bin/env python3
from fractions import Fraction as F

# Exact arithmetic for the strong Numaro witness from the source-bound
# fleet01/B16 report, using its rigorous defect lower bound 38023/10^6.
alpha = F(57,256)
rest = F(465,256)
m1 = F(5,228)
mout = F(5,1024)
deficit = F(38023,10**6)

# Every endpoint-zero symmetric even polynomial of degree <=6 with positive
# centre value can be normalized as
# F_{A,B}(m)=(1-m^2)(1+A m^2+B m^4), hence F(0)=1.
def basis(m):
    x=m*m
    return (1-x, (1-x)*x, (1-x)*x*x)

def selector_coeff(a,b,t):
    q=1-t
    d=abs(b-a)
    c=q*a+t*b
    s=q-t
    out=[]
    for j in range(3):
        out.append(q*basis(a)[j] + t*basis(b)[j] - basis(c)[j]
                   + d*F(1,2)*basis(s)[j])
    return tuple(out)

# Two actual Boolean selector configurations. In each, one restriction is
# constant and the other is a one-variable Boolean gate at a suitable product
# bias, so delta=|a-b|/2 is realized exactly.
C1 = selector_coeff(F(-1), F(31,32), F(31,32))
C2 = selector_coeff(F(3,32), F(1), F(17,32))

assert C1 == (
    F(1953,1048576),
    F(16568379009,1099511627776),
    F(28487677659001281,1152921504606846976),
)
assert C2 == (
    F(258825,1048576),
    -F(236990264175,1099511627776),
    -F(84397791851807175,1152921504606846976),
)

# Strong Numaro witness payment per unit centre F(0)=1.
b1=basis(m1); bo=basis(mout)
O = (
    alpha*b1[0] + rest - bo[0],
    alpha*b1[1] - bo[1],
    alpha*b1[2] - bo[2],
)
assert O == (
    F(62098577,59768832),
    F(16938576520025,203621856882720768),
    F(35311637412221110625,693703711666428733273669632),
)

# Exact dual certificate. Any universally gate-safe F must obey
# C1_0+C1_1 A+C1_2 B >=0 and C2_0+C2_1 A+C2_2 B >=0.
# Positive lambdas satisfying O_j=-lambda1*C1_j-lambda2*C2_j (j=1,2)
# upper-bound witness efficiency by O0+lambda1*C1_0+lambda2*C2_0.
det=C1[1]*C2[2]-C2[1]*C1[2]
lam1=((-O[1])*C2[2]-C2[1]*(-O[2]))/det
lam2=(C1[1]*(-O[2])-(-O[1])*C1[2])/det
assert lam1 == F(106624992234261574365420550,74071884319574458230463049577)
assert lam2 == F(2054409844073332992321877,4222157355711667002846373389)
assert lam1>0 and lam2>0
assert O[1]+lam1*C1[1]+lam2*C2[1] == 0
assert O[2]+lam1*C1[2]+lam2*C2[2] == 0

Rmax = O[0] + lam1*C1[0] + lam2*C2[0]
assert Rmax == F(
    117399595402058107229743783687,
    112981776538836095856994516992
)

# Equality point of the two necessary selector inequalities.
A = F(212299128242176,143773227712611)
B = -F(39145912483708928,40112730531818469)
assert C1[0]+C1[1]*A+C1[2]*B == 0
assert C2[0]+C2[1]*A+C2[2]*B == 0
assert O[0]+O[1]*A+O[2]*B == Rmax

required_center_increment = deficit/Rmax
center_dagger = F(6521851214,10**9)
required_center = center_dagger + required_center_increment
assert required_center_increment == F(
    67123532645877576137039101868544,
    1834368678157157925464746620109375
)

# Compare with the source-proved theta=1/36 safe quartic ray.
Deta = F(7405187762554608605,58643094782223581184)
eta_center = F(35,288)
Reta = Deta/eta_center
assert Reta == F(1481037552510921721,1425352998179045376)
assert Reta < Rmax

# Sharpen the older theta bracket using its actual selector (a,b,t)=(1/5,1,3/5).
# F_theta=(1+theta)(1-m^4)-2theta(1-m^2).
def scalar_def(Fun,a,b,t):
    q=1-t; d=abs(b-a); c=q*a+t*b
    return q*Fun(a)+t*Fun(b)-Fun(c)+d*F(1,2)*Fun(q-t)
F2=lambda m: 1-m*m
F4=lambda m: 1-m**4
S2=scalar_def(F2,F(1,5),F(1),F(3,5))
S4=scalar_def(F4,F(1,5),F(1),F(3,5))
assert S2==F(144,625)
assert S4==F(4896,390625)
theta_bound = S4/(2*S2-S4)
assert theta_bound == F(17,608)

print('PASS')
print('C1', *[str(x) for x in C1])
print('C2', *[str(x) for x in C2])
print('O', *[str(x) for x in O])
print('lambda1', lam1)
print('lambda2', lam2)
print('Aeq', A)
print('Beq', B)
print('Rmax_exact', Rmax)
print('Rmax_decimal', format(float(Rmax), '.18g'))
print('R_eta_decimal', format(float(Reta), '.18g'))
print('relative_efficiency_gap', format(float((Rmax-Reta)/Rmax), '.18g'))
print('theta_upper_exact', theta_bound)
print('theta_upper_decimal', format(float(theta_bound), '.18g'))
print('required_center_increment_exact', required_center_increment)
print('required_center_increment_decimal', format(float(required_center_increment), '.18g'))
print('required_center_decimal', format(float(required_center), '.18g'))
