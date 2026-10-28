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

def const(q):return {2:Q(q)} if q else {}
def eta(args):
 a,g,h,rg,rh=args
 return (1-P(a)[0])*Q(sum(x!=y for x,y in zip(g,h)),len(g))
def aug(args,s):return add(s['T'],const(eta(args)/2))
def target(args,s,factor):
 a,g,h,rg,rh=args;pf=P(mux(a,g,h));na=len(a);out=[];cost={}
 for t,qt in enumerate(s['q']):
  old=s['Q'][t*na:(t+1)*na];pr=pf[t*na:(t+1)*na]
  if not qt:out.extend(old);continue
  k=sum(pr[1:])/qt
  if factor=='legacy':
   ell=Q(15,16)*k+Q(1,32)
   ck(k not in (0,1));ck(Q(1,2)<=ell*(1-k)/(k*(1-ell))<=2)
  else:ell=factor*k/(1+(factor-1)*k)
  non=sum(old[1:]);mass=sum(old);out.append(mass*(1-ell))
  out.extend(mass*ell*v/non if non else Q(0) for v in old[1:])
  cost=add(cost,scale(KL((1-k,k),(1-ell,ell)),qt))
 out=tuple(out);eq(sub(KL(pf,out),s['D']),cost);nn(cost);nn(sub(const(eta(args)/2),cost))
 return out,cost,add(s['S'],const(eta(args)/2),scale(cost,-1))
for k in (Q(0),Q(1,8),Q(1,2),Q(7,8),Q(1)):
 for lam in (Q(1,2),Q(1),Q(2)):
  ell=lam*k/(1+(lam-1)*k);C=KL((1-k,k),(1-ell,ell))
  nn(C);nn(sub(const(k/2),C))
ck(LN2[0]>Q(2,3));ck(LN2[1]<1);ck(9**8>2*8**8)
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
 qs=[target(controls[0],cs[0],'legacy'),target(controls[1],cs[1],Q(1))]
 Ac=sub(aug(data[1],first),avg(*(aug(controls[k],cs[k]) for k in (0,1))));nn(Ac)
 # The next DATA query starts from the ACTUAL odds-changed law qs[0], never from canonical Q.
 curr=controls[0];ca,cg,ch,crg,crh=curr
 refs,rrho,Eout,Oout=channel(mux(*curr[:3]),qs[0][0],2)
 gr,_,Egr,Ogr=channel(cg,crg,0);hr,_,Ehr,Ohr=channel(ch,crh,0)
 nextargs=[(ca,child(cg,0,k),child(ch,0,k),gr[k],hr[k]) for k in (0,1)]
 ns=[canonical(*x,raa[0]) for x in nextargs];tars=[target(nextargs[k],ns[k],(Q(2),Q(1,2))[k]) for k in (0,1)]
 Ad=sub(aug(controls[0],cs[0]),avg(*(aug(nextargs[k],ns[k]) for k in (0,1))));nn(Ad)
 dinh=[KL(P(mux(*nextargs[k][:3])),refs[k]) for k in (0,1)]
 dnew=[add(ns[k]['D'],tars[k][1]) for k in (0,1)]
 sigma=sub(avg(*dnew),add(cs[0]['D'],qs[0][1]));raw=sub(avg(*dnew),avg(*dinh));eq(raw,add(sigma,Eout,Oout))
 eq(sigma,sub(sub(qs[0][2],avg(*(x[2] for x in tars))),Ad))
 deltad=sub(cs[0]['H'],avg(*(x['H'] for x in ns)))
 queriedCE=add(deltad,avg(*(add(ns[k]['H'],dnew[k]) for k in (0,1))))
 deltac=sub(first['H'],avg(*(x['H'] for x in cs)))
 selectedpay=add(deltac,scale(queriedCE,Q(1,2)),scale(add(cs[1]['H'],cs[1]['D'],qs[1][1]),Q(1,2)))
 release=add(Ac,scale(Ad,Q(1,2)));frontS=add(scale(qs[1][2],Q(1,2)),scale(avg(*(x[2] for x in tars)),Q(1,2)))
 eq(selectedpay,sub(sub(add(first['H'],aug(data[1],first)),release),frontS))
 delta0=sub(root['H'],avg(*(x['H'] for x in ds)))
 payment=add(delta0,scale(add(ds[0]['H'],ds[0]['D']),Q(1,2)),scale(selectedpay,Q(1,2)))
 eq(payment,add(root['H'],root['W'],scale(A0,-1),scale(ds[0]['Z'],-Q(1,2)),scale(C1,Q(1,2)),const(eta(data[1])/4),scale(add(release,frontS),-Q(1,2))))
 f=mux(a,g,h);n=len(f).bit_length()-1
 influence=sum(Q(sum(v!=f[x^(1<<i)] for x,v in enumerate(f)),len(f)) for i in range(n));ck(influence==m+Q(29,16))
 reserve=sub(const(4*influence-Q(1,8)),payment);nn(sub(reserve,const(3*m-Q(263,128))))
 rows.append(dict(m=m,first_shape=enc(C1),first_odds=enc(qs[0][1]),next_raw_reset=enc(raw),next_output_refunds=enc(add(Eout,Oout)),next_net_sigma=enc(sigma),original_quota_reserve=enc(reserve),next_reference_branch_masses=[str(x) for x in rrho]))
 if time.monotonic()-START>55:raise TimeoutError('frozen independent55s cap')
