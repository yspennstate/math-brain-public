import itertools,json,numpy as np
from pathlib import Path
# Import runs the full analytic-identity check and preserves its results.
from verify import frame,data,adj
V=frame(1.)
U,t,Ps,pairs,W,tau,G,be,trips=data(V)
support=[()]
for k in [1,2,3]:
 for S in itertools.combinations(range(len(V)),k):
  if np.linalg.svd(V[list(S)],compute_uv=False).min()>1e-10:support.append(S)
def atoms(M):
 D=np.eye(3)-M;detD=np.linalg.det(D).real;L=np.linalg.solve(D,M);Q=V@L@V.conj().T
 return np.array([detD if not S else detD*np.linalg.det(Q[np.ix_(S,S)]).real for S in support])
As=[np.array([[1,.2+.3j,-.1j],[.2-.3j,-.6,.1],[.1j,.1,.3]]),np.diag([1.,-1.,-.4])]
records=[]
for s in [.23,.61]:
 for A in As:
  delta=.005;probs=[atoms(s*np.eye(3)+k*delta*A) for k in [-2,-1,0,1,2]]
  p=probs[2];dp=(probs[0]-8*probs[1]+8*probs[3]-probs[4])/(12*delta)
  ddp=(-probs[0]+16*probs[1]-30*p+16*probs[3]-probs[4])/(12*delta**2)
  hminus=np.sum(dp*dp/p+ddp*np.log(p))
  fv=sum(np.trace(B@A).real**2/ti for B,ti in zip(U,t));fw=sum(b*np.trace(P@A).real**2 for i,j,b,P,c in pairs)
  expected=fv/s+fw/(1-s)-2*np.trace((W+s*tau*np.eye(3))@adj(A)).real
  err=abs(hminus-expected)
  assert err<1e-7
  records.append({'s':s,'atom_count':len(p),'normalization_error':abs(p.sum()-1),'negative_hessian':hminus,'two_frame_value':expected,'error':err})
Path(__file__).with_name('atom_results.json').write_text(json.dumps(records,indent=2))
print(json.dumps(records,indent=2))
