from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from math import lcm
import json,hashlib,sys,time
R=Path(__file__).resolve().parents[1]
checks=0
def ck(v):
 global checks
 checks+=1
 if not v:raise AssertionError(checks)
def add(*fs):
 out={}
 for f in fs:
  for p,c in f.items():out[p]=out.get(p,Q(0))+c
 return {p:c for p,c in out.items() if c}
def scale(f,v):return {p:c*v for p,c in f.items() if c*v}
def sub(f,g):return add(f,scale(g,-1))
@lru_cache(None)
def factor(n):
 out={};p=2
 while p*p<=n:
  while n%p==0:out[p]=out.get(p,0)+1;n//=p
  p+=1
 if n>1:out[n]=out.get(n,0)+1
 return out
def logform(x):return sub(factor(x.numerator),factor(x.denominator))
@lru_cache(None)
def entropy(hist,N):
 return add(*(scale(logform(Q(sq,N*N)),-Q(count*sq,N*N)) for sq,count in hist if sq))
def encode(f):return {str(p):str(c) for p,c in sorted(f.items())}
def decode(f):return {int(p):Q(c) for p,c in f.items()}
@lru_cache(None)
def oddsets(N):
 return tuple(sum(1<<x for x in range(N) if (s&x).bit_count()%2) for s in range(N))
@lru_cache(maxsize=512)
def data(t):
 N=len(t);n=N.bit_length()-1;negative=sum(1<<x for x,v in enumerate(t) if v<0);m=negative.bit_count()
 w=tuple(N-2*m if s==0 else -2*(m-2*(negative&parity).bit_count()) for s,parity in enumerate(oddsets(N)))
 ck(sum(a*a for a in w)==N*N)
 for x,v in enumerate(t):
  ck(sum(a*(-1 if (s&x).bit_count()%2 else 1) for s,a in enumerate(w))==N*v)
 ds=tuple(Q(sum(t[x]!=t[x^(1<<i)] for x in range(N)),N) for i in range(n))
 for i,d in enumerate(ds):ck(d==Q(sum(a*a for s,a in enumerate(w) if s>>i&1),N*N))
 hist={}
 for a in w:hist[a*a]=hist.get(a*a,0)+1
 return entropy(tuple(sorted(hist.items())),N),ds,w
