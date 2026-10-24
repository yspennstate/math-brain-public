"""Exact deterministic tests; these are not samples from the infinite-volume law."""
import itertools, collections, json, time, pathlib
ROOT=pathlib.Path(__file__).resolve().parent
def graph(r):
 vertices=list(itertools.product(range(-r,r+1),repeat=2)); index={x:i for i,x in enumerate(vertices)}
 adj=[[index[y] for y in [(x[0]-1,x[1]),(x[0]+1,x[1]),(x[0],x[1]-1),(x[0],x[1]+1)] if y in index] for x in vertices]
 return vertices,adj,index[(0,0)]
def recurrent(h,adj):
 unburnt=set(range(len(h)))
 while unburnt:
  burn={x for x in unburnt if h[x]>=sum(y in unburnt for y in adj[x])}
  if not burn:return False
  unburnt-=burn
 return True
def avalanche(h,adj,o):
 h=list(h); h[o]+=1; u=[0]*len(h); waves=[]
 while h[o]>=4:
  seen={o}; q=collections.deque([o]); h[o]-=4; u[o]+=1
  for y in adj[o]:h[y]+=1
  q=collections.deque(y for y in adj[o] if y!=o and h[y]>=4)
  while q:
   x=q.popleft()
   if h[x]<4:continue
   assert x not in seen
   seen.add(x); u[x]+=1; h[x]-=4
   for y in adj[x]:
    h[y]+=1
    if y!=o and h[y]>=4:q.append(y)
  assert all(h[x]<4 for x in range(len(h)) if x!=o)
  assert (h[o]>=4)==all(y in seen for y in adj[o]) if len(adj[o])==4 else h[o]<4
  waves.append(seen)
 return u,waves,h
def ordinary(h,adj,o):
 h=list(h);h[o]+=1;u=[0]*len(h);q=collections.deque([o])
 while q:
  x=q.popleft()
  if h[x]<4:continue
  h[x]-=4;u[x]+=1
  for y in adj[x]:
   h[y]+=1
   if h[y]>=4:q.append(y)
 return u,h
def main():
 start=time.monotonic();vs,adj,o=graph(1); count=0;hist=collections.Counter(); nested=None;order=None
 for h in itertools.product(range(4),repeat=9):
  if not recurrent(h,adj):continue
  count+=1;u,w,final=avalanche(h,adj,o);v,final2=ordinary(h,adj,o)
  assert u==v and final==final2
  assert all(u[i]<=2*((2)**2-vs[i][0]**2) for i in range(9))
  hist[len(w)]+=1
  for a,b in zip(w,w[1:]):
   if not b<=a and nested is None:nested={'heights':h,'wave1':sorted(a),'wave2':sorted(b)}
   if not a<=b and order is None:order={'heights':h,'wave1':sorted(a),'wave2':sorted(b)}
 # Check boundary certificate equivalence for arbitrary (not necessarily recurrent) 5x5 states.
 import random
 rng=random.Random(33);v2,a2,o2=graph(2);idx2={x:i for i,x in enumerate(v2)};checked=0
 for _ in range(10000):
  h=[rng.randrange(4) for x in v2]; sub=[h[idx2[x]] for x in vs]
  us,_,_=avalanche(sub,adj,o);ub,_,_=avalanche(h,a2,o2)
  small=any(us[i]>0 for i,x in enumerate(vs) if max(map(abs,x))==1)
  big=any(ub[i]>0 for i,x in enumerate(v2) if max(map(abs,x))==1)
  assert small==big
  checked+=1
 result={'recurrent_3x3_count':count,'wave_count_histogram':dict(hist),'successive_wave_not_decreasing':nested,'successive_wave_not_increasing':order,'certificate_comparisons_5x5':checked,'seconds':time.monotonic()-start,'vertex_order':vs}
 (ROOT/'finite_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8');print(json.dumps(result))
if __name__=='__main__':main()
