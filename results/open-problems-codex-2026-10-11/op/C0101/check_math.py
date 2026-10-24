from fractions import Fraction as F
from itertools import product
import random,json,time,math
from pathlib import Path
R=Path(__file__).parent
random.seed(101)
start=time.time()
def p(A,x):
 return sum(A[i][i]*x[i]*(x[i]-1)//2 for i in range(len(x)))+sum(A[i][j]*x[i]*x[j] for i in range(len(x)) for j in range(i+1,len(x)))
def q(A,x):return sum(F(A[i][j],2)*x[i]*x[j] for i in range(len(x)) for j in range(len(x)))
def delta(fun,x):
 ans=-2*len(x)*fun(x)
 for i in range(len(x)):
  for s in [-1,1]:
   y=list(x);y[i]+=s;ans+=fun(y)
 return ans
nc=0
for d in [1,2,3,4,5,6]:
 for _ in range(80):
  A=[[0]*d for _ in range(d)]
  for i in range(d):
   for j in range(i,d):A[i][j]=A[j][i]=random.randrange(-9,10)
  x=tuple(random.randrange(-20,21) for _ in range(d))
  assert delta(lambda y:p(A,y),x)==sum(A[i][i] for i in range(d))
  assert F(p(A,x))-q(A,x)==-sum(F(A[i][i]*x[i],2) for i in range(d))
  nc+=1
def primitive(a,n):
 if n>=0:return sum(math.floor(a*k) for k in range(n))
 return -sum(math.floor(a*k) for k in range(n,0))
nf=0
for den in range(1,14):
 for num in range(-30,31):
  a=F(num,den)
  for n in range(-35,36):
   assert primitive(a,n+1)-primitive(a,n)==math.floor(a*n)
   b=primitive(a,n+1)+primitive(a,n-1)-2*primitive(a,n)
   assert b<=math.ceil(a)
   assert abs(F(primitive(a,n))-a*n*(n-1)/2)<=abs(n)
   nf+=1
old=delta(lambda x:math.ceil(F(x[0]*x[0],4)),(0,))
assert old==2 and old>F(3,2)
out={'integer_quadratic_checks':nc,'floor_increment_checks':nf,'old_rounding_counterexample':{'a':'1/2','x':0,'laplacian':old,'claimed_upper_bound':'3/2'},'elapsed_seconds':time.time()-start,'all_passed':True}
(R/'math_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(out,flush=True)
