"""Countersearch for the positive outer-correction envelope, exact prime logs."""
from profile_engine import F,add,mul,minus,mean,neg,pack,ev,cmp,pos,lp,Q
from functools import lru_cache
from itertools import product
from pathlib import Path
import json,time,sys
R=Path(__file__).resolve().parents[1];START=time.perf_counter();PILOT='--pilot' in sys.argv;CHECKS=0
def save(n,o):(R/'out'/n).write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
def ck(x):
 global CHECKS
 assert x;CHECKS+=1
def prod(xs):
 r=F(1)
 for x in xs:r*=x
 return r
def entropy(ps):
 r={}
 for p in ps:
  if p:r=add(r,mul(lp(p),-p))
 return r
def truth(name):
 if name=='D':return (1,-1)
 sign=-1 if name[0]=='-' else 1;m=int(name.lstrip('-')[1:])
 return tuple(sign*(-1 if x==0 else 1) for x in range(1<<m))
def canon(t):
 for i in range((len(t)-1).bit_length()):
  if all(t[x]==t[x^(1<<i)] for x in range(len(t))):return canon(tuple(y for x,y in enumerate(t) if not(x>>i&1)))
 return t
@lru_cache(None)
def core(t):
 N=len(t);n=(N-1).bit_length();w=[F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)),N) for s in range(N)]
 ds=[F(sum(t[x]!=t[x^(1<<i)] for x in range(N)),N) for i in range(n)]
 ck(sum(v*v for v in w)==1);ck(sum(ds,F(0))==sum(s.bit_count()*v*v for s,v in enumerate(w)))
 H=entropy(v*v for v in w);I=sum(ds,F(0));ck(cmp(add({2:4*I},neg(H)),{})>=0)
 return {'mu':w[0],'H':H,'I':I}
@lru_cache(None)
def outer(code,mus):
 gate=tuple(1 if code>>z&1 else -1 for z in range(8));w=[F(sum(v*(-1 if (z&M).bit_count()%2 else 1) for z,v in enumerate(gate)),8) for M in range(8)]
 vs=[1-m*m for m in mus]
 co=[sum((w[M]*prod(mus[j] for j in range(3) if (M^U)>>j&1) for M in range(8) if M&U==U),F(0)) for U in range(8)]
 ps=[c*c*prod(vs[j] for j in range(3) if U>>j&1) for U,c in enumerate(co)];ck(sum(ps,F(0))==1)
 qs=[]
 for j in range(3):
  q=sum((prod((1-mus[k])/2 if z>>k&1 else (1+mus[k])/2 for k in range(3) if k!=j) for z in range(8) if not(z>>j&1) and gate[z]!=gate[z|1<<j]),F(0));qs.append(q)
  ck(sum(p for U,p in enumerate(ps) if U>>j&1)==vs[j]*q)
 C=add(entropy(ps),*[mul(entropy([v,1-v]),-q) for v,q in zip(vs,qs)])
 return C,qs,ps,co
def full(code,ts):
 cs=[core(t) for t in ts];C,qs,ps,co=outer(code,tuple(c['mu'] for c in cs))
 H=add(C,*[mul(c['H'],q) for c,q in zip(cs,qs)]);I=sum((c['I']*q for c,q in zip(cs,qs)),F(0))
 return {'C':C,'U':pos(C),'H':H,'I':I,'S':add({2:4*I},neg(H)),'means':[c['mu'] for c in cs],'masses':ps,'coefficients':co}
def record(p):return {k:(pack(v) if isinstance(v,dict) else str(v) if isinstance(v,F) else list(map(str,v))) for k,v in p.items()}
def literal(code,ts):
 dims=[(len(t)-1).bit_length() for t in ts];offset=[0,dims[0],dims[0]+dims[1]];N=1<<sum(dims);vals=[]
 for x in range(N):
  signs=[t[(x>>s)&(len(t)-1)] for t,s in zip(ts,offset)];z=sum((y==-1)<<j for j,y in enumerate(signs));vals.append(1 if code>>z&1 else -1)
 a=vals.copy();step=1
 while step<N:
  for k in range(0,N,2*step):
   for j in range(k,k+step):a[j],a[j+step]=a[j]+a[j+step],a[j]-a[j+step]
  step*=2
 H=entropy(F(v*v,N*N) for v in a);I=F(sum(s.bit_count()*v*v for s,v in enumerate(a)),N*N)
 edges=[F(sum(vals[x]!=vals[x^(1<<j)] for x in range(N)),N) for j in range(sum(dims))];ck(sum(edges,F(0))==I)
 ck(sum(v*v for v in a)==N*N)
 for x in range(N):ck(sum(v*(-1 if (s&x).bit_count()%2 else 1) for s,v in enumerate(a))==N*vals[x])
 return {'H':H,'I':I,'walsh_numerators':a,'truth':vals,'edges':list(map(str,edges))}
def verify(code,ts,kids):
 rows=[]
 for name,functions in [('parent',ts),('child0',kids[0]),('child1',kids[1])]:
  a=full(code,functions);b=literal(code,functions);ck(a['H']==b['H'] and a['I']==b['I'])
  rows.append({'name':name,'spectrum':record(a),'literal_H':pack(b['H']),'literal_I':str(b['I']),'integer_walsh':b['walsh_numerators'],'truth':b['truth'],'edges':b['edges']})
 save('LITERAL_REPRODUCTION.json',{'rows':rows,'method':'whole physical truth table, integer Walsh, direct edges and inverse transform; no composition formula in this lane','full_fei':'OPEN'})
def main():
 # All possible AND restrictions have nonnegative S4, hence their inner hulls are0.
 for m in range(7):
  for s in ['','-']:core(truth(s+'A'+str(m)))
 core((1,));core((-1,));core(truth('D'))
 count=0;found=None
 for code in range(16 if PILOT else 128):
  for m,s,a,b in product(range(2,4 if PILOT else 7),['','-'],['A2','-A2','D'],['A2','-A2','D']):
   names=[s+'A'+str(m),a,b];ts=tuple(truth(n) for n in names);kids=[]
   for bit in [0,1]:kids.append((canon(tuple(y for x,y in enumerate(ts[0]) if x&1==bit)),ts[1],ts[2]))
   p=full(code,ts);zs=[full(code,k) for k in kids];gap=minus(mean([z['U'] for z in zs]),p['U']);count+=1
   if count%64==0:
    ck(time.perf_counter()-START<(55 if PILOT else 300));save('SEARCH_PROGRESS.json',{'rows':count,'outer':code,'seconds':time.perf_counter()-START})
   if cmp(gap,{})>0:
    found={'outer_truth_integer':code,'outer_truth':[1 if code>>z&1 else -1 for z in range(8)],'core_names':names,'queried_core':0,'original_physical_coordinate':0,'dimension':sum((len(t)-1).bit_length() for t in ts),'parent':record(p),'children':[record(z) for z in zs],'drift':pack(gap),'drift_interval_scaled_by_Q':list(map(str,ev(gap))),'Q':str(Q),'rows_before_stop':count,'full_fei':'OPEN','candidate_status':'REFUTED_SUPERHARMONICITY'}
    save('COUNTEREXAMPLE.json',found);verify(code,ts,kids);break
  if found:break
  outer.cache_clear()
 result={'pilot':PILOT,'rows_executed':count,'frozen_maximum_rows':576 if PILOT else 11520,'found_strict_drift':found is not None,'checks':CHECKS,'seconds':time.perf_counter()-START,'full_fei':'OPEN'}
 save('PILOT.json' if PILOT else 'VALIDATION.json',result);print(json.dumps(result))
if __name__=='__main__':main()
