import json,itertools
from pathlib import Path
import numpy as np
import sympy as S
out={}; checks=0

def check(x, label):
 global checks
 assert x,label
 checks+=1

s,r=S.symbols('s r',real=True)
P=360-1017*s+464*s*s+448*s**3
check(S.expand(P.subs(s,r+S.Rational(1,2))-(S.Rational(47,2)-217*r+1136*r*r+448*r**3))==0,'cubic shift')
check(4*912*S.Rational(47,2)-217**2==38639,'cubic discriminant')
check(S.Rational(1,12)-S.Rational(49,1170)>S.Rational(1,25),'traceless gap')
check(S.Rational(31,780)<S.Rational(1,25),'trace lift B')
check(S.Rational(1,39)<S.Rational(13,15),'trace lift u')
check(S.Rational(49,1014)<S.Rational(1,20),'trace cross')
check(sum(S.Rational(7,10)**k/S.factorial(k) for k in range(5))>2,'log2 bound')
a,b=S.symbols('a b',real=True)
check(S.expand(2*(a*a+a*b+b*b)-6*a*b-2*(a-b)**2)==0,'positive adjugate trace')

# Orthonormal basis of Hermitian matrices, with an independent traceless basis.
HB=[]
for k in range(3):
 E=np.zeros((3,3),complex);E[k,k]=1;HB.append(E)
for j,k in itertools.combinations(range(3),2):
 E=np.zeros((3,3),complex);E[j,k]=E[k,j]=1/np.sqrt(2);HB.append(E)
 E=np.zeros((3,3),complex);E[j,k]=1j/np.sqrt(2);E[k,j]=-1j/np.sqrt(2);HB.append(E)
TB=[np.diag([1,-1,0])/np.sqrt(2),np.diag([1,1,-2])/np.sqrt(6)]+HB[3:]

def forms(V,basis=HB):
 t=np.sum(abs(V)**2,axis=1);U=[np.outer(v.conj(),v) for v in V]
 pairs=[]
 for i,j in itertools.combinations(range(len(V)),2):
  w=np.cross(V[i],V[j]);weight=np.vdot(w,w).real
  if weight>1e-14:pairs.append((i,j,weight,np.outer(w,w.conj())))
 triples=[]
 for ix in itertools.combinations(range(len(V)),3):
  weight=abs(np.linalg.det(V[list(ix)]))**2
  if weight>1e-14:triples.append((ix,weight))
 fv=np.array([[np.trace(X@A).real for A in basis] for X in U])
 fw=np.array([[np.trace(X@A).real for A in basis] for i,j,weight,X in pairs])
 weights=np.array([p[2] for p in pairs]);FV=fv.T@np.diag(1/t)@fv;FW=fw.T@np.diag(1/weights)@fw
 W=sum(np.log(t[i]*t[j]/weight)*X for i,j,weight,X in pairs)
 pd={(i,j):weight for i,j,weight,X in pairs}
 tau=sum(weight*np.log(np.prod([pd[tuple(ij)] for ij in itertools.combinations(ix,2)])/np.prod(t[list(ix)])/weight) for ix,weight in triples)
 return FV,FW,W,tau,t,U,pairs,triples

omega=-.5+np.sqrt(3)*.5j
D=[]
for j,k in itertools.combinations(range(3),2):
 for z in range(3):
  n=np.zeros(3,complex);n[j]=1/np.sqrt(2);n[k]=-omega**z/np.sqrt(2)
  D.append(n.conj()/np.sqrt(3))
D=np.array(D)
FD= forms(D)[0]
design_target=np.zeros((9,9))
for j,X in enumerate(HB):
 for k,Y in enumerate(HB):design_target[j,k]=(np.trace(X).real*np.trace(Y).real+np.trace(X@Y).real)/4
check(np.max(abs(FD-design_target))<1e-14,'design moment numeric')

# Exact symbolic polynomial verification of the same design identity.
z=S.sqrt(3)*S.I/2-S.Rational(1,2)
d0,d1,d2,x01,y01,x02,y02,x12,y12=S.symbols('d0 d1 d2 x01 y01 x02 y02 x12 y12',real=True)
A=S.Matrix([[d0,x01+S.I*y01,x02+S.I*y02],[x01-S.I*y01,d1,x12+S.I*y12],[x02-S.I*y02,x12-S.I*y12,d2]])
val=0
for j,k in itertools.combinations(range(3),2):
 for power in range(3):
  n=S.zeros(3,1);n[j]=1/S.sqrt(2);n[k]=-z**power/S.sqrt(2)
  val+=S.expand((n.conjugate().T*A*n)[0]**2)/3
check(S.simplify(S.expand(val-(S.trace(A)**2+S.trace(A*A))/4))==0,'exact design polynomial')

beta=.001;alpha=.5-beta
R=np.array([[1/np.sqrt(2),0,np.sqrt(beta)],[-1/np.sqrt(2),0,np.sqrt(beta)],[0,1/np.sqrt(2),-np.sqrt(alpha)],[0,-1/np.sqrt(2),-np.sqrt(alpha)]],complex)
V=np.vstack([D/np.sqrt(2),R/np.sqrt(2)])
FV,FW,W,tau,weights,Us,pairs,triples=forms(V)
FT=forms(V,TB)[0]
check(np.max(abs(V.conj().T@V-np.eye(3)))<1e-14,'Parseval')
check(np.linalg.eigvalsh(FT)[0]>=1/8-1e-13,'moment threshold')
check(np.max(abs(sum(p[3] for p in pairs)-np.eye(3)))<1e-14,'pair Parseval')
L=np.log(2); eig=np.linalg.eigvalsh(W)
check(eig[0]>-1e-12 and eig[-1]<L+1e-12,'W interval')
check(eig[0]+tau>=-1e-12,'C positivity')
check(np.trace(W).real+3*tau<=3*L+1e-12,'trace bound')

