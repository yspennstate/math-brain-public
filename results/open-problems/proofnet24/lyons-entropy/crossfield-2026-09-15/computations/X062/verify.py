import numpy as np,itertools,json
from pathlib import Path
root=Path(__file__).parent
om=np.exp(2j*np.pi/3); X=np.array([[0,0,1],[1,0,0],[0,1,0]],complex);Z=np.diag([1,om,om**2]);u=np.array([0,1,-1],complex)/np.sqrt(2)
base=np.array([np.linalg.matrix_power(Z,a)@np.linalg.matrix_power(X,b)@u for a in range(3) for b in range(3)])
def frame(eps):
 R=np.diag([1,1,(1-eps**2+2j*eps)/(1+eps**2)])
 ns=np.concatenate([base,base@R.T]);return ns.conj()/np.sqrt(6)
def data(V):
 n=len(V);U=[np.outer(v.conj(),v) for v in V];t=np.array([np.trace(a).real for a in U]); Ps=[a/z for a,z in zip(U,t)];pairs=[];W=np.zeros((3,3),complex);bb={};cc={};Fws=[]
 for i,j in itertools.combinations(range(n),2):
  w=np.cross(V[i],V[j]);b=np.vdot(w,w).real
  if b<1e-24:continue
  P=np.outer(w,w.conj())/b;c=np.log(t[i]*t[j]/b);W+=b*c*P;bb[i,j]=b;cc[i,j]=c;pairs.append((i,j,b,P,c))
 tau=0.;G=np.zeros((3,3),complex);trips=[];be=np.zeros(n)
 for T in itertools.combinations(range(n),3):
  r=abs(np.linalg.det(V[list(T)]))**2
  if r<1e-26:continue
  ct=np.log(np.prod([bb[p] for p in itertools.combinations(T,2)])/(np.prod(t[list(T)])*r));tau+=r*ct;trips.append((T,r,ct))
  for i in T:
   jk=tuple(j for j in T if j!=i);be[i]+=r*(ct+cc[jk])/t[i]
 G=sum(ti*bet*P for ti,bet,P in zip(t,be,Ps))
 return U,t,Ps,pairs,W,tau,G,be,trips
basis=[np.diag([float(i==j) for i in range(3)]).astype(complex) for j in range(3)]
for i,j in itertools.combinations(range(3),2):
 A=np.zeros((3,3),complex);A[i,j]=A[j,i]=1/np.sqrt(2);basis.append(A)
 A=np.zeros((3,3),complex);A[i,j]=1j/np.sqrt(2);A[j,i]=-1j/np.sqrt(2);basis.append(A)
def adj(A):return A@A-np.trace(A)*A+((np.trace(A)**2-np.trace(A@A))/2)*np.eye(3)
def quadmat(fn):
 d=[fn(a) for a in basis];M=np.diag(d)
 for i,j in itertools.combinations(range(9),2):M[i,j]=M[j,i]=(fn(basis[i]+basis[j])-d[i]-d[j])/2
 return M
out=[]
for eps in [1.,1e-4]:
 V=frame(eps);U,t,Ps,pairs,W,tau,G,be,trips=data(V)
 fv=lambda A:sum((np.trace(B@A).real)**2/ti for B,ti in zip(U,t))
 fw=lambda A:sum(b*(np.trace(P@A).real)**2 for i,j,b,P,c in pairs)
 err2=max(abs(fv(A+B)-(np.trace((A+B)@(A+B)).real+np.trace(A+B).real**2)/4) for A in basis for B in basis)
 assert err2<1e-12
 errflag=0.;errdef=0.
 for A in basis+[sum((i+1)*a/9 for i,a in enumerate(basis))]:
  Fi=0.
  for i in range(len(V)):
   Q=np.eye(3)-Ps[i];B=Q@A@Q
   Fi+=t[i]*sum(t[j]*(np.trace(Ps[j]@B).real)**2/(1-np.trace(Ps[i]@Ps[j]).real) for j in range(len(V)) if 1-np.trace(Ps[i]@Ps[j]).real>1e-12)
  errflag=max(errflag,abs(Fi-2*fw(A)))
 PhiW=sum(ti*np.trace(P@W)*P for ti,P in zip(t,Ps))
 D2=PhiW-W+sum(r*c*(sum(Ps[i] for i in T)-np.eye(3)) for T,r,c in trips)
 errdef=np.linalg.norm(G-W-tau*np.eye(3)-D2)
 assert errflag<1e-7 and errdef<1e-11
 assert max(be)<=np.log(2)+1e-12 and min(be)>=-1e-12
 assert np.linalg.eigvalsh(quadmat(lambda A:fw(A)-3*(np.trace(A@A).real+np.trace(A).real**2)/16)).min()>-1e-12
 mins=[]
 for s in [.1,.3,.5,.7,.9]:
  fn=lambda A:fv(A)/s+fw(A)/(1-s)-2*np.trace((W+s*tau*np.eye(3))@adj(A)).real
  mins.append([s,np.linalg.eigvalsh(quadmat(fn)).min()])
 assert min(m for s,m in mins)>.1
 rowsums=np.zeros(len(V))
 for i,j,b,P,c in pairs:rowsums[i]+=t[j]*c;rowsums[j]+=t[i]*c
 out.append({'eps':eps,'design_error':err2,'flag_fisher_error':errflag,'orientation_defect_error':errdef,'trace_identity_error':abs(np.trace(G).real-np.trace(W).real-3*tau),'W_diagonal':np.diag(W).real.tolist(),'tau':tau,'R':max(rowsums),'negative_hessian_min_eigenvalues':mins})
(root/'results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
