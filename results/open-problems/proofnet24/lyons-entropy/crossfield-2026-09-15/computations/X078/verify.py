"""Exact checks for X078. No numerical sign is a proof input."""
import sympy as S
import json
from pathlib import Path
R=S.Rational
checks=0
def ok(t):
 global checks
 assert bool(t)
 checks+=1

def atoms(K):
 return [S.factor((-1)**(3-mask.bit_count())*(K-S.diag(*[0 if mask&(1<<i) else 1 for i in range(3)])).det()) for mask in range(8)]
def logs_coeff(t):
 # Coefficients of -2 sum c_i -2 t tau, in mask order.
 c=[0]*8
 for i,j in [(1,2),(2,0),(0,1)]:
  for mask,sgn in [(1<<i,1),(1<<j,1),(0,-1),((1<<i)|(1<<j),-1)]: c[mask]-=2*sgn
 for mask in range(8):c[mask]-=2*t*(1 if mask.bit_count()%2==0 else -1)
 return c

def log_bounds(x,N=30):
 x=R(x);m=0
 while x>=2:x/=2;m+=1
 while x<1:x*=2;m-=1
 def series(z):
  lo=2*sum(z**(2*j+1)/R(2*j+1) for j in range(N))
  return lo,lo+2*z**(2*N+1)/(R(2*N+1)*(1-z*z))
 l2,u2=series(R(1,3));lr,ur=series((x-1)/(x+1))
 return (lr+m*l2,ur+m*u2) if m>=0 else (lr+m*u2,ur+m*l2)

def linear_log_bounds(c,p):
 lo=R(0);hi=R(0)
 for a,x in zip(c,p):
  l,u=log_bounds(x)
  lo+=a*(l if a>=0 else u);hi+=a*(u if a>=0 else l)
 return lo,hi

K=S.Matrix([[R(1,10),R(1,20),R(1,25)],[R(1,20),R(2,5),R(2,25)],[R(1,25),R(2,25),R(7,10)]])
p=atoms(K);a=S.Matrix([K[i,i] for i in range(3)])
q=[x*(1-x) for x in a]
for J in [K,S.eye(3)-K]:
 for i in (1,2,3):ok(J[:i,:i].det()>0)
ok(K[0,0]<R(1,5))
ratio=S.factor(p[0]*p[3]*p[5]*p[6]/(p[1]*p[2]*p[4]*p[7]))
ok(ratio<1);ok(K[0,1]*K[1,2]*K[2,0]>0)
# Determinant-feasible, biased Walsh atom identity.
for mask in range(8):
 x=S.Matrix([(mask>>i)&1 for i in range(3)])
 mu=S.prod(a[i] if x[i] else 1-a[i] for i in range(3));z=x-a
 f=-sum(K[i,j]**2*z[i]*z[j]/(q[i]*q[j]) for i,j in [(0,1),(0,2),(1,2)])+2*K[0,1]*K[1,2]*K[2,0]*S.prod(z[i]/q[i] for i in range(3))
 ok(S.factor(mu*(1+f)-p[mask])==0)
# Full frozen form, with independent formal atom logarithms.
d=S.symbols('d0:3',real=True);u=S.symbols('u0:3',real=True);v=S.symbols('v0:3',real=True)
z=[u[i]+S.I*v[i] for i in range(3)]
A=S.Matrix([[d[0],z[2],S.conjugate(z[1])],[S.conjugate(z[2]),d[1],z[0]],[z[1],S.conjugate(z[0]),d[2]]])
ell=S.symbols('ell0:8',real=True);tau=ell[0]+ell[3]+ell[5]+ell[6]-ell[1]-ell[2]-ell[4]-ell[7]
c=S.Matrix([ell[2]+ell[4]-ell[0]-ell[6],ell[1]+ell[4]-ell[0]-ell[5],ell[1]+ell[2]-ell[0]-ell[3]])
m=c+tau*a;M=S.diag(*c)+tau*K
jet=S.symbols('jet',real=True);pt=atoms(K+jet*A)
p1=[S.expand(t).coeff(jet,1) for t in pt];p2=[2*S.expand(t).coeff(jet,2) for t in pt]
frozen=S.expand(sum(p2[i]*ell[i] for i in range(8)))
ok(S.expand(frozen+2*S.trace(M*A.adjugate()))==0)
J=K-S.diag(*a);Bm=S.diag(*m)-tau*J;Bp=S.diag(*m)+tau*J
L=S.Matrix([[0,m[2],m[1]],[m[2],0,m[0]],[m[1],m[0],0]])
D=S.diag(K[1,2],K[2,0],K[0,1]);dv=S.Matrix(d);uv=S.Matrix(u);vv=S.Matrix(v)
f2=2*(uv.T*Bm*uv)[0]+2*(vv.T*Bp*vv)[0]+4*tau*(dv.T*D*uv)[0]-(dv.T*L*dv)[0]
ok(S.expand(frozen-f2)==0)
Sigma=S.diag(*a)-K.multiply_elementwise(K)
Sigma_atoms=S.zeros(3)
for mask in range(8):
 x=S.Matrix([(mask>>i)&1 for i in range(3)])-a
 Sigma_atoms+=p[mask]*x*x.T
