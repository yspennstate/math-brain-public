"""Self-check the row criterion and its residual identity against atom calculus."""
from itertools import combinations
from pathlib import Path
import importlib.util,json
import numpy as np
spec=importlib.util.spec_from_file_location('probe','computations/X016/probe.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
p0=np.array([.5,.25,.125,.125]);u=np.sqrt(p0)
v=np.linalg.svd(u[None,:])[2][1:,:].conj().T
U,t,pairs,W,tau,fv,fw=m.data(v);n=v/np.sqrt(t)[:,None]
lam=abs(n@n.conj().T)**2;np.fill_diagonal(lam,0.)
c=-np.log1p(-lam);r=c@t;R=max(r);delta=56/25-R

def direct(s,a):
 K=(s*(v@v.conj().T)).astype(complex);D=v@a@v.conj().T;inc={}
 for k in range(4):
  for T in combinations(range(4),k):
   if not T:inc[T]=(1.,0.,0.);continue
   B=K[np.ix_(T,T)];C=D[np.ix_(T,T)]
   b0=np.linalg.det(B);b1=0j;b2=0j
   for i in range(k):
    Z=B.copy();Z[:,i]=C[:,i];b1+=np.linalg.det(Z)
   for i,j in combinations(range(k),2):
    Z=B.copy();Z[:,i]=C[:,i];Z[:,j]=C[:,j];b2+=2*np.linalg.det(Z)
   inc[T]=(b0.real,b1.real,b2.real)
 ans=0.;FI=0.
 for S in inc:
  atom=np.zeros(3)
  for T,derivs in inc.items():
   if set(S)<=set(T):atom+=(-1)**(len(T)-len(S))*np.array(derivs)
  p,dp,ddp=atom
  assert p>0
  FI+=dp*dp/p;ans+=dp*dp/p+ddp*np.log(p)
 return ans,FI

def pieces(s,a):
 q=1-s;h=np.trace(a).real;na=n@a@n.conj().T;x=np.diag(na).real
 Fv=np.sum(t*x*x);Fw=sum(np.trace(P@a).real**2/b for P,b in pairs)
 QW=np.trace(W@m.adj(a)).real;Ew=Fw-(Fv+h*h)/4
 N=np.sum(t[:,None]*t[None,:]*c*abs(na)**2)
 G=np.sum(t*(R-r)*x*x)+.5*np.sum(t[:,None]*t[None,:]*c*(x[:,None]-x[None,:])**2)+N
 B=a-h*np.eye(3)/3
 C1=1/s+1/(4*q)-R;C2=1/(4*q)-2*s*tau/3
 rhs=C1*Fv+C2*h*h+G+Ew/q+s*tau*np.trace(B@B).real
 bound=delta*Fv+G+Ew/q+s*tau*np.trace(B@B).real
 return dict(Fv=float(Fv),Fw=float(Fw),QW=float(QW),pair_identity_error=float(abs(G-(R*Fv-2*QW))),exterior_remainder=float(Ew),rhs=float(rhs),bound=float(bound))

out={'parseval_error':float(np.linalg.norm(v.conj().T@v-np.eye(3))),
     'R':float(R),'tau':float(tau),'tau_exact':float(.25*np.log(1350000/823543)),
     'delta':float(delta),'W_eigenvalues':np.linalg.eigvalsh(W).tolist(),'checks':[]}
A=np.array([[1,.3+.2j,-.4j],[.3-.2j,-.7,.2], [.4j,.2,.1]],complex)
for s in [.2,.5,.8]:
 row=pieces(s,A);neg,FI=direct(s,A);row.update(s=s,negative_hessian=float(neg),fisher=float(FI),residual_identity_error=float(abs(neg-row['rhs'])),bound_slack=float(neg-row['bound']))
 mat=m.qmat(lambda a:direct(s,a)[0]-delta*pieces(s,a)['Fv'])
 row['minimum_matrix_gap']=float(np.linalg.eigvalsh(mat)[0]);out['checks'].append(row)
Path('computations/X028/results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
