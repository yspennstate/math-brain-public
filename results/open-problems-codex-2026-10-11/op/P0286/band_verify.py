import numpy as np,math,json
from pathlib import Path
from scipy.integrate import quad
from scipy.linalg import eigh_tridiagonal

def parameters(a,b,theta):
 p=a*(1-b);q=(1-a)*b;r=p/q;t=math.sqrt(p*q);h=1-p-q;A=1/math.sqrt(r)
 length=max(50,math.ceil(math.log(1e-16)/math.log(theta)))
 powers=theta**np.arange(length)
 poch=lambda z:np.prod(1-z*powers)
 L=float(poch(theta));pi0=float(poch(r));z=theta/A
 def density(phi):
  if phi==0:
   if abs(A*theta-1)<1e-12:return 2*p*q*(1-theta)/math.pi
   return 0.
  unit=np.exp(1j*phi)
  return float(q*q*pi0*L**3/(2*math.pi)*abs(poch(unit*unit))**2/(abs(poch(A*unit))**2*abs(poch(z*unit))**4))
 return p,q,r,t,h,A,L,pi0,z,poch,density

out={'band_checks':[],'closing_gap':[]}
for theta in [.2,.5,math.sqrt(2/7)]:
 a=.3;b=.6;p,q,r,t,h,A,L,pi0,z,poch,w=parameters(a,b,theta);lam=h+2*t
 base=lambda phi:float(L/(2*math.pi)*abs(poch(np.exp(2j*phi)))**2/abs(poch(A*np.exp(1j*phi)))**2)
 normalized=pi0+quad(base,0,math.pi,epsabs=1e-11)[0]
 assert abs(normalized-1)<1e-10
 K=600;ks=np.arange(K);logd=np.zeros(K);logd[1:]=np.cumsum(np.log1p(-theta**np.arange(1,K)))
 logpi=ks*math.log(r)-logd;logpi-=max(logpi);pi=np.exp(logpi);pi/=sum(pi)
 vals,vecs=eigh_tridiagonal(h+q*theta**ks,t*np.sqrt(1-theta**np.arange(1,K)))
 v=np.sqrt(pi)*(theta**ks-pi@(theta**ks));weights=q*q*(vecs.T@v)**2;weights[vals>1-1e-10]=0
 errors=[]
 for n in [1,2,5,20]:
  integ=quad(lambda phi:(h+2*t*math.cos(phi))**(n-1)*w(phi),0,math.pi,epsabs=1e-12)[0]
  direct=float(weights@(vals**(n-1)));errors.append(abs(integ-direct));assert errors[-1]<1e-10
 critical=abs(theta-math.sqrt(r))<1e-12
 if critical:pref=t**1.5*(1-theta)/math.sqrt(math.pi)
 else:pref=q*q*pi0*L**5/(2*math.sqrt(math.pi)*t**1.5*float(poch(A))**2*float(poch(z))**4)
 ratios=[]
 for n in [1000,10000,1000000]:
  upper=min(math.pi*math.sqrt(n),12*math.sqrt(lam/t))
  f=lambda u:w(u/math.sqrt(n))*max(0,(h+2*t*math.cos(u/math.sqrt(n)))/lam)**(n-1)
  val=quad(f,0,upper,epsabs=1e-13)[0]
  ratio=val/(pref*math.sqrt(lam)) if critical else n*val/(pref*lam**1.5)
  ratios.append(dict(n=n,ratio=ratio))
 assert abs(ratios[-1]['ratio']-1)<.005
 out['band_checks'].append(dict(theta=theta,critical=critical,normalization=normalized,max_covariance_integral_error=max(errors),prefactor=pref,asymptotic_ratios=ratios))

limit=quad(lambda z:math.sqrt(z)/(1+z)*math.exp(-1-z),0,np.inf)[0]/(2*math.pi)
for theta in [.2,.6,.9]:
 for delta in [.02,.01,.005]:
  a=.5;b=a+delta;p,q,r,t,h,A,L,pi0,z,poch,w=parameters(a,b,theta);assert theta<math.sqrt(r)
  n=round(delta**-2)
  val=quad(lambda y:w(delta*y)/delta*max(0,h+2*t*math.cos(delta*y))**(n-1),0,min(math.pi/delta,20),epsabs=1e-10)[0]
  out['closing_gap'].append(dict(theta=theta,delta=delta,n=n,rescaled_covariance=val,limit=limit))
Path('band_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
