"""Direct-character reconstruction, independent KL algebra and rational proof constants."""
from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
import json,time
RUN=Path(__file__).resolve().parents[1];START=time.monotonic();checks=0
def ck(v):
 global checks
 checks+=1
 if not v:raise AssertionError(checks)
def add(*ds):
 out={}
 for d in ds:
  for p,v in d.items():out[p]=out.get(p,Q(0))+v
 return {p:v for p,v in out.items() if v}
def scale(d,q):return {p:v*q for p,v in d.items() if v*q}
def sub(a,b):return add(a,scale(b,-1))
@lru_cache(None)
def lg(x):
 d={}
 for n,s in [(x.numerator,1),(x.denominator,-1)]:
  p=2
  while p*p<=n:
   while n%p==0:d[p]=d.get(p,Q(0))+s;n//=p
   p+=1
  if n>1:d[n]=d.get(n,Q(0))+s
 return {p:v for p,v in d.items() if v}
def KL(p,r):
 ck(sum(p)==sum(r)==1);ck(all(not x or y>0 for x,y in zip(p,r)))
 return add(*(scale(lg(x/y),x) for x,y in zip(p,r) if x))
@lru_cache(None)
def hat(t):return tuple(Q(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t)))
def P(t):return tuple(x*x for x in hat(t))
def child(t,i,b):return tuple(v for x,v in enumerate(t) if ((x>>i)&1)==b)
def inherit(t,r,i):
 aa=hat(t);rows=[[],[]]
 for j in range(len(t)):
  if (j>>i)&1:continue
  k=j|(1<<i);u,v=aa[j],aa[k];mass=r[j]+r[k]
  for b in (0,1):rows[b].append(mass*((u+(-1)**b*v)**2/(2*(u*u+v*v)) if u or v else Q(1,2)))
 rho=[sum(row) for row in rows];ck(sum(rho)==1 and min(rho)>0)
 return [tuple(x/rho[b] for x in rows[b]) for b in (0,1)],rho
def ln_bounds(x):
 z=(x-1)/(x+1);term=z;s=Q(0)
 for k in range(32):s+=2*term/(2*k+1);term*=z*z
 return s,s+2*term/(65*(1-z*z))
LN2=ln_bounds(Q(2))
@lru_cache(None)
def log_bound(p):
 if p==2:return Q(1),Q(1)
 k=p.bit_length()-1;lo,hi=ln_bounds(Q(p,1<<k));return k+lo/LN2[1],k+hi/LN2[0]
def interval(d):
 lo=hi=Q(0)
 for p,v in d.items():
  a,b=log_bound(p);lo+=v*(a if v>=0 else b);hi+=v*(b if v>=0 else a)
 return lo,hi
def nn(d):ck(interval(d)[0]>=0)
def enc(d):return {str(p):str(v) for p,v in d.items()}

def avg(a,b):return scale(add(a,b),Q(1,2))
def eq(a,b):ck(not sub(a,b))
def H(p):return add(*(scale(lg(v),-v) for v in p if v))
def mux(a,g,h):return tuple((g if y==1 else h)[x] for x in range(len(g)) for y in a)
def channel(t,r,i):
 rr,rho=inherit(t,r,i);p=P(t);pp=[];qq=[]
 for j in range(len(t)):
  if (j>>i)&1:continue
  k=j|(1<<i);pp.append(p[j]+p[k]);qq.append(r[j]+r[k])
 E=sub(KL(p,r),KL(tuple(pp),tuple(qq)));O=KL((Q(1,2),Q(1,2)),tuple(rho))
 ds=[KL(P(child(t,i,k)),rr[k]) for k in (0,1)]
 eq(KL(p,r),add(E,O,avg(*ds)));nn(E);nn(O)
 return rr,rho,E,O

def canonical(a,g,h,rg,rh,ra=None):
 p=Q(a.count(-1),len(a));pg,ph=P(g),P(h);pf=P(mux(a,g,h));na=len(a)
 q=tuple((1-p)*u+p*v for u,v in zip(pg,ph));r=tuple((1-p)*u+p*v for u,v in zip(rg,rh))
 W=add(scale(KL(pg,rg),1-p),scale(KL(ph,rh),p));Z=sub(W,KL(q,r));nn(Z)
 out=[]
 for t,qt in enumerate(q):
  row=pf[t*na:(t+1)*na]
  if not qt:out.extend((r[t],)+(Q(0),)*(na-1));continue
  out.append(r[t]*row[0]/qt)
  if ra is None:out.extend(r[t]*v/qt for v in row[1:])
  else:out.extend(r[t]*sum(row[1:])/qt*v/(1-ra[0]) for v in ra[1:])
 out=tuple(out);D=KL(pf,out)
 if ra is None:T=W;S=Z
 else:
  gamma=Q(sum(u!=v for u,v in zip(g,h)),len(g));pa=P(a);V=1-pa[0];beta=1-ra[0]
  Da=KL(pa,ra);vac=KL((1-V,V),(1-beta,beta))
  T=add(W,scale(Da,gamma));S=add(Z,scale(vac,gamma));nn(vac)
 eq(D,sub(T,S))
 return dict(Q=out,D=D,T=T,S=S,W=W,Z=Z,H=H(pf),pf=pf,q=q,r=r)

