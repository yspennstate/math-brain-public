import sympy as sp

e = sp.symbols("e")
s,c = sp.symbols("s c", real=True)
u1,u2,b1,b2,rho1,rho2 = sp.symbols("u1 u2 b1 b2 rho1 rho2", real=True)
C,S = sp.symbols("C S", real=True)

r1 = 1 + e**2*rho1
r2 = 1 + e**2*rho2
q1 = 1 + e*u1
q2 = 1 + e*u2
B1 = e*b1
B2 = e*b2

P1 = sp.Matrix([[-r1*B1, 1],[-r1*q1, 0]])
P2 = sp.Matrix([[-r2*B2, 1],[-r2*q2, 0]])
v = sp.Matrix([s,c])

ratio = sp.simplify((P2*P1*v).dot(P2*P1*v)/(q1*q2))
ratio2 = sp.series(ratio,e,0,3).removeO()
ratio2 = sp.expand(ratio2.subs(c**2,1-s**2))
A = sp.expand(sp.diff(ratio2,e).subs(e,0))
B = sp.expand(sp.diff(ratio2,e,2).subs(e,0)/2)
Q = sp.expand(B - A**2/2)
Q = sp.expand(Q.subs(c**2,1-s**2))

A_target = -2*b1*c*s + 2*b2*c*s + (2*s**2-1)*(u1-u2)
assert sp.simplify(A-A_target) == 0

# Trigonometric compact form: C=cos(2phi), S=sin(2phi).
Q_cs = Q
Q_cs = Q_cs.subs(c**2*s**2,S**2/4)
Q_cs = Q_cs.subs(c*s**3,S*(1-C)/4)
Q_cs = Q_cs.subs(c*s,S/2)
Q_cs = Q_cs.subs(s**4,(1-C)**2/4)
Q_cs = Q_cs.subs(s**2,(1-C)/2)
Q_cs = sp.expand(Q_cs).subs(S**2,1-C**2)
Q_cs = sp.expand(Q_cs)

Q_target = (
    rho1*(1-C)+rho2*(1+C)
    +(sp.Rational(1,2)+C/2-C**2/2)*u1**2
    +(sp.Rational(1,2)-C/2-C**2/2)*u2**2
    +(C**2/2-C/2)*b1**2
    +(C**2/2+C/2)*b2**2
    +C*(1-C)*b1*b2
    +(C**2-1)*u1*u2
    +S*(1-C)*u1*b1
    +C*S*u1*b2
    -S*(1-C)*u2*b1
    -S*(1+C)*u2*b2
)
assert sp.simplify(Q_cs-Q_target) == 0

# Leading expectation when E[u_i]=E[b_i]=0,
# Var(u_i)=Var(b_i)=v_i, with deterministic rho_i.
v1,v2 = sp.symbols("v1 v2", positive=True)
noise = [u1,u2,b1,b2]
variances = [v1,v2,v1,v2]
poly = sp.Poly(Q_target,u1,u2,b1,b2)
EQ=0
for powers,coef in poly.terms():
    val=1
    for power,var in zip(powers,variances):
        if power==0: pass
        elif power==1: val=0
        elif power==2: val*=var
        else: raise AssertionError("unexpected degree")
    EQ += coef*val
EQ=sp.expand(EQ)
EQ_expected = rho1*(1-C)+rho2*(1+C)+(v1+v2)/2
assert sp.simplify(EQ-EQ_expected)==0

# Leading linear variance:
A_cs = C*(u2-u1)+S*(b2-b1)
EA2 = sp.expand(A_cs**2)
poly2=sp.Poly(EA2,u1,u2,b1,b2)
EV=0
for powers,coef in poly2.terms():
    val=1
    for power,var in zip(powers,variances):
        if power==0: pass
        elif power==1: val=0
        elif power==2: val*=var
        else: raise AssertionError("unexpected degree")
    EV += coef*val
EV=sp.expand(EV).subs(S**2,1-C**2)
assert sp.simplify(EV-(v1+v2))==0

print("PAIR_MATRIX_IDENTITY: symbolic construction exact")
print("LINEAR_TERM:", sp.factor(A_cs))
print("QUADRATIC_EXPECTATION:", sp.factor(EQ_expected))
print("LINEAR_VARIANCE:", sp.factor(v1+v2))
print("REPORT_INPUT_ASYMPTOTICS: rho_n=1/(2n)+O(n^-2), v_n=1/(2n)+O(n^-2)")
print("ALGEBRA_PLUS_REPORT_ASYMPTOTICS: pair drift 3/(4m)+O(m^-2)")
print("ALGEBRA_PLUS_REPORT_ASYMPTOTICS: pair variance 1/(2m)+O(m^-2)")
print("TARGET_CGF_AFTER_REMAINDER_PROOF: (3t/4+t^2/4)/m + O_T(m^-3/2)")
print("ALL_EXACT_SYMBOLIC_IDENTITIES_PASS")
