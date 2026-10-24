import sys
sys.dont_write_bytecode=True
import arithmetic as a
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
from pathlib import Path
import json,time
R=Path(__file__).resolve().parents[1];count=0
def ck(v):
 global count
 count+=1
 assert v,count
@lru_cache(None)
def state(g,h,kinds,phase):
 f=a.wrapper(g,h);ag,ah=a.fft(g),a.fft(h);cs=a.rows(kinds);pot=a.potential(g,h,kinds)
 ck(a.ent(f)==a.add(a.scale(a.add(a.ent(g),a.ent(h)),Q(1,2)),pot))
 IS=IC=Q(0)
 for i,k in enumerate(kinds):
  ig,ih=a.inf(g,i),a.inf(h,i);inf=a.inf(f,i+1)
  ck(inf==(ig+ih)/2)
  D=a.add(a.erase(f,i+1),a.scale(a.add(a.erase(g,i),a.erase(h,i)),Q(-1,2)))
  if k=='S':
   IS+=inf
   if phase!='shared':continue
   formula=a.add(*(a.add(a.scale(a.add(a.Phi((ag[c]+ah[c])**2,(ag[c|1<<i]+ah[c|1<<i])**2),a.Phi((ag[c]-ah[c])**2,(ag[c|1<<i]-ah[c|1<<i])**2)),Q(1,4)),a.scale(a.add(a.Phi(ag[c]**2,ag[c|1<<i]**2),a.Phi(ah[c]**2,ah[c|1<<i]**2)),Q(-1,2))) for c in cs if not c&1<<i))
   ck(D==formula);ck(a.absle(D,5*inf));ck(a.absle(a.erase(f,i+1),13*inf));K=8
  else:
   IC+=inf
   if phase!='controls':continue
   ck(a.absle(D,2*inf));ck(a.absle(a.erase(f,i+1),5*inf));K=5
  children=[]
  for b in (0,1):
   gg,hh=a.restrict(g,i,b),a.restrict(h,i,b);kk=kinds[:i]+kinds[i+1:]
   children.append(a.potential(gg,hh,kk))
  ck(a.absle(a.add(pot,a.scale(a.add(*children),Q(-1,2))),K*inf))
 ck(not pot or a.bounds(pot)[0]>=0)
 ck(a.absle(pot,8*IS+5*IC))
 if not kinds:ck(not pot)
def rootg(ucode):return tuple((1 if ucode&1<<(t&3) else -1) if not t&4 else 1 for t in range(16))
def rooth(vcode):return tuple((1 if vcode&1<<(t&3) else -1) if not t&8 else 1 for t in range(16))
def apply(g,h,kinds,assignment):
 for i in range(len(kinds)-1,-1,-1):
  if assignment[i]>=0:
   g,h=a.restrict(g,i,assignment[i]),a.restrict(h,i,assignment[i]);kinds=kinds[:i]+kinds[i+1:]
 return g,h,kinds
