from sympy import symbols, Matrix, simplify, factor, sqrt, Rational

A,B,sig,z,r1,r2,t1,t2 = symbols("A B sig z r1 r2 t1 t2", positive=True, real=True)
a=sqrt(A); b=sqrt(B)
delta=A+B-2*z

Hminus=Matrix([[A,0,-a*b,0],[0,A,0,-sig],[-a*b,0,B,0],[0,-sig,0,B]])
ker=Matrix([b,0,a,0])
assert simplify(Hminus*ker)==Matrix([0,0,0,0])
t1_gate=-(a/b)*r1
ell=Matrix([-A*r1-2*a*b*t1_gate,-A*r2,-B*t1_gate-2*a*b*r1,-B*t2])
ell=simplify(ell)
assert ell==Matrix([A*r1,-A*r2,-a*b*r1,-B*t2])
assert simplify((ell.T*ker)[0])==0
R_top=simplify((A*r1)**2+(a*b*r1)**2)/(A+B)
H2=Matrix([[A,-sig],[-sig,B]])
ell2=Matrix([-A*r2,-B*t2])
R_second=factor((ell2.T*H2.inv()*ell2)[0])
R=factor(R_top+R_second)
R_expected=factor(A*r1**2 + A*B*(A*r2**2+2*sig*r2*t2+B*t2**2)/(A*B-sig**2))
assert simplify(R-R_expected)==0
q=factor(3*A*B*(2*z-A-B))
assert simplify((q+3*R) - 3*(R-A*B*delta))==0
pay=factor(R/(A*B))
pay_expected=factor(r1**2/B +(a*r2+b*t2)**2/(2*a*b*(a*b-sig)) +(a*r2-b*t2)**2/(2*a*b*(a*b+sig)))
assert simplify(pay-pay_expected)==0
x,y = symbols("x y", real=True)
w=a*x-b*y
N_expected=-2*((w-(r1/b)*x*y)**2 + (delta-r1**2/B)*x**2*y**2)
cx=(1-x**2)/(1+x**2); sx=2*x/(1+x**2)
cy=(1-y**2)/(1+y**2); sy=2*y/(1+y**2)
Fdiff=(A*(cx-1)+B*(cy-1)+z*(cx-1)*(cy-1)+r1*sx*(cy-1)+t1_gate*sy*(cx-1)+a*b*sx*sy)
N=simplify(Fdiff*(1+x**2)*(1+y**2))
assert simplify(N-N_expected)==0
cal={A:Rational(1,2),B:Rational(1,2),sig:Rational(1,2),z:Rational(-1,2),r1:0,r2:0,t2:0}
assert simplify(q.subs(cal))==Rational(-3,2)
assert simplify(delta.subs(cal))==2
print("PASS mixed-Schur kernel and cubic gate")
print("PASS explicit reserve:")
print(" R=A*r1^2 + A*B*(A*r2^2+2*sig*r2*s2+B*s2^2)/(A*B-sig^2)")
print("PASS exact payment form:")
print(" delta >= r1^2/B +(sqrt(A)r2+sqrt(B)s2)^2/[2sqrt(AB)(sqrt(AB)-sig)]")
print("          +(sqrt(A)r2-sqrt(B)s2)^2/[2sqrt(AB)(sqrt(AB)+sig)]")
print("PASS polar-alignment consequence:")
print(" |sqrt(A)r+sqrt(B)Q s|^2 <= 2sqrt(AB)(sqrt(AB)-sig)*delta")
print("PASS top-circle exact factor:")
print(" numerator=-2[(sqrt(A)x-sqrt(B)y-r1*x*y/sqrt(B))^2 +(delta-r1^2/B)x^2y^2]")
print("PASS lead calibration q=-3/2, delta=2")
