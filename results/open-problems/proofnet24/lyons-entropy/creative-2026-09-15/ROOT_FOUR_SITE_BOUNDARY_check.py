"""Numerical jet and independent-scale diagnostics, not a universal certificate."""
import json, math
from pathlib import Path
import numpy as np
rng=np.random.default_rng(20260915)
U,_=np.linalg.qr(rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)))
M=np.array([[.31,.04+.03j],[.04-.03j,.67]])
N=np.eye(2)-M; mi=np.linalg.inv(M); ni=np.linalg.inv(N)
d=float(np.linalg.det(M).real); d0=float(np.linalg.det(N).real)
basis=[]
for i in [0,1]:
 A=np.zeros((4,4),complex);A[i,i]=1;basis.append(A)
for i,j in [(0,1),(0,2),(0,3),(1,2),(1,3)]:
 for phase in [1,1j]:
  A=np.zeros((4,4),complex);A[i,j]=phase;A[j,i]=phase.conjugate();basis.append(A)
for A2 in [np.diag([1,0]),np.diag([0,1]),np.array([[0,1],[1,0]]),np.array([[0,1j],[-1j,0]])]:
 A=np.zeros((4,4),complex);A[2:,2:]=A2;basis.append(A)
def decomp(A):
 return A[0,0].real,A[1,1].real,A[1,0],A[2:,0],A[2:,1],A[2:,2:]
def singular(e,h,A):
 a,b,c,x,y,B=decomp(A);t=np.trace(mi@B).real;t0=np.trace(ni@B).real;db=np.linalg.det(B).real
 q=e*(1-h)*d;g=d*((1-h)*a+e*b+e*(1-h)*t)
 f=2*d*(a*b+(1-h)*a*t+e*b*t-abs(c)**2-(1-h)*np.vdot(x,mi@x).real-e*np.vdot(y,mi@y).real)+2*e*(1-h)*db
 q0=h*(1-e)*d0;g0=-d0*(h*a+(1-e)*b+h*(1-e)*t0)
 f0=2*d0*(a*b+h*a*t0+(1-e)*b*t0-abs(c)**2-h*np.vdot(x,ni@x).real-(1-e)*np.vdot(y,ni@y).real)+2*h*(1-e)*db
 return [(q,g,f),(q0,g0,f0)]
def regular(e,h,A):
 K=np.zeros((4,4),complex);K[0,0]=e;K[1,1]=1-h;K[2:,2:]=M;K=U@K@U.conj().T
 Am=U@A@U.conj().T;out=0.
 for mask in range(1,15):
  D=K-np.diag([0 if mask>>i&1 else 1 for i in range(4)])
  sign=(-1)**(4-mask.bit_count());p=sign*np.linalg.det(D).real
  R=np.linalg.solve(D,Am);tr=np.trace(R).real
  g=p*tr;f=p*(tr*tr-np.trace(R@R).real)
  assert p>0
  out-=g*g/p+math.log(p)*f
 return out
def form(fun,bs):
 ds=np.array([fun(A) for A in bs]);out=np.diag(ds)
 for i in range(len(bs)):
  for j in range(i):out[i,j]=out[j,i]=(fun(bs[i]+bs[j])-ds[i]-ds[j])/2
 return (out+out.T)/2
T=form(lambda A:regular(0,0,A),basis[12:])
def principal(e,h,A):
 a,b,c,x,y,B=decomp(A);Le=-math.log(e);Lh=-math.log(h)
 return -d*a*a-d0*b*b-2*d*np.vdot(x,mi@x).real-2*d0*np.vdot(y,ni@y).real-2*(d*Le+d0*Lh)/(Le+Lh)*abs(c)**2+regular(0,0,np.block([[np.zeros((2,2)),np.zeros((2,2))],[np.zeros((2,2)),B]]))
jeterr=0.
for e,h in [(.07,.12),(.17,.03)]:
 K=np.zeros((4,4),complex);K[0,0]=e;K[1,1]=1-h;K[2:,2:]=M
 for _ in range(12):
  A=sum(rng.normal()*B for B in basis)
  for D,E,j in [(K,A,0),(np.eye(4)-K,-A,1)]:
   p=np.linalg.det(D).real;R=np.linalg.solve(D,E);tr=np.trace(R).real
   direct=(p,p*tr,p*(tr**2-np.trace(R@R).real))
   jeterr=max(jeterr,max(abs(x-y) for x,y in zip(direct,singular(e,h,A)[j])))
assert jeterr<1e-11
rows=[]
for power in [1,3,1/3]:
 for delta in [1e-3,1e-6,1e-12,1e-24]:
  e=delta;h=delta**power;Le=-math.log(e);Lh=-math.log(h)
  sc=[math.sqrt(e),math.sqrt(h)]+[1/math.sqrt(Le+Lh)]*2+[1/math.sqrt(Le)]*4+[1/math.sqrt(Lh)]*4+[1]*4
  def full(A):return regular(e,h,A)+sum(-g*g/p-math.log(p)*f for p,g,f in singular(e,h,A))
  H=form(full,[s*A for s,A in zip(sc,basis)]);P=form(lambda A:principal(e,h,A),basis)
  rows.append({'epsilon':e,'eta':h,'max_scaled_hessian_eigenvalue':float(np.linalg.eigvalsh(H)[-1]),'operator_error':float(np.linalg.norm(H-P,2))})
out={'status':'numerical diagnostics only; universal theorem is analytic','jet_max_absolute_error':jeterr,'face_max_hessian_eigenvalue':float(np.linalg.eigvalsh(T)[-1]),'min_endpoint_coordinate_probability':float(min(np.min(abs(U[:,0])**2),np.min(abs(U[:,1])**2))),'min_active_plane_minor_square':float(min(abs(np.linalg.det(U[[i,j],2:]))**2 for i in range(4) for j in range(i))),'samples':rows}
assert out['face_max_hessian_eigenvalue']<0
assert all(r['max_scaled_hessian_eigenvalue']<0 for r in rows)
Path(__file__).with_name('ROOT_FOUR_SITE_BOUNDARY_results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
