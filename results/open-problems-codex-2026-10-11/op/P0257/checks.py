from pathlib import Path
import numpy as np
from scipy.sparse.csgraph import shortest_path
import json, math, time

rng=np.random.default_rng(2571012)
rows=[]
def metric_scores(w):
 d=shortest_path(w,directed=False)
 np.fill_diagonal(d,np.inf)
 s=np.sort(d,axis=1)[:,:2]
 return d,s,s.mean(axis=1)
def nuv(d,start):
 n=len(d); seen=np.zeros(n,bool); seen[start]=True; total=0.; cur=start
 for _ in range(n-1):
  z=d[cur].copy(); z[seen]=np.inf; nxt=int(z.argmin());total+=z[nxt];cur=nxt;seen[cur]=True
 return total,cur

# Random metric instances: all starts and endpoint versions, including clipping.
tested=0
for n in range(3,16):
 for trial in range(15):
  w=np.zeros((n,n));i,j=np.triu_indices(n,1);w[i,j]=rng.exponential(n,len(i));w+=w.T
  d,s,y=metric_scores(w)
  for start in range(n):
   L,last=nuv(d,start)
   assert L+1e-9 >= y.sum()-(s[start,1]+s[last,1])/2
   for R in [.3,1.,3.,10.]:
    assert L+1e-9 >= np.minimum(s,R).mean(axis=1).sum()-R
   tested+=1
rows.append({'check':'finite_metric_inequalities','starts_checked':tested,'passed':True})

# Exact exponential first-passage statistics versus direct-edge statistics.
for n,reps in [(25,120),(60,60),(120,25)]:
 vals=[];lens=[]
 for _ in range(reps):
  w=np.zeros((n,n));i,j=np.triu_indices(n,1);w[i,j]=rng.exponential(n,len(i));w+=w.T
  d,s,y=metric_scores(w);L,_=nuv(d,0)
  vals.append([s[:,0].mean(),(s[:,1]-s[:,0]).mean(),y.mean()]);lens.append(L/n)
 a=np.array(vals)
 rows.append({'check':'meanfield','n':n,'replicates':reps,'measured_first_increment_score':a.mean(0).tolist(),'exact_first_increment_score':[n/(n-1),n/(2*(n-2)),n/(n-1)+n/(4*(n-2))],'nuv_mean':float(np.mean(lens))})

for m,reps in [(8,80),(16,35),(25,15)]:
 vals=[];lens=[]
 n=m*m
 for _ in range(reps):
  w=np.zeros((n,n))
  for x in range(m):
   for y in range(m):
    v=x*m+y
    for dx,dy in [(1,0),(0,1)]:
     a,b=x+dx,y+dy
     if a<m and b<m:
      u=a*m+b;w[v,u]=w[u,v]=rng.exponential()
  d,s,sc=metric_scores(w)
  bulk=[x*m+y for x in range(2,m-2) for y in range(2,m-2)]
  vals.append(sc[bulk].mean());lens.append(nuv(d,0)[0]/n)
 rows.append({'check':'exponential_grid','m':m,'replicates':reps,'bulk_score_mean':float(np.mean(vals)),'bulk_target':1/3,'nuv_mean':float(np.mean(lens))})

# Tail arithmetic: importance-free clipped Monte Carlo, not an LLN claim.
for K in [4,25,100,1000]:
 d=rng.random(100000)**(-2)
 rows.append({'check':'pareto_clipped_minimum','K':K,'exact_mean':2*math.sqrt(K)-1,'measured_mean':float(np.minimum(d,K).mean())})

Path('checks.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
for x in rows:print(x)