A0=np.array([[.4,.3+.2j,-.7+.4j],[.3-.2j,-.8,.6j],[-.7-.4j,-.6j,.2]])
B=A0-np.trace(A0)*np.eye(3)/3;h=np.trace(A0).real
adj=lambda X:X@X-np.trace(X)*X+(.5*(np.trace(X)**2-np.trace(X@X)))*np.eye(3)
fv=lambda X:sum(np.trace(U@X).real**2/t for U,t in zip(Us,weights))
fw=lambda X:sum(np.trace(X@U).real**2/t for i,j,t,U in pairs)
conditional=0
trace_sq=0;norm_sq=0
for i,(t,U) in enumerate(zip(weights,Us)):
 Q=np.eye(3)-U/t;Bi=Q@A0@Q
 Fi=0
 for j,(tj,Uj) in enumerate(zip(weights,Us)):
  dij=np.trace(Q@Uj).real/tj
  if dij>1e-13:Fi+=np.trace(Uj@Bi).real**2/(tj*dij)
 conditional+=t*Fi
 trace_sq+=t*np.trace(Bi).real**2
 norm_sq+=t*np.trace(Bi@Bi).real
check(abs(conditional-2*fw(A0))<1e-12,'conditional frame equality')
check(abs(trace_sq-h*h-fv(A0))<1e-12,'conditional trace identity')
check(abs(norm_sq-np.trace(A0@A0).real-fv(A0))<1e-12,'conditional norm identity')

# Direct measured atom polynomials, independently from the curvature formula.
def atom_probs(M):
 detM=np.linalg.det(M).real;AD=adj(M)
 pp=[np.linalg.det(np.eye(3)-M).real]
 pp += [(np.trace(U@M)-np.trace((t*np.eye(3)-U)@AD)+t*detM).real for t,U in zip(weights,Us)]
 pp += [(np.trace(U@AD)-t*detM).real for i,j,t,U in pairs]
 pp += [weight*detM for ix,weight in triples]
 return np.array(pp)
def actual_q(s,A):
 p=atom_probs(s*np.eye(3))
 vals=[atom_probs(s*np.eye(3)+k*A) for k in [-2,-1,1,2]]
 p1=(vals[0]-8*vals[1]+8*vals[2]-vals[3])/12
 p2=vals[1]+vals[2]-2*p
 return np.sum(p1*p1/p+p2*np.log(p))

results=[]
for s0 in [.1,.5,.9]:
 q=1-s0;T=W+s0*tau*np.eye(3);c=np.trace(W).real/3;E=W-c*np.eye(3);d=c+s0*tau;ls=1/(s0*q)-2*d
 Q=FV/s0+FW/q
 J=np.zeros((9,9))
 for i,X in enumerate(HB):
  J[i,i]=np.trace(T@adj(X)).real
  for j in range(i):
   Y=HB[j];J[i,j]=J[j,i]=(np.trace(T@adj(X+Y)).real-J[i,i]-np.trace(T@adj(Y)).real)/2
 negH=Q-2*J
 check(np.linalg.eigvalsh(negH)[0]>1/26,'full Hessian theorem sample')
 full=fv(A0)/s0+fw(A0)/q-2*np.trace(T@adj(A0)).real
 remainder=fv(B)/s0+fw(B)/q-2*np.trace(T@adj(B)).real-np.trace(E@B).real**2/(3*ls)
 completed=remainder+ls/3*(h+np.trace(E@B).real/ls)**2
 check(abs(full-completed)<1e-12,'full trace square')
 atom=actual_q(s0,A0)
 check(abs(full-atom)<2e-8,'independent atom Hessian')
 check(remainder>np.trace(B@B).real/25,'traceless remainder')
 results.append({'s':s0,'minimum_full_negative_Hessian_eigenvalue':float(np.linalg.eigvalsh(negH)[0]),'direction_curvature':float(full),'atom_identity_error':float(abs(atom-full))})

c=float(np.trace(W).real/3);Eval=eig-c;dm=min(c,c+tau);dp=max(c,c+tau)
anisotropy_rhs=2*Eval[-1]+np.sum(Eval**2)/(3*(4-2*dp))
out={'status':'PASS','checks':checks,'scope':'Numerical values verify identities and explicit example only; report gives the all-parameter theorem.','moment_threshold':'1/8','design_fraction':'1/2','full_uniform_constant':'1/26','example_rows':len(V),'minimum_traceless_frame_moment':float(np.linalg.eigvalsh(FT)[0]),'W_eigenvalues':eig.tolist(),'tau':float(tau),'X008_uniform_anisotropy_test':{'d_minus':dm,'required_lower_bound':float(anisotropy_rhs),'passes':bool(dm>=anisotropy_rhs),'interpretation':'This example overlaps the older anisotropy criterion if passes is true; no disjointness claim is made.'},'scalar_checks':results,'cubic_discriminant':38639,'traceless_gap_exact':str(S.Rational(1,12)-S.Rational(49,1170))}
path=Path(__file__).with_name('results.json');path.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
