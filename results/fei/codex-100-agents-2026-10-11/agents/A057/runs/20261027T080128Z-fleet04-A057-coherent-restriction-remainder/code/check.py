from fractions import Fraction as Q
from pathlib import Path
from itertools import combinations
from functools import lru_cache
import json,time,sys
R=Path(__file__).resolve().parents[1]; start=time.perf_counter(); count=0

def ck(x):
 global count
 assert x
 count+=1

def tak(p,L=4):
 s=Q(0)
 for k in range(L):
  z=2**k*p; f=z-z.numerator//z.denominator
  s+=min(f,1-f)/2**k
 return s
B=[Q(k,16) for k in range(17)]
lines=[(1,0,v) for v in B]+[(0,1,v) for v in B]+[(1,1,2*v) for v in B]+[(1,-1,Q(0))]
verts=set()
for (a,b,c),(d,e,f) in combinations(lines,2):
 det=a*e-b*d
 if det:
  x=(c*e-b*f)/det;y=(a*f-c*d)/det
  if 0<=x<=1 and 0<=y<=1:verts.add((x,y))
vc=[]
for x,y in sorted(verts):
 gap=(tak(x)+tak(y)+abs(x-y))/2-tak((x+y)/2);ck(gap>=0)
 vc.append([str(x),str(y),str(gap)])
(R/'out/BOUNDARY_VERTICES.json').write_text(json.dumps(vc,indent=2),encoding='utf-8')
@lru_cache(None)
def ln(q):
 assert q>0
 e=q.numerator.bit_length()-q.denominator.bit_length();y=q/Q(2)**e
 if y<1:e-=1;y*=2
 z=(y-1)/(y+1);assert 0<=z<=Q(1,3)
 s=Q(0);power=z
 for k in range(70):s+=2*power/(2*k+1);power*=z*z
 tail=2*power/(141*(1-z*z))
 if e:
  l,u=ln(Q(2)) if q!=2 else (None,None)
  # ln2 is handled without recursively calling itself.
  if q==2:
   z=Q(1,3);s=Q(0);power=z
   for k in range(70):s+=2*power/(2*k+1);power*=z*z
   return s,s+2*power/(141*(1-z*z))
  return (s+e*l,s+tail+e*u) if e>=0 else (s+e*u,s+tail+e*l)
 return s,s+tail
def outward(t):
 scale=1<<192;l,u=t
 return Q((l*scale).numerator//(l*scale).denominator,scale),Q(-((-u*scale).numerator//(-u*scale).denominator),scale)
@lru_cache(None)
def log(q):
 l,u=ln(q);a,b=ln(Q(2))
 return outward((l/b,u/a) if l>=0 else (l/a,u/b) if u<=0 else (l/a,u/a))
def eta(q):
 if q==0:return Q(0),Q(0)
 l,u=log(q);return -q*u,-q*l
C=Q(41,20);l2,u2=ln(Q(2));jcoef=2/l2
# p<=1/8: concavity with endpoints and classical edge isoperimetry.
p=Q(1,8);hh=eta(p)[1]+eta(1-p)[1]
small_margin=C*p*4-hh-jcoef*p;ck(small_margin>0);ck(C>2)
rows=[]
for j in range(128,512):
 a=Q(j,1024);b=Q(j+1,1024);m=(a+b)/2
 lr=log(m)[0];ls=log(1-m)[0]
 # Cross-entropy is an affine upper bound for binary entropy on the entire cell.
 def upper(p):return -p*lr-(1-p)*ls
 g1=[C*(p+tak(p))-upper(p)-jcoef*p for p in [a,b]]
 g2=[C*(p+tak(p))-upper(p)-1 for p in [a,b]]
 which=1 if min(g1)>=0 else 2
 gap=min(g1) if which==1 else min(g2);ck(gap>=0)
 rows.append(dict(a=str(a),b=str(b),logm_lower=str(lr),log1m_lower=str(ls),JS_cap=which,gap=str(gap)))
(R/'out/ENTROPY_CELLS.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
# Independent actual finite Boolean functions by direct character sums.
def spec(t):return tuple(Q(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t)))
def H(t):
 l=u=Q(0)
 for z in spec(t):
  a,b=eta(z*z);l+=a;u+=b
 return l,u
def inf(t):return sum((Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t)) for i in range((len(t)).bit_length()-1)),Q(0))
def child(t,i,bit):return tuple(t[(x&((1<<i)-1))|((x>>i)<<(i+1))|(bit<<i)] for x in range(len(t)//2))
maxratio=Q(0); functions=edges=0
for n in range(4):
 for mask in range(1<<(1<<n)):
  t=tuple(1 if mask>>x&1 else -1 for x in range(1<<n));functions+=1
  sp=spec(t);I=inf(t);h=H(t)
  ck(sum((a*a for a in sp),Q(0))==1)
  ck(sum((a*a*s.bit_count() for s,a in enumerate(sp)),Q(0))==I)
  density=Q(t.count(-1),len(t));ck(I/2>=tak(density))
  for i in range(n):
   edges+=1;t0=child(t,i,0);t1=child(t,i,1);h0=H(t0);h1=H(t1);p=Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t))),len(t))
   dl=h[0]-(h0[1]+h1[1])/2;du=h[1]-(h0[0]+h1[0])/2
   ck((inf(t0)+inf(t1))/2==I-p)
   ck(du<=C*I)
   # Two tickets + reserve, each new query consumes one; no renewal.
   ck(Q(9,2)==2*C+Q(2,5));ck(C*I-du>=0)
   for t1x in [t0,t1]:
    for k in range(n-1):
     aa=H(child(t1x,k,0));bb=H(child(t1x,k,1));dx=H(t1x)[1]-(aa[0]+bb[0])/2
     ck(dx<=C*inf(t1x))
   if I:maxratio=max(maxratio,du/I)
# Float-free imported A091 finite seed recurrence, independently simplified.
m=Q(0);Il=Q(1);Hl=Hu=Q(0)
def addint(*args):return sum((x[0] for x in args),Q(0)),sum((x[1] for x in args),Q(0))
def scale(c,t):return (c*t[0],c*t[1]) if c>=0 else (c*t[1],c*t[0])
seedrows=[]
for d in range(6):
 seedrows.append(dict(depth=d,mean=str(m),I=str(Il),H=[str(Hl),str(Hu)]))
 if d==5:break
 v=1-m*m;a=(1+m)/2;mn=(1-2*m-m*m)/2
 em=eta(m*m);En=(Hl-em[1],Hu-em[0])
 # Combined coefficient of child nonempty entropy is 1+m.
 Hl,Hu=addint(eta(mn*mn),scale(1+m,En),scale(2*v,eta(a*a)),(v*v/2,v*v/2))
 Il=(1+m)*Il;m=mn
ck(Hl-Q(9,2)*Il>Q(1,10))
ck(Q(128)*(Hl-Q(9,2)*Il)-7-Q(9,32)>Q(883,160))
result=dict(status='PASS',checks=count,functions=functions,coordinates=edges,boundary_vertices=len(verts),entropy_cells=len(rows),ticket='41/20',two_ticket_reserve='2/5',small_endpoint_margin=str(small_margin),max_finite_ratio_upper=str(maxratio),seed=seedrows[-1],seed_margin_lower=str(Hl-Q(9,2)*Il),seconds=time.perf_counter()-start)
(R/'out/CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps({k:result[k] for k in ['status','checks','functions','coordinates','boundary_vertices','entropy_cells','seconds']}))
