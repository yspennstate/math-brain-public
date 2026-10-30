from pathlib import Path
from fractions import Fraction as R
from collections import Counter
import json,time,sys
RUN=Path(__file__).resolve().parents[1]
spec=json.loads((RUN/'FROZEN_SPEC.json').read_text());start=time.perf_counter();assertions=0
def ck(x,msg):
 global assertions
 assert x,msg
 assertions+=1
 assert time.perf_counter()-start<60,'frozen runtime'
def fwht(a):
 a=list(a);d=1
 while d<len(a):
  for i in range(0,len(a),2*d):
   for j in range(i,i+d):a[j],a[j+d]=a[j]+a[j+d],a[j]-a[j+d]
  d*=2
 return a
def spectrum(t):return [R(x*x,len(t)**2) for x in fwht(t)]
def influence(p):return sum(w*s.bit_count() for s,w in enumerate(p))
def lnunit(q):
 z=(q-1)/(q+1);v=z;ans=R(0)
 for j in range(36):ans+=2*v/(2*j+1);v*=z*z
 return ans,ans+2*v/(73*(1-z*z))
L2=lnunit(R(2));cache={}
def log(q):
 if q in cache:return cache[q]
 original=q;e=0
 while q<1:q*=2;e-=1
 while q>=2:q/=2;e+=1
 lo,hi=lnunit(q);D=1<<80
 ans=(R(((e+lo/L2[1])*D).__floor__(),D),R(((e+hi/L2[0])*D).__ceil__(),D));cache[original]=ans;return ans
def interval(expr):
 lo=hi=R(0)
 for q,w in expr.items():
  if not w:continue
  a,b=log(q)
  if w<0:a,b=b,a
  lo+=w*a;hi+=w*b
 return lo,hi
def ce(p,q):
 ck(sum(q)==1,'Q normalization');ck(all(not x or y for x,y in zip(p,q)),'true support')
 return interval(Counter({})) if not any(p) else interval(collect(p,q))
def collect(p,q):
 out=Counter()
 for a,b in zip(p,q):
  if a:out[b]-=a
 return out
