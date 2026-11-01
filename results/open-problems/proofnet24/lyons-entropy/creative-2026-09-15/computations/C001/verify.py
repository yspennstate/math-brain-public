"""Arithmetic supplements and finite diagnostics for C001.
The theorem is proved analytically in agents/C001.md; numerical output is not a proof.
Run with the workspace Python (requires numpy).
"""
from fractions import Fraction as F
import json, math, pathlib
import numpy as np

checks = {
  'log_lower':F(56,81)-F(1,150)>F(2,3),
  'log_upper':F(25,36)<F(7,10),
  'b1_upper':F(1,300)+F(7,10)*F(3,8)<F(1,3),
  'b2_lower':F(1,4)+F(4,9)>F(2,3),
  'b2_upper':F(2,3)+F(21,40)<F(6,5),
  'b3_remainder':F(1,12)+F(7,20)+F(7,60)<1,
  'h23_bound':F(1,300)+F(7,20)<F(3,8),
  'R_lower':1-F(3,400)-F(27,512)>F(9,10),
  'E_upper':F(27,16)+F(1,40)+F(1,192)<F(7,4),
  'margin':F(81,100)-F(371,512)==F(1093,12800),
  'final_margin':F(1093,21200)>F(1,20),
  'e5_lower':sum(F(5**k,math.factorial(k)) for k in range(7))>100,
}
assert all(checks.values()), checks

def point(t):
  a=math.sqrt(1-t); s=math.sqrt(t); Z=6+t
  L=np.array([[1,a,-.5j*s],[a,1,.5*s],[.5j*s,.5*s,1]],complex)
  K=np.eye(3)-np.linalg.inv(np.eye(3)+L)
  u=-math.log(t); d=-math.log1p(-t/4); tau=math.log(2)-2*d
  M=np.diag([d,d,u])+tau*K
  # Determinant from positive eigenvalues; all subsequent diagnostics are floating point.
  delta=np.linalg.det(M).real
  p=(8+5*t)/(4*Z); q2=6*t/(8+5*t); q3=(4-t)/(8-t); pi3=(8-t)/(4*Z)
  alpha=(8*a+1j*t)/(8+5*t)
  W=np.array([[1,-alpha,2j*s/(8-t)],[0,1,2*s*(1+1j*a)/(8-t)],[0,0,1]],complex)
  om=np.array([1/(p*(1-p)),p/(q2*(1-q2)),pi3/(q3*(1-q3))])
  H=W.conj().T@M@W; b=np.diag(H).real
  gam=abs(H)**2/(b[:,None]*b[None,:]); kap=delta/(om*b*b)
  E=kap[0]+kap[2]+2*gam[0,2]; R=1-gam[0,1]-gam[1,2]
  x=np.array([1,R/(1+kap[1]),1]); r=x/b
  C=abs(H)**2+delta*np.diag(1/om)
  trial=2*b@r-r@C@r
  Sigma=-abs(K)**2; np.fill_diagonal(Sigma,np.diag(K).real*(1-np.diag(K).real))
  dm=np.diag(M).real; ind=dm@np.linalg.solve(abs(M)**2+delta*Sigma,dm)
  Q=K[:2,:2]-np.diag([0,1]); v=-np.linalg.solve(Q,K[:2,2])
  assert np.max(abs(W[:2,2]-v))<1e-12
  assert abs(np.linalg.det(L).real-t/2)<1e-12
  assert np.min(np.linalg.eigvalsh(M))>0
  assert trial>=2+1/(20*u)-1e-10
  assert E*(1+kap[1])<R*R
  return dict(t=t, u=u, trial=trial, proved_lower=2+1/(20*u), indicator=ind,
              indicator_scaled_defect=(ind-2)/(t*u), E=E, R=R,kappa=kap.tolist(),
              gamma12=gam[0,1],gamma13=gam[0,2],gamma23=gam[1,2])

points=[point(t) for t in [1e-2,1e-3,1e-4,1e-6,1e-8]]
result={'exact_rational_checks':checks,'diagnostics_not_proof':points,
        'predicted_indicator_scaled_limit':-(2+3*math.log(2))/(24*math.log(2))}
print(json.dumps(result,indent=2))
pathlib.Path(__file__).with_name('output.json').write_text(json.dumps(result,indent=2)+'\n')
