import itertools,json,math
from pathlib import Path
import numpy as np
import mpmath as mp
mp.mp.dps=24
out={'constants':[],'neutral_decomposition':[],'graph_checks':[]}
for s in [.2,.5,.8]:
 for a in [.005,.02,.08]:
  K=4*a*a*s*(s+1)*(1-2*a)**(-s-2);D=2*K*float(mp.zeta(s+2));R=1/(256*D)
  out['constants'].append(dict(s=s,a=a,K=K,D=D,analytic_disk_radius=R))
# Check the decomposition on deterministic displacements, including wrap-around pairs.
for s in [.2,.5,.8]:
 for n in [2,3,5]:
  a=.02;u=[mp.mpf(str(a*math.sin(1.7*i+.3))) for i in range(n)]
  def g(t):
   r=t/n;return mp.power(n,-s)*(mp.zeta(s,r)+mp.zeta(s,1-r))
  def gp(t):
   r=t/n;return mp.power(n,-s-1)*s*(-mp.zeta(s+1,r)+mp.zeta(s+1,1-r))
  h=2*sum(g(j-i+u[j]-u[i]) for i in range(n) for j in range(i+1,n))
  ground=2*mp.zeta(s)*(n-mp.power(n,1-s))
  rem=mp.mpf(0);linear=mp.mpf(0);ratio=0;wmin=mp.inf
  K=4*a*a*s*(s+1)*(1-2*a)**(-s-2)
  for i in range(n):
   for j in range(i+1,n):
    r=j-i;d=u[j]-u[i];w=2*(g(r+d)-g(r)-gp(r)*d)
    J=K*mp.power(n,-s-2)*(mp.zeta(s+2,mp.mpf(r)/n)+mp.zeta(s+2,1-mp.mpf(r)/n))
    rem+=w;linear+=2*gp(r)*d;wmin=min(wmin,w);ratio=max(ratio,float(w/J))
  out['neutral_decomposition'].append(dict(s=s,N=n,decomposition_error=float(abs(h-ground-rem)),linear_sum=float(linear),minimum_pair_remainder=float(wmin),maximum_bound_ratio=ratio))
# Exhaustive small connected-graph/tree majorant check, with positive deterministic edge weights.
for n in range(2,6):
 edges=list(itertools.combinations(range(n),2));weights=[.002/(1+j-i)**2 for i,j in edges]
 conn=0.;tree=0.;count=0
 for mask in range(1<<len(edges)):
  adj=[set() for _ in range(n)];prod=1.;ne=0
  for k,(i,j) in enumerate(edges):
   if mask>>k&1:adj[i].add(j);adj[j].add(i);prod*=weights[k];ne+=1
  seen={0};stack=[0]
  while stack:
   for v in adj[stack.pop()]:
    if v not in seen:seen.add(v);stack.append(v)
  if len(seen)==n:
   conn+=prod;count+=1
   if ne==n-1:tree+=prod
 b=max(sum(weights[k] for k,e in enumerate(edges) if i in e) for i in range(n))
 bound=math.exp(n*b/2)*tree
 out['graph_checks'].append(dict(vertices=n,connected_graphs=count,connected_weight=conn,tree_majorant=bound,ratio=conn/bound))
Path('second_numerics.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print('max decomposition error',max(x['decomposition_error'] for x in out['neutral_decomposition']))
print('max pair-bound ratio',max(x['maximum_bound_ratio'] for x in out['neutral_decomposition']))
print('graph ratios',[x['ratio'] for x in out['graph_checks']])
print('radii for a=.02',[(x['s'],x['analytic_disk_radius']) for x in out['constants'] if x['a']==.02])
