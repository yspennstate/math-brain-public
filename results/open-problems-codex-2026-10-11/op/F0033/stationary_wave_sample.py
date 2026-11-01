"""Exact Wilson/burning sampling of finite wired stationary sandpiles.
Monte Carlo evidence only; a single job, bounded by 180 seconds.
"""
import random,time,collections,json,pathlib
from finite_checks import graph,avalanche,recurrent
def sample(r,rng):
 vs,adj,o=graph(r);ix={x:i for i,x in enumerate(vs)};n=len(vs)
 directions=[(-1,0),(1,0),(0,-1),(0,1)]
 nb=[[ix.get((x+dx,y+dy),-1) for dx,dy in directions] for x,y in vs]
 tree={-1};successor={};parent=[-2]*n;edge=[-1]*n
 for start in range(n):
  if start in tree:continue
  cur=start
  while cur not in tree:
   d=rng.randrange(4);nxt=nb[cur][d];successor[cur]=(nxt,d);cur=nxt
  cur=start
  while cur not in tree:
   tree.add(cur);nxt,d=successor[cur];parent[cur]=nxt;edge[cur]=d;cur=nxt
 dist={-1:0}
 for start in range(n):
  path=[];cur=start
  while cur not in dist:path.append(cur);cur=parent[cur]
  depth=dist[cur]
  for cur in reversed(path):depth+=1;dist[cur]=depth
 h=[]
 for i in range(n):
  earlier=sum(dist[j]<dist[i] for j in nb[i])
  choices=[d for d,j in enumerate(nb[i]) if dist[j]==dist[i]-1]
  assert edge[i] in choices
  h.append(4-earlier+choices.index(edge[i]))
 return vs,adj,o,h
def run():
 rng=random.Random(330033);start=time.monotonic();out=[]
 for r,reps in [(1,4000),(4,400),(8,300),(16,200),(32,100)]:
  hist=collections.Counter();reach=collections.Counter();wavesum=0;total=0
  for k in range(reps):
   if time.monotonic()-start>180:break
   vs,adj,o,h=sample(r,rng)
   if k<3:assert recurrent(h,adj)
   u,w,f=avalanche(h,adj,o);hist[len(w)]+=1;wavesum+=len(w);total+=sum(u)
   radius=lambda a:max([max(map(abs,vs[i])) for i in a],default=-1)
   first=radius(w[0]) if w else -1;whole=radius({i for i,x in enumerate(u) if x})
   for a in [1,2,4,8,16,32]:
    if a<=r:
     reach['first_ge_'+str(a)]+=int(first>=a);reach['whole_ge_'+str(a)]+=int(whole>=a)
  count=sum(hist.values())
  out.append({'r':r,'samples':count,'N_histogram':dict(hist),'reach_counts':dict(reach),
              'mean_N':wavesum/count if count else None,'mean_total':total/count if count else None})
  pathlib.Path('stationary_wave_results.json').write_text(json.dumps({'seed':330033,'seconds':time.monotonic()-start,'results':out},indent=2),encoding='utf-8')
  print(json.dumps(out[-1]),flush=True)
  if time.monotonic()-start>180:break
if __name__=='__main__':run()
