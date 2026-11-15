"""Derive the compensated cubic from the softmax vector fields, exactly."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime
import sympy as S
import json

x,y=S.symbols('x y'); p=[x,y,1-x-y]
def D(i,f):
    return S.Poly(S.expand(x*((1 if i==0 else 0)-p[i])*S.diff(f,x)+y*((1 if i==1 else 0)-p[i])*S.diff(f,y)),x,y).as_expr()
def coeff(f):
    d=[D(i,f) for i in range(3)]
    cubic=sum(D(i,D(i,d[i])) for i in range(3))
    total=0
    for i in range(3):
        j,k=[r for r in range(3) if r!=i]
        mixed=D(j,D(j,f))-2*D(j,D(k,f))+D(k,D(k,f))
        total+=p[i]*(cubic-d[i]-mixed)/4
    return S.expand(total)
A=9*sum(q*q for q in p)-3; J=sum((3*q-1)**3 for q in p)
SA=coeff(A); SQ=coeff(S.expand(A*A)); beta=S.Rational(49,4)
assert S.expand(SA+(6-A)*(A-J)/18)==0
assert S.expand(SQ-(4*A-4*A*A+S.Rational(2,3)*A**3+J*(-2+3*A-S.Rational(5,9)*A*A)))==0
a,j,t=S.symbols('a j t')
C=(4-beta/3)*a+(-4+beta/18)*a*a+S.Rational(2,3)*a**3
B=beta/3-2+(3-beta/18)*a-S.Rational(5,9)*a*a
bound1=(C+B*j).subs({a:6*t*t,j:6*t**3})
expected1=-2*t*t*(1-t)**2*(48*(t-S.Rational(23,384))**2+S.Rational(239,3072)+60*t**3)
assert S.expand(bound1-expected1)==0
assert S.expand(C+B*(3*a/2-3)+(6-a)**2*(24*a+25)/144)==0
discriminant=S.prod((3*p[i]-3*p[k])**2 for i in range(3) for k in range(i+1,3))
assert S.expand(A**3/6-J*J-discriminant/3)==0
assert S.expand(coeff(S.expand(A*A+beta*A))-SQ-beta*SA)==0
out={'at':datetime.now().astimezone().isoformat(),'complete':True,'method':'Independent exact Sympy two-coordinate softmax vector fields; no producer imports','checked':['S_A identity','S_Q identity','linearity','simplex discriminant','B>=0 completed square factorization','B<0 boundary factorization'],'strict':'0<A<6: both branch upper bounds strictly negative','script_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
Path('checks/t067_compensated_cubic_own.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out))
