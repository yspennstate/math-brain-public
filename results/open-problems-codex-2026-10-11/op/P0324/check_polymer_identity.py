import itertools,json,cmath,math
from pathlib import Path
import mpmath as m
m.mp.dps=24
n=4;s=m.mpf('.5');a=m.mpf('.02');z=.5+.1j
nodes=[-a*m.sqrt(m.mpf(3)/5),m.mpf(0),a*m.sqrt(m.mpf(3)/5)];weights=[5/18,4/9,5/18]
edges=list(itertools.combinations(range(n),2))
def g(t):
 r=t/n;return m.power(n,-s)*(m.zeta(s,r)+m.zeta(s,1-r))
def gp(t):
 r=t/n;return s*m.power(n,-s-1)*(-m.zeta(s+1,r)+m.zeta(s+1,1-r))
W={}
for i,j in edges:
 r=j-i
 W[i,j]=[[float(2*(g(r+v-u)-g(r)-gp(r)*(v-u))) for v in nodes] for u in nodes]
activity={};direct=0j
for config in itertools.product(range(3),repeat=n):
 w=math.prod(weights[c] for c in config)
 direct+=w*cmath.exp(-z*sum(W[i,j][config[i]][config[j]] for i,j in edges))
for mask in range(1,1<<n):
 verts=[i for i in range(n) if mask>>i&1]
 if len(verts)<2:continue
 es=list(itertools.combinations(verts,2));connected=[]
 for gm in range(1<<len(es)):
  adj={i:set() for i in verts}
  for k,(i,j) in enumerate(es):
   if gm>>k&1:adj[i].add(j);adj[j].add(i)
  seen={verts[0]};stack=[verts[0]]
  while stack:
   for v in adj[stack.pop()]:
    if v not in seen:seen.add(v);stack.append(v)
  if len(seen)==len(verts):connected.append(gm)
 val=0j
 for conf in itertools.product(range(3),repeat=len(verts)):
  c=dict(zip(verts,conf));ws=math.prod(weights[t] for t in conf)
  fs=[cmath.exp(-z*W[i,j][c[i]][c[j]])-1 for i,j in es]
  val+=ws*sum(math.prod(fs[k] for k in range(len(es)) if gm>>k&1) for gm in connected)
 activity[mask]=val
memo={0:1+0j}
def Xi(mask):
 if mask in memo:return memo[mask]
 bit=mask&-mask
 val=Xi(mask^bit)
 for sm,w in activity.items():
  if sm&bit and sm&mask==sm:val+=w*Xi(mask^sm)
 memo[mask]=val;return val
poly=Xi((1<<n)-1)
out=dict(N=n,s=float(s),a=float(a),z_real=z.real,z_imag=z.imag,direct=[direct.real,direct.imag],polymer=[poly.real,poly.imag],absolute_error=abs(direct-poly),note='Exact finite-spin graph identity using three-point product quadrature; not a quadrature accuracy assertion.')
Path('polymer_identity_check.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(out)
