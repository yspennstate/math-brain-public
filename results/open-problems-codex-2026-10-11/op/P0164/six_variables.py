from itertools import combinations
from collections import Counter
from pathlib import Path
import json,numpy as np
n=6;N=64
pairs=[x for x in range(N) if x.bit_count()==2]
triple_reps=[x for x in range(N) if x.bit_count()==3 and x<63-x]
deg=[x.bit_count() for x in range(N)]

def spectrum(f):
 a=list(f);h=1
 while h<N:
  for i in range(0,N,2*h):
   for j in range(h):u,v=a[i+j],a[i+j+h];a[i+j],a[i+j+h]=u+v,u-v
  h*=2
 W=[0]*7
 for s,c in enumerate(a):W[deg[s]]+=c*c
 return tuple(W)

functions={};family_count=0;stats=Counter()
for m in range(1<<len(pairs)):
 E=[pairs[j] for j in range(len(pairs)) if m>>j&1]
 if any(a&b==0 for a,b in combinations(E,2)):continue
 family_count+=1
 fixed={};free=[]
 for a in triple_reps:
  b=63-a;wa=any(e&a==e for e in E);wb=any(e&b==e for e in E)
  assert not(wa and wb)
  if wa or wb:fixed[a]=1 if wa else -1
  else:free.append(a)
 for flags in range(1<<len(free)):
  f=[-1]*N
  for x in range(N):
   if deg[x]>=5:f[x]=1
   elif deg[x]==4:f[x]=1 if 63-x not in E else -1
   elif deg[x]==2:f[x]=1 if x in E else -1
  for a,val in fixed.items():f[a]=val;f[63-a]=-val
  for j,a in enumerate(free):f[a]=1 if flags>>j&1 else -1;f[63-a]=-f[a]
  assert all(f[63-x]==-f[x] for x in range(N))
  assert all(f[x]<=f[x|(1<<i)] for x in range(N) for i in range(n))
  assert tuple(f) not in functions
  w=spectrum(f);assert sum(w)==4096;assert not any(w[k] for k in [0,2,4,6])
  functions[tuple(f)]=(w,E,flags)
for i in range(n):
 f=tuple(1 if x>>i&1 else -1 for x in range(N));functions[f]=(spectrum(f),None,None)
rows={}
for f,(w,E,flags) in functions.items():
 stats[w]+=1;rows.setdefault(w,dict(spectrum=list(w),denominator=4096,E=E,positive_masks=[x for x in range(N) if f[x]>0]))
rs=np.linspace(.0001,.9999,10000)
for w,row in rows.items():
 row['count']=stats[w];gap=sum(w[k]/4096*rs**k for k in range(7))-2/np.pi*np.arcsin(rs)
 row['min_grid_gap']=float(gap.min());row['rho_at_min']=float(rs[gap.argmin()])
result=dict(n=6,pair_families=family_count,function_count=len(functions),spectra=sorted(rows.values(),key=lambda x:x['spectrum']))
Path('six_spectra.json').write_text(json.dumps(result,indent=2),encoding='utf8')
Path('six_truth_tables.json').write_text(json.dumps([dict(positive_masks=[x for x in range(N) if f[x]>0],spectrum=w) for f,(w,E,flags) in functions.items()]),encoding='utf8')
print('families',family_count,'functions',len(functions),'spectra',len(rows))
for row in result['spectra']:print(row['spectrum'],row['count'],row['min_grid_gap'])
