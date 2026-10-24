from fractions import Fraction as FQ
import sympy as sp

# 1. Factor-two event tilt algebra and first-zero barrier.
theta, r = sp.symbols('theta r', positive=True)
a,b,ap,bp,p,pp = sp.symbols('a b ap bp p pp')
c = a*b-p
cp = ap*bp-pp
de = a-ap
df = b-bp
ath=(a+theta*r*ap)/(1+theta*r)
bth=(b+theta*r*bp)/(1+theta*r)
pth=(p+theta*r*pp)/(1+theta*r)
N=sp.factor((1+theta*r)**2*(ath*bth-pth))
N_target=sp.expand(c+theta*r*(c+cp-de*df)+theta**2*r**2*cp)
assert sp.expand(N-N_target)==0
x=sp.symbols('x')
N_x=sp.expand(c+theta*r*(c+cp-x)+theta**2*r**2*cp)
x_at_zero=sp.factor(sp.solve(sp.Eq(N_x,0),x)[0])
assert sp.simplify(x_at_zero-((1+1/(theta*r))*c+(1+theta*r)*cp))==0
uniform_remainder=sp.expand(c+r*(c+cp-(32*c+cp))+r**2*cp)
assert sp.factor(uniform_remainder)==sp.factor(c*(1-31*r)+r**2*cp)

# 2. Five-state terminal polynomial and virtual-pair Rayleigh invariant.
D,P,Q,S,T,g,h,k=sp.symbols('D P Q S T g h k')
poly=D*(1+g+h+k+g*h+g*k+h*k)+P*(1+h+k)+Q*(1+g+k)+S*(1+g+h)+T
Delta_gh=sp.factor(sp.diff(poly,g)*sp.diff(poly,h)-poly*sp.diff(poly,g,h))
expected=D**2*k**2+D**2*k+2*D*S*k+D*S-D*T+P*Q+P*S+Q*S+S**2
assert sp.expand(Delta_gh-expected)==0
constant=sp.expand(Delta_gh.subs(k,0))
assert constant == D*S-D*T+P*Q+P*S+Q*S+S**2

# 3. Generic stability-preserver route kill for L=1+gh*d_g*d_h.
f=(1+g)*(1+h)
Lf=sp.expand(f+g*h*sp.diff(f,g,h))
assert Lf==1+g+h+2*g*h
Delta_L=sp.expand(sp.diff(Lf,g)*sp.diff(Lf,h)-Lf*sp.diff(Lf,g,h))
assert Delta_L==-1

# 4. Exact stress test from prior P14 route-kill graph, now for the physical ratio.
F=FQ(18133,8); Fe=Ff=FQ(3465,4); Fef=FQ(655,2)
d=FQ(406); de0=df0=FQ(100); def0=FQ(24)
q0=Fe*Ff-F*Fef
q1=Fe*df0+de0*Ff-F*def0-d*Fef
q2=de0*df0-d*def0
assert (q0,q1,q2)==(FQ(64555,8),FQ(-14114),FQ(256))
r0=(d/FQ(16))/F
c0=q0/(F*F)
cp0=q2/(d*d)
delta=Fe/F-de0/d
assert r0==FQ(203,18133)
assert delta==FQ(500140,3680999)
ratio=r0*delta*delta/((1+r0)*(c0+r0*cp0))
barrier_ratio=delta*delta/(32*c0+cp0)
assert ratio==FQ(15633751225,121473515472)
assert barrier_ratio==FQ(15633751225,43879174676)
assert ratio < 1 and barrier_ratio < 1

# 5. Independent finite audit of latest P15 claim P15-I0066-HETEROGENEOUS-LYAPUNOV-05B.
xv,yv=sp.symbols('x y', real=True)
z=sp.Matrix([xv,yv])
V=(xv*xv+yv*yv)**2
grad=sp.Matrix([sp.diff(V,xv),sp.diff(V,yv)])
H=sp.hessian(V,(xv,yv))
J=sp.Matrix([[0,-1],[1,0]])
Dm=sp.diag(1,-1)
M1=sp.diag(sp.Rational(17,8),sp.Rational(23,8))
C1=sp.Rational(7,8)*J
C2=sp.Rational(5,8)*Dm
Q1=sp.expand(grad.dot(M1*z)-sp.Rational(1,2)*sum(((C*z).T*H*(C*z))[0] for C in (C1,C2)))
Q1_expected=(37*xv**4+148*xv**2*yv**2+61*yv**4)/8
assert sp.expand(Q1-Q1_expected)==0
loss=4*sp.Rational(1,8)+(12*sp.Rational(1,8)+6*sp.Rational(1,64))+(6*sp.Rational(1,8)+6*sp.Rational(1,64))
assert loss==sp.Rational(47,16)
margin=sp.Rational(9,2)-loss
assert margin==sp.Rational(25,16)
resid=sp.factor(Q1-margin*(xv*xv+yv*yv)**2)
assert sp.expand(resid-(49*xv**4+246*xv**2*yv**2+97*yv**4)/16)==0
comm=C1*C2-C2*C1
assert comm==sp.Matrix([[0,sp.Rational(35,32)],[sp.Rational(35,32),0]])

print('P14_EVENT_TILT_IDENTITY_OK')
print('FIRST_ZERO_PRODUCT = (1+1/(theta*r))*c + (1+theta*r)*cprime')
print('UNIFORM_32_REMAINDER = c*(1-31*r) + r^2*cprime')
print('TERMINAL_DELTA_GH=', sp.sstr(Delta_gh))
print('TERMINAL_CONSTANT=', sp.sstr(constant))
print('STABILITY_OPERATOR_LF=', sp.sstr(Lf))
print('STABILITY_OPERATOR_RAYLEIGH_DELTA=', Delta_L)
print('ROUTEKILL_R=', r0)
print('ROUTEKILL_DELTA=', delta)
print('ROUTEKILL_PHYSICAL_RATIO=', ratio, float(ratio))
print('ROUTEKILL_32_BARRIER_RATIO=', barrier_ratio, float(barrier_ratio))
print('P15_Q1=', sp.sstr(Q1))
print('P15_LOSS=', loss)
print('P15_MARGIN=', margin)
print('P15_RESID=', sp.sstr(resid))
print('P15_COMM=', comm.tolist())
print('ALL_EXACT_CHECKS_PASSED')
