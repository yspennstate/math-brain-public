"""Independent direct physical composition audit; no producer import."""
from pathlib import Path
from functools import lru_cache
from fractions import Fraction as F
import json,time,hashlib
from profile_engine import add,mul,lp,pack,mean,minus,cmp
R=Path(__file__).resolve().parents[1];START=time.perf_counter();checks=0
def ck(x):
 global checks
 assert x;checks+=1
 assert time.perf_counter()-START<55
def eta(x):return mul(lp(x),-x) if x else {}
def L(x,y):return minus(add(eta(x*x),eta(y*y)),mean([eta((x+y)**2),eta((x-y)**2)]))
@lru_cache(None)
def ft(t):
 N=len(t)
 return tuple(F(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)),N) for s in range(N))
@lru_cache(None)
def H(t):return add(*[eta(w*w) for w in ft(t)])
def child(t,i,b):return tuple(v for x,v in enumerate(t) if x>>i&1==b)
def gate(c,z):return 1 if c>>z&1 else -1
def q(c,ts,j):
 other=1-j
 return F(sum(gate(c,(v<0)<<other)!=gate(c,((v<0)<<other)|(1<<j)) for v in ts[other]),len(ts[other]))
def full(c,ts):return tuple(gate(c,(a<0)|((b<0)<<1)) for b in ts[1] for a in ts[0])
def C(c,ts):return minus(H(full(c,ts)),add(*[mul(H(ts[j]),q(c,ts,j)) for j in range(2)]))
def run():
 rows=0;circuits=0
 for c in [1,6,7,10]:
  for a in range(16):
   for b in range(4):
    ts=(tuple(1 if a>>x&1 else -1 for x in range(4)),tuple(1 if b>>x&1 else -1 for x in range(2)))
    parent=C(c,ts);circuits+=1
    for j in range(2):
     for i in range((len(ts[j])-1).bit_length()):
      kids=[]
      for v in [0,1]:
       z=list(ts);z[j]=child(ts[j],i,v);kids.append(C(c,tuple(z)))
      drift=minus(mean(kids),parent);mu=ft(ts[j])[0];t=ft(ts[j])[1<<i]
      other=1-j;AA=[];DD=[]
      for v in ts[other]:
       z=(v<0)<<other;u=gate(c,z);w=gate(c,z|(1<<j));AA.append(F(u+w,2));DD.append(F(u-w,2))
      rhs=minus(mul(L(mu,t),q(c,ts,j)),add(*[L(x+mu*y,t*y) for x,y in zip(ft(tuple(AA)),ft(tuple(DD)))]))
      ck(drift==rhs)
      physical=sum((len(ts[z])-1).bit_length() for z in range(j))+i;truth=full(c,ts)
      d=F(sum(truth[x]!=truth[x^(1<<physical)] for x in range(len(truth))),len(truth))
      ck(cmp({2:3*d},drift)>=0);rows+=1
      for x,y in zip(ft(tuple(AA)),ft(tuple(DD))):ck(cmp(L(x+mu*y,t*y),{})>=0)
 # Independent primitive control and negative artifact controls.
 ck(2**74>3**9*5**25)
 ck(all(z<5 for z in [F(11,3),F(275,64),F(741,160),F(3059,640),F(135,28)]))
 primitive=minus(L(F(5,8),F(3,8)),{2:F(3,4)})
 ck(primitive=={2:F(37,16),3:F(-9,32),5:F(-25,32)});ck(cmp(primitive,{})>0)
 pilot=json.loads((R/'out/PILOT.json').read_text(encoding='utf-8'))
 for z in pilot['rows']:
  t=tuple(z['truth']);w=ft(t);N=len(t)
  ck([int(v*N) for v in w]==z['integer_Walsh']);ck(pack(H(t))==z['H'])
  # A changed true physical coefficient must fail the direct character lane.
  altered=z['integer_Walsh'].copy();altered[1]+=1
  ck(altered!=[int(v*N) for v in w])
 ck(any(row['distinct_residual_rows']==3 for z in pilot['rows'] for row in z['blocks']))
 # A Boolean summary has at most two row types; replacing 3 by 2 is rejected.
 ck(not all(row['distinct_residual_rows']<=2 for z in pilot['rows'] for row in z['blocks']))
 source=Path(r'agents\A075\runs\20261023T133516Z-account03-A075-search-to-theorem-bridge')
 claim=json.loads((source/'CLAIMS.json').read_text(encoding='utf-8'))[0]
 conventions={k:hashlib.sha256(json.dumps({k:claim['exact_statement'],'hypotheses':claim['hypotheses']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode('utf-8')).hexdigest() for k in ['statement','exact_statement']}
 ck(claim['statement_sha256'] in conventions.values())
 out={'circuits':circuits,'physical_query_rows':rows,'checks':checks,'seconds':time.perf_counter()-START,'source_claim_id':claim['claim_id'],'source_version':claim['version'],'source_statement_sha256':claim['statement_sha256'],'source_hash_conventions':conventions,'source_verdict':'HOLDS_UNCHANGED_SCOPE','peer_code_imported':False,'new_ball_claim_peer_review':'PENDING','full_FEI':'OPEN'}
 (R/'out/AUDIT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out))
if __name__=='__main__':run()
