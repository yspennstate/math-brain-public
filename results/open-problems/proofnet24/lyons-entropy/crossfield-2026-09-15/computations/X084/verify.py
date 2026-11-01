"""Exact self-checks for X084; finite evaluations do not certify domains."""
from fractions import Fraction as F
from pathlib import Path
import json
import math
import sympy as sp

checks = 0
def ok(value):
    global checks
    assert bool(value)
    checks += 1

# Every numeric inequality used in the two domain proofs is rational.
ok(sum(F(7,10)**j / math.factorial(j) for j in range(5)) > 2)
ok(sum(F(2)**j / math.factorial(j) for j in range(5)) == 7)
ok(sum(F(3)**j / math.factorial(j) for j in range(7)) > 19)
ok(3**6 < 768 < 1024)
ok(3**6 < 1999 < 7**4)
ok(F(255,256) > F(9,16))
ok(F(7555,4096) > F(9,5))
ok(F(383,128) > F(29,10))
ok(F(2809,1024) < F(11,4))
ok(F(13,10)*F(12,5) > F(11,4))
ok(2-F(13,4)*F(49,1024) == F(7555,4096))
ok(F(1,8)+F(7,2)*F(7,32)+F(49,64) == F(53,32))
ok(1-F(999,1000)**2 < F(1,500))
ok(F(200,19)+F(27,20) < 12)
ok(2-F(1,500)*((4+F(3,2))**2+16) == F(763,400))
ok(F(763,400) > F(19,10))
ok(3-F(40,361) == F(1043,361))
ok(F(1043,361) > F(14,5))
ok(F(1,500)*36**2 == F(324,125))
ok(F(7,5)*F(23,10) > F(324,125))

r,s=sp.symbols('r s', positive=True)
a,b,c=1-r*r,1-s*s,1-r*r*s*s
k=sp.log(c/(a*b))/2
R=sp.atanh(r)
ok(sp.simplify(sp.diff(k,s)-s*a/(b*c)) == 0)
ok(sp.simplify(2/b+2*r*r/c-(4/b-2*a/(b*c))) == 0)
ok(sp.simplify(2*(2*c-b)/(a*c)-(2/a+2*s*s/c)) == 0)
ok(sp.simplify(sp.diff(R+r*sp.log(a)/2,r)-(1+sp.log(a)/2)) == 0)
for var in (r,s):
    difference=R-k-sp.log(1+r)+sp.log(1+a*s*s/b)/2
    ok(sp.simplify(sp.diff(difference,var)) == 0)
ok(sp.simplify((c/(a*b)).subs({r:0,s:0})) == 1)
ok(sp.simplify(sp.diff(a*R*R,r)-2*R*(1-r*R)) == 0)
ok(sp.simplify(sp.diff(sp.sqrt(a)*R,r)-(1-r*R)/sp.sqrt(a)) == 0)
ok(sp.simplify(sp.diff(sp.sqrt(a)*R**2,r)-R*(2-r*R)/sp.sqrt(a)) == 0)

# The replica identity is verified at an arbitrary exponent on a physical
# normalized two-atom polynomial path, retaining its nonzero acceleration.
t,q=sp.symbols('t q', real=True)
polys=[sp.Rational(2,5)+t/7+t*t/9,sp.Rational(3,5)-t/7-t*t/9]
direct=sum(sp.diff(p**q,t,2).subs(t,0) for p in polys)
compensated=0
for p in polys:
    p0,p1,p2=p.subs(t,0),sp.diff(p,t).subs(t,0),sp.diff(p,t,2).subs(t,0)
    compensated+=p0**(q-2)*p1*p1+p2*(p0**(q-1)-1)/(q-1)
ok(sp.simplify(direct-q*(q-1)*compensated) == 0)
shannon=-sum(p*sp.log(p) for p in polys)
limit=sp.limit(compensated,q,1)
ok(sp.simplify(limit+sp.diff(shannon,t,2).subs(t,0)) == 0)

# Optional finite diagnostics evaluate the exact congruence for interior
# points of the two proved domains. The proof is the inequalities above.
diagnostics=[]
for rv,sv in [(0.999,0.9),(0.999,0),(0.999999,0.98),(0.99999,0.9)]:
    av,bv,cv=1-rv*rv,1-sv*sv,1-rv*rv*sv*sv
    Rv,Sv,Dv=math.atanh(rv),math.atanh(sv),math.atanh(rv*sv)
    kv=.5*math.log(cv/(av*bv))
    t11,t12,t21,t22=Rv+sv*Dv,Sv-sv*kv,Rv-rv*kv,Sv+rv*Dv
    m11=2/av+2*sv*sv/cv-t11*t11-t12*t12
    m22=2/bv+2*rv*rv/cv-t21*t21-t22*t22
    m12=2/cv-2*kv-t11*t21-t12*t22
    n11,n22,n12=av*m11,m22,math.sqrt(av)*m12
    eigmin=.5*(n11+n22-math.sqrt((n11-n22)**2+4*n12*n12))
    ok(av<=bv*bv/256 or (rv>=.999 and sv<=.9))
    ok(eigmin>=.5-1e-10)
    diagnostics.append({'r':rv,'s':sv,'scaled_schur_min_eigenvalue':eigmin})

result={'status':'PASS','exact_assertions':checks-2*len(diagnostics),
        'diagnostic_assertions':2*len(diagnostics),'diagnostics':diagnostics,
        'scope':'Analytic proof in agents/X084.md; finite diagnostics are not domain certificates.'}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
