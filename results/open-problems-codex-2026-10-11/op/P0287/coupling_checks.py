from itertools import product
from fractions import Fraction as F
import pathlib,json,random
P=pathlib.Path(__file__).parent;out={}
def jump(x,y):return (0,1) if x==1 and y==0 else (x,y)
local=0
for a,b,x,y in product((0,1),repeat=4):
 aa,bb=jump(a,b);xx,yy=jump(x,y)
 assert (xx-aa)+(yy-bb)==(x-a)+(y-b)
 assert (xx-aa)-(x-a)==int((a,b)==(1,0))-int((x,y)==(1,0))
 if a<=x and b<=y:assert aa<=xx and bb<=yy;local+=1
out['ordered_local_updates']=local

# Exhaustive Boolean identity, including the first-hole and all-ones cases.
runcases=0
for n in range(1,13):
 for w in product((0,1),repeat=n+1):
  prefix=1;s=0
  for j in range(n):prefix*=w[j];s+=prefix*(1-w[j+1])
  tail=prefix*w[n]
  assert w[0]==s+tail
  assert s<=sum(w[j]*(1-w[j+1]) for j in range(n))
  runcases+=1
out['occupied_run_cases']=runcases

# Closed finite windows are used only to test the pathwise conservation law,
# not to approximate a positive-current stationary full-line law.
rng=random.Random(28720261012);events=0
for trial in range(100):
 n=33;center=n//2;k=(F(1,2),F(2),F(8))[trial%3]
 xi=[int(rng.random()<0.3) for _ in range(n)];eta=xi.copy()
 left_x=left_e=right_x=right_e=kills=0
 for step in range(500):
  events+=1
  if rng.random()<float(k)/(n-1+float(k)):
   if eta[center]:eta[center]=0;kills+=1
  else:
   j=rng.randrange(n-1);jx=int(xi[j]==1 and xi[j+1]==0);je=int(eta[j]==1 and eta[j+1]==0)
   xi[j],xi[j+1]=jump(xi[j],xi[j+1]);eta[j],eta[j+1]=jump(eta[j],eta[j+1])
   if j==center-1:left_x+=jx;left_e+=je
   if j==center:right_x+=jx;right_e+=je
  assert all(e<=x for e,x in zip(eta,xi))
  assert sum(x-e for x,e in zip(xi,eta))==kills
  assert left_e-left_x==sum(xi[i]-eta[i] for i in range(center))
  assert right_x-right_e==sum(xi[i]-eta[i] for i in range(center+1,n))
out['pathwise_trials']=100;out['pathwise_events']=events

def solve(A,b):
 n=len(b);A=[row.copy()+[rhs] for row,rhs in zip(A,b)]
 for j in range(n):
  pivot=next(i for i in range(j,n) if A[i][j]);A[j],A[pivot]=A[pivot],A[j]
  z=A[j][j];A[j]=[v/z for v in A[j]]
  for i in range(n):
   if i!=j and A[i][j]:
    z=A[i][j];A[i]=[v-z*w for v,w in zip(A[i],A[j])]
 return [row[-1] for row in A]
finite=[]
for n in (3,5):
 for k in (F(1,2),F(1),F(2),F(8)):
  r=1/(2*(1+k));alpha=r;beta=1-r;M=2**n;center=n//2
  Q=[[F(0) for _ in range(M)] for _ in range(M)]
  for s in range(M):
   moves=[]
   if not s&1:moves.append((s|1,alpha))
   if s&(1<<(n-1)):moves.append((s^(1<<(n-1)),beta))
   if s&(1<<center):moves.append((s^(1<<center),k))
   for j in range(n-1):
    if (s>>j)&3==1:moves.append((s^(3<<j),F(1)))
   for t,rate in moves:Q[s][t]+=rate;Q[s][s]-=rate
  A=[[Q[s][t] for s in range(M)] for t in range(M)];A[-1]=[F(1)]*M;b=[F(0)]*M;b[-1]=1
  pi=solve(A,b);assert min(pi)>0 and sum(pi)==1
  assert all(sum(pi[s]*Q[s][t] for s in range(M))==0 for t in range(M))
  p=[sum(pi[s] for s in range(M) if (s>>j)&1) for j in range(n)]
  J=[sum(pi[s] for s in range(M) if (s>>j)&3==1) for j in range(n-1)]
  q=sum(pi[s] for s in range(M) if (s>>center)&3==3)
  jin=J[center-1];jout=J[center];bound=1/(4*(1+k)**2)
  assert jin>=r*(1-r) and jout>=bound and jout<=r/(1+k)
  assert jin-jout==k*p[center] and p[center]==jout+q and q<=r*r
  # Every occupied-site cylinder obeys the necessary domination moment bound.
  for mask in range(1,M):assert sum(pi[s] for s in range(M) if s&mask==mask)<=r**mask.bit_count()
  finite.append({'n':n,'kappa':str(k),'rho':str(r),'Jleft':str(jin),'Jright':str(jout),'positive_lower_bound':str(bound),'pair_probability':str(q),'all_residuals':'0','domination_moment_checks':M-1})
out['exact_finite_chains']=finite
# Unsynchronized bond clocks would fail the order assumption.
eta=(1,0);xi=jump(1,0);assert eta[0]>xi[0]
out['negative_control_independent_clocks']='order fails, as required'
out['result']='PASS'
(P/'coupling_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps({'result':'PASS','local_ordered_cases':local,'run_cases':runcases,'pathwise_events':events,'exact_chains':len(finite)}))
