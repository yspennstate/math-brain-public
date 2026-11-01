from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time,sys
import helper as h
R=Path(__file__).resolve().parents[1];start=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x,checks;checks+=1
 if time.perf_counter()-start>(55 if '--pilot' in sys.argv else 240):raise TimeoutError('frozen runtime cap')
@lru_cache(None)
def fast(v):
 w=list(v);N=len(w);j=1
 while j<N:
  for a in range(0,N,2*j):
   for b in range(a,a+j):u,z=w[b],w[b+j];w[b],w[b+j]=u+z,u-z
  j*=2
 return tuple(F(x*x,N*N) for x in w)
h.spec=lambda v:fast(tuple(v))
def le(x,y):ck(x==y or x[1]<=y[0])
def rec(x):
 d=1<<40
 return [str(F((x[0]*d).__floor__(),d)),str(F((x[1]*d).__ceil__(),d))]
@lru_cache(None)
def floor(a,b,r,Rt):
 v,P,Q=h.floor(a,b,r,list(Rt));return tuple(v),tuple(P),tuple(Q)
def envelope(a,b,r,Rt):return h.W(a,b,r,list(Rt))
def action(a,b,r,Rt,kind):
 v,P,Q=floor(a,b,r,Rt);n=a+b;e=F(2,1<<(n+r));s=F(1,1<<a);t=F(1,1<<n)
 j=0 if kind=='A' else n if kind=='C' else a
 ck((kind!='A' or a>=2) and (kind!='C' or r>=2) and (kind!='D' or (b>=1 and r>=1)))
 old=tuple(h.marginal(Q,j));off=h.child(list(v),j,1);on=h.child(list(v),j,0)
 Poff=h.spec(off);costoff=h.CE(Poff,old);debit=h.B(P,j)
 if kind=='A':an,bn,rn=a-1,b,r
 elif kind=='C':an,bn,rn=a,b,r-1
 else:an,bn,rn=a,b-1,r
 Rnew=Rt if kind=='C' else tuple(h.cal(h.marginal(Rt,j),h.spec(h.src(an,bn))))
 vn,pn,qn=floor(an,bn,rn,Rnew);ck(tuple(on)==vn)
 oldW=envelope(a,b,r,Rt);newW=envelope(an,bn,rn,Rnew)
 local=h.add(debit,h.mul(F(1,2),costoff),h.mul(F(1,2),newW))
 excess=h.sub(local,oldW);limit=-e if kind=='A' else (8 if kind=='C' else 9)*e
 le(excess,(limit,limit))
 if kind=='D':
  source=h.spec(h.src(a,b));c=h.CE(source,Rt);cnew=h.CE(h.spec(h.src(a,b-1)),Rnew)
  le(cnew,c);ck(debit[1]<12*e);ck(h.sub(costoff,c)[1]<14*e)
  k=(2*s-e)**2/(4*s*s-4*s*e+2*e*t);hh=e/s
  ck(0<hh<=F(1,2));ck(1/k<=1+hh)
  n2=1<<(n-1);coeff=h.src(a,b-1);Pg=h.spec(coeff)
  # Independently evaluate BOTH terms of the exact old off-reference atom.
  Re=[(1-hh)*Rt[T]+hh*(1-2*s)*int(T==0)+2*e*t for T in range(1<<n)]
  for S,pS in enumerate(Pg):
   if not pS:continue
   T=(S&((1<<j)-1))|((S>>j)<<(j+1));Tj=T|(1<<j)
   gh=(1-2*s) if S==0 else -2*s
   expected=Re[T]*(gh+e)**2/(gh*gh+2*e*gh+2*e*t)+Re[Tj]*e*e/(2*e*t)
   ck(old[S]==expected)
   ck(old[S]>=Rt[T]*(1-hh)*k if S else old[S]>=Rt[0])
  ck(len(set(off))==len(set(on))==2)
 return (an,bn,rn,Rnew),debit,costoff,excess
