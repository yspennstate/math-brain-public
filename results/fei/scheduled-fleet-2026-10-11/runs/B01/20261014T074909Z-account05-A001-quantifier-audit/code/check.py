from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys
RUN=Path(__file__).resolve().parents[1]
spec=json.loads((RUN/'out/FROZEN_SPEC.json').read_text())
count=0
def ck(x):
 global count
 count+=1
 assert x,count
def fw(a):
 a=list(a);k=1
 while k<len(a):
  for o in range(0,len(a),2*k):
   for j in range(o,o+k):
    u,v=a[j],a[j+k];a[j],a[j+k]=u+v,u-v
  k*=2
 return a
@lru_cache(None)
def factors(n):
 ans={};j=2
 while j*j<=n:
  while n%j==0:ans[j]=ans.get(j,0)+1;n//=j
  j=3 if j==2 else j+2
 if n>1:ans[n]=ans.get(n,0)+1
 return ans
def log(q):
 q=F(q);a=factors(q.numerator).copy()
 for p,v in factors(q.denominator).items():a[p]=a.get(p,0)-v
 return {p:F(v) for p,v in a.items() if v}
def add(*terms):
 a={}
 for c,d in terms:
  for p,v in d.items():a[p]=a.get(p,F(0))+c*v
 return {p:v for p,v in a.items() if v}
def const(q):return {2:F(q)} if q else {}
def eta(q):return add((-q,log(q))) if q else {}
def entropy(p):return add(*[(1,eta(q)) for q in p])
def phi(a,b):return add((1,eta(a)),(1,eta(b)),(-1,eta(a+b)))
def lnunit(q):
 z=(q-1)/(q+1)
 lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
 return lo,lo+2*z**65/(65*(1-z*z))
