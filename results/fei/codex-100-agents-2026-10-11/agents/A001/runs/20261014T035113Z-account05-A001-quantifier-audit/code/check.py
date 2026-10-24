from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,sys,time
RUN=Path(__file__).resolve().parents[1];spec=json.loads((RUN/'out/FROZEN_SPEC.json').read_text())
count=0
def ck(x):
 global count
 count+=1;assert x,count
@lru_cache(None)
def factors(n):
 out={};d=2
 while d*d<=n:
  while n%d==0:out[d]=out.get(d,0)+1;n//=d
  d=3 if d==2 else d+2
 if n>1:out[n]=out.get(n,0)+1
 return out
@lru_cache(None)
def lg(q):
 q=F(q);out=factors(q.numerator).copy()
 for p,e in factors(q.denominator).items():out[p]=out.get(p,0)-e
 return {p:F(v) for p,v in out.items() if v}
def add(*items):
 out={}
 for a,d in items:
  for p,c in d.items():out[p]=out.get(p,F(0))+a*c
 return {p:c for p,c in out.items() if c}
def kl(mu,q):return add(*[(a,lg(a/b)) for a,b in zip(mu,q) if a])
def ln_unit(q):
 z=(q-1)/(q+1);low=2*sum((z**(2*j+1)/F(2*j+1) for j in range(24)),F(0))
 return low,low+2*z**49/(49*(1-z*z))
