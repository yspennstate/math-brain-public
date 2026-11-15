"""Small reproducible MRA experiments. Numerical optimizers are not certified MLEs."""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:
 os.environ[key]='1'
import resource
try:
 resource.setrlimit(resource.RLIMIT_AS,(3*1024**3,resource.getrlimit(resource.RLIMIT_AS)[1]))
except (ValueError, OSError):
 pass  # Darwin/sandbox may reject RLIMIT_AS; bounded array sizes and measured RSS remain in force.
import csv,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from scipy.special import logsumexp
ROOT=Path(__file__).resolve().parents[1]

def shifts(x): return np.array([np.roll(x,s) for s in range(len(x))])
def err(x,u): return float(np.min(np.sum((shifts(x)-u)**2,axis=1))/np.dot(u,u))
def spectrum(Y,sigma):
 F=np.fft.fft(Y,axis=1,norm='ortho')
 power=np.maximum(np.mean(abs(F)**2,axis=0)-sigma**2,0)
 mean0=np.mean(F[:,0].real)
 return np.sqrt(power),mean0

def project(x,amp,dc):
 F=np.fft.fft(x,norm='ortho'); phase=F/np.maximum(abs(F),1e-100)
 F=amp*phase; F[0]=dc
 return np.fft.ifft(F,norm='ortho').real

def objective(Y,x,sigma):
 C=np.einsum('ij,kj->ik',Y,shifts(x),optimize=False)
 return float(np.dot(x,x)/(2*sigma**2)-np.mean(logsumexp(C/sigma**2,axis=1))+np.log(len(x)))

def marginal(Y,x,sigma,maxiter=100,polish=50,amp=None,dc=None):
 L=len(x); old=objective(Y,x,sigma)
 for i in range(maxiter):
  S=shifts(x); C=np.einsum('ij,kj->ik',Y,S,optimize=False)/sigma**2; W=np.exp(C-logsumexp(C,axis=1,keepdims=True))
  A=np.einsum('ik,ij->kj',W,Y,optimize=False)/len(Y)
  z=sum(np.roll(A[s],-s) for s in range(L))
  if amp is not None: z=project(z,amp,dc)
  val=objective(Y,z,sigma)
  if val>old+1e-9: raise RuntimeError('EM monotonicity failed')
  step=np.linalg.norm(z-x); x=z; old=val
  if step<1e-7: break
 if polish and amp is None:
  def fg(x):
   C=np.einsum('ij,kj->ik',Y,shifts(x),optimize=False)/sigma**2; W=np.exp(C-logsumexp(C,axis=1,keepdims=True))
   A=np.einsum('ik,ij->kj',W,Y,optimize=False)/len(Y)
   grad=(x-sum(np.roll(A[s],-s) for s in range(L)))/sigma**2
   return objective(Y,x,sigma),grad
  result=minimize(fg,x,jac=True,method='L-BFGS-B',options={'maxiter':polish,'gtol':1e-9,'ftol':1e-12})
  x=result.x
 return x,i+1

def hard(Y,x,maxiter=100,amp=None,dc=None):
 L=len(x)
 for i in range(maxiter):
  labels=np.argmax(np.einsum('ij,kj->ik',Y,shifts(x),optimize=False),axis=1)
  z=np.zeros(L)
  for s in range(L):
   if np.any(labels==s): z+=np.roll(np.sum(Y[labels==s],axis=0),-s)/len(Y)
  if amp is not None: z=project(z,amp,dc)
  step=np.linalg.norm(x-z); x=z
  if step<1e-7: break
 return x,i+1

def hardloss(Y,x): return float(np.dot(x,x)-2*np.mean(np.max(np.einsum('ij,kj->ik',Y,shifts(x),optimize=False),axis=1)))

