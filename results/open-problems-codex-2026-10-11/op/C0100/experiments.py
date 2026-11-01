import json,time,math,pathlib
from collections import deque
P=pathlib.Path('.'); start=time.monotonic()
def stabilize(a,L):
 a=list(a);u=[0]*(L*L); q=deque(i for i,v in enumerate(a) if v>=4);inq=bytearray(L*L)
 for i in q:inq[i]=1
 actions=0
 while q:
  i=q.popleft();inq[i]=0;k=a[i]//4
  if not k:continue
  a[i]-=4*k;u[i]+=k;row,col=divmod(i,L)
  for z in ((i-L if row else -1),(i+L if row+1<L else -1),(i-1 if col else -1),(i+1 if col+1<L else -1)):
   if z<0:continue
   a[z]+=k
   if a[z]>=4 and not inq[z]:q.append(z);inq[z]=1
  actions+=1
  if actions%100000==0 and time.monotonic()-start>240:raise TimeoutError('240 second experiment cap')
 return a,u,actions
with open('experiments.jsonl','w',encoding='utf8') as out:
 for n in [256,1024,4096,16384]:
  R=math.ceil(math.sqrt(n))+3;L=2*R+1;a=[0]*(L*L);a[R*L+R]=n;s,u,actions=stabilize(a,L)
  assert sum(s)==n and max(s)<4 and min(s)>=0
  assert not any(u[i] for i in range(L*L) if i//L in [0,L-1] or i%L in [0,L-1])
  stats=[]
  for cx,cy,r in [(0,0,.2),(0,0,.5),(.25,.25,.1)]:
   h=[0]*4
   for i,v in enumerate(s):
    y,x=divmod(i,L);x=(x-R)/math.sqrt(n);y=(y-R)/math.sqrt(n)
    if (x-cx)**2+(y-cy)**2<r*r:h[v]+=1
   stats.append(dict(ball=[cx,cy,r],count=sum(h),fractions=[v/sum(h) for v in h]))
  row=dict(model='point_source_Z2',n=n,L=L,actions=actions,total_topplings=sum(u),mass=sum(s),balls=stats,seconds=time.monotonic()-start)
  out.write(json.dumps(row)+'\n');out.flush();print(json.dumps(row),flush=True)
 for L in [9,18,36,72]:
  m=[3]*(L*L);t,_,_=stabilize([6]*(L*L),L);e,_,actions=stabilize([6-v for v in t],L)
  ee,_,_=stabilize([2*v for v in e],L);assert ee==e
  b=[int(i//L==0)+int(i//L==L-1)+int(i%L==0)+int(i%L==L-1) for i in range(L*L)]
  burn,bu,_=stabilize([e[i]+b[i] for i in range(L*L)],L);assert burn==e and all(v==1 for v in bu)
  h=[e.count(j)/(L*L) for j in range(4)];row=dict(model='wired_square_identity',L=L,fractions=h,idempotence=True,burning_once=True,seconds=time.monotonic()-start)
  out.write(json.dumps(row)+'\n');out.flush();print(json.dumps(row),flush=True)
