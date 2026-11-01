import sympy as sp

t = sp.symbols("t", real=True)
s2, s3, s6 = sp.sqrt(2), sp.sqrt(3), sp.sqrt(6)
a = 1+s2
D = 3+2*s2
C1 = 17+9*s2
Cm = 27+15*s2-8*s3-4*s6
Cp = 27+15*s2+8*s3+4*s6

t1 = -2-s3+s2+s6
t2 = 1/s3
assert sp.simplify(t1-sp.tan(sp.pi/24)) == 0
assert sp.simplify(t2-sp.tan(sp.pi/6)) == 0

R1 = (-sp.Rational(7,4)/(t-a) - C1/8/(t-a)**2 - D/4/(t-a)**3
      +sp.Rational(7,4)/(t+a) - C1/8/(t+a)**2 + D/4/(t+a)**3)
R2 = (sp.Rational(1,12)/(t-a) + Cm/24/(t-a)**2 + D/4/(t-a)**3
      -sp.Rational(1,12)/(t+a) + Cp/24/(t+a)**2 - D/4/(t+a)**3)

cos = (1-t**2)/(1+t**2)
sin = 2*t/(1+t**2)
b0 = 1+s2*cos
b1 = 1+s2*(-sp.Rational(1,2)*cos+s3/2*sin)
b2 = 1+s2*(-sp.Rational(1,2)*cos-s3/2*sin)

def J(a0,a1,a2):
    M=a0
    S1=a0+a1+a2
    S2=a0*a1+a0*a2+a1*a2
    S3=a0*a1*a2
    return 1/M-S1/(2*M**2)+S2/(3*M**3)-S3/(4*M**4)

assert sp.simplify(R1-2*J(b0,b1,b2)/(1+t**2)) == 0
assert sp.simplify(R2-2*J(b0,b1,-b2)/(1+t**2)) == 0

def Npart(B,C,Bp,Cp3):
    return -B/(t-a)-C/(2*(t-a)**2)-Bp/(t+a)-Cp3/(2*(t+a)**2)

N1=Npart(-C1/8,-D/4,-C1/8,D/4)
N2=Npart(Cm/24,D/4,Cp/24,-D/4)
rat=sp.simplify(12*s3*(N1.subs(t,t1)-N1.subs(t,0)+N2.subs(t,t2)-N2.subs(t,t1)))
rat0=-sp.Rational(165,4)+12*s3+15*s2
assert sp.simplify(rat-rat0) == 0

L1=sp.simplify((a+t1)/(a-t1))
L2=sp.simplify((a-t2)/(a+t2))
assert sp.simplify(L1-(s6/6+s2/2)) == 0
peak=rat0+22*s3*sp.log(L1)+s3*sp.log(L2)

B=sp.eye(3)-sp.Rational(2,3)*sp.ones(3)
lam=sp.symbols("lam")
char=sp.factor(B.charpoly(lam).as_expr())
assert sp.expand(char-(lam-1)**2*(lam+1)) == 0

q=sp.symbols("q", positive=True)
Hlo=4*s2/(3*sp.sqrt(q))-1
Hhi=1/q-1/(12*q**2)
assert sp.simplify(Hlo.subs(q,sp.Rational(1,2))-Hhi.subs(q,sp.Rational(1,2))) == 0
assert sp.simplify(sp.diff(Hhi,q)-(sp.Rational(1,6)-q)/q**3) == 0
cross=2*(sp.integrate((1-q)*Hlo,(q,0,sp.Rational(1,2)))+
         sp.integrate((1-q)*Hhi,(q,sp.Rational(1,2),1)))
cross0=sp.Rational(91,36)+sp.Rational(13,6)*sp.log(2)
assert sp.simplify(cross-cross0) == 0

print("PASS exact tangent-cell partial fractions")
print("charpoly =", char)
print("symmetric six-variable peak =", sp.N(peak,30))
print("gap to 3sqrt(2) =", sp.N(3*s2-peak,30))
print("cross witness peak =", sp.N(cross0,30))
print("H(1/2) =", sp.simplify(Hlo.subs(q,sp.Rational(1,2))))
