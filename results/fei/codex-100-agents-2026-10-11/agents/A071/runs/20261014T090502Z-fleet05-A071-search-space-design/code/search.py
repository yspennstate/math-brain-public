import itertools,json,time,argparse
from fractions import Fraction as Q
from functools import lru_cache
import arithmetic as a
R=a.ROOT
def save(n,x):a.save(n,x)
def div(x,c):return a.mul(x,1/c)
def hi(x):return float(x[1])
def lo(x):return float(x[0])
@lru_cache(None)
def outer(p0,p=Q(3,64)):
 ps=[p0]+[p]*5;c=list(map(Q,a.J))
 for j,p in enumerate(ps):
  for x in range(64):
   if not x>>j&1:
    u,v=c[x],c[x|1<<j];c[x]=(1-p)*u+p*v;c[x|1<<j]=v-u
 sq=[]
 for x,z in enumerate(c):
  w=z*z
  for j,p in enumerate(ps):
   if x>>j&1:w*=p*(1-p)
  sq.append(w)
 a.ck(sum(sq)==1);qs=[]
 for j in range(6):
  q=Q(0)
  for x in range(64):
   if x>>j&1 or a.J[x]==a.J[x|1<<j]:continue
   w=Q(1)
   for k,p in enumerate(ps):
    if k!=j:w*=p if x>>k&1 else 1-p
   q+=w
  qs.append(q)
 C=a.entropy_prob(sq)
 for q,p in zip(qs,ps):C=a.sub(C,a.mul(a.h2(4*p*(1-p)),q))
 return C,qs
G=a.core([1-2*(x in {0,1,2}) for x in range(64)])
@lru_cache(None)
def state(tag):
 free=[i for i,t in enumerate(tag) if t==2];base=sum((t==1)<<i for i,t in enumerate(tag))
 truth=[]
 for x in range(1<<len(free)):
  y=base+sum(((x>>k)&1)<<j for k,j in enumerate(free));truth.append(1-2*(y in {0,1,2}))
 g=a.core(truth);C,qs=outer(g['p']);H=a.add(a.mul(g['H'],qs[0]),a.mul(G['H'],sum(qs[1:])))
 H=a.add(H,C);I=qs[0]*g['I']+sum(qs[1:])*G['I']
 return {'tag':tag,'free':free,'core':g,'C':C,'qs':qs,'H':H,'I':I}
def run(pilot):
 t=time.perf_counter();tags=[(2,)*6,(0,2,2,2,2,2),(1,2,2,2,2,2)] if pilot else list(itertools.product(range(3),repeat=6))
 records=[];edges=[];maxima={};counts={}
 def candidate(name,value,witness):
  if name not in maxima or value[0]>maxima[name]['interval'][1]:maxima[name]={'interval':value,'witness':witness}
  elif value[1]>=maxima[name]['interval'][0] and value!=maxima[name]['interval']:
   # Overlap is allowed only for symmetry-equivalent equal rational laws.
   maxima[name]['interval']=(max(value[0],maxima[name]['interval'][0]),max(value[1],maxima[name]['interval'][1]))
 for tag in tags:
  s=state(tag);g=s['core'];p=g['p'];q=s['qs'][0]
  a.ck(q==outer(Q(3,64))[1][0]);a.ck(sum(s['qs'])>0)
  candidate('full_terminal_H_over_I',div(s['H'],s['I']),tag)
  M=a.sub(a.mul(a.sub((Q(4)*G['I'],)*2,G['H']),sum(s['qs'][1:])),s['C'])
  m45=a.sub(a.mul(a.sub((Q(9,2)*G['I'],)*2,G['H']),sum(s['qs'][1:])),s['C'])
  counts['negative_other_owner_rate4']=counts.get('negative_other_owner_rate4',0)+(M[1]<0)
  counts['negative_other_owner_rate9over2']=counts.get('negative_other_owner_rate9over2',0)+(m45[1]<0)
  if g['I']:
   Cplus=outer(Q(0))[0];Cminus=outer(Q(1))[0]
   D=a.sub(s['C'],a.add(a.mul(Cplus,1-p),a.mul(Cminus,p)))
   K=div(a.add(a.mul(g['H'],q),D),q*g['I'])
   candidate('complete_selected_reveal_required_rate',K,tag)
  records.append({'tag':tag,'p':p,'H':s['H'],'I':s['I'],'C':s['C'],'other_owner4':M,'other_owner9over2':m45})
  for k,j in enumerate(s['free']):
   children=[]
   for bit in (0,1):
    child=list(tag);child[j]=bit;children.append(state(tuple(child)))
   a.ck(s['I']-sum(c['I'] for c in children)/2==q*g['influences'][k])
   dH=a.sub(s['H'],a.mul(a.add(children[0]['H'],children[1]['H']),Q(1,2)))
   dc=a.sub(s['C'],a.mul(a.add(children[0]['C'],children[1]['C']),Q(1,2)))
   dcore=a.sub(g['H'],a.mul(a.add(children[0]['core']['H'],children[1]['core']['H']),Q(1,2)))
   residual=a.sub(dH,a.add(a.mul(dcore,q),dc));a.ck(residual[0]<=0<=residual[1])
   inf=q*g['influences'][k]
   if inf:candidate('individual_query_required_rate',div(dH,inf),[tag,j])
   else:a.ck(dH[0]<=0<=dH[1])
   edges.append({'tag':tag,'coordinate':j,'Inf':inf,'DeltaH':dH,'DeltaC':dc})
  save('PILOT_PARTIAL.json' if pilot else 'STATES_PARTIAL.json',records)
 save('PILOT_EDGES.json' if pilot else 'EDGES.json',edges)
 out={'states':len(records),'edges':len(edges),'maxima':maxima,'counts':counts,'checks':a.checks,'seconds':time.perf_counter()-t}
 save('PILOT.json' if pilot else 'RESULTS.json',out);print(json.dumps(a.enc(out)))
if __name__=='__main__':run('--pilot' in __import__('sys').argv)
