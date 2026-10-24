from fractions import Fraction as Q
from itertools import product,combinations
from functools import lru_cache
from pathlib import Path
import json,time
root=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def ck(x):
 global checks
 assert x
 checks+=1
@lru_cache(None)
def ln(x):
 k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def s(x):
  t=(x-1)/(x+1);a=2*sum((t**(2*j+1)/Q(2*j+1) for j in range(24)),Q(0))
  return a,a+2*t**49/(49*(1-t*t))
 a,b=s(x);l,u=s(Q(2))
 return (a+k*l,b+k*u) if k>=0 else (a+k*u,b+k*l)
def H(x):
 if not x:return Q(0),Q(0)
 l,u=ln(1/(x*x));return x*x*l,x*x*u
def add(terms):return tuple(sum((a*b[i] for a,b in terms),Q(0)) for i in (0,1))
def ent(P,W,pred=lambda s:True):return add([(W[s],H(c)) for s,c in P.items() if s and pred(s)])
def table(mask):return {x:Q(1 if (mask>>sum(a<<i for i,a in enumerate(x)))&1 else -1) for x in product((0,1),repeat=4)}
def spectrum(T,p):
 c={};W={};P={}
 for s in range(16):
  m=Q(0);den=Q(1);w=Q(1)
  for i in range(4):
   if s>>i&1:den*=p[i]*(1-p[i]);w*=4*p[i]*(1-p[i])
  for x,f in T.items():
   a=f
   for i in range(4):
    a*=p[i] if x[i] else 1-p[i]
    if s>>i&1:a*=x[i]-p[i]
   m+=a
  c[s]=m/(2**s.bit_count()*den);W[s]=w;P[s]=m*m/den
 ck(sum(P.values())==1)
 I=sum(s.bit_count()*P[s] for s in P);V=sum(P[s] for s in P if s);D=I-V
 physical=Q(0)
 for i in range(4):
  val=Q(0)
  for x in product((0,1),repeat=3):
   a=list(x);a.insert(i,0);b=a.copy();b[i]=1
   mass=Q(1)
   for j in range(4):
    if j!=i:mass*=p[j] if a[j] else 1-p[j]
   val+=mass*((T[tuple(b)]-T[tuple(a)])/2)**2
  physical+=4*p[i]*(1-p[i])*val
 ck(physical==I)
 return c,W,D,P
T=table(56067)
for a,b,c,z in T:ck(T[a,b,c,z]==1-2*b-2*c+2*b*c+2*z*c+2*z*a*b-2*z*a*c)
reflected={(a,x,y,z):T[a,1-x,1-y,z] for a,x,y,z in T}
components=[{x:Q(1 if (x[0] and x[1] and x[3]) else -1) for x in T},{x:Q(1 if (not x[0] and x[2] and x[3]) else -1) for x in T},{x:Q(1 if (not x[1] and not x[2]) else -1) for x in T}]
for x in T:ck(T[x]==sum(A[x] for A in components)+2)
rows={}
for size in (2,3):
 for B in combinations(range(4),size):
  O=[i for i in range(4) if i not in B];rs=set()
  for b in product((0,1),repeat=size):
   row=[]
   for o in product((0,1),repeat=4-size):
    x=[0]*4
    for j,i in enumerate(B):x[i]=b[j]
    for j,i in enumerate(O):x[i]=o[j]
    row.append(T[tuple(x)])
   rs.add(tuple(row))
  ck(len(rs)>2);rows[str(B)]=len(rs)