LN2=lnunit(F(2))
@lru_cache(None)
def lint(q):
 q=F(q);k=0
 while q<1:q*=2;k-=1
 while q>=2:q/=2;k+=1
 lo,hi=lnunit(q);lo=lo/LN2[1]+k;hi=hi/LN2[0]+k;g=1<<90
 return F((lo*g).numerator//(lo*g).denominator,g),F(-((-hi*g).numerator//(-hi*g).denominator),g)
def interval(d):
 lo=hi=F(0)
 for p,c in d.items():
  a,b=lint(p)
  if c<0:a,b=b,a
  lo+=c*a;hi+=c*b
 return lo,hi
def enc(d):return {str(p):str(c) for p,c in sorted(d.items())}
def record(d):return dict(prime_log=enc(d),interval=[str(x) for x in interval(d)])
def amplitudes(v):return [F(x,len(v)) for x in fw(v)]
def spectrum(v):return [a*a for a in amplitudes(v)]
def inf(v,j):return F(sum(v[x]!=v[x^(1<<j)] for x in range(len(v))),len(v))
def totalinf(v):return sum((inf(v,j) for j in range(len(v).bit_length()-1)),F(0))
def erase(v,j):
 p=spectrum(v);return add(*[(1,phi(p[t],p[t|(1<<j)])) for t in range(len(v)) if not t&(1<<j)])
def insert(t,j,s):return (t&((1<<j)-1))|((t>>j)<<(j+1))|(s<<j)
def restrict(v,j,s):return [v[insert(t,j,s)] for t in range(len(v)//2)]
def transport(v,j,s):
 a=amplitudes(v);child=restrict(v,j,s);ac=amplitudes(child)
 for t,x in enumerate(ac):
  u=insert(t,j,0);ck(x==a[u]+((-1)**s)*a[u|(1<<j)])
 ck(sum(x*x for x in ac)==1)
 return child
def tree(v,coordinates):
 if not coordinates:return {},entropy(spectrum(v)),totalinf(v)
 j=coordinates[0];children=[transport(v,j,s) for s in (0,1)]
 rest=[k-int(k>j) for k in coordinates[1:]]
 sub=[tree(c,rest) for c in children]
 bill=add((1,erase(v,j)),*[(F(1,2),z[0]) for z in sub])
 terminal=add(*[(F(1,2),z[1]) for z in sub])
 ti=sum((z[2]/2 for z in sub),F(0))
 ck(totalinf(v)==inf(v,j)+sum(totalinf(c)/2 for c in children))
 return bill,terminal,ti
def selector(b,c):return [b[y] if s==0 else c[y] for y in range(len(b)) for s in (0,1)]
def encoded(b,c):
 out=[]
 for y in range(len(b)):
  for x in range(8):out.append(b[y] if x.bit_count()<=1 else c[y])
 return out
def majbill(b,c):
 ba,ca=amplitudes(b),amplitudes(c);terms=[]
 for u,v in zip(ba,ca):
  A=(u+v)/2;D=(u-v)/2
  terms.extend([(1,phi(A*A,D*D/4)),(F(1,2),phi((A+D/2)**2,D*D/4)),(F(1,2),phi((A-D/2)**2,D*D/4)),(1,const(D*D/2)),(F(1,2),phi(A*A,D*D))])
 return add(*terms)
start=time.perf_counter();b=[1 if y&7==0 else -1 for y in range(64)];c=b[:];c[0]=-1
delta=F(1,64);G=selector(b,c);root=encoded(b,c)
Hb,Hc=entropy(spectrum(b)),entropy(spectrum(c));Ib,Ic=totalinf(b),totalinf(c)
ck(Ib==Ic==F(3,4))
Hterm=add((F(1,2),Hb),(F(1,2),Hc))
S=add((1,const(4*(Ib+Ic)/2)),(-1,Hterm));Q=erase(G,0)
initial=add((1,Q),(1,const(delta)));remaining=add((1,S),(-1,initial))
ck(interval(remaining)[0]>0)
actualInitial,initialTerminal,initialLeafI=tree(root,[0,1,2])
ck(initialTerminal==Hterm);ck(initialLeafI==(Ib+Ic)/2)
ck(actualInitial==majbill(b,c))
initialInteraction=add((1,actualInitial),(-1,initial))
actualRemaining=add((1,S),(-1,actualInitial))
rows=[]
domain=[0] if '--pilot' in sys.argv else list(range(6))
for j in domain:
 ck(time.perf_counter()-start<55)
 bc=[transport(b,j,s) for s in (0,1)];cc=[transport(c,j,s) for s in (0,1)]
 actualchildren=[transport(root,j+3,s) for s in (0,1)]
 for z in (0,1):ck(actualchildren[z]==encoded(bc[z],cc[z]))
 Qchild=add(*[(F(1,2),erase(selector(bc[s],cc[s]),0)) for s in (0,1)])
 Bdata=erase(root,j+3);ck(Bdata==erase(G,j+1))
 ej=inf(root,j+3);ck(ej==(inf(b,j)+inf(c,j))/2)
 # Preserve the already booked delta encoder bill, rather than replace it by a fresh bank.
 childdelta=sum(F(sum(u!=v for u,v in zip(bc[s],cc[s])),len(bc[s]))/2 for s in (0,1));ck(childdelta==delta)
 proposed=add((1,Bdata),(1,Qchild),(1,const(delta)))
 direct,terminal,leafI=tree(root,[j+3,0,1,2])
 W=direct
 ck(W==add((1,Bdata),*[(F(1,2),majbill(bc[s],cc[s])) for s in (0,1)]))
 interaction=add((1,W),(-1,proposed))
 increment=add((1,W),(-1,initial))
 margin=add((1,remaining),(-1,increment));ck(margin==add((1,S),(-1,W)))
 mlo,mhi=interval(margin);ck(mlo>0 or mhi<0)
 leafH=add(*[(F(1,4),entropy(spectrum(v))) for v in bc+cc]);ck(terminal==leafH)
 avgdeltaH=add((1,Hterm),(-1,leafH));ck(interval(avgdeltaH)[0]>=0)
 completeMargin=add((1,const(4*(Ib+Ic)/2)),(-1,W),(-1,leafH))
 ck(completeMargin==add((1,margin),(1,avgdeltaH)))
 clo,chi=interval(completeMargin);ck(clo>0 or chi<0)
 # The actual new bank is recorded only as a diagnostic: it is never credited as fresh reserve.
 newS=add((1,const(4*leafI)),(-1,leafH))
 ck(newS==add((1,S),(-1,const(4*ej)),(1,avgdeltaH)))
 ck(leafI==(Ib+Ic)/2-ej)
 row=dict(query=j,type='active' if j<3 else 'dummy',physical_influence=str(ej),incoming_reserve=record(S),booked_initial=record(initial),remaining_initial=record(remaining),data_erasure=record(Bdata),transported_shadow=record(Qchild),signed_shadow_change=record(add((1,Qchild),(-1,Q))),encoder_interaction=record(interaction),increment=record(increment),same_bank_margin=record(margin),whole_bill=record(W),terminal_entropy=record(leafH),terminal_entropy_release=record(avgdeltaH),diagnostic_new_bank=record(newS),full_terminal_margin=record(completeMargin))
 rows.append(row)
 (RUN/'out/CHECKPOINT.json').write_text(json.dumps(dict(completed=len(rows),assertions=count,latest=row),indent=2)+'\n')
output=dict(status='PASS',cases=len(rows),assertions=count,seconds=time.perf_counter()-start,root=dict(I_b=str(Ib),I_c=str(Ic),Q=record(Q),S4=record(S),initial_booked=record(initial),actual_initial_encoder_bill=record(actualInitial),initial_encoder_interaction=record(initialInteraction),actual_remaining=record(actualRemaining),remaining=record(remaining)),rows=rows)
name='PILOT.json' if '--pilot' in sys.argv else 'CHECK.json'
(RUN/'out'/name).write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:v for k,v in output.items() if k not in ['root','rows']}))
