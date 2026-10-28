"""One original odds envelope, exact mixed-tree and raw/signed accounting."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import sys,json,time
import previous_mixed as p
b=p.b;e=p.e;R=Path(__file__).resolve().parents[1];START=time.monotonic()
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot';assert MODE in ('pilot','full')
checks=edges=0;CAP=F(1,2);VALUES=(F(1,2),F(1),F(2))
def ck(v,msg=''):
 global checks
 checks+=1
 if not v:raise AssertionError((checks,msg))
def sub(a,b):return e.add(a,e.scale(b,-1))
def eq(a,b,msg=''):ck(not sub(a,b),msg)
def const(v):return {2:F(v)} if v else {}
def nn(a,msg=''):ck(e.enclosure(a)[0]>=0,(msg,a,e.enclosure(a)))
def enc(d):return {str(k):str(v) for k,v in d.items()}

@lru_cache(None)
def state(args,ra,epsilon):
 s=p.shaped(args,ra);base=s['base'];a,g,h,rg,rh=args
 V=1-b.spectrum(a)[0];gamma=sum(F(x!=y,len(g)) for x,y in zip(g,h));eta=V*gamma
 Q=list(s['Q']);q=b.spectrum(b.mux(a,g,h));C={};na=len(a);nd=len(g)
 for t in range(nd):
  inds=[u+na*t for u in range(na)];qt=sum(q[j] for j in inds)
  if not qt:continue
  k=sum(q[j] for j in inds[1:])/qt
  if epsilon=='legacy':
   ell=F(15,16)*k+F(1,32)
   if k in (0,1):ck(ell==k,'legacy only at actual interior rows')
   else:ck(F(1,2)<=ell*(1-k)/(k*(1-ell))<=2,'literal legacy relative odds range')
  else:
   ck(F(1,2)<=epsilon<=2)
   ell=epsilon*k/(1+(epsilon-1)*k)
  row=sum(Q[j] for j in inds);non=sum(Q[j] for j in inds[1:])
  if ell:
   ck(non>0,'conditional profile available')
   B=[Q[j]/non for j in inds[1:]]
  else:B=[F(0)]*(na-1)
  Q[inds[0]]=row*(1-ell)
  for j,v in zip(inds[1:],B):Q[j]=row*ell*v
  C=e.add(C,e.scale(b.kl((1-k,k),(1-ell,ell)),qt))
 Q=tuple(Q);cap=eta/2
 nn(C);nn(sub(const(cap),C),'one original influence-scaled allowance')
 plus=e.add(s['S'],const(cap),e.scale(C,-1));nn(plus)
 D=e.add(s['D'],C);T=e.add(s['T'],const(cap));eq(D,b.kl(q,Q));eq(D,sub(T,plus))
 return dict(Q=Q,C=C,D=D,T=T,S=plus,old=s,epsilon=epsilon,cap=cap,eta=eta)

@lru_cache(None)
def children(args,ra,i):
 a,g,h,rg,rh=args;na=len(a).bit_length()-1
 if i<na:
  rr,E,O,rho=b.physical(a,ra,i)
  return tuple(((b.restrict(a,i,k),g,h,rg,rh),rr[k]) for k in (0,1))
 j=i-na;gg,Eg,Og,rhog=b.physical(g,rg,j);hh,Eh,Oh,rhoh=b.physical(h,rh,j)
 return tuple(((a,b.restrict(g,j,k),b.restrict(h,j,k),gg[k],hh[k]),ra) for k in (0,1))

def edge(args,ra,epsilon,i,targetpair):
 global edges
 edges+=1;s=state(args,ra,epsilon);aa=children(args,ra,i)
 cs=[state(*aa[k],targetpair[k]) for k in (0,1)]
 A=sub(s['T'],b.avg(*(x['T'] for x in cs)));nn(A,'same T contraction')
 sigma=sub(b.avg(*(x['D'] for x in cs)),s['D'])
 eq(sigma,sub(sub(s['S'],b.avg(*(x['S'] for x in cs))),A),'one-bank signed balance')
 f=b.mux(*args[:3]);rr,E,O,rho=b.physical(f,s['Q'],i)
 inherited=[b.kl(b.spectrum(b.restrict(f,i,k)),rr[k]) for k in (0,1)]
 raw=sub(b.avg(*(x['D'] for x in cs)),b.avg(*inherited))
 eq(raw,e.add(sigma,E,O),'CURRENT reference raw reset and BOTH refunds')
 H=s['old']['base']['H'];dh=sub(H,b.avg(*(x['old']['base']['H'] for x in cs)))
 paid=e.add(dh,b.avg(*(e.add(x['old']['base']['H'],x['D']) for x in cs)))
 eq(paid,sub(sub(e.add(H,s['T']),A),b.avg(*(x['S'] for x in cs))),'both full terminals')
 return aa,cs,A,dict(raw=raw,sigma=sigma,E=E,O=O,rho=rho)

def bits(n):
 for k in range(1<<(1<<n)):yield tuple(-1 if (k>>x)&1 else 1 for x in range(1<<n))

def census():
 roots=0;na=1 if MODE=='pilot' else 2
 for a in bits(na):
  pa=b.spectrum(a);ra=tuple((v+F(1,len(a)))/2 for v in pa)
  for g in bits(1):
   for h in bits(1):
    args=(a,g,h,(F(1,2),)*2,(F(1,2),)*2);roots+=1
    for epsilon in VALUES:
     for i in range(na+1):
      for pair in ((VALUES[0],VALUES[2]),(VALUES[2],VALUES[0]),(VALUES[1],VALUES[2])):edge(args,ra,epsilon,i,pair)
    if time.monotonic()-START>(55 if MODE=='pilot' else 240):raise TimeoutError('frozen cap')
 return roots

def walk(args,ra,epsilon,labels,policy,history=()):
 s=state(args,ra,epsilon)
 stop=not labels or (policy==2 and len(history)>=3) or (policy==1 and len(history)>=3 and sum(history)%2==0)
 if stop:return dict(path={},ce=e.add(s['old']['base']['H'],s['D']),A={},S=s['S'],nodes=0,leaves=1,raw={},refund={})
 na=len(args[0]).bit_length()-1
 if not history:i=0;pair=('legacy',F(1))  # literal stage8 CONTROL and first odds payment
 elif len(history)==1 and len(args[1])>1:i=na;pair=(F(2),F(1,2))  # required NEXT shared DATA x1
 else:
  i=0 if policy!=1 or sum(history)%2==0 else len(labels)-1
  pair=(VALUES[(len(history)+sum(history))%3],VALUES[(len(history)+sum(history)+1)%3])
 aa,cs,A,receipt=edge(args,ra,epsilon,i,pair)
 rest=labels[:i]+labels[i+1:]
 rr=[walk(*aa[k],pair[k],rest,policy,history+(k,)) for k in (0,1)]
 H=s['old']['base']['H'];delta=sub(H,b.avg(*(x['old']['base']['H'] for x in cs)))
 out={key:b.avg(*(x[key] for x in rr)) for key in ('path','ce','A','S','raw','refund')}
 out['path']=e.add(delta,out['path']);out['A']=e.add(A,out['A'])
 out['raw']=e.add(receipt['raw'],out['raw']);out['refund']=e.add(receipt['E'],receipt['O'],out['refund'])
 out['nodes']=1+sum(x['nodes'] for x in rr);out['leaves']=sum(x['leaves'] for x in rr)
 eq(e.add(out['path'],out['ce'],out['A'],out['S']),e.add(H,s['T']),'one ORIGINAL envelope at full frontier')
 eq(sub(out['raw'],out['refund']),sub(sub(s['S'],out['S']),out['A']),'signed reset history')
 return out

def actual():
 rows=[]
 for m in (1,2,3):
  args=p.c.instance(m);a,g,h,rg,rh=args;root=b.profile(*args)
  gg,Eg,Og,rhog=b.physical(g,rg,0);hh,Eh,Oh,rhoh=b.physical(h,rh,0)
  data=[(a,b.restrict(g,0,k),b.restrict(h,0,k),gg[k],hh[k]) for k in (0,1)];ds=[b.profile(*x) for x in data]
  pa=b.spectrum(a);V=1-pa[0];ra=(pa[0],)+tuple(V*(F(7,8)*v/V+F(1,56)) for v in pa[1:])
  first=state(data[1],ra,F(1));C1=sub(first['old']['T'],ds[1]['W']);nn(sub(const(F(1,128)),C1))
  A0=sub(root['W'],b.avg(*(x['W'] for x in ds)));nn(A0)
  # Read back the literal first odds reference from stage8 construction, not merely its cost.
  cc=children(data[1],ra,0);st=state(*cc[0],'legacy')
  oldbase=p.shaped(cc[0][0],cc[0][1]);oldQ,oldC,_=p.odds(cc[0][0],oldbase['Q'],F(1,16));ck(oldQ==st['Q']);eq(oldC,st['C'])
  for policy in range(3):
   result=walk(data[1],ra,F(1),tuple(range((len(a)*len(data[1][1])).bit_length()-1)),policy)
   delta0=sub(root['H'],b.avg(*(x['H'] for x in ds)))
   payment=e.add(delta0,e.scale(e.add(ds[0]['H'],ds[0]['D']),F(1,2)),e.scale(e.add(result['path'],result['ce']),F(1,2)))
   formula=e.add(root['H'],root['W'],e.scale(A0,-1),e.scale(ds[0]['Z'],-F(1,2)),e.scale(C1,F(1,2)),const(first['cap']/2),e.scale(e.add(result['A'],result['S']),-F(1,2)))
   eq(payment,formula,'original DATA sibling plus all selected terminals')
   I=e.stats(b.mux(*args[:3]))[3];ck(I==m+F(29,16))
   reserve=sub(const(4*I-F(1,8)),payment);nn(sub(reserve,const(3*m-F(263,128))))
   rows.append(dict(m=m,policy=policy,nodes=1+result['nodes'],leaves=1+result['leaves'],first_C1=enc(C1),payment=enc(payment),reserve=enc(reserve),bound=str(3*m-F(263,128)),selected_A=enc(result['A']),selected_frontier_Splus=enc(result['S']),raw_resets=enc(result['raw']),refunds=enc(result['refund'])))
 return rows

def guard():
 rows=[];C=e.scale(e.lg(F(9,8)),F(1,2));ck(9**8>2*8**8)
 for depth in (1,2,4,8):
  a=tuple(1 if y%2==0 else -1 for y in range(1<<(depth+1)))
  g=(1,-1,1,-1);h=(1,1,-1,-1)
  args=(a,g,h,b.spectrum(g),b.spectrum(h));ra=b.spectrum(a)
  s=state(args,ra,F(2));eq(s['C'],C);ck(s['eta']==F(1,2))
  rootzero=state(args,ra,F(1));eq(rootzero['old']['T'],{});eq(rootzero['old']['S'],{})
  aa,cs,A,rec=edge(args,ra,F(2),1,(F(1),F(1)))
  eq(rec['raw'],e.scale(C,-1));eq(e.add(rec['E'],rec['O']),{})
  signed=C;positive=e.scale(C,depth)
  if depth>=4:nn(sub(positive,const(F(1,4))))
  nn(sub(const(F(1,4)),signed))
  rows.append(dict(depth=depth,signed=enc(signed),positive_parts=enc(positive),allowance='1/4',canonical_T={},canonical_S={}))
 return rows

def main():
 roots=census();histories=[];guards=[]
 if MODE=='full':histories=actual();guards=guard()
 out=dict(status='PASS',mode=MODE,roots=roots,edge_rows=edges,assertions=checks,source_assertions=b.checks,previous_mixed_assertions=p.checks,prior_adapter_assertions=p.c.count,seconds=round(time.monotonic()-START,6),histories=histories,guards=guards,cached_states=state.cache_info().currsize)
 (R/'out'/('logit_pilot.json' if MODE=='pilot' else 'logit_main.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in out.items() if k not in ('histories','guards')}))
if __name__=='__main__':main()
