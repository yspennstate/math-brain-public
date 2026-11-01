"""Exact determinant checks for X034; floating logs only corroborate identities."""
import itertools,json
from pathlib import Path
from fractions import Fraction
from collections import deque
import sympy as S
import mpmath as mp

out=Path(__file__).resolve().parent
I=S.I;Q=S.Rational;t=S.symbols('t',real=True)
K0=S.Matrix([[30,7,-5*I,3-2*I],[7,40,6,2*I],[5*I,6,60,-8],[3+2*I,-2*I,-8,70]])/100
k=K0[1:,0];R0=K0[1:,1:]
w=S.Matrix([I/40,Q(1,50)+I/100,-Q(1,50)+I/100]);lam=S.Integer(5);d=-Q(1,20)
F=lam*k*k.H
A=S.zeros(4);A[0,0]=d;A[1:,0]=w;A[0,1:]=w.H;A[1:,1:]=F
Kt=K0+t*A;Rt=R0+t*F;R3t=R0+3*t*F
checks=0

def simp(x):return S.simplify(S.expand_complex(x))
def check_zero(x):
 global checks
 if isinstance(x,S.MatrixBase):
  assert all(simp(z)==0 for z in x),x
 else:assert simp(x)==0,x
 checks+=1

def atom_data(M):
 n=M.rows;out=[]
 for bits in itertools.product((0,1),repeat=n):
  V=M-S.diag(*[1-b for b in bits]);sgn=(-1)**(n-sum(bits))
  r=S.factor(sgn*V.det());G=sgn*V.adjugate()
  out.append((bits,r,G))
 return out

def l1_upper(z):return abs(S.re(z))+abs(S.im(z))
def contraction_margins(M):
 global checks
 lows=[];ups=[]
 for i in range(M.rows):
  rad=sum(l1_upper(M[i,j]) for j in range(M.rows) if j!=i)
  lows.append(simp(M[i,i]-rad));ups.append(simp(1-M[i,i]-rad))
 assert all(v>0 for v in lows+ups)
 checks+=2
 return {'lower':list(map(str,lows)),'upper':list(map(str,ups))}

margins={'K0':contraction_margins(K0),'K1':contraction_margins(K0+A),'R_extrapolated':contraction_margins(R0+3*F)}
assert A.rank()==3;checks+=1
knorm=simp((k.H*k)[0]);wperp=w-k*simp((k.H*w)[0])/knorm
wnorm=simp((wperp.H*wperp)[0]);assert knorm>0 and wnorm>0;checks+=2
check_zero(A.det())
charpoly=S.factor(A.charpoly().as_expr())
active_det=-lam*knorm*wnorm
assert active_det<0;checks+=1

at=atom_data(Kt);r_at=atom_data(Rt);r3_at=atom_data(R3t)
rmap={bits:(r,G) for bits,r,G in r_at};r3map={bits:(r,G) for bits,r,G in r3_at}
check_zero(sum(p for _,p,_ in at)-1)
check_zero(sum(p for _,p,_ in r_at)-1)
# Affineness and annihilation hold separately for every atom-gradient, hence for arbitrary g.
for bits,r,G in r_at:
 check_zero(S.diff(r,t,2))
 check_zero(G.diff(t,2))
 check_zero(G.diff(t)*k)
 G3=r3map[bits][1]
 check_zero(G+2*t*G.diff(t)-G3)
# Every frozen table follows by linearity from the next atomwise identity.
for bits,p,G in at:
 sign=1 if bits[0] else -1
 grad=rmap[bits[1:]][1];grad3=r3map[bits[1:]][1]
 predicted=sign*(2*lam*d*(k.H*grad*k)[0]-2*(w.H*grad3*w)[0])
 check_zero(S.diff(p,t,2)-predicted)
 check_zero(S.diff(p,t,4))

# Exact matrix score normalization and completely positive score identity at R0.
a0=atom_data(R0);EY=S.zeros(3);lhs=S.zeros(3);rhs=S.zeros(3);C=k*k.H
for bits,r,G in a0:
 Y=G/r
 EY+=r*Y
 lhs+=r*S.trace(Y*C)*Y
 rhs+=r*Y*C*Y
check_zero(EY);check_zero(lhs-rhs)
# Positive rank-one score increments.
amap={bits:(r,G/r) for bits,r,G in a0}
for bits,(r,Y) in amap.items():
 for j,b in enumerate(bits):
  if b:continue
  new=list(bits);new[j]=1;rp,Yp=amap[tuple(new)]
  e=S.eye(3)[:,j]
  check_zero(Yp-Y-(r/rp)*Y*e*e.H*Y)

