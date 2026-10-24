import numpy as np,json,time
from pathlib import Path
rng=np.random.default_rng(4521012)
laws={'constant2':([2],[1.]),'constant3':([3],[1.]),'mix1_5':([1,5],[.6,.4])}
ks=[16,64,256]
def sizes(W,D):
 n=len(D);pref=np.zeros((n,n),dtype=bool)
 for i in range(n):
  ix=np.argpartition(W[i],int(D[i])-1)[:int(D[i])];pref[i,ix]=True
 a,b=np.where(np.triu(pref & pref.T,1));p=np.arange(n);sz=np.ones(n,dtype=int)
 def find(i):
  while p[i]!=i:p[i]=p[p[i]];i=p[i]
  return i
 for i,j in zip(a,b):
  i,j=find(i),find(j)
  if i!=j:p[j]=i;sz[i]+=sz[j]
 return np.array([sz[i] for i in range(n) if find(i)==i])
def tree_at_least(vals,probs,k):
 d=int(rng.choice(vals,p=probs));queue=[(d,rng.gamma(d+1))];count=1;pos=0
 while pos<len(queue):
  m,x=queue[pos];pos+=1
  for _ in range(m):
   d=int(rng.choice(vals,p=probs));z=rng.gamma(d)
   if rng.random()*x<z:
    count+=1
    if count>=k:return True
    queue.append((d-1,z))
 return False
out={'seed':4521012,'graphs':[],'ewt':[]};start=time.monotonic()
for law,(vals,probs) in laws.items():
 for n in [256,512,1024,2048]:
  rows=[]
  for rep in range(8):
   A=rng.random((n,n));W=np.triu(A,1);W+=W.T;np.fill_diagonal(W,np.inf);del A
   D=rng.choice(vals,size=n,p=probs);s=sizes(W,D);del W
   row={'L1':float(max(s)/n)}
   for k in ks:
    large=s[s>=k]/n;S=float(sum(large));row['S'+str(k)]=S;row['Q'+str(k)]=float(S*S-sum(large*large))
   rows.append(row)
  avg={key:float(np.mean([r[key] for r in rows])) for key in rows[0]}
  sd={key:float(np.std([r[key] for r in rows],ddof=1)) for key in rows[0]}
  out['graphs'].append({'law':law,'n':n,'reps':8,'mean':avg,'sd':sd});Path('simulation_results.json').write_text(json.dumps(out,indent=2));print(law,n,avg,flush=True)
 for k in ks:
  reps=3000;phat=float(np.mean([tree_at_least(vals,probs,k) for _ in range(reps)]));out['ewt'].append({'law':law,'k':k,'reps':reps,'probability_estimate':phat,'SE':(phat*(1-phat)/reps)**.5});Path('simulation_results.json').write_text(json.dumps(out,indent=2))
print('seconds',time.monotonic()-start,flush=True)
