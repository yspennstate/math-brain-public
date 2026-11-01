import numpy as np,itertools,json,pathlib,time
rng=np.random.default_rng(36012)
def generate(L,T,b):
 z=rng.random((T,L)); left=z>=(1-b)/2; right=z<(1+b)/2
 left[:,0]=False; right[:,-1]=False
 return left,right

def brute(L,T,left,right):
 paths=[[x] for x in range(0,L,2)]; found=set()
 # Enumerate all terminal paths; dead tails are retained for earlier meetings.
 dead=[]
 for t in range(T):
  new=[]
  for p in paths:
   x=p[-1]; children=[]
   if left[t,x]: children.append(p+[x-1])
   if right[t,x]: children.append(p+[x+1])
   if children: new.extend(children)
   else: dead.append(p)
  paths=new
 for p,q in itertools.combinations(paths+dead,2):
  if p[0]>q[0] or (p[0]==q[0] and len(p)>1 and len(q)>1 and p[1]>q[1]): p,q=q,p
  for t in range(1,min(len(p),len(q))):
   if p[t]==q[t]:
    if p[0]<q[0] or t>1:
     if all(p[u]<q[u] for u in range(1,t)): found.add((p[t],t))
    break
   if p[t]>q[t]: break
 return found

def dp(L,T,left,right):
 occ=np.zeros(L,bool); occ[::2]=True
 # Diagonal at time zero permits distinct children from the same source.
 A=np.triu(occ[:,None]&occ[None,:]); found=set()
 for t in range(T):
  l=left[t]; r=right[t]
  k=np.arange(L-2); meets=A[k,k+2]&r[k]&l[k+2]
  found.update((int(x)+1,t+1) for x in k[meets])
  B=np.zeros_like(A)
  z=A&r[:,None]&r[None,:]; B[1:,1:]|=z[:-1,:-1]
  z=A&r[:,None]&l[None,:]; B[1:,:-1]|=z[:-1,1:]
  z=A&l[:,None]&r[None,:]; B[:-1,1:]|=z[1:,:-1]
  z=A&l[:,None]&l[None,:]; B[:-1,:-1]|=z[1:,1:]
  A=np.triu(B,1)
 return found

n=200; total=0
for k in range(n):
 L=int(rng.integers(5,10)); T=int(rng.integers(2,6)); b=float(rng.choice([0.,.1,.3,.7,1.])); l,r=generate(L,T,b)
 a=brute(L,T,l,r); d=dp(L,T,l,r)
 assert a==d,(k,a,d)
 total+=len(a)
print('brute/DP agreement',n,'cases;',total,'meeting sites')
pathlib.Path('dp_checks.json').write_text(json.dumps({'seed':36012,'trials':n,'total_sites':total,'mismatches':0,'model':'finite planar nearest-neighbour arrows with linear interpolation','memory':'one L by L Boolean matrix and temporaries; L<=9'},indent=2),encoding='utf8')
# Fresh small scaling diagnostic. These are numerical observations only.
with pathlib.Path('scaling_samples.jsonl').open('w',encoding='utf8') as f:
 for h in [.1,.05,.025]:
  for sample in range(3):
   started=time.monotonic(); half=3.; L=int(round(2*half/h))+1; T=int(round(.5/h**2)); l,r=generate(L,T,h)
   out=dp(L,T,l,r); count=sum(abs((x-(L-1)/2)*h)<=1 and .1<=t*h*h<=.5 for x,t in out)
   z={'h':h,'sample':sample,'count':count,'L':L,'steps':T,'seconds':time.monotonic()-started,'boundary':'killed at +/-3','window':'[-1,1] x [0.1,0.5]'}
   f.write(json.dumps(z)+'\n'); f.flush(); print(json.dumps(z),flush=True)
