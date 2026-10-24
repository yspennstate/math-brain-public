"""Exact checks for X077. These verify identities, not the open entropy sign."""
from pathlib import Path
import json
import sympy as s

ROOT = Path(__file__).resolve().parent
checks = []

def check(expr, label):
    assert s.factor(s.expand(expr)) == 0, (label, s.factor(expr))
    checks.append(label)

def cayley(t):
    a,b,c,d,e,f,g,h = [t[i] for i in [0,1,2,4,3,5,6,7]]
    return (a*a*h*h+b*b*g*g+c*c*f*f+d*d*e*e
       -2*(a*h*(b*g+c*f+d*e)+b*g*c*f+b*g*d*e+c*f*d*e)
       +4*(a*e*f*g+h*b*c*d))

t = s.symbols('t0:8')
m = [sum(t[v] for v in range(8) if v & u == u) for u in range(8)]
check(cayley(t)-cayley(m), 'Cayley invariance under moment inversion')
g12=t[1]*t[2]-t[0]*t[3]
g13=t[1]*t[4]-t[0]*t[5]
g23=t[2]*t[4]-t[0]*t[6]
C=(t[0]**2*t[7]+2*t[1]*t[2]*t[4]
   -t[0]*(t[1]*t[6]+t[2]*t[5]+t[4]*t[3]))/2
check(4*(C*C-g12*g13*g23)-t[0]**2*cayley(t), 'Odds discriminant identity')

a1,a2,a3,x1,x2,x3,q = s.symbols('a1 a2 a3 x1 x2 x3 q', real=True)
a=[a1,a2,a3];x=[x1,x2,x3]
detK=a1*a2*a3-a1*x1-a2*x2-a3*x3+2*q
mom=[1,a1,a2,a1*a2-x3,a3,a1*a3-x2,a2*a3-x1,detK]
check(cayley(mom)-4*(q*q-x1*x2*x3), 'Hermitian principal-minor Cayley identity')
p=[sum((-1)**((v^u).bit_count())*mom[v]
       for v in range(8) if v & u == u) for u in range(8)]
for u in range(8):
    check(s.diff(p[u],q)-2*(-1)**(3-u.bit_count()), f'Phase atom derivative {u}')

for i in range(3):
    j,k=[v for v in range(3) if v!=i]
    pp=lambda mask:p[mask]
    # Differentiate logarithms as rational terms to avoid branch assumptions.
    cp=sum(s.diff(pp(v),q)/pp(v) for v in [1<<j,1<<k])
    cp-=sum(s.diff(pp(v),q)/pp(v) for v in [0,(1<<j)|(1<<k)])
    target=2*sum(1/pp(v) for v in [1<<j,1<<k,0,(1<<j)|(1<<k)])
    check(cp-target, f'Conditional logarithm derivative {i}')
tauprime=sum((1 if v.bit_count()%2==0 else -1)*s.diff(p[v],q)/p[v]
             for v in range(8))
check(tauprime+2*sum(1/v for v in p), 'Triple logarithm derivative')

c1,c2,c3,tau = s.symbols('c1 c2 c3 tau', real=True)
u1,v1,u2,v2,u3,v3=s.symbols('u1 v1 u2 v2 u3 v3', real=True)
ks=[u1+s.I*v1,u2+s.I*v2,u3+s.I*v3]
K=s.Matrix([[a1,ks[2],s.conjugate(ks[1])],
            [s.conjugate(ks[2]),a2,ks[0]],
            [ks[1],s.conjugate(ks[0]),a3]])
M=s.diag(c1,c2,c3)+tau*K
E=c1*c2*c3+tau*(a1*c2*c3+a2*c1*c3+a3*c1*c2)
E+=tau**2*(c1*(a2*a3-ks[0]*s.conjugate(ks[0]))
    +c2*(a1*a3-ks[1]*s.conjugate(ks[1]))
    +c3*(a1*a2-ks[2]*s.conjugate(ks[2])))+tau**3*K.det()
check(M.det()-E, 'Atom-only determinant E(p)')

r=s.symbols('r1:4', real=True);b=s.symbols('s1:4', real=True)
z=[r[i]+s.I*b[i] for i in range(3)]
A=s.Matrix([[0,z[2],s.conjugate(z[1])],
            [s.conjugate(z[2]),0,z[0]],
            [z[1],s.conjugate(z[0]),0]])
frozen=-2*s.trace(M*A.adjugate())
claimed=2*sum(M[i,i]*(z[i]*s.conjugate(z[i])) for i in range(3))
claimed-=4*tau*sum(s.re(ks[i]*z[(i+1)%3]*z[(i+2)%3]) for i in range(3))
check(frozen-claimed, 'Complete zero-diagonal frozen form')

m1,m2,m3,l,h1,h2,h3=s.symbols('m1 m2 m3 l h1 h2 h3', real=True)
Bminus=s.Matrix([[m1,-l*h3,-l*h2],[-l*h3,m2,-l*h1],[-l*h2,-l*h1,m3]])
Bplus=s.Matrix([[m1,l*h3,l*h2],[l*h3,m2,l*h1],[l*h2,l*h1,m3]])
phase_stripped=2*sum(mm*(rr*rr+ss*ss) for mm,rr,ss in zip([m1,m2,m3],r,b))
phase_stripped-=4*l*sum(hh*(r[(i+1)%3]*r[(i+2)%3]-b[(i+1)%3]*b[(i+2)%3])
                              for i,hh in enumerate([h1,h2,h3]))
check(phase_stripped-2*(s.Matrix(r).T*Bminus*s.Matrix(r))[0]
      -2*(s.Matrix(b).T*Bplus*s.Matrix(b))[0], 'Independent tangent-phase rotation split')
base=m1*m2*m3-l*l*(m1*h1*h1+m2*h2*h2+m3*h3*h3)
check(Bminus.det()-(base-2*l**3*h1*h2*h3), 'Minus determinant')
check(Bplus.det()-(base+2*l**3*h1*h2*h3), 'Plus determinant')
C2=Bminus[:2,:2];v=Bminus[:2,2]
rho=m3-(v.T*C2.inv()*v)[0]
assert s.factor(rho-Bminus.det()/C2.det())==0
checks.append('Positive two-by-two Schur factor')

# One exact, dense, nonsymmetric complex measured tensor.
K0=s.Matrix([[s.Rational(1,5),s.Rational(1,10),(1+s.I)/20],
             [s.Rational(1,10),s.Rational(3,5),s.Rational(1,10)],
             [(1-s.I)/20,s.Rational(1,10),s.Rational(4,5)]])
p0=[s.factor((-1)**(3-u.bit_count())*
     (K0-s.diag(*[int(not (u>>i)&1) for i in range(3)])).det()) for u in range(8)]
Q0=s.expand(K0[0,1]*K0[1,2]*K0[2,0])
check(cayley(p0)+4*s.im(Q0)**2, 'Complex witness Cayley identity')
assert all(v>0 for v in p0)
checks.append('Strict witness atom positivity')
assert all(K0[:i,:i].det()>0 and (s.eye(3)-K0)[:i,:i].det()>0 for i in range(1,4))
checks.append('Strict witness kernel positivity')

out={'status':'PASS','exact_assertions':len(checks),'checks':checks,
     'witness_atoms':[str(v) for v in p0], 'witness_loop':str(Q0),
     'witness_cayley':str(s.factor(cayley(p0))),
     'open_claims':'No universal sign for the Fisher-wing scalar or moving diagonals is tested or asserted.'}
(ROOT/'results.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'PASS: {len(checks)} exact assertions')