def marginal(p,i):
 out=[R(0)]*(len(p)//2)
 for s,w in enumerate(p):out[(s&((1<<i)-1))|((s>>(i+1))<<i)]+=w
 return out
def children(t,i):
 out=[]
 for b in [0,1]:out.append([t[(s&((1<<i)-1))|((s>>i)<<(i+1))|(b<<i)] for s in range(len(t)//2)])
 return out
def node(t,q,i):
 p=spectrum(t);ch=children(t,i);pc=[spectrum(x) for x in ch];qc=marginal(q,i);pm=marginal(p,i)
 ck(all(pm[s]==(pc[0][s]+pc[1][s])/2 for s in range(len(pm))),'exact child erased-law identity')
 charge=Counter()
 for s,w in enumerate(p):
  if w:
   r=(s&((1<<i)-1))|((s>>(i+1))<<i);ck(qc[r]>=q[s]>0,'conditional likelihood')
   charge[qc[r]/q[s]]+=w
 bill=interval(charge);cp=ce(p,q);cc=[ce(x,qc) for x in pc]
 avg=((cc[0][0]+cc[1][0])/2,(cc[0][1]+cc[1][1])/2)
 ck(bill[0]>=0,'nonnegative inherited query charge')
 ck(cp[0]-avg[1]<=bill[1] and bill[0]<=cp[1]-avg[0],'full conditional CE identity')
 inf=sum(w for s,w in enumerate(p) if s&(1<<i))
 ck(influence(p)==inf+(influence(pc[0])+influence(pc[1]))/2,'physical influence telescope')
 ck(inf>0,'query essential')
 return ch,qc,bill,cp,inf
def svalue(w):return -1 if w==0 else 1
records=[]
for k in (spec['pilot_domain'] if '--pilot' in sys.argv else spec['domain']):
 d=R(1,1<<k);N=1<<(k+2)
 # physical order core q,u,v0,... then mask z0,z1 then gate x
 h=[(-1 if (w&1) else 1) if (w>>2)==0 else (-1 if w&2 else 1) for w in range(N)]
 ph=spectrum(h);qh=[w/2 for w in ph];qh[1]+=R(1,2)
 ck(sum(h)==0,'balanced parent');ck(ph[0]==qh[0]==0,'forced empty full row')
 ck(influence(ph)==1+k*d,'source root core influence')
 n=k+5
 t=[];q=[]
 for w in range(1<<n):
  core=w&(N-1);mask=(w>>(k+2))&3;gate=w>>(k+4)
  t.append(1 if gate==0 else h[core]*svalue(mask))
  q.append(qh[core]/16+(R(1,4) if core==0 and mask==0 else 0))
 p=spectrum(t);rootcost=ce(p,q)
 ck(influence(p)==(3+k*d)/2,'source full influence')
 ck(rootcost[1]<4*influence(p),'root eligibility')
 ch,q1,bill0,_,inf0=node(t,q,0);ck(inf0==d/2,'first q influence')
 leaves=[];bills=[];firstcosts=[];conversions=[]
 for b,tc in enumerate(ch):
  cp=spectrum(tc);firstcosts.append(ce(cp,q1));ck(firstcosts[-1][1]<4*influence(cp),'q child eligibility')
  # Fresh activation child differs ONLY by gate conditional on empty data row.
  fresh=list(q1);half=len(q1)//2;data_mass=q1[0]+q1[half];true_mass=cp[0]+cp[half]
  fresh[0]=data_mass*cp[0]/true_mass;fresh[half]=data_mass*cp[half]/true_mass
  freshcost=ce(cp,fresh)
  ee=Counter()
  for ss,w in enumerate(cp):
   if w:ee[fresh[ss]/q1[ss]]+=w
  conversion=interval(ee);conversions.append(conversion)
  ck(conversion[0]>0 and conversion[1]<d*d,'explicit inherited-terminal conversion')
  ck(firstcosts[-1][0]-freshcost[1]<=conversion[1] and conversion[0]<=firstcosts[-1][1]-freshcost[0],'conversion identity')
  ck(bill0[1]+conversion[1]<R(5,8),'old first debit ceiling retained with conversion')
  # after deleting q, physical first-v index is1
  lc,q2,bill1,_,inf1=node(tc,q1,1);ck(inf1==d/2,'second v influence')
  bills.append(bill1)
  ck(bill1[1]<d+(2*k+5)*d*d<=3*d<=R(3,8),'second debit fits same remaining reserve')
  ck(bill0[1]+conversion[1]+bill1[1]<1,'one private half-reserve pays both plus conversion')
  for r,tl in enumerate(lc):
   pl=spectrum(tl);cl=ce(pl,q2);il=influence(pl)
   ck(cl[1]<4*il,'complete terminal rate4 eligibility')
   if r==1:ck(il==R(3,2),'inactive terminal physical influence');ck(cl[1]<4,'inactive terminal cost bound')
   else:
    ck(il==R(3,2)+(k-2)*d+(R(-1,2) if b==0 else R(1,2))*d,'active terminal influence')
    ck(cl[1]<4+4*(k-1)*d,'active terminal analytic cost bound')
   # direct edges independent of Walsh
   for j in range(n-2):
    edge=R(sum(tl[w]!=tl[w^(1<<j)] for w in range(len(tl))),len(tl))
    ck(edge==sum(v for s,v in enumerate(pl) if s&(1<<j)),'terminal physical edges')
   leaves.append({'q':b,'v':r,'I':str(il),'CE_interval':[str(x) for x in cl]})
 # exact cancellation certificate written in logs of rational reference atoms
 expr=collect(p,q)
 for tc in ch:
  pc=spectrum(tc)
  for atom,w in collect(pc,q1).items():expr[atom]-=w/2
 for tc in ch:
  pc=spectrum(tc)
  for atom,w in collect(pc,q1).items():expr[atom]+=w/2
  for tl in children(tc,1):
   for atom,w in collect(spectrum(tl),q2).items():expr[atom]-=w/4
 leafexpr=Counter()
 for tc in ch:
  for tl in children(tc,1):
   for atom,w in collect(spectrum(tl),q2).items():leafexpr[atom]+=w/4
 rootexpr=collect(p,q)
 ck(all(expr[a]+leafexpr[a]==rootexpr[a] for a in set(expr)|set(leafexpr)|set(rootexpr)),'exact full two-query ledger cancellation')
 # Independently reconstruct A020 fixed-positive biased-child refund in natural/bit form.
 a=d*d/4;tref=(1+d*d)/8
 lam=interval({a/tref:a/2,(1+tref)/(1+a):(1+a)/2})
 ck(lam[0]>R(1,32) and lam[1]<R(1,2),'source forced positive-row Lambda sign')
 rec={'k':k,'delta':str(d),'root_I':str(influence(p)),'root_CE':[str(x) for x in rootcost],'first_inherited_debit':[str(x) for x in bill0],'child_conversion_debits':[[str(x) for x in z] for z in conversions],'second_inherited_debits':[[str(x) for x in z] for z in bills],'source_fresh_lift_Lambda':[str(x) for x in lam],'terminals':leaves}
 records.append(rec);(RUN/f'out/CASE_k{k}.json').write_text(json.dumps(rec,indent=2)+'\n')
out={'status':'PASS','cases':len(records),'assertions':assertions,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'rational identities and rigorous rational logarithm intervals','records':records}
(RUN/('out/PILOT.json' if '--pilot' in sys.argv else 'out/CHECK.json')).write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='records'}))
