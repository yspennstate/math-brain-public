import json, math, pathlib
import numpy as np
from scipy.integrate import quad

rng=np.random.default_rng(840409)
out={}
def sphere(n,d):
 a=rng.normal(size=(n,d)); return a/np.linalg.norm(a,axis=1)[:,None]
def geometry(theta):
 d=theta.shape[1]; us=[]; aa=[]
 for i in range(d+1):
  retained=np.delete(theta,i,axis=0)
  _,_,vh=np.linalg.svd(retained[1:]-retained[0])
  u=vh[-1]; a=retained[0]@u
  if a<theta[i]@u: u=-u; a=-a
  us.append(u); aa.append(a)
 return np.array(us),np.array(aa)
for d in [2,3,4,5]:
 p=d-1
 theta=sphere(d+1,d)
 if d==2:
  # All three points in one open semicircle: tests the missing-hull-indicator issue.
  angles=np.array([-.65,.1,.8]); theta=np.column_stack((np.cos(angles),np.sin(angles)))
 u,a=geometry(theta); times=np.linspace(.07,.42,d+1); q=np.tanh(times)
 phi=sphere(180000,d)
 h=((1-a*q)/(1-(phi@u.T)*q))**p
 vals=np.maximum(0,np.max(h-1,axis=1))
 A=float(vals.mean()); Ase=float(vals.std()/np.sqrt(len(vals)))
 if d==2:
  def integrand(x):
   b=u@np.array([math.cos(x),math.sin(x)])
   return max(0,float(np.max((1-a*q)/(1-b*q)-1)))/(2*math.pi)
  A,err=quad(integrand,0,2*math.pi,epsabs=1e-10,limit=500)
  Ase=err
 predicted=(1+A)**(-(d+1))
 n=6500; wins=0; mismatch=0
 for _ in range(n):
  s=rng.gamma(d+1)
  bound=s*math.exp(2*p*float(max(times)))
  N=rng.poisson(bound-s)
  angles=sphere(N,d); R=rng.uniform(s,bound,N)
  # Evaluate the original hyperboloid scores, with no H/void formula.
  X0=np.cosh(times); Xv=np.sinh(times)[:,None]*u
  retained=s*(X0-a*np.sinh(times))**p
  competitor=R[:,None]*(X0[None,:]-angles@Xv.T)**p
  direct=bool(np.all(competitor>=retained[None,:]))
  wins+=direct
  # Solve equalities algebraically and compare first crossings to direct tests.
  k=(R/s)**(1/p); b=angles@u.T
  den=k[:,None]*b-a
  with np.errstate(divide='ignore',invalid='ignore'):
   roots=(k[:,None]-1)/den
  valid=(b>a)&(roots>0)&(roots<1)
  roots=np.where(valid,roots,np.inf)
  via_crossing=bool(np.all(roots>q))
  mismatch+=direct!=via_crossing
 s=1.73; eps=1e-6
 def radii(v): return s*(np.sqrt(1+v@v)-theta@v)**(-p)
 J=np.column_stack([np.ones(d+1)]+[(radii(eps*np.eye(d)[j])-radii(-eps*np.eye(d)[j]))/(2*eps) for j in range(d)])
 actual=abs(np.linalg.det(J)); target=(p*s)**d*abs(np.linalg.det(np.column_stack((np.ones(d+1),theta))))
 out[str(d)]={'A':A,'A_error_estimate':Ase,'prediction':predicted,'direct_score_simulation':wins/n,'binomial_se':math.sqrt(predicted*(1-predicted)/n),'trials':n,'crossing_disagreements':mismatch,'jacobian_relative_error':abs(actual-target)/target,'theta':theta.tolist()}
# Independent planar determinant normalization.
theta=sphere(450000,2).reshape(150000,3,2)
D=np.abs(np.linalg.det(np.concatenate((np.ones((150000,3,1)),theta),axis=2)))
out['planar_normalization']={'estimate':float(D.mean()),'se':float(D.std()/math.sqrt(len(D))),'exact':3/math.pi}
gint=quad(lambda g:math.sin(g)*(1-g/(2*math.pi))/math.pi,0,2*math.pi)[0]
out['exact_gap_integral_numeric']={'value':gint,'expected':1/math.pi}
pathlib.Path(__file__).with_name('independent_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
