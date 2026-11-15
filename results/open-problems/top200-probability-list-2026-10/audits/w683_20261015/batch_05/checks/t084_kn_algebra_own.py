"""Own universal Hermite elimination, Riccati and boundary-transition algebra."""
from pathlib import Path
from hashlib import sha256
from datetime import datetime
import json
import sympy as S

n,t,r=S.symbols('n t r');a0,PP,RR=S.symbols('a0 PP RR');h=(n-2)*(n-3)
X=((n+a0)*RR-PP)/(a0*(n-2))
Y=((n+a0)*X-RR)/(a0*(n-3))
Z=PP-(n-1)*RR;E=RR-(n-2)*X;L=X-(n-3)*Y;D=X-(n-4)*Y
expected=[Z,(PP-n*RR)/a0,(n*PP-(n*n+2*a0)*RR)/(a0*a0*(n-2)),((n-4)*a0*(n-2)*RR+(a0-n*(n-4))*((n+a0)*RR-PP))/(a0*a0*h)]
for left,right in zip([Z,E,L,D],expected):assert S.cancel(left-right)==0
Lz=((2+n*t)*r-2*t)/(n-2)
Dz=(1-2*(n-4)*t+(-1/t+2*n-9+n*(n-4)*t)*r)/h
assert S.cancel(L/Z-Lz.subs({r:E/Z,t:1/a0},simultaneous=True))==0
assert S.cancel(D/Z-Dz.subs({r:E/Z,t:1/a0},simultaneous=True))==0
B=n*n*t*t+(2*n+1)*t-1
phi=t-2*n*t*t+B*r-n*(n-1)*t*r*r
assert S.cancel(r+2*(n-2)*Lz+h*Dz/2-n*(n-1)*r*r/2-phi/(2*t))==0
delta=t*h;aa=t-2*(n-4)*t*t;bb=-1+(2*n-9)*t+n*(n-4)*t*t
F=delta*r*r-bb*r-aa
assert S.cancel(F-delta*(r*r-Dz))==0
M=S.symbols('M')
choose2=lambda z:z*(z-1)/2
E3=choose2(M-1)-(n-2);D4=choose2(M-2)-2*(n-2)-2
assert S.expand((M-1)**2+2*E3-D4-M*(M-2)-choose2(M))==2
assert S.expand(2*(M-1)-(M+M-3))==1
assert S.expand(E3-M*(M-1)+M*M-choose2(M))==3-n
r1=-(n+6)/n**3;r2=(42-5*n)/n**5
rho=2/n+r1/t+r2/t**2
res=S.expand(2*t*t*S.diff(rho,t)-phi.subs(r,rho))
assert S.cancel(res.coeff(t,1))==0 and S.cancel(res.coeff(t,0))==0
flimit=S.expand(F.subs(r,rho)).coeff(t,0)
assert S.cancel(flimit-4*h/n**4)==0

G=S.expand(2*t*t*S.diff(F,t)+S.diff(F,r)*phi)
LL=n**3*(n-4)*t**4+2*n*(n*n-4*n-6)*t**3+3*(n*n-9*n+3)*t*t+2*(n*n-9*n+9)*t-(2*n-3)
CC=2*n*n*(n-4)*t**3+3*n*(n-6)*t*t+(2*n*n-16*n+15)*t-(2*n-3)
A=n*(n-4)
J=2*A*A*t**3-6*A*(n-2)*t*t+6*(n-1)*(n-3)*t-(2*n-3)
remainder=h*G-F*(-2*h*n*(n-1)*t*r+2*h*t+2*h*B-n*(n-1)*bb)-2*(LL*r-t*CC)
assert S.Poly(S.expand(remainder),n,t,r).is_zero
assert S.Poly(S.expand(delta*t*t*CC*CC-bb*t*LL*CC-aa*LL*LL+h*h*t**5*J),n,t).is_zero
assert S.expand(S.diff(J,t)-6*((A*t-(n-2))**2-1))==0
assert S.cancel(J.subs(t,(n-3)/A)+(n-6)/(n-4))==0
assert S.cancel(J.subs(t,(n-1)/A)+(n-2)/n)==0
assert S.expand((n-1)*(n-3)-A)==3
disc=S.expand(bb*bb+4*delta*aa)
display=1+(18-4*n)*t+(6*n*n-48*n+105)*t*t+(-4*n**3+38*n*n-136*n+192)*t**3+n*n*(n-4)**2*t**4
assert S.expand(disc-display)==0
c,u,x=S.symbols('c u x')
d=disc.subs(n,c+3)
first=S.cancel(c**4*(1+u)**4*d.subs(t,u/(c*(1+u))))
cf=[c**4,6*c**3,c*c*(6*c+15),-2*c*(c+1)*(2*c-9),-3*(c-3)*(c+1)]
assert S.expand(first-sum(v*u**i for i,v in enumerate(cf)))==0
second=S.cancel(c**4*d.subs(t,(1+u)/c))
cs=[-3*(c-3)*(c+1),2*(2*c**3-13*c*c+3*c+18),9*(2*c**3-5*c*c-2*c+6),6*(c-1)*(3*c*c-c-6),(c+3)**2*(c-1)**2]
assert S.expand(second-sum(v*u**i for i,v in enumerate(cs)))==0
assert S.expand((2*c**3-5*c*c-2*c+6).subs(c,x+4))==2*x**3+19*x*x+54*x+46
assert S.expand((3*c*c-c-6).subs(c,x+4))==3*x*x+23*x+38
assert S.cancel(G.subs(r,bb/(2*delta))+t*t*S.diff(disc,t)/(2*delta)-disc/(2*h))==0

# Compare all four common-argument Hermite counts with independent K4..K6 census.
counts=json.loads(Path('checks/t084_kn_counts_own.json').read_text());assert counts['complete']
for row in counts['rows']:
    nn=row['n']
    if nn<4:continue
    bp=nn+1/t;pa=1/t;P=[S.Integer(1),bp]
    for k in range(2,nn):P.append(S.expand(bp*P[-1]-pa*(k-1)*P[-2]))
    q=lambda k:P[k]-k*P[k-1] if k else P[0]
    terms=[q(nn-1),q(nn-2),q(nn-3),P[nn-3]-(nn-4)*P[nn-4]]
    for key,value in zip(['partition','edge','adjacent_pair','disjoint_pair'],terms):
        predicted=S.Poly(S.cancel(t**(nn-1)*value),t)
        assert {int(e[0]):int(v) for e,v in predicted.terms()}=={int(k):v for k,v in row[key].items()},(nn,key)
out={'complete':True,'at':datetime.now().astimezone().isoformat(),'method':'Own Sympy universal polynomial identities plus independent labelled forest counts','C016':['four Hermite eliminations','affine incident and disjoint equations4/5','Riccati equation8','Rayleigh quadratic','small-t leading coefficients1 and2','Laurent r1/r2','strict infinity limit4h/n^4','all four counts K4..K6'],'C017':['linear boundary remainder identity1','root-product identity2','J derivative and both stationary values','beta>tc numerator3','discriminant quartic','both whole positive-axis substitutions','c=x+4 positivity expansions'],'C018':['double-root calibration modulo discriminant'],'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
Path('checks/t084_kn_algebra_own.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(out))