def child(t,b):return tuple(t[2*x+b] for x in range(len(t)//2))
def profiles():
 return [(a,b,c,4-a-b-c) for a in range(5) for b in range(5-a) for c in range(5-a-b)]
def core(profile):
 return tuple(v for count,pair in zip(profile,[(1,1),(1,-1),(-1,1),(-1,-1)]) for _ in range(count) for v in pair)
def profile_of(t,i):
 out=[0]*4
 for x in range(len(t)):
  if x>>i&1:continue
  pair=(t[x],t[x|(1<<i)])
  out[[(1,1),(1,-1),(-1,1),(-1,-1)].index(pair)]+=1
 return tuple(out)
def compose(h,g):return tuple(h[(1 if g[x&7]<0 else 0)+2*(x>>3)] for x in range(32))
def C(h,g):
 # g may be a two-bit physical child, so this separate evaluation retains both outside bits.
 N=len(g);t=tuple(h[(1 if g[x&(N-1)]<0 else 0)+2*(x//N)] for x in range(4*N))
 q=Q(sum(h[2*z]!=h[2*z+1] for z in range(4)),4)
 return t,q,sub(data(t)[0],scale(data(g)[0],q))
MAXIMUM={2:Q(-4),3:Q(3)}
@lru_cache(None)
def integer_sign(key):
 form=dict(key);den=lcm(*(c.denominator for c in form.values())) if form else 1
 a=b=1
 for p,c in form.items():
  exponent=int(c*den)
  if exponent>0:a*=p**exponent
  else:b*=p**(-exponent)
 return (a>b)-(a<b)
def sign(f):return integer_sign(tuple(sorted(f.items())))
def save(name,obj):
 p=R/'out'/name;tmp=p.with_suffix('.tmp');tmp.write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8');tmp.replace(p)
def freeze():
 save('FROZEN_SPEC.json',{'helper_version':'A074-oriented-edge-histogram-v1','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'actual_Boolean_family':'F=h(g,y1,y2), h all256 three-input sign tables, g all256 three-bit tables and each of3 queries, queried gate input arbitrary','parameter_domain':'all35 ordered (++,+-,-+,--) edge histograms summing4; one explicit actual g representative each; outer masks0..255','case_count':8960,'positive_influence_case_count':7200,'symmetry':'physical query relabeling and outer argument relabeling; within-core histogram reduction proved by exact full-row cancellation, with ALL35 signed profiles retained','arithmetic':'integer truth masks, bitset character counts, Fraction prime-log forms; strict signs by LCM-cleared integer powers, equality symbolic','memory_estimate_mb':120,'max_runtime_seconds':{'pilot':55,'main':180},'pilot':'all35 profiles, outer masks0..15 (560 actual circuits)','automatic_dimension_escalation':False})
 print('FROZEN')
def main():
 mode=sys.argv[1]
 if mode=='freeze':freeze();return
 start=time.monotonic();spec=json.loads((R/'out/FROZEN_SPEC.json').read_text(encoding='utf-8'))
 ck(spec['helper_sha256']==hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 cap=55 if mode=='pilot' else 180;outer=16 if mode=='pilot' else 256
 ps=profiles();ck(len(ps)==35);ck(len(set(ps))==35)
 # Full coverage reconstruction independent of any producer signature list.
 coverage={};edge_rows=0
 for mask in range(256):
  t=tuple(-1 if mask>>x&1 else 1 for x in range(8))
  for i in range(3):
   p=profile_of(t,i);ck(p in ps);coverage[p]=coverage.get(p,0)+1;edge_rows+=1
 ck(edge_rows==768);ck(set(coverage)==set(ps))
 save(mode+'_COVERAGE.json',{'core_query_rows':edge_rows,'profiles':[{ 'counts':list(p),'multiplicity':coverage[p]} for p in ps]})
 rows=positive=zero=equality=0;witness=None;distinct=set();chunks=[]
 for hm in range(outer):
  if time.monotonic()-start>cap:raise TimeoutError('frozen cap')
  h=tuple(-1 if hm>>x&1 else 1 for x in range(8));chunk=[]
  for p in ps:
   g=core(p);t,q,c=C(h,g);ck(t==compose(h,g));Hg,dg,wg=data(g);d=dg[0];physical=q*d
   ck(Q(wg[0],8)==Q(p[0]-p[3],4));ck(Q(wg[1],8)==Q(p[1]-p[2],4));ck(d==Q(p[1]+p[2],4))
   child_data=[C(h,child(g,b)) for b in (0,1)]
   for b,(tt,qq,cc) in enumerate(child_data):ck(tt==child(t,b));ck(qq==q)
   drift=sub(scale(add(*(v[2] for v in child_data)),Q(1,2)),c)
   ck(data(t)[1][0]==physical)
   gap=sub(scale(MAXIMUM,physical),drift)
   ck(sign(gap)>=0)
   if physical:
    positive+=1;ratio=scale(drift,1/physical);distinct.add(tuple(sorted(ratio.items())))
    if not gap:
     equality+=1
     if witness is None:witness={'outer_mask':hm,'profile':list(p),'core_truth':list(g),'full_truth_mask':sum(1<<x for x,v in enumerate(t) if v<0),'physical_influence':str(physical),'drift':encode(drift),'ratio':encode(ratio),'full_entropy':encode(data(t)[0]),'core_entropy':encode(Hg),'children_entropy':[encode(data(v[0])[0]) for v in child_data]}
   else:zero+=1;ck(not drift)
   rows+=1;chunk.append({'outer_mask':hm,'profile':list(p),'influence':str(physical),'drift':encode(drift),'gap':encode(gap),'equality':bool(physical and not gap)})
  if hm%16==15:
   name=f'{mode}_CHUNK_{hm//16:02}.json';save(name,chunks+chunk);chunks=[]
  else:chunks.extend(chunk)
 ck(rows==outer*35)
 if mode=='main':ck(positive==7200);ck(equality>0);ck(sign(sub(MAXIMUM,{2:Q(1,2)}))>0)
 save(mode.upper()+'.json',{'status':'PASS','actual_circuits':rows,'positive_influence_rows':positive,'zero_influence_rows':zero,'equality_rows':equality,'distinct_ratio_profiles':len(distinct),'checks':checks,'elapsed_seconds':time.monotonic()-start,'maximum':encode(MAXIMUM),'witness':witness,'sign_certificates':integer_sign.cache_info().currsize,'arithmetic':'exact integer powers; no float signs; no producer imports'})
 print(json.dumps({'mode':mode,'rows':rows,'positive':positive,'equality':equality,'checks':checks,'seconds':time.monotonic()-start}))
if __name__=='__main__':main()