def increasing_edge_flow(bs):
 """Exact rational max flow on the increasing cube; div(flow)=bs."""
 global checks
 nodes=list(bs);idx={v:i for i,v in enumerate(nodes)};n=len(nodes)
 source=n;sink=n+1
 b=[Fraction(simp(bs[v])) for v in nodes]
 check_zero(sum(b))
 mass=sum(x for x in b if x>0)
 edges=[(v,j) for v in nodes for j in range(len(v)) if v[j]==0]
 if mass==0:return {e:Fraction(0) for e in edges}
 cap={};adj=[set() for _ in range(n+2)]
 def add(u,v,c):
  cap[(u,v)]=cap.get((u,v),Fraction(0))+c
  cap.setdefault((v,u),Fraction(0));adj[u].add(v);adj[v].add(u)
 for v,j in edges:
  vp=list(v);vp[j]=1;add(idx[v],idx[tuple(vp)],mass)
 for j,x in enumerate(b):
  if x<0:add(source,j,-x)
  elif x>0:add(j,sink,x)
 value=Fraction(0)
 while True:
  parent={source:None};q=deque([source])
  while q and sink not in parent:
   u=q.popleft()
   for v in sorted(adj[u]):
    if v not in parent and cap[(u,v)]>0:parent[v]=u;q.append(v)
  if sink not in parent:break
  v=sink;delta=mass
  while parent[v] is not None:
   u=parent[v];delta=min(delta,cap[(u,v)]);v=u
  v=sink
  while parent[v] is not None:
   u=parent[v];cap[(u,v)]-=delta;cap[(v,u)]+=delta;v=u
  value+=delta
 assert value==mass;checks+=1
 flow={};div={v:Fraction(0) for v in nodes}
 for v,j in edges:
  vp=list(v);vp[j]=1;vp=tuple(vp)
  c=mass-cap[(idx[v],idx[vp])];flow[(v,j)]=c
  div[v]-=c;div[vp]+=c
 check_zero(S.Matrix([div[v]-bs[v] for v in nodes]))
 return flow

transport=[]
for st in [Q(0),Q(1,2),Q(1)]:
 b1={bits:simp((k.H*G*k)[0].subs(t,st)) for bits,r,G in r_at}
 b2={bits:simp((w.H*G*w)[0].subs(t,st)) for bits,r,G in r3_at}
 c1=increasing_edge_flow(b1);c2=increasing_edge_flow(b2)
 z={e:Fraction(-lam*d)*c1[e]+c2[e] for e in c1}
 assert all(v>=0 for v in z.values());checks+=1
 acc={bits:S.Integer(0) for bits,p,G in at}
 for (bits,j),weight in z.items():
  bp=list(bits);bp[j]=1;bp=tuple(bp)
  acc[(0,)+bits]-=2*weight;acc[(1,)+bits]+=2*weight
  acc[(0,)+bp]+=2*weight;acc[(1,)+bp]-=2*weight
 check_zero(S.Matrix([acc[bits]-S.diff(p,t,2).subs(t,st) for bits,p,G in at]))
 transport.append({'t':str(st),'nonzero_face_weights':{'%s;j=%d'%(''.join(map(str,bits)),j+1):str(v) for (bits,j),v in z.items() if v},'atom_acceleration_residual':'exactly zero'})

exact_checks=checks
mp.mp.dps=60
def mval(z):
 z=S.simplify(z)
 return mp.mpc(str(S.N(S.re(z),65)),str(S.N(S.im(z),65)))
def scalar(z):
 v=mval(z);assert abs(v.imag)<mp.mpf('1e-55');return v.real
samples=[]
for st in [Q(0),Q(1,2),Q(1)]:
 vals={bits:scalar(p.subs(t,st)) for bits,p,G in at}
 direct=mp.mpf(0);fisher=mp.mpf(0)
 for bits,p,G in at:
  p0=vals[bits];p1=scalar(S.diff(p,t).subs(t,st));p2=scalar(S.diff(p,t,2).subs(t,st))
  fisher+=p1*p1/p0
  direct+=p1*p1/p0+p2*mp.log(p0)
 qterm=mp.mpf(0);extterm=mp.mpf(0)
 for bits,r,G in r_at:
  g=mp.log(vals[(0,)+bits]/vals[(1,)+bits])
  qterm+=g*scalar((k.H*G*k)[0].subs(t,st))
  G3=r3map[bits][1]
  extterm+=g*scalar((w.H*G3*w)[0].subs(t,st))
 rhs_num=fisher-2*scalar(lam*d)*qterm+2*extterm
 assert abs(direct-rhs_num)<mp.mpf('1e-50');checks+=1
 samples.append({'t':str(st),'minus_Hpp':str(direct),'full_Fisher':str(fisher),'signed_diagonal_compensation':str(-2*scalar(lam*d)*qterm),'extrapolated_coupling_compensation':str(2*extterm),'identity_error':str(abs(direct-rhs_num))})

# Corroborate (6) numerically at the selfmatched first-coordinate conditional law.
B=mp.matrix(3);P=mp.matrix(3)
for bits,r,G in a0:
 Y=G/r;q=simp(K0[0,0]-(k.H*Y*k)[0]);rr=scalar(r)
 f=mp.log((1-scalar(q))/scalar(q))
 Cmat=Y*k*k.H*Y
 for i in range(3):
  for j in range(3):
   B[i,j]+=rr*f*mval(Y[i,j]);P[i,j]+=rr*mval(Cmat[i,j])
cp_eigs=list(mp.eighe(B-4*P,eigvals_only=True))
result={'status':'PASS','exact_assertions':exact_checks,'high_precision_identity_assertions':checks-exact_checks,'strict_contraction_rational_margins':margins,'rank_A':3,'inertia_A':[2,1,1],'active_determinant':str(active_det),'norm_k_squared':str(knorm),'norm_w_perp_squared':str(wnorm),'characteristic_polynomial':str(charpoly),'jensen_improvement_coefficient':'1/200','exact_face_transport':transport,'curvature_samples_illustrative':samples,'CP_subtraction_eigenvalues_illustrative':list(map(str,cp_eigs))}
(out/'certificate.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
