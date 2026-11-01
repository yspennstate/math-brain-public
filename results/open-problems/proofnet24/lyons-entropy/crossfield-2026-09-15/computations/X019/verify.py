"""Standalone exact certificate verification. Uses only Python's standard library."""
from fractions import Fraction as F
from itertools import combinations, product
from math import lcm,gcd,prod
from pathlib import Path
import json,time
BASE=Path(__file__).resolve().parent
E=range(6); PAIRS=list(combinations(E,2));TRIPLES=list(combinations(E,3))
ATOMS=[(a,b) for a in PAIRS for b in PAIRS if not set(a)&set(b)]
LAM=F(3960,10201);DEL=F(9401,10201)
assert LAM*LAM+DEL*DEL==1

def matvec(M,v):return [sum(x*y for x,y in zip(row,v)) for row in M]
def coeff():
 A=[(1+LAM)/3,(1-LAM)/3,F(1,3)]; B=[(1-LAM/2)/3,(1+LAM/2)/3,F(1,3)]
 out=[[F(0)]*5 for _ in range(50)]; ds={(0,1):1,(1,2):2,(0,2):3}
 for offset,weights in [(0,A),(35,B)]:
  for k,(i,j) in enumerate(PAIRS):
   r,s=i//2,j//2
   if r==s:out[offset+k][0]=weights[r]**2
   else:
    w=weights[r]*weights[s]/2
    out[offset+k][0]=w;out[offset+k][ds[r,s]]=-(-1)**(i%2+j%2)*w
 for k,M in enumerate(TRIPLES):
  rs=[i//2 for i in M]
  if len(set(rs))==2:
   r=next(x for x in rs if rs.count(x)==2);s=next(x for x in rs if rs.count(x)==1);t=3-r-s
   out[15+k][0]=A[r]*B[t]
  else:
   sig=[(-1)**(i%2) for i in M]
   out[15+k]=[F(3-LAM*LAM,36),-(1-LAM*LAM)*sig[0]*sig[1]/36,-(1-LAM)*sig[1]*sig[2]/36,-(1+LAM)*sig[0]*sig[2]/36,DEL*prod(sig)/36]
 return out

def incidence(x):
 out=[F(0)]*50;h=[F(0)]*15
 for v,(a,b) in zip(x,ATOMS):
  out[PAIRS.index(a)]+=v;out[35+PAIRS.index(b)]+=v
  J=tuple(sorted(set(E)-set(a)-set(b)));h[PAIRS.index(J)]+=v
  for j in J:out[15+TRIPLES.index(tuple(sorted(a+(j,))))]+=v
 return out,h

def physical(v):
 C,a,b,c,e=v
 if C<abs(a):return False
 A=a*a+3*e*e;B=2*(C*a-b*c);Z=C*C-b*b-c*c-3*e*e
 vals=[A-B+Z,A+B+Z]
 if A and -2*A<=B<=2*A:vals.append(Z-B*B/(4*A))
 return min(vals)>=0

def normalized(v):
 scale=lcm(*(x.denominator for x in v));out=[int(x*scale) for x in v];g=gcd(*out)
 return tuple(x//g for x in out)

def constraints():
 cons=[]
 for i in range(3):
  for sg in [-1,1]:
   v=[F(1)]+[F(0)]*4;v[i+1]=F(sg);cons.append(tuple(v))
 for eps in product([-1,1],repeat=3):
  if prod(eps)!=1:continue
  cons.append((F(3,2),F(eps[0]),F(eps[1]),F(eps[2]),F(0)))
  for sg in [-1,1]:
   cons.append((3-LAM*LAM,-(1-LAM*LAM)*eps[0],-(1-LAM)*eps[1],-(1+LAM)*eps[2],sg*DEL))
   cons.append((3+LAM*LAM/2,(1+LAM*LAM/2)*eps[0],(1+2*LAM)*eps[1],-(1-2*LAM)*eps[2],sg*DEL))
 for sg in [-1,1]:cons.append((F(7,4),F(0),F(0),F(0),F(sg)))
 assert len(cons)==28
 return cons

CP=list(combinations(range(4),2))
def det4(M):
 s=0
 for i,j in CP:
  k,l=[z for z in range(4) if z not in (i,j)]
  s+=(-1)**(i+j+1)*(M[0][i]*M[1][j]-M[0][j]*M[1][i])*(M[2][k]*M[3][l]-M[2][l]*M[3][k])
 return s

def exact_vertices(cons):
 # Integer Cramer's rule; no floating point geometry or feasibility calls.
 rows=[normalized(v) for v in cons]
 HH=[[-x for x in v[1:]] for v in rows];kk=[v[0] for v in rows]
 vertices=set();nonsingular=0
 for ix in combinations(range(len(cons)),4):
  M=[HH[j] for j in ix];rhs=[kk[j] for j in ix];d=det4(M)
  if not d:continue
  nonsingular+=1;nums=[]
  for col in range(4):
   R=[list(row) for row in M]
   for rr in range(4):R[rr][col]=rhs[rr]
   nums.append(det4(R))
  if d<0:d=-d;nums=[-x for x in nums]
  if all(sum(a*b for a,b in zip(h,nums))<=k*d for h,k in zip(HH,kk)):
   vertices.add(tuple(F(x,d) for x in nums))
 return vertices,nonsingular

def signs(p):
 for sg in product([-1,1],repeat=3):
  yield (p[0]*sg[0]*sg[1],p[1]*sg[1]*sg[2],p[2]*sg[0]*sg[2],p[3]*prod(sg)),sg

def interpolate(p,vs,xs,cons):
 # Fixed vertex order, fixed inequality order; every operation is rational.
 def rec(p,indices):
  m=F(len(indices));q=tuple(sum(vs[j][k] for j in indices)/m for k in range(4))
  xb=[sum(xs[j][k] for j in indices)/m for k in range(90)]
  if p==q:return xb,0
  u=tuple(a-b for a,b in zip(p,q));candidates=[]
  for i,v in enumerate(cons):
   den=-sum(v[k+1]*u[k] for k in range(4))
   if den>0:candidates.append((sum(v[k]*([F(1)]+list(q))[k] for k in range(5))/den,i))
  rho,i=min(candidates);assert rho>=1
  pp=tuple(q[k]+rho*u[k] for k in range(4))
  selected=[j for j in indices if sum(cons[i][k]*([F(1)]+list(vs[j]))[k] for k in range(5))==0]
  assert selected and len(selected)<len(indices)
  xx,steps=rec(pp,selected)
  return [(1-1/rho)*b+y/rho for b,y in zip(xb,xx)],steps+1
 assert all(sum(a*b for a,b in zip(v,[F(1),*p]))>=0 for v in cons)
 return rec(p,list(range(len(vs))))

# Exact arithmetic in Q(sqrt(-3)); normalized Q itself is tildeQ/sqrt(3).
def add(x,y):return(x[0]+y[0],x[1]+y[1])
def neg(x):return(-x[0],-x[1])
def mul(x,y):return(x[0]*y[0]-3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x):return(x[0],-x[1])
def ab2(x):return x[0]*x[0]+3*x[1]*x[1]
Z=(F(0),F(0));ONE=(F(1),F(0));OM=(F(-1,2),F(1,2))
def det(M):
 n=len(M)
 if not n:return ONE
 ans=Z
 for j in range(n):
  val=mul(M[0][j],det([[M[r][s] for s in range(n) if s!=j] for r in range(1,n)]))
  ans=add(ans,neg(val) if j%2 else val)
 return ans

def exact_example():
 c=F(99,101);s=F(20,101)
 sc=[[(c+s,F(0)),add((c,F(0)),mul((s,F(0)),OM)),add((c,F(0)),mul((s,F(0)),conj(OM)))],[(c-s,F(0)),add((-s,F(0)),mul((c,F(0)),OM)),add((-s,F(0)),mul((c,F(0)),conj(OM)))],[ONE,conj(OM),OM]]
 V=[[[ONE,Z],[Z,ONE]], [[(F(3,5),F(0)),(F(4,5),F(0))],[(F(-4,5),F(0)),(F(3,5),F(0))]], [[(F(5,13),F(0)),mul((F(12,13),F(0)),OM)],[neg(mul((F(12,13),F(0)),conj(OM))),(F(5,13),F(0))]]]
 Q=[[mul(sc[r][block],V[r][sigma][column]) for block in range(3) for column in range(2)] for r in range(3) for sigma in range(2)]
 for j in range(6):
  for k in range(6):
   z=Z
   for i in range(6):z=add(z,mul(conj(Q[i][j]),Q[i][k]))
   assert z==((F(3),F(0)) if j==k else Z)
 minors={}
 def mn(rows,cols):return det([[Q[i][j] for j in cols] for i in rows])
 vals=[]
 for pair in PAIRS:vals.append(ab2(mn(pair,[0,1]))/9)
 for triple in TRIPLES:vals.append((ab2(mn(triple,[0,1,2]))+ab2(mn(triple,[0,1,3])))/27)
 for pair in PAIRS:vals.append(ab2(mn(pair,[4,5]))/9)
 p=(F(-7,25),F(-607,4225),F(-119,169),F(-864,845))
 assert vals==matvec(coeff(),[F(1),*p])
 signed=[]
 for a,b in ATOMS:
  J=tuple(sorted(set(E)-set(a)-set(b)));top=tuple(sorted(set(E)-set(b)))
  sg=(-1)**sum(i>j for i in a for j in J)
  signed.append(F(sg)*mul(mul(mn(a,[0,1]),mn(J,[2,3])),conj(mn(top,[0,1,2,3])))[0]/81)
 assert incidence(signed)[0]==vals
 return p,Q,vals,signed

if __name__=='__main__':
 start=time.monotonic();data=json.load(open(BASE/'certificate.json'))
 T=coeff();assert T==[[F(x) for x in row] for row in data['coeff']]
 cons=constraints();given=[tuple(F(x) for x in data['constraints'][i]) for i in data['keep']]
 assert {normalized(v) for v in cons}=={normalized(v) for v in given}
 assert all(physical(v) for v in cons)
 vs=[tuple(F(x) for x in p) for p in data['vertices']];xs=[]
 for p,x in zip(vs,data['couplings']):
  full=[F(x.get(str(j),'0')) for j in range(90)]
  assert min(full)>=0 and sum(full)==1
  marg,h=incidence(full);target=matvec(T,[F(1),*p]);assert marg==target and h==target[35:]
  xs.append(full)
 print('Exact rational couplings:',len(vs),flush=True)
 actual,nonsingular=exact_vertices(cons)
 assert actual==set(vs)
 print('Exact exhaustive intersections: 20475; nonsingular:',nonsingular,'vertices:',len(actual),flush=True)
 remaining=set(vs);orbits=[]
 while remaining:
  p=min(remaining);orb={v for v,sg in signs(p)};assert orb<=set(vs)
  orbits.append((p,len(orb)));remaining-=orb
 p,Q,vals,signed=exact_example()
 x,steps=interpolate(p,vs,xs,cons);assert min(x)>0 and incidence(x)[0]==vals and sum(x)==1
 assert steps<=4
 out={'status':'PASS','couplings':len(vs),'marginal_equations':50*len(vs),'added_pair_equations':15*len(vs),'constraints':len(cons),'exact_intersections':20475,'nonsingular_intersections':nonsingular,'vertices':len(vs),'sign_orbits':len(orbits),'example':{'parameters':[str(z) for z in p],'Q_tilde':[[[str(a),str(b)] for a,b in row] for row in Q],'probabilities':[str(z) for z in vals],'coupling':[str(z) for z in x],'signed_exterior':[str(z) for z in signed],'minimum_probability':str(min(vals)),'minimum_coupling':str(min(x)),'negative_signed_weights':sum(z<0 for z in signed),'minimum_signed_weight':str(min(signed)),'interpolation_steps':steps},'vertex_orbits':[{'representative':[str(x) for x in p],'size':size} for p,size in orbits],'elapsed_seconds':time.monotonic()-start}
 json.dump(out,open(BASE/'verified_output.json','w'),indent=2)
 print(json.dumps({k:v for k,v in out.items() if k not in ['example','vertex_orbits']}),flush=True)
 print('Example minimum probability:',min(vals),'minimum positive coupling:',min(x),'negative signed weights:',sum(z<0 for z in signed),'minimum signed weight:',min(signed),'interpolation steps:',steps,flush=True)