def signal(L,rng):
 # A bounded-away-from-zero Fourier spectrum, norm one, with a nonzero DC coefficient.
 F=np.ones(L,dtype=complex)/np.sqrt(L)
 for k in range(1,(L+1)//2):
  F[k]*=np.exp(1j*rng.uniform(-np.pi,np.pi)); F[-k]=F[k].conjugate()
 return np.fft.ifft(F,norm='ortho').real

def recovery():
 rng=np.random.default_rng(57001)
 U={L:signal(L,rng) for L in range(5,16)}
 (ROOT/'data'/'signals.json').write_text(json.dumps({L:u.tolist() for L,u in U.items()},indent=2))
 cases=[]
 for L in range(5,16):
  for sigma in [.5,1.5,3.]:
   for n in [200,2000]:
    for rep in range(2): cases.append(('length_sweep',L,sigma,n,rep))
 for L in [5,9,15]:
  for sigma in [.5,1.5]:
   for n in [20000]:
    for rep in range(3): cases.append(('large_n',L,sigma,n,rep))
 for sigma in [1.,1.5,2.]:
  for ratio in [100,1000]:
   for rep in range(3): cases.append(('scaling',5,sigma,int(round(ratio*sigma**6)),rep))
 fields=['suite','L','sigma','n','rep','seed','method','relative_squared_error','objective','iterations']
 start=time.time()
 with (ROOT/'data'/'recovery.csv').open('w') as file:
  out=csv.DictWriter(file,fieldnames=fields);out.writeheader()
  for j,(suite,L,sigma,n,rep) in enumerate(cases):
   seed=5700000+j; rg=np.random.default_rng(seed); u=U[L]
   labels=rg.integers(L,size=n); Y=shifts(u)[labels]+sigma*rg.normal(size=(n,L))
   amp,dc=spectrum(Y,sigma)
   initial=[project(rg.normal(size=L),np.abs(np.fft.fft(u,norm='ortho')),np.fft.fft(u,norm='ortho')[0].real) for _ in range(2)]
   candidates={k:[] for k in ['marginal','quasi_raw','quasi_post_power','quasi_constrained']}
   for init in initial:
    x,it=marginal(Y,init,sigma)
    candidates['marginal'].append((objective(Y,x,sigma),x,it))
    x,it=hard(Y,init)
    candidates['quasi_raw'].append((hardloss(Y,x),x,it))
    z=project(x,amp,dc)
    # Keep the shift solution selected by the original quasi objective before power correction.
    candidates['quasi_post_power'].append((hardloss(Y,x),z,it))
    x,it=hard(Y,project(init,amp,dc),amp=amp,dc=dc)
    candidates['quasi_constrained'].append((hardloss(Y,x),x,it))
   for method,vals in candidates.items():
    val,x,it=min(vals,key=lambda t:t[0])
    out.writerow(dict(suite=suite,L=L,sigma=sigma,n=n,rep=rep,seed=seed,method=method,relative_squared_error=err(x,u),objective=val,iterations=it))
   file.flush()
   assert np.all(np.isfinite(Y))
   assert all(np.isfinite(v[0]) and np.all(np.isfinite(v[1])) for vals in candidates.values() for v in vals)
   assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<4*1024**3
   if j%10==0: print('recovery',j+1,'/',len(cases),'elapsed',round(time.time()-start,1),flush=True)
 print('recovery complete',round(time.time()-start,1),flush=True)

def moment_scaling():
 # k=1,2 are independent circular complex Gaussian coordinates for L=5.
 rg=np.random.default_rng(57002); L=5;u=signal(L,rg); F=np.fft.fft(u,norm='ortho')
 a,b=abs(F[1])**2,abs(F[2])**2; target=F[1]**2*F[2].conjugate()
 with (ROOT/'data'/'moment_scaling.csv').open('w') as file:
  out=csv.writer(file);out.writerow(['sigma','n','rep','squared_error','exact_variance_over_n'])
  for sigma in [1.,1.5,2.,3.,4.,6.]:
   n=20000; exact=((a*a+4*a*b)*sigma**2+(4*a+2*b)*sigma**4+2*sigma**6)/n
   for rep in range(100):
    # Generating these two Fourier coefficients is exactly distributionally equivalent to full MRA:
    # their cubic product is invariant to shifts.
    f1=F[1]+sigma/np.sqrt(2)*(rg.normal(size=n)+1j*rg.normal(size=n))
    f2=F[2]+sigma/np.sqrt(2)*(rg.normal(size=n)+1j*rg.normal(size=n))
    B=np.mean(f1**2*f2.conjugate())
    out.writerow([sigma,n,rep,abs(B-target)**2,exact])
 print('moment scaling complete',flush=True)

def audit():
 rg=np.random.default_rng(57003);L=7;u=signal(L,rg);Y=rg.normal(size=(31,L));x=rg.normal(size=L);sigma=1.3
 C=np.einsum('ij,kj->ik',Y,shifts(x),optimize=False)
 direct=np.array([[Y[i]@np.roll(x,s) for s in range(L)] for i in range(len(Y))])
 assert np.allclose(C,direct)
 shifted=np.array([np.roll(y,int(s)) for y,s in zip(Y,rg.integers(L,size=len(Y)))])
 assert abs(objective(Y,x,sigma)-objective(shifted,x,sigma))<1e-10
 assert abs(hardloss(Y,x)-hardloss(shifted,x))<1e-10
 amp=abs(np.fft.fft(u,norm='ortho')); dc=np.fft.fft(u,norm='ortho')[0].real
 assert np.max(abs(abs(np.fft.fft(project(x,amp,dc),norm='ortho'))-amp))<1e-12
 labels=np.argmax(C,axis=1);aligned=np.array([np.roll(y,-int(s)) for y,s in zip(Y,labels)])
 z=aligned.mean(axis=0)
 pairwise=sum(np.linalg.norm(v-w)**2 for v in aligned for w in aligned)
 assert abs(pairwise-2*len(Y)*np.sum((aligned-z)**2))<1e-7
 x,it=marginal(Y,x,sigma,maxiter=5,polish=0)
 assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<4*1024**3
 try:
  from threadpoolctl import threadpool_info
  pools=threadpool_info(); assert all(p['num_threads']<=1 for p in pools)
 except ImportError: pools='threadpoolctl unavailable'
 metadata={'seed_base':57001,'nice':os.getpriority(os.PRIO_PROCESS,0),'address_space_limit_bytes':resource.getrlimit(resource.RLIMIT_AS)[0],'threadpools':pools,'numpy':np.__version__,'checks':'correlation indexing, likelihood/hard-loss shift invariance, Fourier projection, pairwise/profile identity, EM monotonicity'}
 assert metadata['nice']>=10
 (ROOT/'data'/'audit.json').write_text(json.dumps(metadata,indent=2)+'\n')
 print('audit passed, nice',metadata['nice'],flush=True)
if __name__=='__main__':
 audit(); recovery(); moment_scaling()
 (ROOT/'data'/'resource_usage.json').write_text(json.dumps({'maxrss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'user_cpu_seconds':resource.getrusage(resource.RUSAGE_SELF).ru_utime},indent=2))
