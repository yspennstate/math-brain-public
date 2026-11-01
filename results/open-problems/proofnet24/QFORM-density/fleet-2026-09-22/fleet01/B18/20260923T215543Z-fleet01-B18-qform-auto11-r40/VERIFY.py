import sympy as s

kappa=s.Rational(3,16)
p=s.Rational(5,8)
eps=s.sqrt(3*p*(1-p)*kappa)
a=p-eps
b=1-p-eps
h=kappa/a
C=6*s.sqrt(s.E)*(2*h)**s.Rational(-1,2)*(3-4*h)**(-1)*(a*b)**s.Rational(-1,2)
C_closed=32*(20-3*s.sqrt(15))*s.sqrt(s.E)/(9*(4-s.sqrt(15))**s.Rational(3,2))
kstar=(s.sqrt(313)-13)/24

assert s.simplify(eps-3*s.sqrt(15)/32)==0
assert s.simplify(a-(20-3*s.sqrt(15))/32)==0
assert s.simplify(b-(12-3*s.sqrt(15))/32)==0
assert b>0
assert h<s.Rational(3,4)
assert s.simplify(C-C_closed)==0
assert C<1086
assert s.simplify(12*kstar**2+13*kstar-3)==0
assert kstar>s.Rational(3,16)

partner=3*2**s.Rational(5,3)*(s.Rational(1,16))**s.Rational(-1,3)
assert s.simplify(partner-24)==0

print('eps =', eps, float(eps))
print('a =', a, float(a))
print('b =', b, float(b))
print('h =', s.simplify(h), float(h))
print('C =', s.simplify(C), float(C))
print('kappa_star =', kstar, float(kstar))
print('partner threshold bound =', s.simplify(partner))
