from collections import deque
from fractions import Fraction
import itertools,json,pathlib,time
out={};start=time.monotonic()
def line(n):
 s={0:n};u={};q=deque([0])
 while q:
  x=q.popleft();k=s.get(x,0)//2
  if not k:continue
  s[x]-=2*k;u[x]=u.get(x,0)+k
  for y in [x-1,x+1]:
   s[y]=s.get(y,0)+k
   if s[y]>=2:q.append(y)
 return {x:v for x,v in s.items() if v},u
for n in range(1,201):
 s,u=line(n);k=n//2;expected={x:1 for x in range(-k,k+1) if n%2 or x!=0}
 assert s==expected
 for x in range(-k-2,k+3):
  expected_u=(k-abs(x))*(k-abs(x)+1)//2 if abs(x)<=k else 0
  assert u.get(x,0)==expected_u
out['one_dimensional']={'n_range':[1,200],'exact_height_and_odometer_formula':True}
L=3
for model in ['constant2','checkerboard13']:
 s=[2 if model=='constant2' else 1+2*((i//L+i%L)%2) for i in range(L*L)]
 for bits in range(1,1<<(L*L)):
  X={i for i in range(L*L) if bits>>i&1};witness=False
  for i in X:
   y,x=divmod(i,L);neighbors=[j for j in X if abs(j//L-y)+abs(j%L-x)==1]
   if s[i]>=len(neighbors):witness=True;break
  assert witness
out['recurrence_obstruction']={'L':L,'nonempty_subsets_each':511,'both_recurrent':True}
for weights in itertools.product(range(5),repeat=4):
 if not sum(weights):continue
 p0,p1,p2,p3=[Fraction(x,sum(weights)) for x in weights]
 m1=p1+2*p2+3*p3;m2=p2+3*p3;m3=p3
 assert [1-m1+m2-m3,m1-2*m2+3*m3,m2-3*m3,m3]==[p0,p1,p2,p3]
out['moment_inversion']={'weight_vectors':624,'exact_rational_checks':True}
out['seconds']=time.monotonic()-start
pathlib.Path('finite_checks.json').write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps(out,indent=2))