ck(Q(5,8)*(Q(4,5)-Q(16,23))**2/(2*Q(16,23)*Q(7,23))==Q(9,560))
ck(Q(9,560)/Q(3,4)==Q(3,140)>Q(1,48))
curv=Q(9,10)*Q(2,5)**2/Q(7,8)**2+Q(1,10)*Q(2,5)**2/Q(1,10)**2
ck(curv==Q(10952,6125))
upper=Q(5,8)*Q(1,16)**2/2*Q(3,2)*curv
ck(upper==Q(4107,1254400)<Q(1,256))
ck((Q(1,48)-Q(1,256))/2-Q(1,128)==Q(1,1536))
rows=[]
for m in (0,1,2,3):
 a=tuple(-1 if y in (0,1,2) else 1 for y in range(8))
 g=tuple((-1 if x%8==0 else 1)*(-1 if (x>>3).bit_count()%2 else 1) for x in range(1<<(m+3)))
 h=tuple((-1 if (x%8).bit_count()>=2 else 1)*(-1 if (x>>3).bit_count()%2 else 1) for x in range(1<<(m+3)))
 rg=rh=tuple(Q(1,len(g)) for _ in g);root=canonical(a,g,h,rg,rh)
 pa=P(a);V=1-pa[0];A=tuple(x/V for x in pa[1:]);B=tuple(Q(7,8)*x+Q(1,56) for x in A);ra=(pa[0],)+tuple(V*x for x in B)
 gg,rhog,Eg,Og=channel(g,rg,0);hh,rhoh,Eh,Oh=channel(h,rh,0)
 dk=[(a,child(g,0,k),child(h,0,k),gg[k],hh[k]) for k in (0,1)]
 ds=[canonical(*x) for x in dk];A0=sub(root['W'],avg(*(x['W'] for x in ds)));nn(A0)
 first=canonical(*dk[1],ra);C1=sub(first['D'],ds[1]['D']);nn(sub({2:Q(1,128)},C1))
 eq(sub(first['T'],ds[1]['W']),C1)
 raa,rhoa,Ea,Oa=channel(a,ra,0)
 control=[(child(a,0,k),)+dk[1][1:] for k in (0,1)]
 cs=[canonical(*control[k],raa[k]) for k in (0,1)]
 Ac=sub(first['T'],avg(*(x['T'] for x in cs)));eq(Ac,scale(add(Ea,Oa),Q(3,4)));nn(Ac)
 outr,rhof,Ef,Of=channel(mux(*dk[1][:3]),first['Q'],0)
 raw=sub(avg(*(x['D'] for x in cs)),avg(*(KL(P(mux(*control[k][:3])),outr[k]) for k in (0,1))))
 sigma=sub(avg(*(x['D'] for x in cs)),first['D']);eq(raw,add(sigma,Ef,Of))
 ck(rhoa!=rhof)
 M=1<<(m+2);beta=Q(8*M,13*M-12)
 Z=scale(KL((Q(4,5),Q(1,5)),(beta,1-beta)),Q(5,8));eq(cs[0]['Z'],Z)
 f=mux(*control[0][:3]);pf=P(f);old=cs[0]['Q'];new=[]
 for t,qt in enumerate(cs[0]['q']):
  row=old[t*4:(t+1)*4];pt=pf[t*4:(t+1)*4]
  if not qt:new.extend(row);continue
  k=sum(pt[1:])/qt;ell=Q(15,16)*k+Q(1,32);mass=sum(row);non=sum(row[1:])
  new.append(mass*(1-ell));new.extend(mass*ell*v/non for v in row[1:])
 new=tuple(new);C=sub(KL(pf,new),cs[0]['D'])
 eq(C,scale(KL((Q(9,10),Q(1,10)),(Q(7,8),Q(1,8))),Q(5,8)));ck(interval(C)[0]>0);nn(sub({2:Q(1,256)},C))
 margin=sub(avg(sub(cs[0]['S'],C),cs[1]['S']),C1)
 entropy_path=add(sub(root['H'],avg(*(x['H'] for x in ds))),scale(sub(ds[1]['H'],avg(*(x['H'] for x in cs))),Q(1,2)))
 term=add(scale(add(ds[0]['H'],ds[0]['D']),Q(1,2)),scale(add(cs[0]['H'],cs[0]['D'],C,cs[1]['H'],cs[1]['D']),Q(1,4)))
 payment=add(entropy_path,term)
 rhs=add(root['H'],root['W'],scale(A0,-1),scale(ds[0]['Z'],-Q(1,2)),scale(C1,Q(1,2)),scale(Ac,-Q(1,2)),scale(add(sub(cs[0]['S'],C),cs[1]['S']),-Q(1,4)))
 eq(payment,rhs)
 # One more DATA query must inherit the ACTUAL odds-changed law, including new vacuum mass.
 nextrefs,nextrho,En,On=channel(f,new,2)
 childCE=avg(*(add(H(P(child(f,2,k))),KL(P(child(f,2,k)),nextrefs[k])) for k in (0,1)))
 dh=sub(H(pf),avg(*(H(P(child(f,2,k))) for k in (0,1))))
 eq(add(H(pf),KL(pf,new)),add(dh,childCE,En,On))
 if m:
  nn(sub(Z,{2:Q(1,48)}));nn(sub(margin,{2:Q(1,1536)}));nn(sub(add(root['H'],root['W']),add(payment,{2:Q(1,3072)})))
 else:ck(not Z);ck(interval(C)[0]>0)
 rows.append(dict(m=m,first_C1=enc(C1),odds_C=enc(C),selected_Z=enc(Z),account_margin=enc(margin),controller_rho=[str(x) for x in rhoa],output_rho=[str(x) for x in rhof],next_output_rho=[str(x) for x in nextrho]))
 if time.monotonic()-START>55:raise TimeoutError('frozen55s cap')
result=dict(status='PASS',cases=4,assertions=checks,seconds=round(time.monotonic()-START,6),rows=rows,representation='direct character sums and separate physical channels; no main/helper imports',rational_Z_lower='3/140',rational_cost_upper=str(upper))
(RUN/'out/independent.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
