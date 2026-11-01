from pathlib import Path
import numpy as np,json,time
from scipy.linalg import expm
from scipy.optimize import root
from scipy.special import gammaln
rng=np.random.default_rng(1900192);start=time.time();results={}
cases=[('scalar',np.array([[-1.]]),np.array([1.])),('spiral',np.array([[-1.,-1.],[1.,-1.]]),np.array([1.,0.])),('nonnormal',np.array([[-1.,2.],[0.,-1.]]),np.array([0.,1.])),('diagonal3',np.diag([-3.,-2.,-1.]),np.ones(3))]
jac=[]
def endpoint(A,a,x,s,i,T=1.):
 times=np.r_[0.,s,T];out=expm(A*T)@x
 for k in range(len(times)-1):
  if (i+k)%2:out+=(expm(A*(T-times[k+1]))-expm(A*(T-times[k])))@a
 return out
for name,A,a in cases:
 d=len(a);b=A@a;K=np.column_stack([np.linalg.matrix_power(A,k)@a for k in range(d)])
 maxerror=0.;mindet=np.inf
 for z in range(60):
  n=d+int(rng.integers(0,3));s=np.sort(rng.uniform(.08,.92,n))
  while np.min(np.diff(np.r_[0,s,1]))<.02:s=np.sort(rng.uniform(.08,.92,n))
  x=rng.normal(size=d);i=int(rng.integers(0,2));h=1e-6
  exact=np.column_stack([((1 if (i+j)%2==0 else -1)*expm(A*(1-s[j]))@b) for j in range(d)])
  numeric=[]
  for j in range(d):
   ss=s.copy();ss[j]+=h;tt=s.copy();tt[j]-=h
   numeric.append((endpoint(A,a,x,ss,i)-endpoint(A,a,x,tt,i))/(2*h))
  numeric=np.column_stack(numeric);maxerror=max(maxerror,float(np.max(abs(exact-numeric))));mindet=min(mindet,float(abs(np.linalg.det(exact))))
 assert maxerror<1e-8 and mindet>1e-12
 jac.append({'model':name,'dimension':d,'controllability_determinant':float(np.linalg.det(K)),'D':float(-np.trace(A)),'cases':60,'max_jacobian_error':maxerror,'min_abs_jacobian_determinant':mindet})
results['fixed_time_jacobians']=jac
# Exact killed finite-count CTMC probabilities, not a Monte Carlo approximation.
counts=[]
for name,d,D,p,l0,l1,T in [('spiral_positive',2,2.,1.2,.5,3.,30.),('nonnormal_positive',2,2.,2.,1.3,2.,30.),('diagonal3_positive',3,6.,2.,3.5,4.,45.),('diagonal3_p3',3,6.,3.,4.3,5.1,70.)]:
 beta=D*(1-1/p);m=min(l0,l1);G=np.zeros((2*d,2*d))
 for k in range(d):
  for i,l in enumerate([l0,l1]):
   G[2*k+i,2*k+i]=-l
   if k+1<d:G[2*k+i,2*(k+1)+1-i]=l
 Q=expm(G*T);actual=[float(Q[i].sum()) for i in [0,1]]
 bare=float(np.exp(-m*T)*sum((m*T)**k/np.math.factorial(k) for k in range(d))) if hasattr(np,'math') else None
 import math
 bare=float(np.exp(-m*T)*sum((m*T)**k/math.factorial(k) for k in range(d)))
 weighted=float(np.exp(beta*T)*bare);assert max(actual)<=bare*(1+1e-8);assert weighted<.5
 counts.append({'model':name,'d':d,'p':p,'rates':[l0,l1],'T':T,'beta':beta,'actual_low_count_probabilities':actual,'poisson_upper_bound':bare,'weighted_upper_bound':weighted,'chosen_extra_discard_budget':float(.25*np.exp(-beta*T)),'resulting_remainder_norm_bound':weighted+.25})
results['remainder_checks']=counts
# Three positive pulses whose integral cancels to 0. Proof uses IFT; root is diagnostic only.
A=np.array([[-1.,-1.],[1.,-1.]]);a=np.array([1.,0.]);b=A@a
ts=.2+np.arange(3)*2*np.pi/3;k=np.exp(ts);eps=.0005;h3=eps*k[2]
def F(h):return sum((expm(A*t)-expm(A*(t+hh)))@a for t,hh in zip(ts,h))
r=root(lambda v:F(np.r_[v,h3]),eps*k[:2],tol=1e-11);hs=np.r_[r.x,h3];res=float(np.linalg.norm(F(hs)))
assert res<1e-12 and np.all(hs>0) and np.all(hs<np.pi/3)
W=np.column_stack([-expm(A*(ts[j]+hs[j]))@b for j in range(2)])
relations=sum(k[j]*(-expm(A*ts[j])@b) for j in range(3));assert np.linalg.norm(relations)<1e-11
results['three_pulse_diagnostic']={'starts':ts.tolist(),'lengths':hs.tolist(),'positive':bool(np.all(hs>0)),'residual':res,'first_two_derivative_determinant':float(np.linalg.det(W)),'positive_linear_relation_residual':float(np.linalg.norm(relations)),'solver_success':bool(r.success),'proof_basis':'Implicit-function theorem; numerical root alone is not proof.'}
# Exact 1D boundary case: m=D is bounded, so do not generalize spiral L-infinity iff.
import sympy as sp
x,l0,l1,alpha,p=sp.symbols('x l0 l1 alpha p',positive=True)
rho0=2*(1-x)**2;rho1=2*x*(1-x)
results['scalar_critical_check']={'rho0_mass':str(sp.integrate(rho0,(x,0,1))),'rho1_mass':str(sp.integrate(rho1,(x,0,1))),'total_density':str(sp.expand(rho0+rho1)),'rho0_stationary_flux_residual':str(sp.simplify(sp.diff(x*rho0,x)-rho0+2*rho1)),'finite_p_exponent_identity':str(sp.simplify(p*(l0/alpha-1)+1-(p/alpha)*(l0-alpha*(1-1/p))))}
assert results['scalar_critical_check']['rho0_stationary_flux_residual']=='0'
assert results['scalar_critical_check']['finite_p_exponent_identity']=='0'
results['elapsed_seconds']=time.time()-start
Path('followup_numerics.json').write_text(json.dumps(results,indent=2),encoding='utf8');print(json.dumps(results,indent=2))