ck(all(any(T[x]!=T[tuple(v^(i==j) for j,v in enumerate(x))] for x in T) for i in range(4)))
l2,u2=ln(Q(2))
def coherent(alpha,q,e,d):
 c,W,D,P=spectrum(reflected,[alpha,e,d,q]);u=4*alpha*(1-alpha);w=4*q*(1-q);vx=4*e*(1-e);vy=4*d*(1-d)
 expected={1:q*(d-e),2:d-q*alpha,4:e-q*(1-alpha),8:1-alpha*e-(1-alpha)*d,3:-q/2,5:q/2,9:(d-e)/2,6:Q(1,2),10:-alpha/2,12:-(1-alpha)/2,11:-Q(1,4),13:Q(1,4)}
 for s in range(1,16):ck(c[s]==expected.get(s,0))
 Le=4*alpha*q*(2-alpha-q);Ld=4*(1-alpha)*q*(1+alpha-q)
 ck(D==Le*e*(1-e)+Ld*d*(1-d)+u*w*(d-e)**2/4+4*e*d*(1-e)*(1-d))
 Ke=add([(2*w*alpha,(Q(1),Q(1))),(4,H(q*alpha)),(4*u,H(q/2)),(4*w,H(alpha/2)),(u*w/4,(4*l2,4*u2))])
 la,ua=ln(1/alpha);lq,uq=ln(1/q)
 R=(2*l2+2*((1-q)+q*lq+alpha*la)/(2-alpha-q),2*u2+2*((1-q)+q*uq+alpha*ua)/(2-alpha-q))
 ck(max(Ke[0]/Le,R[0])<=min(Ke[1]/Le,R[1]));ck(R[1]<4+2*l2)
 return c,W,D,ent(c,W)
general=0
for p in product((Q(1,4),Q(1,2),Q(3,4)),repeat=4):
 c,W,D,P=spectrum(T,p);ds=[spectrum(A,p)[2] for A in components]
 a,b,c0,z=p;loss=2*(4*a*(1-a))*b*c0*z*(1-z)
 ck(D-sum(ds)==-loss)
 coherent(a,z,1-b,1-c0);general+=1
face=[]
for alpha,q in product((Q(1,4),Q(1,2),Q(3,4)),repeat=2):
 for e,d in ((Q(1,64),Q(1,128)),(Q(1,128),Q(1,64)),(Q(1,64),Q(1,64)),(Q(1,1024),Q(1,32768))):
  c,W,D,E=coherent(alpha,q,e,d);ck(E[1]<(4+2*l2)*D)
  face.append({'alpha':str(alpha),'q':str(q),'e':str(e),'d':str(d)})
slice_cases=0
for k in range(1,9):
 e=Q(1,2**k);r=1-e;c,W,D,E=coherent(Q(1,2),Q(1,2),e,e)
 ck(D==2*r*e*(1+2*r*e));L=r*r/2
 A=add([(1,H(r)),(8*r*e,H(Q(1,4)-e)),(Q(3,2)*r*e,(4*l2,4*u2)),(4*r*r*e*e,(2*l2,2*u2))])
 ck(max(A[0],E[0])<=min(A[1],E[1]));ck(E[1]<=(1+4*l2)*D)
 hi=ent(c,W,lambda s:s.bit_count()>=2);ck(hi[1]<=3*l2*D)
 if e<=Q(1,4):ck(L/D>=1/(8*e))
 slice_cases+=1
path=[]
def outward(v):
 scale=10**9
 return [str(Q((v[0]*scale).__floor__(),scale)),str(Q((v[1]*scale).__ceil__(),scale))]
for k in range(2,10):
 t=Q(1,2**k);c,W,D,E=coherent(1-t*t,1-t,t**6,t**8)
 path.append({'t':str(t),'D_over_t7':str(D/t**7),'ratio_bits':outward((E[0]/D/u2,E[1]/D/l2))})
out={'helper_version':'A042-coherent-face-v1','assertions_passed':checks,'general_cases':general,'two_rate_cases':len(face),'slice_cases':slice_cases,'corner_path_cases':len(path),'prime_row_counts':rows,'corner_path':path,'runtime_seconds':time.monotonic()-start,'continuum_proof':'PROOF.md; finite fixtures validate exact formulas only'}
(root/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='corner_path'},indent=2))
