from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json,time
root=Path(__file__).resolve().parents[1];start=time.monotonic();checks=0
def test(b):
 global checks
 checks+=1
 if not b:raise AssertionError(checks)
 if time.monotonic()-start>55:raise TimeoutError('frozen cap')
def chars(t):return [F(sum(t[x]*(1 if (x&s).bit_count()%2==0 else -1) for x in range(len(t))),len(t)) for s in range(len(t))]
@lru_cache(maxsize=2048)
def natural(x):
 k=0
 while x>=2:x/=2;k+=1
 while x<1:x*=2;k-=1
 def atanh(t):
  v=(t-1)/(t+1);power=v;total=F(0)
  for j in range(20):total+=2*power/(2*j+1);power*=v*v
  return total,total+2*power/(41*(1-v*v))
 a,b=atanh(x);c,d=atanh(F(2));return a+k*(c if k>=0 else d),b+k*(d if k>=0 else c)
def ce(p,q):
 lo=hi=F(0)
 for a,b in zip(p,q):
  if a:
   test(b>0);x,y=natural(1/b);lo+=a*x;hi+=a*y
 l,h=natural(F(2));return lo/h,hi/l
def rank(matrix):
 a=[list(r) for r in matrix];row=0
 for col in range(len(a[0])):
  p=next((i for i in range(row,len(a)) if a[i][col]),None)
  if p is None:continue
  a[row],a[p]=a[p],a[row];z=a[row][col];a[row]=[x/z for x in a[row]]
  for i in range(len(a)):
   if i!=row and a[i][col]:
    z=a[i][col];a[i]=[u-z*v for u,v in zip(a[i],a[row])]
  row+=1
  if row==len(a):break
 return row
profiles=[]
for m in [2,3,5]:
 L=2**m;N=L*L
 g=[-1 if (x%(2**m))==(x//(2**m)) else 1 for x in range(N)]
 h=[(-1)**((x%(2**m))&(x//(2**m))).bit_count() for x in range(N)]
 t=[g[x//2] if x%2==0 else h[x//2] for x in range(2*N)]
 ag,ah,af=chars(g),chars(h),chars(t);pg=[x*x for x in ag];ph=[x*x for x in ah];pf=[x*x for x in af]
 u=F(1,N);q=[(a+b)/2 for a,b in zip(pg,ph)]
 r0=sum((u*pg[j]/(2*q[j]) for j in range(N)),F(0));r1=1-r0
 q0=[u*pg[j]/(2*q[j]*r0) for j in range(N)];q1=[u*ph[j]/(2*q[j]*r1) for j in range(N)]
 test(sum(pf)==sum(pg)==sum(ph)==sum(q0)==sum(q1)==1)
 test(all(pf[2*j]+pf[2*j+1]==q[j] for j in range(N)))
 test(rank([[q0[s+L*v] for v in range(L)] for s in range(L)])==L)
 test(rank([[q0[s+L*v] for v in range(1,L)] for s in range(1,L)])==L-1)
 I=F(0)
 for i in range(2*m+1):I+=F(sum(t[x]!=t[x^(1<<i)] for x in range(2*N)),2*N)
 test(4*I-F(1,8)-(2*m+1)==F(7,8)+F(8*m-2,L))
 Gce=ce(pg,q0);Hce=ce(ph,q1)
 test(Gce[0]>m-F(1,2));test(Hce[1]<2*m+1)
 if m>=5:test(Gce[0]-F(16*m,L)>0)
 test(Hce[1]-4*m<0)
 test(any(q0[j]==0 and u>0 for j in range(N)))
 # Exact source-atom Bayes factor: true parent-to-child joint p/2; current reference r*q.
 for j in range(N):
  test(r0*q0[j]+r1*q1[j]==u)
  test(q[j]*(pg[j]/(2*q[j]))==pg[j]/2)
  test(q[j]*(ph[j]/(2*q[j]))==ph[j]/2)
 profiles.append({'m':m,'G_reference_rank':L,'nonempty_minor_rank':L-1,'bad_G_child':m>=5,'both_reference_branch_masses_positive':r0>0 and r1>0})
m=10;L=2**m
test(F(1,8)-F(17*m-1,2*L)==F(87,2048))
test(L>68*m-4)
test(1+F(8*m-2,L)>1) # removing old debit admits every JS<=1 at this query
out={'status':'PASS','profiles':profiles,'exact_assertions':checks,'seconds':time.monotonic()-start,'main_helper_imports':False,'rung':'same-author alternate representation, not peer acceptance'}
(root/'out/independent.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='profiles'}))
