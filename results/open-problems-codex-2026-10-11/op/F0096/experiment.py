import math,itertools,json,random,time
from pathlib import Path
from fractions import Fraction
P=Path(__file__).parent
rng=random.Random(96)
def fall(a,k):
 return math.prod(range(a-k+1,a+1)) if a>=k else 0
def pairing_events():
 degrees=[4,4,3,3]; owners=[v for v,d in enumerate(degrees) for _ in range(d)]
 counts=[0,0,0,0];total=0
 def rec(stubs,partners):
  nonlocal total
  if not stubs:
   total+=1
   flags=[all(degrees[owners[partners[s]]]==3 for s in range(4*v,4*v+4)) for v in [0,1]]
   counts[flags[0]+2*flags[1]]+=1;return
  a=stubs[0]
  for i in range(1,len(stubs)):
   b=stubs[i];partners[a]=b;partners[b]=a
   rec(stubs[1:i]+stubs[i+1:],partners)
 rec(list(range(14)),{})
 marginal=Fraction(counts[1]+counts[3],total)
 expected=Fraction(fall(6,4),math.prod(14-(2*j+1) for j in range(4)))
 assert marginal==expected and counts[3]==0
 return {'degrees':degrees,'total_pairings':total,'flag_counts':counts,'marginal':str(marginal),'formula':str(expected),'joint':0}
def hamilton(adj):
 n=len(adj); full=(1<<n)-1
 # Held--Karp reachability, anchored at vertex zero.
 reachable={1:1}
 for mask in range(1,full+1,2):
  ends=reachable.get(mask,0)
  while ends:
   b=ends&-ends;ends-=b;v=b.bit_length()-1
   choices=adj[v]&~mask
   while choices:
    z=choices&-choices;choices-=z
    new=mask|z;reachable[new]=reachable.get(new,0)|z
 return bool(reachable.get(full,0)&adj[0])
def enumerate_six():
 n=6;edges=list(itertools.combinations(range(n),2));table={};witness=None
 for mask in range(1<<len(edges)):
  adj=[0]*n;deg=[0]*n
  for j,(u,v) in enumerate(edges):
   if mask>>j&1: adj[u]|=1<<v;adj[v]|=1<<u;deg[u]+=1;deg[v]+=1
  if min(deg)<3:continue
  m=mask.bit_count(); ham=hamilton(adj)
  obstruct=any(deg[v]==4 and all(deg[u]==3 for u in range(n) if adj[v]>>u&1) for v in range(n))
  row=table.setdefault(m,{'graphs':0,'hamiltonian':0,'cubic_obstruction':0})
  row['graphs']+=1;row['hamiltonian']+=ham;row['cubic_obstruction']+=obstruct
  if obstruct and ham and witness is None:witness={'degrees':deg,'edges':[e for j,e in enumerate(edges) if mask>>j&1]}
 return {'n':n,'table':table,'hamiltonian_obstruction_witness':witness}
def distribution(lam):
 terms=[1.0]
 for e in range(1,100):terms.append(terms[-1]*lam/(3+e))
 z=sum(terms);mean=sum((3+e)*t for e,t in enumerate(terms))/z
 return mean,1/z,terms[1]/z
def constants(c):
 lo=0.;hi=2*c+10
 for _ in range(100):
  mid=(lo+hi)/2
  if distribution(mid)[0]<2*c:lo=mid
  else:hi=mid
 lam=(lo+hi)/2;mu,p3,p4=distribution(lam)
 return {'c':c,'lambda':lam,'mean':mu,'p3':p3,'p4':p4,'theta':p4*(3*p3/(2*c))**4}
def sample_degrees(n,m):
 excess=2*m-3*n;w=[1.]
 for e in range(1,excess+1):w.append(w[-1]/(3+e))
 dp=[[0.]*(excess+1) for _ in range(n+1)];dp[0][0]=1.
 for k in range(1,n+1):
  for s in range(excess+1):dp[k][s]=sum(w[e]*dp[k-1][s-e] for e in range(s+1))
 def one():
  rem=excess;ds=[]
  for k in range(n,0,-1):
   weights=[w[e]*dp[k-1][rem-e] for e in range(rem+1)]
   e=rng.choices(range(rem+1),weights=weights)[0];ds.append(3+e);rem-=e
  return ds
 return one
def samples(n,m,count):
 draw=sample_degrees(n,m);accepted=trials=obs=ham=0
 while accepted<count:
  trials+=1;ds=draw();stubs=[i for i,d in enumerate(ds) for _ in range(d)];rng.shuffle(stubs);adj=[0]*n;ok=True
  for u,v in zip(stubs[::2],stubs[1::2]):
   if u==v or adj[u]>>v&1:ok=False;break
   adj[u]|=1<<v;adj[v]|=1<<u
  if not ok:continue
  accepted+=1
  obs+=any(ds[v]==4 and all(ds[u]==3 for u in range(n) if adj[v]>>u&1) for v in range(n))
  ham+=hamilton(adj)
 return {'n':n,'m':m,'accepted':accepted,'trials':trials,'hamiltonian':ham,'cubic_obstruction':obs}
result={'pairings':pairing_events()};(P/'experiments.json').write_text(json.dumps(result,indent=2))
result['exhaustive']=enumerate_six();(P/'experiments.json').write_text(json.dumps(result,indent=2))
result['constants']=[constants(c) for c in [1.5001,1.51,1.6,1.8,2.,2.662,3.]]
result['samples']=[]
for n,m in [(12,18),(12,19),(12,20),(14,23),(16,26)]:
 r=samples(n,m,100);result['samples'].append(r);(P/'experiments.json').write_text(json.dumps(result,indent=2));print(r,flush=True)
print(json.dumps(result,indent=2))
