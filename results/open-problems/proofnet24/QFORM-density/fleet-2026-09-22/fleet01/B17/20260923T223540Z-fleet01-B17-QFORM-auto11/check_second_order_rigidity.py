import sympy as sp

x=sp.symbols('x', positive=True)
xs=sp.sqrt(6)/(sp.sqrt(6)+sp.sqrt(57))
ys=(1-xs)/2

# first-order total-dimension coefficient for aligned negative bank 3
K=(sp.Rational(1,640))*(sp.Rational(228,1)/(1-x)+sp.Rational(24,1)/x)
Kstar=sp.simplify(K.subs(x,xs))
assert sp.simplify(sp.diff(K,x).subs(x,xs))==0
assert sp.simplify(sp.diff(K,x,2).subs(x,xs))>0

# exact second-order cone coefficients at u=(0,0,1)
a0=sp.Rational(-4833,327680)
a1=sp.Rational(-173,17920)
b00=sp.Rational(7803,819200)
b01=sp.Rational(603,51200)
H=sp.simplify((2*a0+b00)/((1-x)/2)**2+a1/x**2+2*b01/(x*((1-x)/2)))
Hstar=sp.simplify(H.subs(x,xs))
Htarget=sp.Rational(-1299963,13619200)+sp.Rational(108550,13619200)*sp.sqrt(38)
assert sp.simplify(Hstar-Htarget)==0

# orientation penalty for N(u1+u2)->ell
ctheta=sp.simplify(sp.Rational(1,20)*(sp.Rational(3,16)/ys+sp.Rational(9,4)/xs))
ctarget=sp.Rational(21,160)+sp.Rational(87,1520)*sp.sqrt(38)
assert sp.simplify(ctheta-ctarget)==0
assert ctheta>0

# allocation quadratic penalty for sqrt(N)(p-p*) -> d
qpos=sp.simplify(sp.Rational(57,640)/ys**3)
qneg=sp.simplify(sp.Rational(24,640)/xs**3)
assert qpos>0 and qneg>0

# exact genuinely rotated rational Householder axis used in the source theorem
N=sp.symbols('N', integer=True, positive=True)
den=N**4+5
norm=sp.simplify(((2*N**2)**2+(4*N**2)**2+(N**4-5)**2)/den**2)
leak=sp.simplify(((2*N**2)**2+(4*N**2)**2)/den**2)
assert norm==1
assert leak==20*N**4/(N**4+5)**2

print('PASS QFORM_B17_SECOND_ORDER_RIGIDITY')
print('xstar =', sp.radsimp(xs))
print('ystar =', sp.radsimp(ys))
print('Kstar =', sp.radsimp(Kstar), float(Kstar))
print('Hstar =', sp.radsimp(Hstar), float(Hstar))
print('ctheta =', sp.radsimp(ctheta), float(ctheta))
print('qpos =', sp.radsimp(qpos), float(qpos))
print('qneg =', sp.radsimp(qneg), float(qneg))
print('leak =', sp.factor(leak))