def policy(mode):
 start=time.perf_counter();limit=16 if mode.endswith('pilot') else 256;roots=visits=0;kinds=('S','S','X','Y')
 for uc,vc in product(range(16),repeat=2):
  if roots>=limit:break
  g,h=rootg(uc),rooth(vc)
  phaseu=tuple(1 if uc&1<<j else -1 for j in range(4));phasev=tuple(1 if vc&1<<j else -1 for j in range(4))
  f=a.wrapper(g,h);isource=(sum((a.inf(phaseu,i)+a.inf(phasev,i) for i in range(2)),Q(0)))/4
  m,n=Q(sum(phaseu),4),Q(sum(phasev),4);corr=Q(sum(x*y for x,y in zip(phaseu,phasev)),4)
  ic=(2-m-n)/4;iz=((1-m)/2+(1-n)/2-(1-m-n+corr)/4)/2
  ck(sum((a.inf(f,i) for i in range(5)),Q(0))==isource+ic+iz);ck(a.inf(f,0)==iz);ck(a.absle(a.ent(f),16*(isource+ic)))
  for ss in product((-1,0,1),repeat=2):
   gg,hh,kk=apply(g,h,kinds,ss+(-1,-1));state(gg,hh,kk,'shared');visits+=1
  for ss in product((0,1),repeat=2):
   for xy in product((-1,0,1),repeat=2):
    gg,hh,kk=apply(g,h,kinds,ss+xy);state(gg,hh,kk,'controls');visits+=1
  roots+=1
 out={'mode':mode,'roots':roots,'node_visits':visits,'distinct_nodes':state.cache_info().currsize,'exact_assertions':count,'seconds':time.perf_counter()-start,'failures':0,'arithmetic':'exact Fraction and prime-log expressions with rational atanh enclosures'}
 (R/'out'/('check_'+mode+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
def review(mode):
 start=time.perf_counter();limit=128 if mode.endswith('pilot') else 4096;roots=0
 for uc,vc in product(range(256),range(16)):
  if roots>=limit:break
  g=tuple(1 if uc&1<<j else -1 for j in range(8));h=tuple(1 if vc&1<<(j&3) else -1 for j in range(8));f=a.wrapper(g,h)
  d=a.inf(g,2);delta=Q(sum(x!=y for x,y in zip(g,h)),8)
  A=a.add(a.erase(f,3),a.scale(a.erase(g,2),Q(-1,4)))
  upper=a.add(((2,d),),a.scale(a.Phi(4*delta-d,d),Q(1,2)))
  ck(d<=2*delta);ck(not A or a.bounds(A)[0]>=0)
  gap=a.add(upper,a.scale(A,-1));ck(not gap or a.bounds(gap)[0]>=0);ck(a.absle(A,4*delta))
  roots+=1
 # Actual eligible mark fractions: k=2,4,6 and remaining gate widths0,1,2,3.
 for k,l in product((2,4,6),range(4)):
  p=Q(1,1<<l);h=Q(1,1<<(k//2));aa=Q(1,1<<k)
  delta=p*(1-h+aa)/2;d0=p*(1-h+2*aa)/2
  ck(d0/2<=Q(2,3)*delta);ck(12*delta-6*d0>=4*delta)
  if k==2:ck(d0/2==Q(2,3)*delta)
 out={'mode':mode,'admission_cases':roots,'exact_assertions':count,'seconds':time.perf_counter()-start,'failures':0,'scope':'A076 v5 private admission and A077 v1 generic geometric mark; not full bundled/family acceptance'}
 (R/'out'/('check_'+mode+'.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
def weak():
 start=time.perf_counter();rows=[]
 for k in (2,4,8,16,32,64):
  p=Q(1,1<<k);b=Q(1,1<<(k//2));IS=k*p/2;IC=k*p*(1-b);iz=p*(1-b)-p*p*(1-2*b)/2
  ck(IS>0 and IC>0 and iz>0);ck(1-p+p/b<2);ck(1/b==(1<<(k//2)))
  if k in (2,4):
   u=tuple((-1)**sum(((j>>i)&1)*((j>>(i+1))&1) for i in range(0,k,2)) for j in range(1<<k));v=tuple(x*(-1 if j&1 else 1) for j,x in enumerate(u))
   ck(Q(sum(u),len(u))==b);ck(Q(sum(v),len(v))==b);ck(sum(x*y for x,y in zip(u,v))==0)
   ck(all(abs(x)==b for x in a.fft(u)));ck(sum((a.inf(u,i) for i in range(k)),Q(0))==Q(k,2));ck(sum((a.inf(v,i) for i in range(k)),Q(0))==Q(k,2))
  rows.append({'k':k,'p':str(p),'IS':str(IS),'IC':str(IC),'Iz':str(iz),'total_I':str(IS+IC+iz),'root_profile_norm':str(1-p+p/b),'fixed_slice_norm':str(1/b)})
 out={'cases':len(rows),'exact_assertions':count,'seconds':time.perf_counter()-start,'failures':0,'rows':rows}
 (R/'out/weak_regime.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='rows'}))
if __name__=='__main__':
 mode=sys.argv[1]
 if mode.startswith('policy'):policy(mode)
 elif mode.startswith('review'):review(mode)
 else:weak()
