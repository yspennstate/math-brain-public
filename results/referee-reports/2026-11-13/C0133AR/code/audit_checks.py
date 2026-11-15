"""Independent finite audits of history conditioning and pathwise counts."""
import itertools,json,os,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
D=((1,0),(-1,0),(0,1),(0,-1))
STACKS=(((.7,.1,.1,.1),(.1,.6,.2,.1),(.2,.1,.3,.4)),
        ((.1,.2,.4,.3),(.6,.1,.1,.2),(.15,.65,.1,.1)))

def likelihood(path,offset=None):
 # Independently average a complete path likelihood over two latent stack
 # types at each site. Never replace posterior stacks by prior stacks.
 counts=dict(offset or {});products={}
 for a,b in zip(path,path[1:]):
  idx=counts.get(a,0);counts[a]=idx+1
  step=D.index((b[0]-a[0],b[1]-a[1]));v=products.setdefault(a,[1.,1.])
  for typ in (0,1):v[typ]*=STACKS[typ][idx%3][step]
 return math.prod((v[0]+v[1])/2 for v in products.values())

def continuations(start,limit,target,strict=False):
 def visit(p):
  if p[-1][0]==target:yield p;return
  if len(p)-1==limit:return
  for dx,dy in D:
   q=(p[-1][0]+dx,p[-1][1]+dy)
   if strict and q[0]<=0:continue
   yield from visit(p+[q])
 yield from visit([start])

def prefix_audit():
 rows=[];H=7;L=3
 for eta in [[(-1,0),(0,0)],[(-1,0),(-2,0),(-1,0),(0,0)]]:
  eta_weight=likelihood(eta)
  for c in (0,1,2):
   direct=0.
   for future in continuations((0,0),H,L):
    last=max(i for i,x in enumerate(future) if x[0]==0)
    if last<=c:direct+=likelihood(eta+future[1:])/eta_weight
   grouped=0.;bound=0.;false_independence=0.
   for length in range(c+1):
    for choices in itertools.product(range(4),repeat=length):
     p=[(0,0)]
     for a in choices:p.append((p[-1][0]+D[a][0],p[-1][1]+D[a][1]))
     if p[-1][0]!=0:continue
     offset={}
     for x in p[:-1]:offset[x]=offset.get(x,0)+1
     qmean=0.
     for future in continuations(p[-1],H-length,L,strict=True):
      grouped+=likelihood(eta+p[1:]+future[1:])/eta_weight
      qmean+=likelihood(future,offset)
     bound+=qmean
     false_independence+=likelihood(eta+p[1:])/eta_weight*qmean
   assert abs(direct-grouped)<1e-12
   assert direct<=bound+1e-12
   rows.append(dict(eta=eta,c=c,direct=direct,grouped=grouped,bound=bound,
    invalid_product_of_marginals=false_independence))
 assert any(abs(r["direct"]-r["invalid_product_of_marginals"])>1e-5 for r in rows)
 return rows

def counting_audit():
 paths=checks=0
 for increments in itertools.product((-1,0,1),repeat=9):
  x=[0]
  for a in increments:x.append(x[-1]+a)
  top=max(x)
  if top<2:continue
  paths+=1;T={m:x.index(m) for m in range(top+1)}
  for L in range(1,min(top,4)+1):
   M=top-L;sets=[];h=[]
   for m in range(M+1):
    a=[t for t in range(T[m],T[m+L]) if x[t]==m];sets.append(a);h.append(a[-1]-T[m])
   assert sum(map(len,sets))<=T[M+L]
   assert sum(h)<=L*T[M+L]
   for m,a in enumerate(sets):
    if L<top-m:
     b=[t for t in range(T[m],T[m+L+1]) if x[t]==m]
     assert set(a)<=set(b)
     if a[-1]<b[-1]:assert len(a)<len(b)
   checks+=1
 return dict(projected_paths=paths,width_checks=checks,path_length=9)

if __name__=="__main__":
 if os.getpriority(os.PRIO_PROCESS,0)<10:os.setpriority(os.PRIO_PROCESS,0,10)
 result=dict(prefix=prefix_audit(),counting=counting_audit(),nice=os.getpriority(os.PRIO_PROCESS,0))
 (ROOT/"data/audit_checks.json").write_text(json.dumps(result,indent=2))
 print(json.dumps(result,indent=2))
