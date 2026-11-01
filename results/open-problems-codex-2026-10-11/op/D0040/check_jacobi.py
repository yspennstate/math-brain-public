import json, math, pathlib
import numpy as np
from scipy.linalg import eigh
from scipy.stats import ks_2samp
from scipy.special import gammaln
P=pathlib.Path(__file__).resolve().parent
rng=np.random.default_rng(240040)

def factors(beta,r,s,n,N):
 i=np.arange(1,n+1); g=beta/2
 p=rng.beta(g*(r+i),g*(s+i),size=(N,n))
 q=np.zeros((N,n)); q[:,1:]=rng.beta(g*i[:-1],g*(r+s+1+i[:-1]),size=(N,n-1))
 d=np.sqrt(p*(1-q)); e=np.sqrt((1-p[:,:-1])*q[:,1:])
 f=np.sqrt((1-p)*(1-q)); h=np.sqrt(p[:,:-1]*q[:,1:])
 B=np.zeros((N,n,n)); C=B.copy()
 j=np.arange(n); B[:,j,j]=d; C[:,j,j]=f
 j=np.arange(n-1); B[:,j+1,j]=e; C[:,j+1,j]=-h
 return B,C,p,q

def mixed_moment(beta,r,s,n,k,l):
 g=beta/2
 def poch(z,k): return gammaln(z+k)-gammaln(z)
 return math.exp(sum(poch(g*(r+i),k)+poch(g*(s+i),l)-poch(g*(r+s+n+i),k+l) for i in range(1,n+1)))

out={'seed':240040,'moment_checks':[],'wishart_comparisons':[]}
for beta,r,s,n in [(0.8,-0.4,-0.3,4),(1,2,3,4),(2,1,0,4),(4,0,0.5,8),(2,-0.8,0.2,5)]:
 N=12000; B,C,p,q=factors(beta,r,s,n,N)
 J=B@B.transpose(0,2,1); complement=C@C.transpose(0,2,1)
 ev=np.linalg.eigvalsh(J); prev=np.linalg.eigvalsh(J[:,:-1,:-1])
 assert np.allclose(J[:,:-1,:-1],B[:,:-1,:-1]@B[:,:-1,:-1].transpose(0,2,1))
 err=float(np.max(np.abs(J+complement-np.eye(n))))
 assert err<2e-14
 D=np.prod(p,axis=1)*np.prod(1-q,axis=1)
 E=np.prod(1-p,axis=1)*np.prod(1-q,axis=1)
 R=np.eye(n)[::-1]; L=R@B.transpose(0,2,1)@R
 specerr=float(np.max(np.abs(ev-np.linalg.eigvalsh(L@L.transpose(0,2,1)))))
 row=dict(beta=beta,r=r,s=s,n=n,samples=N,complement_error=err,reversal_spectral_error=specerr,min_eigenvalue=float(ev.min()),max_eigenvalue=float(ev.max()),min_interlacing_gap=float(min(np.min(prev-ev[:,:-1]),np.min(ev[:,1:]-prev))),trace_mean=float(ev.sum(axis=1).mean()),trace_target=n*(n+r)/(2*n+r+s),moments=[])
 for k,l in [(1,0),(0,1),(1,1),(2,1),(0,2)]:
  X=D**k*E**l; target=mixed_moment(beta,r,s,n,k,l)
  variance=max(0.,mixed_moment(beta,r,s,n,2*k,2*l)-target**2)
  se=math.sqrt(variance/N)
  row['moments'].append(dict(k=k,l=l,mean=float(X.mean()),target=target,standard_error=se,z=float((X.mean()-target)/se)))
 out['moment_checks'].append(row)
 (P/'jacobi_numerical_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')

for beta in [1,2]:
 n=4; r=2; s=3; N=5000
 B,_,_,_=factors(beta,r,s,n,N)
 model=np.linalg.eigvalsh(B@B.transpose(0,2,1))
 target=np.zeros((N,n))
 for j in range(N):
  X=rng.normal(size=(n,n+r)); Y=rng.normal(size=(n,n+s))
  if beta==2:
   X=X+1j*rng.normal(size=X.shape); Y=Y+1j*rng.normal(size=Y.shape)
  A=X@X.conj().T; W=Y@Y.conj().T
  target[j]=eigh(A,A+W,eigvals_only=True)
 comparisons=[]
 projections=[(f'ordered eigenvalue {i+1}',model[:,i],target[:,i]) for i in range(n)]
 projections.extend([('trace',model.sum(axis=1),target.sum(axis=1)),('sum squares',(model**2).sum(axis=1),(target**2).sum(axis=1)),('determinant',model.prod(axis=1),target.prod(axis=1))])
 for name,x,y in projections:
  res=ks_2samp(x,y)
  comparisons.append(dict(statistic=name,KS=float(res.statistic),p_value=float(res.pvalue)))
 out['wishart_comparisons'].append(dict(beta=beta,r=r,s=s,n=n,samples_per_law=N,comparisons=comparisons))
 (P/'jacobi_numerical_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