LN2=ln_unit(F(2))
@lru_cache(None)
def log_interval(q):
 q=F(q);k=0
 while q<1:q*=2;k-=1
 while q>=2:q/=2;k+=1
 lo,hi=ln_unit(q);corners=[x/y+k for x in (lo,hi) for y in LN2];grid=1<<70
 a=min(corners)*grid;b=max(corners)*grid
 return F(a.numerator//a.denominator,grid),F(-((-b.numerator)//b.denominator),grid)
def enclosure(d):
 lo=hi=F(0)
 for p,c in d.items():
  a,b=log_interval(p)
  if c<0:a,b=b,a
  lo+=c*a;hi+=c*b
 return lo,hi
def walsh(a):
 a=a[:];step=1
 while step<len(a):
  for b in range(0,len(a),2*step):
   for j in range(b,b+step):
    u,v=a[j],a[j+step];a[j],a[j+step]=u+v,u-v
  step*=2
 return a
def parameters(d,r):
 delta=F(1,1<<d);t=F(1,1<<(d//2));alpha=F(1,1<<r);w=4*alpha*alpha;e=delta/2
 A=1-delta+2*delta*alpha*alpha
 R=[1+2*s*t*(alpha-1)+delta*((alpha-1)**2+alpha*alpha) for s in (1,-1)]
 weights=[F(1,2)+t/2,F(1,2)-t/2]
 return delta,t,alpha,w,e,A,R,weights
mode=sys.argv[1];t0=time.perf_counter();rows=[]
if mode=='physical':
 for d,r in spec['truth_table_domain']:
  delta,t,alpha,w,e,A,R,weights=parameters(d,r);N=d+2*r;size=1<<N
  def bent(y):return (-1)**sum(((y>>(2*j))&1)*((y>>(2*j+1))&1) for j in range(d//2))
  vals=[]
  for x in range(size):
   y=x&((1<<d)-1);s=x>>d
   q=(-1)**sum(((s>>(2*j))&3)==3 for j in range(r))
   vals.append(bent(y) if y else q)
  fw=walsh(vals);p=[F(c*c,size*size) for c in fw];ck(sum(p)==1);ck(all(a>0 for a in p))
  bw=walsh([bent(y) for y in range(1<<d)]);qw=walsh([(-1)**sum(((s>>(2*j))&3)==3 for j in range(r)) for s in range(1<<(2*r))])
  ck(all(abs(c)==1<<r for c in qw));ck(all(abs(c)==1<<(d//2) for c in bw))
  for s,c in enumerate(fw):
   y=s&((1<<d)-1);sel=s>>d
   expected=F(bw[y],1<<d)+delta*(alpha-1) if not sel else delta*F(qw[sel],1<<(2*r))
   ck(F(c,size)==expected)
  Dy=add(*[(a,lg(A/b)) for a,b in zip(weights,R)])
  z=A/(1-e);D0=add((1,kl([w,1-w],[z,1-z])),(w,Dy))
  Dbin=kl([F(1,2)]*2,[1-e,e]);selector_M4={};totalL4={}
  all_e=[]
  for i in range(N):
   bit=1<<i;lower=[s for s in range(size) if not s&bit]
   ei=sum(p[s|bit] for s in lower);physical=F(sum(vals[x]!=vals[x^bit] for x in range(size)),size)
   ck(ei==physical);ck(ei==(F(1,2)+delta*(1-alpha) if i<d else e));all_e.append(ei)
   mu=[p[s|bit]/ei for s in lower];ref=[p[s]+p[s|bit] for s in lower]
   ck(sum(mu)==sum(ref)==1)
   if i<d:continue
   partner=d+((i-d)^1);spectmask=((1<<N)-1)^((1<<d)-1)^(1<<i)^(1<<partner)
   mb=[F(0)]*2;rb=[F(0)]*2;m4=[F(0)]*4;r4=[F(0)]*4
   for s,a,b in zip(lower,mu,ref):
    v=(s>>partner)&1;j=2*v+int(bool(s&spectmask))
    mb[v]+=a;rb[v]+=b;m4[j]+=a;r4[j]+=b
   ck(mb==[F(1,2)]*2);ck(rb==[1-e,e])
   ck(m4==[w/2,(1-w)/2,w/2,(1-w)/2]);ck(r4==[A,e*(1-w),e*w,e*(1-w)])
   D=kl(mu,ref);DB=kl(mb,rb);D4=kl(m4,r4)
   ck(D==add((1,DB),(F(1,2),D0)))
   ck(add((1,D),(-1,D4))==add((w/2,Dy)))
   M4=add((ei,lg(1/ei)),(-ei,D4));L4=add((ei,D),(-ei,D4))
   expectedM4=add((ei*(1+w*F(d+2*r-1,2)),{2:F(1)}),(ei*w/2,lg(A)))
   ck(M4==expectedM4)
   selector_M4=add((1,selector_M4),(1,M4));totalL4=add((1,totalL4),(1,L4))
  I=sum(all_e);owner=all_e[0];J=r*delta
  ck(I==F(d,2)+d*delta*(1-alpha)+J)
  ck(totalL4==add((r*delta*w/2,Dy)))
  ck(selector_M4==add((J*(1+w*F(d+2*r-1,2)),{2:F(1)}),(J*w/2,lg(A))))
  loss=enclosure(totalL4);ck(loss[0]>0);ck(loss[1]<owner/2)
  budget=enclosure(add((1,selector_M4),(1,totalL4),(-J,{2:F(1)})))
  ck(budget[1]<F(3,2)*owner)
  H=add(*[(a,lg(1/a)) for a in p]);ck(enclosure(H)[1]<=4*I)
  ck(3*R[0]-A==2*(1-t)*(1-2*t)+6*t*(1-t)*alpha+4*t*t*alpha*alpha)
  if r>=2:
   ck(enclosure(D0)[0]>=F(3*d,4)-1)
  rows.append(dict(d=d,r=r,N=N,I=str(I),four_cell_loss_interval=[str(v) for v in loss],owner_influence=str(owner),combined_extra_interval=[str(v) for v in budget],status='PASS'))
 ck(len(rows)==9)
elif mode=='symbolic':
 for d in spec['symbolic_domain']['d']:
  for r in (1,2,4,1<<d):
   delta,t,alpha,w,e,A,R,weights=parameters(d,r);owner=F(1,2)+delta*(1-alpha)
   ck(A>0);ck(R[0]>0);ck(sum(a*b for a,b in zip(weights,R))==A)
   ck(3*R[0]-A==2*(1-t)*(1-2*t)+6*t*(1-t)*alpha+4*t*t*alpha*alpha);ck(A<=3*R[0]);ck(A<=3*R[1])
   ck(r*w<=1);ck(r*r*w<=1);ck(delta*(F(d,2)+2)<=F(3,4));ck(F(3,4)<=F(3,2)*owner)
   ck(delta<=owner/2)
   cells=[A,e*(1-w),e*w,e*(1-w)];ck(sum(cells)==1)
   if r>=2:
    ck(w<=F(1,4));ck((1-e)/e>=1<<d)
   if r==1<<d:
    ck(r*delta==1)
   rows.append(dict(d=d,r=r,binary_total_loss_at_least=str(r*delta*(F(3*d,8)-F(1,2))) if r>=2 else 'not asserted',four_cell_total_loss_less_than=str(delta),combined_extra_less_than=str(F(3,2)*owner),all_normalizers='1',status='PASS'))
 ck(len(rows)==16)
else:raise ValueError(mode)
result=dict(status='PASS',mode=mode,cases=len(rows),assertions=count,failures=0,runtime_seconds=time.perf_counter()-t0,rows=rows,arithmetic='Integer/Fraction prime-log identities; outward intervals or exact polynomial bounds',full_FEI='OPEN')
(RUN/('out/'+mode.upper()+'.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
