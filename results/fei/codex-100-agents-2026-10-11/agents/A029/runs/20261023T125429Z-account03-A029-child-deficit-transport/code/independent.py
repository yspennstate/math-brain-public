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

CAP=Q(1,8)
def const(q):return {2:Q(q)} if q else {}
def target(args,s,epsilon):
 a,g,h,rg,rh=args;pf=P(mux(a,g,h));na=len(a);out=[];cost={}
 for t,qt in enumerate(s['q']):
  old=s['Q'][t*na:(t+1)*na];pr=pf[t*na:(t+1)*na]
  if not qt:out.extend(old);continue
  k=sum(pr[1:])/qt;ell=(1-epsilon)*k+epsilon/2;non=sum(old[1:]);mass=sum(old)
  out.append(mass*(1-ell));out.extend(mass*ell*v/non for v in old[1:])
  cost=add(cost,scale(KL((1-k,k),(1-ell,ell)),qt))
 out=tuple(out);eq(sub(KL(pf,out),s['D']),cost);nn(cost);nn(sub(const(CAP),cost));ck(all(y>=Q(15,16)*x for x,y in zip(s['Q'],out)))
 return out,cost,add(s['S'],const(CAP),scale(cost,-1))
ck(16**8<2*15**8);ck(32**32>2*31**32)
rows=[]
for m in (1,2,3):
 a=tuple(-1 if y<3 else 1 for y in range(8))
 g=tuple((-1 if x%8==0 else 1)*(-1 if (x>>3).bit_count()%2 else 1) for x in range(1<<(m+3)))
 h=tuple((-1 if (x%8).bit_count()>=2 else 1)*(-1 if (x>>3).bit_count()%2 else 1) for x in range(1<<(m+3)))
 rg=rh=tuple(Q(1,len(g)) for _ in g);root=canonical(a,g,h,rg,rh);pa=P(a);V=1-pa[0];ra=(pa[0],)+tuple(Q(7,8)*v+V/Q(56) for v in pa[1:])
 gg,_,Eg,Og=channel(g,rg,0);hh,_,Eh,Oh=channel(h,rh,0)
 data=[(a,child(g,0,k),child(h,0,k),gg[k],hh[k]) for k in (0,1)];ds=[canonical(*x) for x in data]
 A0=sub(root['W'],avg(*(x['W'] for x in ds)));nn(A0)
 first=canonical(*data[1],ra);C1=sub(first['T'],ds[1]['W']);nn(sub(const(Q(1,128)),C1));eq(C1,sub(first['D'],ds[1]['D']))
 raa,_,Ea,Oa=channel(a,ra,0);controls=[(child(a,0,k),)+data[1][1:] for k in (0,1)]
 cs=[canonical(*controls[k],raa[k]) for k in (0,1)]
 qs=[target(controls[0],cs[0],Q(1,16)),target(controls[1],cs[1],Q(0))]
 Ac=sub(first['T'],avg(*(x['T'] for x in cs)));nn(Ac)
 # The next DATA query starts from the ACTUAL odds-changed law qs[0], never from canonical Q.
 curr=controls[0];ca,cg,ch,crg,crh=curr
 refs,rrho,Eout,Oout=channel(mux(*curr[:3]),qs[0][0],2)
 gr,_,Egr,Ogr=channel(cg,crg,0);hr,_,Ehr,Ohr=channel(ch,crh,0)
 nextargs=[(ca,child(cg,0,k),child(ch,0,k),gr[k],hr[k]) for k in (0,1)]
 ns=[canonical(*x,raa[0]) for x in nextargs];tars=[target(nextargs[k],ns[k],(Q(1,64),Q(1,16))[k]) for k in (0,1)]
 Ad=sub(cs[0]['T'],avg(*(x['T'] for x in ns)));nn(Ad)
 dinh=[KL(P(mux(*nextargs[k][:3])),refs[k]) for k in (0,1)]
 dnew=[add(ns[k]['D'],tars[k][1]) for k in (0,1)]
 sigma=sub(avg(*dnew),add(cs[0]['D'],qs[0][1]));raw=sub(avg(*dnew),avg(*dinh));eq(raw,add(sigma,Eout,Oout))
 eq(sigma,sub(sub(qs[0][2],avg(*(x[2] for x in tars))),Ad))
 deltad=sub(cs[0]['H'],avg(*(x['H'] for x in ns)))
 queriedCE=add(deltad,avg(*(add(ns[k]['H'],dnew[k]) for k in (0,1))))
 deltac=sub(first['H'],avg(*(x['H'] for x in cs)))
 selectedpay=add(deltac,scale(queriedCE,Q(1,2)),scale(add(cs[1]['H'],cs[1]['D'],qs[1][1]),Q(1,2)))
 release=add(Ac,scale(Ad,Q(1,2)));frontS=add(scale(qs[1][2],Q(1,2)),scale(avg(*(x[2] for x in tars)),Q(1,2)))
 eq(selectedpay,sub(sub(add(first['H'],first['T'],const(CAP)),release),frontS))
 delta0=sub(root['H'],avg(*(x['H'] for x in ds)))
 payment=add(delta0,scale(add(ds[0]['H'],ds[0]['D']),Q(1,2)),scale(selectedpay,Q(1,2)))
 eq(payment,add(root['H'],root['W'],scale(A0,-1),scale(ds[0]['Z'],-Q(1,2)),scale(C1,Q(1,2)),const(CAP/2),scale(add(release,frontS),-Q(1,2))))
 f=mux(a,g,h);n=len(f).bit_length()-1
 influence=sum(Q(sum(v!=f[x^(1<<i)] for x,v in enumerate(f)),len(f)) for i in range(n));ck(influence==m+Q(29,16))
 reserve=sub(const(4*influence-Q(1,8)),payment);nn(sub(reserve,const(3*m-Q(497,256))))
 rows.append(dict(m=m,first_shape=enc(C1),first_odds=enc(qs[0][1]),next_raw_reset=enc(raw),next_output_refunds=enc(add(Eout,Oout)),next_net_sigma=enc(sigma),original_quota_reserve=enc(reserve),next_reference_branch_masses=[str(x) for x in rrho]))
 if time.monotonic()-START>55:raise TimeoutError('frozen independent55s cap')
# Actual Boolean dummy-control witness, separate direct-character path.
a=tuple(1 if y%2==0 else -1 for y in range(32));g=(1,-1);h=(-1,1);args=(a,g,h,P(g),P(g));ra=P(a)
s=canonical(*args,ra);eq(s['T'],{});eq(s['S'],{})
q,C,S=target(args,s,Q(1,16));eq(C,lg(Q(32,31)));ck(interval(C)[0]>0);nn(sub(scale(C,4),const(CAP)))
inh,rho,E,O=channel(mux(*args[:3]),q,1);rra,_,_,_=channel(a,ra,1)
for k in (0,1):
 ar=(child(a,1,k),g,h,P(g),P(g));ss=canonical(*ar,rra[k]);tar=target(ar,ss,Q(1,16));ck(inh[k]==tar[0]);eq(tar[1],C)
eq(add(E,O),{})
out=dict(status='PASS',cases=3,dummy_control_witness=1,assertions=checks,seconds=round(time.monotonic()-START,6),rows=rows,representation='direct characters, separately coded pair channels and physical edge influence; no main/helper imports',cap_certificate='16^8 < 2*15^8',clipping_certificate='32^32 > 2*31^32')
(RUN/'out/independent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
