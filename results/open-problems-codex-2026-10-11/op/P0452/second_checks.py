import json,itertools,numpy as np
from pathlib import Path
from scipy.special import gammainc
rng=np.random.default_rng(4522026)
out={}
# Greedy finite partition lemma, all ordered compositions of S<=15.
cases=0
for S in range(1,16):
 for mask in range(1<<max(0,S-1)):
  blocks=[];start=0
  for i in range(1,S):
   if mask>>(i-1)&1:blocks.append(i-start);start=i
  blocks.append(S-start)
  for eta in range(1,S+1):
   if S>=3*eta and max(blocks)<S-eta:
    middle=[w for w in blocks if eta<=w<=S-eta]
    if middle:a=middle[0]
    else:
     a=0
     for w in blocks:
      a+=w
      if a>=eta:break
    assert eta<=a<=S-eta
   cases+=1
out['partition_cases']=cases
# Independent finite-type proxy of the slot reproduction mechanism.
dvals=[1,3,7];probs=[.1,.8,.1]
cuts=np.array([0.,.5,1.,2.,4.,8.,16.,np.inf]);xs0=np.array([.25,.75,1.5,3.,6.,12.,24.])
mu=[];ms=[];xs=[];ds=[]
for d,p in zip(dvals,probs):
 cdf=np.r_[gammainc(d,cuts[:-1]),1.]
 for x,q in zip(xs0,np.diff(cdf)*p):mu.append(q);ms.append(d-1);xs.append(x);ds.append(d)
mu=np.array(mu);ms=np.array(ms);xs=np.array(xs);ds=np.array(ds)
M=ms[:,None]*np.minimum(xs[:,None],xs[None,:])/xs[:,None]*mu[None,:]
K=np.where((ds==3)&(xs>=.75)&(xs<=12))[0];O=np.array([i for i in range(len(xs)) if i not in K])
eps=float(np.dot(mu[O],ms[O]));assert eps<1
A=M[np.ix_(K,K)];U=M[np.ix_(K,O)];V=M[np.ix_(O,K)];Q=M[np.ix_(O,O)]
R=A+U@np.linalg.solve(np.eye(len(O))-Q,V)
rad=lambda X:float(max(np.abs(np.linalg.eigvals(X))))
assert rad(M)>1 and rad(R)>1
pi=mu[K]*xs[K]/ms[K]
symmetry_error=float(np.max(np.abs(pi[:,None]*R-(pi[:,None]*R).T)))
assert symmetry_error<1e-12
assert np.all(Q@ms[O]<=eps*ms[O]+1e-12)
trunc=[]
for N in [0,1,2,4,8,16]:
 T=A.copy();power=np.eye(len(O))
 for j in range(N):T+=U@power@V;power=power@Q
 loss=float(max(np.sum(R-T,axis=1)))
 bound=2*eps**(N+1)/(1-eps)
 assert loss<=bound+1e-10
 trunc.append({'max_outside_vertices':N,'spectral_radius':rad(T),'norm_error':loss,'bound':bound})
rootmu=[];rootds=[];rootxs=[]
for d,p in zip(dvals,probs):
 cdf=np.r_[gammainc(d+1,cuts[:-1]),1.]
 for x,q in zip(xs0,np.diff(cdf)*p):rootmu.append(q);rootds.append(d);rootxs.append(x)
rootmu=np.array(rootmu);rootds=np.array(rootds);rootxs=np.array(rootxs)
continuity=[]
for t in [.5,1.,2.,4.,8.,16.,32.]:
 H=np.minimum(np.minimum(xs[:,None],xs[None,:]),t)/xs[:,None]*mu[None,:]
 e=np.zeros(len(xs))
 for j in range(20000):
  enew=(1-H@(1-e))**ms
  if max(abs(enew-e))<1e-13: e=enew;break
  e=enew
 hr=np.minimum(np.minimum(rootxs[:,None],xs[None,:]),t)/rootxs[:,None]*mu[None,:]
 rho=float(1-np.dot(rootmu,(1-hr@(1-e))**rootds))
 continuity.append({'cutoff':t,'survival':rho,'iterations':j+1})
out['finite_type_proxy']={'epsilon':eps,'full_radius':rad(M),'return_radius':rad(R),'weighted_symmetry_error':symmetry_error,'return_truncations':trunc,'survival_by_cutoff':continuity}
# Active-leaf identity in fresh backbone variables, not independent vertex rankings.
motif=[]
for d in [2,3,7]:
 for t in [1.,3.,6.]:
  reps=100000;z=rng.gamma(d,size=reps);costs=rng.random((reps,d-1))*z[:,None]
  success=np.min(costs,axis=1)>t
  est=float(np.mean(success));theory=float(np.exp(-t));se=(theory*(1-theory)/reps)**.5
  assert abs(est-theory)<6*se
  motif.append({'budget':d,'time':t,'reps':reps,'estimate':est,'theory':theory,'standard_error':se})
out['active_leaf']=motif
Path('second_checks.json').write_text(json.dumps(out,indent=2))
print('partition cases',cases,flush=True)
print('finite-type radii',rad(M),rad(R),'epsilon',eps,flush=True)
print('all motif estimates within 6 standard errors',flush=True)
