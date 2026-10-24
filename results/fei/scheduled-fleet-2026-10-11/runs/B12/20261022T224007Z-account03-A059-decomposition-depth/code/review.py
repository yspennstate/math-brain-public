from pathlib import Path
from fractions import Fraction as Q
import itertools,time,json,sys
import exact as E
R=Path(__file__).resolve().parents[1];start=time.perf_counter();pilot='--pilot' in sys.argv
tabs=[(1,),(-1,),(1,-1),(-1,1)];core=list(itertools.product(tabs,repeat=3))
and2=(-1,-1,-1,1);core.append((and2,tuple(-x for x in and2),and2))
bs=list(itertools.product([0,1],repeat=4));count=0;roots=0
for B in (bs[:2] if pilot else bs):
 for u,v,g in (core[:4] if pilot else core):
  roots+=1;dims=[len(h).bit_length()-1 for h in [u,v,g]]
  table=[]
  for z in range(len(g)):
   for w in range(len(v)):
    for t in range(len(u)):
     for b in range(4):
      for a in [0,1]:
       for y in [0,1]:table.append(g[z] if y==0 else u[t] if a else v[w] if B[b] else g[z])
  spectrum=E.walsh(tuple(table));p=Q(sum(B),4);c=1-p;q=Q(1,2)
  m=Q(sum(u),len(u));n=Q(sum(v),len(v));z=Q(sum(g),len(g));h=p*n+c*z
  Vu=1-m*m;Vv=1-n*n;VG=1-z*z;VH=1-h*h;M=1-m*h;L=(1-q)*h+q*m;w=q*(m-h)
  S=VH-c*c*VG;P=E.phi((1-q)**2,q*q)
  R0=E.add(E.phi((z+L)**2,w*w),E.phi((L-z)**2,w*w));R0={k:v/4 for k,v in R0.items()}
  RG=E.add(E.phi((1+(1-q)*c)**2,q*q*c*c),E.phi(((1-q)*c-1)**2,q*q*c*c));RG={k:v/4 for k,v in RG.items()}
  expected={2:(q-2*q*q)*M+q*q*Vu}
  expected=E.add(E.add(E.add(expected,P,S/2),RG,VG),R0)
  for i in [1,2,3]:
   count+=1;er={}
   for t,aa in enumerate(spectrum):
    if not ((t>>i)&1):er=E.add(er,E.phi(aa*aa,spectrum[t|(1<<i)]**2))
   d=E.influence(spectrum,i)
   if i==1:E.ok(er==expected,'A091 FULL grouped identity')
   E.le(er,{2:12*d},'A091/A057 claimed12 erasure')
  E.walsh.cache_clear();E.cost_cached.cache_clear();E.bounds_cached.cache_clear()
  if time.perf_counter()-start>(55 if pilot else 175):raise RuntimeError('frozen cap')
E.ok(roots==(8 if pilot else 1040));E.ok(count==(24 if pilot else 3120))
out=dict(status='PASS',roots=roots,query_cases=count,assertions=E.checks,seconds=time.perf_counter()-start,pilot=pilot,scope='A091 first-private grouped identity and A057 later-private erasure price; analytic argument independently reconstructed in REVIEW.md')
(R/'out'/('review_pilot.json' if pilot else 'review_validation.json')).write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