# Actual relative-odds guard outside A028@9 no-liability Markov image.
a=tuple(1 if y%2==0 else -1 for y in range(32));g=(1,-1,1,-1);h=(1,1,-1,-1)
args=(a,g,h,P(g),P(h));ra=P(a);s=canonical(*args,ra)
eq(s['T'],{});eq(s['S'],{});ck(eta(args)==Q(1,2))
q,C,S=target(args,s,Q(2));eq(C,scale(lg(Q(9,8)),Q(1,2)));ck(interval(C)[0]>0)
nn(sub(scale(C,4),const(Q(1,4))))
inh,rho,E,O=channel(mux(*args[:3]),q,1);rra,_,_,_=channel(a,ra,1)
for k in (0,1):
 ar=(child(a,1,k),g,h,P(g),P(h));ss=canonical(*ar,rra[k]);tar=target(ar,ss,Q(2));ck(inh[k]==tar[0]);eq(tar[1],C)
eq(add(E,O),{})
# All-n obstruction is proved symbolically; these are exact compressed witnesses.
rare=[]
for n in (4,8,12,16,20):
 delta=Q(1,1<<n);q0=1-2*delta+2*delta*delta;k0=delta*delta/q0
 ell=Q(15,16)*k0+Q(1,32);C=scale(KL((1-k0,k0),(1-ell,ell)),q0)
 ck(q0>=Q(7,8) and k0<=Q(1,224));nn(sub(C,const(Q(1,1024))))
 I=(n+1)*delta;atom=(1-delta)**2;small=delta**2;mult=(1<<(n+1))-1
 ck(atom+mult*small==1)
 entropy=add(scale(lg(atom),-atom),scale(lg(small),-mult*small));nn(sub(const(4*I),entropy))
 if n>=12:nn(sub(C,const(4*I)))
 rare.append(dict(n=n,influence=str(I),q0=str(q0),k0=str(k0),cost=enc(C),entropy=enc(entropy),cost_exceeds_4I=n>=12))
for n in (1,2,3,4):
 aa=(1,-1);gg=(1,)*(1<<n);hh=(-1,)+(1,)*((1<<n)-1);f=mux(aa,gg,hh);pf=P(f)
 delta=Q(1,1<<n);ck(pf[0]==(1-delta)**2);ck(all(v==delta**2 for v in pf[1:]))
 measured=sum(Q(sum(v!=f[x^(1<<i)] for x,v in enumerate(f)),len(f)) for i in range(n+1))
 ck(measured==(n+1)*delta)
ck(Q(27783,16777216)>Q(1,1024))
out=dict(status='PASS',cases=3,dummy_control_witness=1,scalar_cases=15,compressed_rare_cases=5,truth_table_rare_cases=4,assertions=checks,seconds=round(time.monotonic()-START,6),rows=rows,rare=rare,representation='direct characters and separate KL/pair-channel algebra; no main/helper imports',clipping_certificate='9^8 > 2*8^8')
(RUN/'out/relative_independent.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n');print(json.dumps({k:v for k,v in out.items() if k not in ('rows','rare')}))
