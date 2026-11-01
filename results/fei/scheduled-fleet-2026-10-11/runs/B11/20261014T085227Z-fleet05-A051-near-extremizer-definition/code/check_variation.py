from pathlib import Path
from fractions import Fraction as Q
import json,time,hashlib
import exact_tools as d
import independent_arithmetic as r
ROOT=Path(__file__).resolve().parent.parent
checks=0
def ck(v):
 global checks
 assert v
 checks+=1
def add(*terms):return d.add(terms)
def lo(v):return d.interval(v)[0] if v else Q(0)
def coefflog(a):
 if not a:return {}
 return add((2,r.logalg(abs(a))))
def table(n,t):return tuple((t>>x)&1 for x in range(1<<n))
def influence(t):
 n=(len(t)-1).bit_length()
 return Q(sum(t[x]!=t[x^(1<<i)] for x in range(len(t)) for i in range(n)),len(t))
def boundary(t,e):
 n=(len(t)-1).bit_length()
 return sum((2*t[x]-1)*(2*t[y]-1) for x in range(len(t)) for i in range(n)
            for y in [x^(1<<i)] if x<y and ((e>>x)^(e>>y))&1)
start=time.perf_counter();records=[];all_tables={};maxima={}
for n in range(4):
 N=1<<n; rows=[]
 for t in range(1<<N):
  truth=table(n,t);a=[Q(v,N) for v in d.fwht([2*v-1 for v in truth])]
  H=r.ent([v*v for v in a]);I=sum(s.bit_count()*v*v for s,v in enumerate(a))
  ck(I==influence(truth));ck(sum(v*v for v in a)==1)
  G=[add(*[(v*(-1 if (s&x).bit_count()%2 else 1),coefflog(v)) for s,v in enumerate(a) if v]) for x in range(N)]
  subsets=[{}]*(1<<N)
  for e in range(1,1<<N):
   bit=e&-e;x=bit.bit_length()-1
   subsets[e]=add((1,subsets[e^bit]),(2*truth[x]-1,G[x]))
  rows.append((truth,a,H,I,G,subsets))
 all_tables[n]=rows
 for K in (1,2,3,4):
  best=0;D=add((1,rows[0][2]),(-K,{2:rows[0][3]}))
  for t,row in enumerate(rows[1:],1):
   new=add((1,row[2]),(-K,{2:row[3]}));diff=add((1,new),(-1,D))
   bounds=d.interval(diff) if diff else (Q(0),Q(0))
   ck(not diff or bounds[0]>0 or bounds[1]<0)
   if bounds[0]>0:best=t;D=new
  winners=[t for t,row in enumerate(rows) if add((1,row[2]),(-K,{2:row[3]}))==D]
  maxima[n,K]=best
  records.append({'n':n,'K':K,'best_table':best,'number_of_maximizers':len(winners),'D':d.enc(D),'positive':lo(D)>0})
 if n:
  for t,row in enumerate(rows):
   truth,a,H,I,G,subsets=row
   for e in range(1<<N):
    edited=rows[t^e];delta=Q(e.bit_count(),N)
    ck(edited[3]-I==Q(2*boundary(truth,e),N))
    gap=add((1,edited[2]),(-1,H),(Q(-4,N),subsets[e]),(12*delta,{2:Q(1)}))
    ck(lo(gap)>=0)
   for K in (1,2,3,4):
    if t!=maxima[n,K]:continue
    for e in range(1<<N):
     # rational relaxation 2/ln2 < 3 of V3
     gap=add((Q(K*boundary(truth,e),2)+3*e.bit_count(),{2:Q(1)}),(-1,subsets[e]))
     ck(lo(gap)>=0)
  (ROOT/'out'/f'N{n}_MAXIMA.json').write_text(json.dumps([v for v in records if v['n']==n],indent=2)+'\n')
 ck(time.perf_counter()-start<55)
pilot_checks=checks;pilot_time=time.perf_counter()-start
# Separate representation: direct character sums and physical boundary replay.
independent=0
for n,rows in all_tables.items():
 N=1<<n
 for t,row in enumerate(rows):
  truth,a,H,I,G,subs=row
  ar=r.direct_coeffs(truth);ck(ar==a);ck(r.ent([v*v for v in ar])==H)
  for x in range(N):
   changed=list(truth);changed[x]=1-changed[x]
   p=sum(truth[x]!=truth[x^(1<<i)] for i in range(n))
   ck(influence(changed)-I==Q(2*n-4*p,N))
  independent+=2+N
 for K in (1,2,3,4):
  t=maxima[n,K];truth,a,H,I,G,subs=rows[t]
  for e in range(1<<N):
   # Recompute entropy and the spectral inner product without subset recursion.
   changed=table(n,t^e);anew=r.direct_coeffs(changed);b=[v-u for u,v in zip(a,anew)]
   dot=r.combine(*[(u*v,coefflog(u)) for u,v in zip(a,b) if u and v])
   delta=Q(e.bit_count(),N)
   gap=r.combine((1,r.ent([v*v for v in anew])),(-1,H),(2,dot),(12*delta,{2:Q(1)}))
   ck(not gap or r.bounds(gap)[0]>=0)
   ck(sum(u*v for u,v in zip(a,b))==-2*delta)
   ck(sum(v*v for v in b)==4*delta)
   independent+=3
summary={'assertions':checks,'pilot_assertions':pilot_checks,'independent_assertions':independent,
 'pilot_seconds':pilot_time,'total_seconds':time.perf_counter()-start,'tables':278,'ordered_edit_pairs':65808,
 'helper_assertions':d.ASSERTIONS,'maxima':records,'arithmetic':'exact rational prime logarithms with proved rational bounds','status':'PASS'}
(ROOT/'out/SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='maxima'}))
