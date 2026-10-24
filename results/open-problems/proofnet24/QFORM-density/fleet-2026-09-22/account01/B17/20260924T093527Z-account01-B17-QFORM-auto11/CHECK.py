import sympy as sp

q,a,t,u=sp.symbols('q a t u', nonnegative=True)

# Exact two-macro formula and expansion.
a_q=3*q/(2-q)
I_a=sp.sqrt(sp.pi)/(2*sp.sqrt(a))*sp.erf(sp.sqrt(a))-(1-sp.exp(-a))/(2*a)
p_q=12/sp.sqrt(2-q)*I_a.subs(a,a_q)
ratio=sp.simplify(p_q/(3*sp.sqrt(2)))
assert sp.series(ratio,q,0,5).removeO() == 1-sp.Rational(3,160)*q**2-sp.Rational(1,224)*q**3+sp.Rational(3,10240)*q**4

p_half=sp.simplify(p_q.subs(q,sp.Rational(1,2)))
assert sp.simplify(p_half-2*sp.sqrt(6)*(sp.sqrt(sp.pi)*sp.erf(1)-1+sp.exp(-1))) == 0
assert 4.22060 < float(sp.N(p_half,30)) < 4.22061

# Degree-nine Taylor/Bernstein positivity certificate for H(a) on 0<=a<=3.
x=sp.symbols('x', nonnegative=True)
S9=sum((-x)**j/sp.factorial(j) for j in range(10))
A9=sp.integrate(S9.subs(x,a*u**2),(u,0,1))
H9=sp.factor(6*a*A9-(a+6)*(1-S9.subs(x,a)))
betas=[
    sp.Rational(1,10),sp.Rational(73,980),sp.Rational(337,5880),
    sp.Rational(4847,107800),sp.Rational(100553,2802800),
    sp.Rational(973307,33633600),sp.Rational(9059871,381180800),
    sp.Rational(7674201,517316800)
]
bern=sum(betas[j]*sp.binomial(7,j)*t**j*(1-t)**(7-j) for j in range(8))
assert sp.simplify(H9.subs(a,3*t)-(3*t)**3*bern) == 0
assert all(beta > 0 for beta in betas)

# Exact dense frame matrices.
n=sp.Matrix([1,2,4])/sp.sqrt(21)
P=n*n.T
B=sp.eye(3)-2*P
V=sp.Matrix([[1,1,1],[1,-1,1],[1,1,-1],[1,-1,-1]])/2
assert sp.simplify(B*B-sp.eye(3)) == sp.zeros(3)
assert sp.simplify(V.T*V-sp.eye(3)) == sp.zeros(3)
assert all(sp.simplify(z) != 0 for z in V*n)

q0=sp.Rational(1,2)
Dcomp=sp.simplify(V*(sp.eye(3)-(2-q0)*P)*V.T)
Dcomp_expected=sp.Matrix([
[-sp.Rational(1,8),-sp.Rational(1,8),sp.Rational(3,8),sp.Rational(3,8)],
[-sp.Rational(1,8),sp.Rational(33,56),-sp.Rational(11,56),sp.Rational(29,56)],
[sp.Rational(3,8),-sp.Rational(11,56),sp.Rational(41,56),sp.Rational(9,56)],
[sp.Rational(3,8),sp.Rational(29,56),sp.Rational(9,56),sp.Rational(17,56)]])
assert Dcomp == Dcomp_expected
assert all(Dcomp[i,j] != 0 for i in range(4) for j in range(4))

S=sp.eye(3)+(sp.sqrt(1-q0)-1)*P
assert sp.simplify(S*S-(sp.eye(3)-q0*P)) == sp.zeros(3)
assert sp.simplify(q0*P+S*S-sp.eye(3)) == sp.zeros(3)

Dun=sp.simplify(V*B*V.T)
Dun_expected=sp.Matrix([
[-sp.Rational(5,12),-sp.Rational(1,4),sp.Rational(5,12),sp.Rational(7,12)],
[-sp.Rational(1,4),sp.Rational(15,28),-sp.Rational(5,28),sp.Rational(17,28)],
[sp.Rational(5,12),-sp.Rational(5,28),sp.Rational(61,84),sp.Rational(11,84)],
[sp.Rational(7,12),sp.Rational(17,28),sp.Rational(11,84),sp.Rational(13,84)]])
assert Dun == Dun_expected
assert all(Dun[i,j] != 0 for i in range(4) for j in range(4))

G=sp.eye(3)+q0*P
C=sp.simplify(G*B)
assert C.eigenvals() == {sp.Integer(1):2,-sp.Rational(3,2):1}

# Partner quantitative average for the uncompensated sibling.
s=sp.symbols('s', nonnegative=True)
Eexp=sp.simplify(2*sp.integrate((1-s)*sp.exp(-sp.Rational(3,2)*s**2),(s,0,1)))
E_expected=-sp.Rational(2,3)+sp.Rational(2,3)*sp.exp(-sp.Rational(3,2))+sp.sqrt(6*sp.pi)*sp.erf(sp.sqrt(6)/2)/3
assert sp.simplify(Eexp-E_expected) == 0
C0=3*sp.sqrt(2)
C1=12*sp.exp(-sp.Rational(1,2))/sp.sqrt(2*sp.pi)
Cpartner=sp.simplify(C1+(C0-C1)*Eexp)
assert 3.98660 < float(sp.N(Cpartner,30)) < 3.98662

# k equal macro rows: leading fragmentation loss.
k=sp.symbols('k', positive=True)
m2=k/sp.Integer(12)
m4=k*(5*k-2)/sp.Integer(240)
c=6*q/(k*(2-q))
Rk=sp.sqrt(2/(2-q))*(1-c*m2+c**2*m4/2)
assert sp.series(Rk,q,0,3).removeO() == 1-sp.Rational(3,80)*q**2/k

print('PASS_QFORM_B17_TWO_MACRO_MINORITY_WITNESS')
print('C2 =', sp.N(p_half,40))
print('gap_to_3sqrt2 =', sp.N(3*sp.sqrt(2)-p_half,40))
print('partner_bound =', sp.N(Cpartner,40))
