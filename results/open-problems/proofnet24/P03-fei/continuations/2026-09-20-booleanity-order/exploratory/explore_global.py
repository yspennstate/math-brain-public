import numpy as np, numba as nb, json, math
from pathlib import Path

@nb.njit
def fwht(a):
 a=a.copy(); h=1
 while h<a.size:
  for k in range(0,a.size,2*h):
   for j in range(h):
    u=a[k+j];v=a[k+j+h];a[k+j]=u+v;a[k+j+h]=u-v
  h*=2
 return a
@nb.njit
def ent(x):
 return -x*np.log2(x) if x>0 else 0.
@nb.njit
def metrics(a):
 N=len(a);n=int(np.log2(N));p=(a/N)**2
 H=0.;B=0.;J=0.;minrat=1e100;sumd=0.;Z=0.
 for q in p:H+=ent(q)
 for i in range(n):
  Ii=0.;Bi=0.;di=0.
  for s in range(N):
   if s&(1<<i):Ii+=p[s]
   else:
    t=s|(1<<i);Bi+=ent(p[s])+ent(p[t])-ent(p[s]+p[t])
    di+=ent(p[s])+ent(p[t])-0.5*(ent(((a[s]+a[t])/N)**2)+ent(((a[s]-a[t])/N)**2))
  Ji=min(Ii,1-Ii);J+=Ji;B+=Bi;sumd+=di;Z+=di-Bi
  if Ji>1e-14:minrat=min(minrat,di/Ji)
 return np.array([H,B,J,minrat,sumd,Z])
@nb.njit
def enum4():
 n=4;N=1<<n; best=np.zeros(4);codes=np.zeros(4,np.int64)
 for code in range(1<<N):
  f=np.ones(N)
  for x in range(N):
   if code&(1<<x): f[x]=-1
  m=metrics(fwht(f));j=m[2]
  if j<1e-14:continue
  vals=np.array([m[0]/j,m[1]/j,m[3],m[5]/j])
  for k in range(4):
   if vals[k]>best[k]:best[k]=vals[k];codes[k]=code
 return best,codes
@nb.njit
def anneal(n,mode,steps,seed):
 np.random.seed(seed);N=1<<n;x=np.arange(N);par=np.zeros(N)
 for t in range(N):
  q=t;c=0
  while q: c^=q&1;q>>=1
  par[t]=1-2*c
 glob=-1.;bestf=np.ones(N);accepted=0;evals=0
 for rep in range(8):
  # Vary initialization between sparse defects, thresholds, and random tables.
  f=np.ones(N)
  for t in range(N):
   if rep%3==0:
    if np.random.random()<0.025:f[t]=-1
   elif rep%3==1:
    if np.random.random()<0.2:f[t]=-1
   else:
    if np.random.random()<0.5:f[t]=-1
  a=fwht(f);m=metrics(a)
  val=m[mode]/m[2] if m[2]>1e-14 else 0
  if mode==3:val=m[3]
  for k in range(steps):
   u=np.random.randint(N);b=a.copy()
   for s in range(N):b[s]-=2*f[u]*par[s&u]
   mm=metrics(b);evals+=1
   if mm[2]<1e-14:continue
   vv=mm[mode]/mm[2]
   if mode==3:vv=mm[3]
   temp=0.1*(1-k/steps)**3+0.00001
   if vv>=val or np.random.random()<np.exp((vv-val)/temp):
    f[u]=-f[u];a=b;val=vv;accepted+=1
   if val>glob:glob=val;bestf=f.copy()
 return glob,bestf,evals,accepted

if __name__=='__main__':
 best,codes=enum4();out={'status':'EXPLORATORY_FLOATING_POINT','n4_maxima':dict(zip(['H_over_J','B_over_J','min_decrement_over_j','JS_over_J'],best.tolist())),'n4_codes':codes.tolist(),'anneal':[]}
 for n in (5,6,7,8):
  val,f,e,a=anneal(n,1,2500,20260920+n)
  m=metrics(fwht(f));row={'n':n,'objective':'B/J','value':val,'metrics':m.tolist(),'negative_indices':np.flatnonzero(f<0).tolist(),'evaluations':e,'acceptances':a}
  out['anneal'].append(row);print(n,val,m,flush=True)
 Path(__file__).with_name('exploratory_global.json').write_text(json.dumps(out,indent=2)+'\n')
 print(out['n4_maxima'])
