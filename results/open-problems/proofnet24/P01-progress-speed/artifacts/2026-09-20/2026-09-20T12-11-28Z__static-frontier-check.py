from fractions import Fraction as F
import sympy as sp

def theta(D,p):
    tau=F(5,3*D+2)
    return p*tau/(1-p+p*tau)

def delta(D,t):
    return F(1)-(D-1)*t+2*(D-1)*t*t

def margin(D,t):
    den=F(5,3)+(D-1)*t
    return 2*delta(D,t)/(den*den)

def p2(D):
    return F(3,8)+F(35,32*D)+F(435,128*D*D)

for D,p0,target in [
    (52,F(1987,5000),F(1,90000)),
    (245,F(1186,3125),F(1,500000)),
]:
    t=theta(D,p0); de=delta(D,t); ma=margin(D,t)
    assert t < F(1,4)
    assert de>0 and ma>target
    print(f"D={D} p0={p0}={float(p0):.12f} Theta={t} delta={de} margin={ma}={float(ma):.12e} target_pass={ma>target}")

D=sp.symbols('D', integer=True, positive=True)
p=sp.Rational(3,8)+sp.Rational(35,32)/D+sp.Rational(435,128)/D**2
tau=sp.Rational(5)/(3*D+2)
t=sp.factor(p*tau/(1-p+p*tau))
qgap=sp.factor(sp.Rational(1,4)-t)
de=sp.factor(1-(D-1)*t+2*(D-1)*t**2)
den=sp.factor(sp.Rational(5,3)+(D-1)*t)
ma=sp.factor(2*de/den**2)
assert sp.simplify(t-(48*D**2+140*D+435)/(48*D**3-4*D**2-177*D+261))==0
assert sp.simplify(qgap-(48*D**3-196*D**2-737*D-1479)/(4*(48*D**3-4*D**2-177*D+261)))==0
assert sp.simplify(de-2*(74064*D**3+88292*D**2-55767*D-98397)/(48*D**3-4*D**2-177*D+261)**2)==0
assert sp.simplify(ma-9*(74064*D**3+88292*D**2-55767*D-98397)/(4096*D**4*(3*D+2)**2))==0
Q=48*D**3-196*D**2-737*D-1479
Qp=sp.diff(Q,D)
assert Q.subs(D,7)>0 and Qp.subs(D,7)>0
assert sp.diff(Qp,D).subs(D,7)>0
G=74064*D**3+88292*D**2-55767*D-98397
assert G.subs(D,7)>0 and sp.diff(G,D).subs(D,7)>0 and sp.diff(G,D,2).subs(D,7)>0
print("p2-Theta:",t)
print("p2-quarter-gap:",qgap)
print("p2-margin:",ma)

x=sp.symbols('x', positive=True)
Dx=1/x
q=(1-sp.sqrt(1-8/(Dx-1)))/4
pstar=sp.simplify(q*(3*Dx+2)/(5+3*(Dx-1)*q))
series=sp.series(pstar,x,0,5)
print("pstar-series:",series)
assert series.removeO().coeff(x,1)==sp.Rational(35,32)
assert series.removeO().coeff(x,2)==sp.Rational(435,128)
assert series.removeO().coeff(x,3)==sp.Rational(7715,512)

a=sp.symbols('a', real=True)
p1=sp.Rational(3,8)+a/D
t1=sp.factor(p1*(sp.Rational(5)/(3*D+2))/(1-p1+p1*(sp.Rational(5)/(3*D+2))))
num1=sp.Poly(sp.expand(sp.together(1-(D-1)*t1+2*(D-1)*t1**2).as_numer_denom()[0]),D)
lead1=sp.factor(num1.LC())
assert sp.simplify(lead1+30*(32*a-35))==0
print("first-order-leading:",lead1)

print("ALL_EXACT_CHECKS_PASS")
