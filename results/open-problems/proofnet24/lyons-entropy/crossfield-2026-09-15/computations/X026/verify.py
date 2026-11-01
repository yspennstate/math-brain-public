"""Deterministic exact checks of X026's affine identities; no numerical sign proof."""
import itertools, json
import sympy as s
from pathlib import Path
I=s.I
R=s.Rational
n=4
subsets=[tuple(i for i in range(n) if m>>i&1) for m in range(16)]
sgn=[(-1)**len(t) for t in subsets]


def rr(x):return s.simplify(s.re(x))
def norm2(X):return rr(s.trace(X.H*X))
def jets(K,A):
 out=[]
 for mask,T in enumerate(subsets):
  M=K-s.diag(*[0 if i in T else 1 for i in range(n)])
  p=s.simplify((-1)**(n-len(T))*M.det())
  Q=M.inv()*A
  a=s.simplify(p*s.trace(Q))
  b=s.simplify(p*(s.trace(Q)**2-s.trace(Q*Q)))
  out.append((p,a,b))
 assert sum(v[0] for v in out)==1
 assert sum(v[1] for v in out)==sum(v[2] for v in out)==0
 assert all(v[0]>0 for v in out)
 return out


def alpha_vector(e):
 return [R(1,4)*((-1)**(2-sum(i in t for i in e))) for t in subsets]

B=s.Matrix([[R(1,7)+I/11,R(1,9)-I/13],[-R(1,8)+I/17,R(1,10)+I/19]])
U=s.Matrix([[0,R(1,6)+I/7],[R(1,6)-I/7,0]])
V=s.Matrix([[0,-R(1,8)+I/9],[-R(1,8)-I/9,0]])
AB=s.zeros(4);AB[:2,2:]=B;AB[2:,:2]=B.H
A0=s.diag(U,V)
cross=[(0,2),(0,3),(1,2),(1,3)]
all_edges=list(itertools.combinations(range(4),2))
results=[]
for name,Z in [
 ('positive_tau_independent_phase',s.Matrix([[R(1,4),R(1,4)],[R(1,4),I/4]])),
 ('negative_tau_large_coherence',s.Matrix([[R(2,5),R(1,5)],[-R(1,5)+I/100,R(39,100)]]))]:
 K=s.eye(4)/2;K[:2,2:]=Z;K[2:,:2]=Z.H
 J=K-s.eye(4)/2
 margin=s.eye(2)/4-Z*Z.H
 assert margin[0,0]>0 and s.simplify(margin.det())>0
 jb,j0,jboth=jets(K,AB),jets(K,A0),jets(K,AB+A0)
 p=[v[0] for v in jb]
 assert all(p[m]==p[15-m] for m in range(16))
 assert all(jb[m][1]==jb[15-m][1] for m in range(16))
 assert all(j0[m][1]==-j0[15-m][1] for m in range(16))
 d=s.simplify(Z.det()); dp=s.simplify(s.trace(Z.adjugate()*B))
 dd=s.simplify(2*rr(dp*s.conjugate(dp))+4*rr(s.conjugate(d)*B.det()))
 alpha={e:alpha_vector(e) for e in all_edges}
 for m in range(16):
  predicted=-2*sum(alpha[e][m]*rr(B[e[0],e[1]-2]*s.conjugate(B[e[0],e[1]-2])) for e in cross)+sgn[m]*dd
  assert s.simplify(predicted-jb[m][2])==0
 detj_dd=s.simplify(-2*s.trace(Z.adjugate().H*V*Z.adjugate()*U))
 for m in range(16):
  pred=2*sum(alpha[e][m]*A0.extract(e,e).det() for e in all_edges)+sgn[m]*detj_dd
  assert s.simplify(pred-j0[m][2])==0
 mixed=[s.simplify((jboth[m][2]-jb[m][2]-j0[m][2])/2) for m in range(16)]
 assert all(s.simplify(mixed[m]+mixed[15-m])==0 for m in range(16))
 assert sum(jb[m][1]*j0[m][1]/p[m] for m in range(16))==0
 ell=s.simplify(s.trace(K.inv()*AB))
 qk=s.simplify(s.trace(K.inv()*AB*K.inv()*AB))
 eta=s.simplify(2*s.trace(Z*Z.H*(s.eye(2)/4+Z*Z.H).inv()))
 assert 0<eta<2 and s.simplify(eta*qk-ell**2)>0
 Bstar=-Z*(s.eye(2)/4-Z.H*Z)*(s.eye(2)/4+Z.H*Z).inv()
 Astar=s.zeros(4);Astar[:2,2:]=Bstar;Astar[2:,:2]=Bstar.H
 assert s.simplify(s.trace(K.inv()*Astar)-eta)==0
 assert s.simplify(s.trace(K.inv()*Astar*K.inv()*Astar)-eta)==0
 ep=s.simplify(s.prod(p[m] for m in range(16) if len(subsets[m])%2==0))
 op=s.simplify(s.prod(p[m] for m in range(16) if len(subsets[m])%2))
 ratio=s.simplify(op/ep)
 tau=s.log(ratio)
 fisher_b=s.simplify(sum(v[1]**2/v[0] for v in jb))
 assert s.simplify(fisher_b-2*p[0]*ell**2/(1-2*p[0]))>=0
 # Exact G Hessian and the displayed square completion, including d acceleration.
 Gdd=s.simplify(-norm2(B)/2-dd)
 absd=s.sqrt(rr(d*s.conjugate(d)))
 phase=d/absd
 Sd=s.simplify(rr((B[0,0]+phase*s.conjugate(B[1,1]))*s.conjugate(B[0,0]+phase*s.conjugate(B[1,1])))+rr((B[0,1]-phase*s.conjugate(B[1,0]))*s.conjugate(B[0,1]-phase*s.conjugate(B[1,0]))))
 square_rhs=s.simplify(-2*rr(dp*s.conjugate(dp))-(R(1,2)-2*absd)*norm2(B)-2*absd*Sd)
 assert s.simplify(square_rhs-Gdd)==0
 assert absd<R(1,4)
 if name.startswith('positive'):
  assert ratio==R(2401,1377)**2
  assert eta>1
  # log x < x-1 proves tau < 2048/1377 < 4; eta<2 gives c(eta)<1/2.
  assert 2*(R(2401,1377)-1)<4
 else:
  assert ratio<1 and eta>1
 def curvature(j):
  fi=s.simplify(sum(v[1]**2/v[0] for v in j))
  frozen=-sum(v[2]*s.log(v[0]) for v in j)
  return {'fisher':str(s.N(fi,30)),'frozen':str(s.N(frozen,30)),'hessian':str(s.N(frozen-fi,30))}
 results.append({'name':name,'Z':str(Z),'det_K':str(p[0]),'tau_log_argument':str(ratio),
                 'tau_decimal':str(s.N(tau,30)),'eta':str(eta),'eta_decimal':str(s.N(eta,30)),
                 'loop_product':str(s.simplify(Z[0,0]*s.conjugate(Z[1,0])*Z[1,1]*s.conjugate(Z[0,1]))),
                 'cross_block':curvature(jb),'missing_edges':curvature(j0),'combined':curvature(jboth),
                 'exact_checks':'atom jets; even/odd score split; centered polynomial; determinant acceleration; mixed block cancellation; eta inequality; event Fisher bound; negative-tau squares; feasibility and tau sign: PASS'})
Path(__file__).with_name('results.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps(results,indent=2))
