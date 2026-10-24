import json,numpy as np
from scipy.special import gammainc
from pathlib import Path
xs0=np.array([.25,.75,1.5,3.,6.,12.,24.]);cuts=np.array([0,.5,1,2,4,8,16,np.inf]);mu=[];ms=[];xs=[];ds=[]
for d,p in [(1,.1),(3,.8),(7,.1)]:
 cdf=np.r_[gammainc(d,cuts[:-1]),1.]
 for x,q in zip(xs0,np.diff(cdf)*p):mu.append(q);ms.append(d-1);xs.append(x);ds.append(d)
mu=np.array(mu);ms=np.array(ms);xs=np.array(xs);ds=np.array(ds)
M=ms[:,None]*np.minimum(xs[:,None],xs[None,:])/xs[:,None]*mu[None,:]
K=np.where((ds==3)&(xs<=3))[0];O=np.array([i for i in range(len(xs)) if i not in K]);A=M[np.ix_(K,K)];U=M[np.ix_(K,O)];V=M[np.ix_(O,K)];Q=M[np.ix_(O,O)];R=A+U@np.linalg.solve(np.eye(len(O))-Q,V)
rad=lambda X:float(max(np.abs(np.linalg.eigvals(X))))
eps=float(np.dot(mu[O],ms[O]));assert eps<1 and rad(A)<1 and rad(R)>1
pi=mu[K]*xs[K]/ms[K];sym=float(np.max(abs(pi[:,None]*R-(pi[:,None]*R).T)));assert sym<1e-12
rows=[]
for N in [0,1,2,4,8,16]:
 T=A.copy();power=np.eye(len(O))
 for j in range(N):T+=U@power@V;power=power@Q
 bound=2*eps**(N+1)/(1-eps);loss=float(max(np.sum(R-T,axis=1)))
 assert loss<=bound+1e-10
 assert np.max(abs(pi[:,None]*T-(pi[:,None]*T).T))<1e-12
 rows.append({'N':N,'radius':rad(T),'norm_loss':loss,'bound':bound})
r={'epsilon':eps,'direct_radius':rad(A),'return_radius':rad(R),'weighted_symmetry_error':sym,'truncations':rows}
Path('return_stress.json').write_text(json.dumps(r,indent=2));print(r)
