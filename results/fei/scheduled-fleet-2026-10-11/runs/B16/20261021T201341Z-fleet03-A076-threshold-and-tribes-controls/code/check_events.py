"""Frozen common-event certificate. Source-complete argument is section7."""
from pathlib import Path
import sys,json,time
exec(compile((Path(__file__).parent/'arithmetic.py').read_text(encoding='utf-8'),'arithmetic.py','exec'))
pilot='--pilot' in sys.argv
def cn(q):return {} if not q else {F(2):F(q)}
def mean(v):return F(sum(v),len(v))
def direct(t):return tuple(F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t)))
def delt(t,i):return plus((H(t),F(1)),(H(child(t,i,0)),F(-1,2)),(H(child(t,i,1)),F(-1,2)))
def form(h,event,v):return tuple(h[s]*(v[x] if event[s] else 1) for s in range(len(h)) for x in range(len(v)))
roots=queries=reproductions=0
for d in range(2 if pilot else 3):
 for hm in range(1<<(1<<d)):
  h=tuple(1-2*((hm>>s)&1) for s in range(1<<d))
  for am in range(1<<(1<<d)):
   event=tuple((am>>s)&1 for s in range(1<<d));p=F(sum(event),len(event));product=tuple(1-2*a for a in event);kap=I(product)/2
   if p:leq({1/p:p},kap)
   c=coeff(tuple(h[s]*event[s] for s in range(len(h))));b=coeff(h)
   eq(sum(x*x for x in c),p);eq(sum(x*y for x,y in zip(b,c)),p)
   hd=tuple(h[s]*product[s] for s in range(len(h)))
   hw=plus(*[(phi(x*x/p),F(1)) for x in c]) if p else {}
   for n in range(2 if pilot else 3):
    for vm in range(1<<(1<<n)):
     v=tuple(1-2*((vm>>x)&1) for x in range(1<<n));mu=mean(v);f=form(h,event,v);cv=coeff(v);cf=coeff(f)
     eq(I(f),p*I(v)+(1+mu)*I(h)/2+(1-mu)*I(hd)/2)
     for s in range(len(h)):
      eq(cf[s*len(v)],b[s]+(mu-1)*c[s])
      for t in range(1,len(v)):eq(cf[s*len(v)+t],c[s]*cv[t])
     if p:
      row=plus(*[(phi((b1+(mu-1)*c1)**2),F(1)) for b1,c1 in zip(b,c)])
      formh=plus((H(v),p),(row,F(1)),(hw,p*(1-mu*mu)),({1/p:p*(1-mu*mu)},F(1)),(phi(mu*mu),-p))
      equal_expr(plus((H(f),F(1)),(formh,F(-1))))
     else:eq(f,tuple(h[s] for s in range(len(h)) for x in range(len(v))))
     for i in range(n):
      a=cv[1<<i];iv=inf(v,i);iff=inf(f,i);eq(iff,p*iv)
      vv=[child(v,i,t) for t in [0,1]];ff=[child(f,i,t) for t in [0,1]]
      for v1,f1 in zip(vv,ff):eq(f1,form(h,event,v1))
      r=kap*(1-mu*mu);rc=[kap*(1-mean(v1)**2) for v1 in vv];rel=r-sum(rc)/2;eq(rel,kap*a*a)
      leq(plus((delt(f,i),F(1)),(delt(v,i),-p)),rel+11*iff)
      leq(plus((B(f,i),F(1)),(B(v,i),-p)),rel+14*iff)
      equal_expr(plus((cn(5*I(f)),F(1)),(H(f),F(-1)),
       (plus(*[(plus((cn(5*I(f1)),F(1)),(H(f1),F(-1))),F(1,2)) for f1 in ff]),F(-1)),
       (cn(5*iff),F(-1)),(delt(f,i),F(1))))
      queries+=1
     if d<=1 and n<=1:eq(cf,direct(f));reproductions+=1
     roots+=1;coeff.cache_clear()
     if time.perf_counter()-start>(60 if pilot else 900):raise TimeoutError('Frozen runtime guard')
result=dict(status='PASS',mode='PILOT' if pilot else 'FULL',roots=roots,private_queries=queries,exact_assertions=checks,
 direct_spectrum_reproductions=reproductions,elapsed_seconds=time.perf_counter()-start,memory='180 MB frozen estimate; actual peak not measured')
(ROOT/'out'/('EVENT_PILOT.json' if pilot else 'EVENT_FULL.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
