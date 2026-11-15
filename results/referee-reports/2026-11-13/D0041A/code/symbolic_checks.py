"""Exact polynomial identities for controls and contour-transform bookkeeping."""
import os
os.environ.update(OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1')
import sympy as S
from pathlib import Path
s,z,q,p,v,A,B=S.symbols('s z q p v A B')
M=S.Matrix([[q*q,-z*q-p],[-z*q+p,z*z-s-q*q]])
N=S.Matrix([[0,q],[q,-z]])
def ds(expr):
    return S.diff(expr,s)+p*S.diff(expr,q)+(s*q+2*q**3)*S.diff(expr,p)-q*q*S.diff(expr,v)-q*B/2*S.diff(expr,A)-q*A/2*S.diff(expr,B)
curv=M.applyfunc(ds)-N.diff(z)+M*N-N*M
assert all(S.expand(x)==0 for x in curv)
H=v+q**4-p**2+s*q**2
assert S.expand(ds(H))==0
phi1=p+v*q
phi2=s*q-v*p-(v*v+q*q)*q/2
assert S.expand(ds(phi1)-(s*q+q**3+v*p))==0
wronskian=S.expand(q*ds(phi1)-p*phi1)
assert S.expand(wronskian+v-H)==0
assert S.expand(phi2-((s+(v*v-q*q)/2)*q-v*phi1))==0
R2=S.Matrix([[1,0]])
res2=(R2*N+v*R2)+R2*(M.diff(z)+M*M)+(s-z*z)*R2*M
assert all(S.expand(x)==0 for x in res2-S.Matrix([[H,0]]))
r=S.Matrix([[A,B]])
res4=2*(r.applyfunc(ds)+r*N+v*r/2)+r*(M.diff(z)+M*M)+(s-z*z)*r*M
assert all(S.expand(x)==0 for x in res4-H*r)
# Finite-N normalization expansion, epsilon=4^(1/3)w*N^(-1/3).
e=S.symbols('e')
phase=2*(1-e)/(2-e)-1-S.log(1-e)/2
assert S.series(phase,e,0,4).removeO()==e**3/24
# Conjugation by exp(w^3/6) and integration by parts.
t,T,w=S.symbols('t T w')
K=S.Function('K')(t,T)
exp=S.exp(-w*T/2)
integrand=S.diff(K,t)+(T*T-t*T)*K/2+w*w*(t-T)*K/2+2*w*K
kernel=S.diff(K,t)+2*S.diff((t-T)*K,T,2)+4*S.diff(K,T)+(T*T-t*T)*K/2
assert S.simplify(kernel-(S.diff(K,t)+(t-T)*(2*S.diff(K,T,2)-T*K/2)))==0
boundary=2*(exp*S.diff((t-T)*K,T)-S.diff(exp,T)*(t-T)*K)+4*exp*K
# exp*integrand - exp*kernel is an exact derivative, with this sign.
assert S.simplify(exp*(integrand-kernel)+S.diff(boundary,T))==0
# Square root determinant reduction: K=A0(T)*sqrt(F(t))*sqrt(D(t,T)).
D,Dt,DT,DTT,a,aT=S.symbols('D Dt DT DTT a aT')
logKT=a+DT/(2*D)
logKTT=aT+(DTT/D-DT**2/D**2)/2
expr=v/2+Dt/(2*D)+(t-T)*(2*(logKTT+logKT**2)-T/2)
poly=D*Dt+v*D**2+(t-T)*((4*(aT+a*a)-T)*D**2+4*a*D*DT+2*D*DTT-DT**2)
assert S.simplify(2*D**2*expr-poly)==0
lines=[
'Lax zero-curvature matrix = 0 (using q\'\'=s*q+2*q^3).',
'Hamiltonian derivative = 0; H=v+q^4-p^2+s*q^2.',
'phi1=p+v*q implies W(q,phi1)=-v, when H=0.',
'phi2=s*q-v*p-(v^2+q^2)*q/2 follows by exact quadrature reduction.',
'beta=2 residual coefficients = (H,0).',
'beta=4 scaled residual coefficients = H*(A,B).',
'finite-N normalization cubic coefficient = epsilon^3/24.',
'normalized contour transform identity and exact boundary concomitant verified.',
'square-root determinant polynomial reduction verified.',
'No Mo-specific determinant identity has been proved by this script.'
]
Path('data/symbolic_checks.txt').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines))
