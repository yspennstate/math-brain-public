from itertools import combinations
import json
from pathlib import Path
import numpy as np

I=np.eye(3)
def adj(A):
 h=np.trace(A);return A@A-h*A+(h*h-np.trace(A@A))/2*I

def basis():
 out=[]
 for i in range(3):
  a=np.zeros((3,3),complex);a[i,i]=1;out.append(a)
 for i,j in combinations(range(3),2):
  a=np.zeros((3,3),complex);a[i,j]=a[j,i]=1/np.sqrt(2);out.append(a)
  a=np.zeros((3,3),complex);a[i,j]=1j/np.sqrt(2);a[j,i]=-1j/np.sqrt(2);out.append(a)
 return out
BASIS=basis()
def qmat(f):
 d=np.array([f(b) for b in BASIS]);ans=np.diag(d)
 for i,j in combinations(range(9),2):ans[i,j]=ans[j,i]=(f(BASIS[i]+BASIS[j])-d[i]-d[j])/2
 return ans

def parseval(raw):
 e,u=np.linalg.eigh(raw.conj().T@raw);return raw@((u/np.sqrt(e))@u.conj().T)

def data(v):
 U=[np.outer(z.conj(),z) for z in v];t=np.array([np.trace(u).real for u in U]);pairs=[];W=0*I.astype(complex);E2=0.;E1=-sum(x*np.log(x) for x in t if x>1e-25)
 for i,j in combinations(range(len(v)),2):
  z=np.cross(v[i],v[j]);b=np.vdot(z,z).real
  if b>1e-25:
   P=np.outer(z,z.conj());pairs.append((P,b));W+=np.log(t[i]*t[j]/b)*P;E2-=b*np.log(b)
 E3=0.
 for ind in combinations(range(len(v)),3):
  r=abs(np.linalg.det(v[list(ind)]))**2
  if r>1e-25:E3-=r*np.log(r)
 fv=qmat(lambda a:sum(np.trace(u@a).real**2/x for u,x in zip(U,t) if x>1e-25))
 fw=qmat(lambda a:sum(np.trace(P@a).real**2/b for P,b in pairs))
 return U,t,pairs,W,E1-E2+E3,fv,fw

def probes():
 om=np.exp(2j*np.pi/3);F=np.array([[om**(i*j) for j in range(3)] for i in range(3)])/np.sqrt(3)
 z=np.array([0,1,1j,-1+.5j,2-1j,.5+.75j]);generic=parseval(np.column_stack((np.ones(6),z,z*z)))
 raw=np.array([[1,0,0],[0,1,0],[0,0,1],[1,1,0],[1,1j,0]],complex);block=parseval(raw)
 frames=[('generic',generic),('block',block)]
 for eps in (.001,.01,.1,.5):frames.append(('basis_mixture_'+str(eps),np.vstack((np.sqrt(1-eps)*I,np.sqrt(eps)*F))))
 out=[]
 for label,v in frames:
  U,t,pairs,W,tau,fv,fw=data(v);qw=qmat(lambda a:np.trace(W@adj(a)).real);qt=qmat(lambda a:np.trace((W+tau*I)@adj(a)).real)
  out.append(dict(label=label, W_eigs=np.linalg.eigvalsh(W).tolist(),tau=tau,Fv_minus_QW=np.linalg.eigvalsh(fv-qw).tolist(),Fw_minus_QT=np.linalg.eigvalsh(fw-qt).tolist(),C1_eigs=np.linalg.eigvalsh(2*fv+fw-2*qw).tolist(),C2_eigs=np.linalg.eigvalsh(fv+2*fw-2*qt).tolist()))
 return out
if __name__=='__main__':
 out=probes();Path(__file__).with_name('probe_results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