def raws(a,b,mode):
 P=h.spec(h.src(a,b));N=len(P)
 raw=P if mode=='matching' else [F(1,N)]*N if mode=='uniform' else [F(2*(i+1),N*(N+1)) for i in range(N)] if mode=='increasing' else [F(1000 if i==(1<<a) else 1,1000+N-1) for i in range(N)]
 return tuple(h.cal(raw,P))
def histories(a,b,r,Rt):
 e0=F(2,1<<(a+b+r));Ig=F(2*a,1<<a);c=h.CE(h.spec(h.src(a,b)),Rt)
 C0=max(4,(c[1]/Ig).__ceil__());K=2*C0+10
 v,P,Q=floor(a,b,r,Rt);quota=K*h.influence(list(v));W0=envelope(a,b,r,Rt)
 ck(quota-W0[1]>=5*a*(1<<(b+r))*e0)
 nodes=steps=final_closures=0;minimum=None
 def walk(a,b,r,Rt,reach,debit,terms,nc,nd):
  nonlocal nodes,steps,final_closures,minimum
  nodes+=1;v,P,Q=floor(a,b,r,Rt)
  full=h.add(debit,terms,h.mul(reach,h.CE(P,Q)))
  ck(full[1]<=quota-12*e0)
  ck(reach*F(2,1<<(a+b+r))==e0)
  margin=quota-full[1];minimum=margin if minimum is None else min(minimum,margin)
  if a==1:
   final_closures+=1
   old=h.marginal(Q,0);off=h.child(list(v),0,1);on=h.child(list(v),0,0)
   ck(set(off)=={1})
   Poff=h.spec(off);Pon=h.spec(on)
   last=h.add(h.B(P,0),h.mul(F(1,2),h.CE(Poff,old)),h.mul(F(1,2),h.CE(Pon,Pon)))
   le(last,envelope(a,b,r,Rt))
   completed=h.add(debit,terms,h.mul(reach,last))
   ck(completed[1]<=quota-12*e0)
  kinds=(['A'] if a>=2 else [])+(['C'] if r>=2 else [])+(['D'] if b>=1 and r>=1 else [])
  for kind in kinds:
   nxt,d,off,_=action(a,b,r,Rt,kind);steps+=1
   walk(*nxt,reach/2,h.add(debit,h.mul(reach,d)),h.add(terms,h.mul(reach/2,off)),nc+(kind=='C'),nd+(kind=='D'))
 walk(a,b,r,Rt,F(1),(F(0),F(0)),(F(0),F(0)),0,0)
 ck(5*a*(1<<(b+r))-8*(r-1)-9*b>=12)
 return {'nodes':nodes,'steps':steps,'final_active_closures':final_closures,'C0':C0,'original_quota':str(quota),'minimum_complete_margin':str(F((minimum*(1<<40)).__floor__(),1<<40)),'required_retained_margin':str(12*e0)}
def main():
 pilot='--pilot' in sys.argv;rows=[]
 for a in ([1,2] if pilot else [1,2,3]):
  for b in ([1] if pilot else [1,2]):
   for r in ([2] if pilot else [2,3]):
    for mode in (['matching','increasing'] if pilot else ['matching','uniform','increasing','dummy-singleton-spiked']):
     Rt=raws(a,b,mode);nxt,d,off,ex=action(a,b,r,Rt,'D');z=histories(a,b,r,Rt)
     rows.append({'a':a,'b':b,'r':r,'reference':mode,'dummy_local_excess':rec(ex),**z})
     (R/'out/CHECKPOINT.json').write_text(json.dumps({'status':'PARTIAL','completed_roots':len(rows),'rows':rows},indent=2)+'\n',encoding='utf-8')
     floor.cache_clear();fast.cache_clear();h.log.cache_clear()
 out={'status':'PASS','mode':'pilot' if pilot else 'main','roots':len(rows),'assertions':checks,'helper_assertions':h.checks,'history_prefixes':sum(z['nodes'] for z in rows),'history_steps':sum(z['steps'] for z in rows),'final_active_closures':sum(z['final_active_closures'] for z in rows),'seconds':time.perf_counter()-start,'rows':rows}
 (R/'out'/('PILOT.json' if pilot else 'VALIDATION.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
if __name__=='__main__':main()
