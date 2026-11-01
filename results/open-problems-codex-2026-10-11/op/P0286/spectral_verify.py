import numpy as np, math, json
from scipy.linalg import eigh_tridiagonal
from pathlib import Path

def case(a,b,theta,K=600):
 p=a*(1-b);q=(1-a)*b;r=p/q;h=1-p-q;t=math.sqrt(p*q);A=1/math.sqrt(r)
 ks=np.arange(K); powers=theta**ks
 logdk=np.zeros(K);logdk[1:]=np.cumsum(np.log1p(-theta**np.arange(1,K)))
 logpi=ks*math.log(r)-logdk;logpi-=max(logpi);pi=np.exp(logpi);pi/=sum(pi)
 d=h+q*powers;e=t*np.sqrt(1-theta**np.arange(1,K))
 vals,vecs=eigh_tridiagonal(d,e)
 lp=h+2*t
 expected=[];j=0
 while A*theta**j>1+1e-12:
  expected.append(h+q*theta**j+p*theta**(-j));j+=1
 observed=[float(v) for v in vals if v>lp+1e-8]
 assert len(observed)==len(expected),(theta,observed,expected)
 assert max(abs(x-y) for x,y in zip(observed,sorted(expected)))<1e-11
 # Check both infinite-factorization identities in an interior finite block.
 L=50;B=np.diag(np.full(L+1,A**(-.5)))
 B+=np.diag(-math.sqrt(A)*np.sqrt(1-theta**np.arange(1,L+1)),1)
 Kmat=np.diag(A*theta**np.arange(L+1))+np.diag(np.sqrt(1-theta**np.arange(1,L+1)),1)+np.diag(np.sqrt(1-theta**np.arange(1,L+1)),-1)
 H=(A+1/A)*np.eye(L+1)-Kmat
 facerr=np.max(abs(B.T@B-H))
 partner=Kmat.copy();partner[np.diag_indices(L+1)]=A*theta**(np.arange(L+1)+1)
 swaperr=np.max(abs((B@B.T-((A+1/A)*np.eye(L+1)-partner))[:-1,:-1]))
 assert facerr<1e-12 and swaperr<1e-12
 out=dict(a=a,b=b,theta=theta,r=r,threshold=math.sqrt(r),continuous_upper=lp,discrete_eigenvalues=sorted(expected,reverse=True),observed_discrete=observed,factor_error=facerr,swap_interior_error=swaperr)
 if theta>math.sqrt(r):
  lam=h+q*theta+p/theta
  amp=p*q*(1-theta)*(1-r/theta**2)
  g=theta**(-ks[:150])-1/(1-r/theta)
  # Direct Markov eigenfunction identity away from the artificial upper boundary.
  err=[]
  for k in range(1,120):
   pg=p*g[k+1]+q*(1-theta**k)*g[k-1]+(h+q*theta**k)*g[k]
   err.append(abs(pg-lam*g[k])/max(1,abs(g[k])))
  pg0=p*g[1]+(h+q)*g[0];err.append(abs(pg0-lam*g[0]))
  assert max(err)<1e-12
  v=np.sqrt(pi)*(powers-pi@powers)
  weights=q*q*(vecs.T@v)**2
  idx=np.argmin(abs(vals-lam));w=float(weights[idx]);assert abs(w-amp)<1e-11
  rest=h+q*theta**2+p/theta**2 if theta**2>math.sqrt(r) else lp
  # Remove only the stationary eigenvector's numerical roundoff weight.
  weights[vals>1-1e-10]=0
  ratios=[]
  for n in [10,100,1000]:
   ratio=float(np.sum(weights*(vals/lam)**(n-1))/amp)
   rem=float(np.sum(weights*np.maximum(vals,0)**(n-1))-amp*lam**(n-1))
   bound=q*q*(pi@((powers-pi@powers)**2))*rest**(n-1)
   assert -1e-12<=rem<=bound+1e-12
   ratios.append(dict(n=n,covariance_over_leading_term=ratio))
  out.update(leading_eigenvalue=lam,leading_amplitude=amp,observed_amplitude=w,eigenfunction_relative_residual=max(err),remainder_rate=rest,ratios=ratios)
 return out

out=[case(.3,.6,theta) for theta in [.2,.5,math.sqrt(2/7),.7,.9]]
Path('spectral_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