ok(Sigma_atoms==Sigma)
for i in range(3):ok(S.expand(sum(p1[mask]*((mask>>i)&1) for mask in range(8))-d[i])==0)
# Projection identity via its moment identities: normalization, centered score,
# and covariance suffice for the full symbolic Pythagoras identity.
ok(S.expand(sum(p1))==0)
# X033 overlap identity.
x,y,zv=S.symbols('x y z',real=True)
H=S.Matrix([[1,zv,y],[zv,1,x],[y,x,1]]);one=S.ones(3,1)
ok(S.expand((one.T*H.adjugate()*one)[0]-2*H.det()-((1-x-y-zv)**2-4*x*y*zv))==0)
# Non-count-uniform boundary family, with every nonempty limiting atom positive.
e=S.symbols('eps',real=True);w=S.Matrix([R(1,3),R(2,3),R(2,3)])
Ke=S.eye(3)/4+(R(3,4)-e)*w*w.T;pe=atoms(Ke)
for mask in range(8):
 k=mask.bit_count();ws=sum(w[i]**2 for i in range(3) if mask&(1<<i));mu=R(1,4)**k*R(3,4)**(3-k)
 ok(S.factor(pe[mask]-mu*(4*e/3+(4-16*e/3)*ws))==0)
 if mask:ok(pe[mask].subs(e,0)>0)
ok(pe[0]==9*e/16);ok(pe[1]!=pe[2]);ok(S.trace(Ke.subs(e,0))==R(3,2))
a0=S.Matrix([Ke[i,i].subs(e,0) for i in range(3)]);K0=Ke.subs(e,0);Sig0=S.diag(*a0)-K0.multiply_elementwise(K0)
for i in (1,2,3):ok(Sig0[:i,:i].det()>0)
# One exact finite witness: marginal projection plus entire frozen term <0,
# while complete measured curvature is strictly positive.
ef=R(1,10000);Kf=Ke.subs(e,ef);pf=[t.subs(e,ef) for t in pe];af=S.Matrix([Kf[i,i] for i in range(3)]);Sigf=S.diag(*af)-Kf.multiply_elementwise(Kf)
proj=(one.T*Sigf.inv()*one)[0];lc=logs_coeff(S.trace(Kf));flo,fhi=linear_log_bounds(lc,pf)
ok(proj+fhi<-1)
ratiof=S.factor(pf[0]*pf[3]*pf[5]*pf[6]/(pf[1]*pf[2]*pf[4]*pf[7]));ok(ratiof<1)
pft=atoms(Kf+jet*S.eye(3));pft1=[S.expand(t).coeff(jet,1) for t in pft];FI=sum(t*t/p0 for t,p0 in zip(pft1,pf))
ok(FI+flo>5615)
res={'checks':checks,'example_atoms':[str(t) for t in p],'example_exp_tau':str(ratio),'boundary_v':['1/3','2/3','2/3'],'finite_epsilon':str(ef),'marginal_fisher':float(proj),'full_fisher':float(FI),'marginal_plus_frozen_interval':[float(proj+flo),float(proj+fhi)],'full_curvature_interval':[float(FI+flo),float(FI+fhi)],'limiting_marginal_fisher':str((one.T*Sig0.inv()*one)[0])}
Path('computations/X078/verified_output.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
