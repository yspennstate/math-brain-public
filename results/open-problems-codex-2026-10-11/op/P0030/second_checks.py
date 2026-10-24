import math,json,pathlib,random
from fractions import Fraction as F

def fill(f,perm,maxsteps=1000):
 n=len(f);a=list(f);b=[F(1)]*n;dest=[F(0)]*n;source=[F(0)]*n;orbit=list(range(n))
 for step in range(maxsteps):
  h=[min(x,y) for x,y in zip(a,b)]
  for i in range(n):source[i]+=h[orbit[i]]
  dest=[d+x for d,x in zip(dest,h)]
  b=[x-y for x,y in zip(b,h)]
  left=[x-y for x,y in zip(a,h)];an=[F(0)]*n
  for i in range(n):an[perm[i]]=left[i]
  a=an;orbit=[perm[i] for i in orbit]
  assert sum(a)==sum(b)
  if sum(b)==0:
   assert source==f and dest==[F(1)]*n
   return dict(steps=step+1,residual=0,exact_source_rows=True,exact_uniform_destination=True)
 return dict(steps=maxsteps,residual=str(sum(b)/n),source_mass=str(sum(a)/n))

rng=random.Random(300012);cases=[]
for n in [2,3,4,5,8,13,23]:
 for j in range(20):
  w=[rng.randrange(0,15) for _ in range(n)]
  if not sum(w):w[0]=1
  f=[F(n*x,sum(w)) for x in w]
  r=fill(f,[(i+1)%n for i in range(n)])
  assert r['residual']==0;cases.append(r)
control=fill([F(0)]*4+[F(2)]*4,[1,2,3,0,5,6,7,4],maxsteps=50)
assert control['residual']=='1/2'

# Exact finite-product Hellinger identity evaluated by full binary enumeration.
# Reference coordinates are fair bits; densities are 1 +/- e_i.
eps=[.2/(i+1) for i in range(10)];errors=[]
for n,m in [(1,3),(2,7),(5,10),(9,10)]:
 overlap=0
 for bits in range(1<<m):
  fn=fm=1.
  for i in range(m):
   fact=1+(eps[i] if (bits>>i)&1 else -eps[i]);fm*=fact
   if i<n:fn*=fact
  overlap+=math.sqrt(fn*fm)/(1<<m)
 rho=[(math.sqrt(1+e)+math.sqrt(1-e))/2 for e in eps]
 exact=math.prod(rho[n:m]);err=abs(overlap-exact);assert err<1e-12;errors.append(err)

# Numerical integration for the concrete Brownian stopping example; no simulated paths needed.
N=40000;step=18/N
normal=lambda z: math.exp(-z*z/2)/math.sqrt(2*math.pi)
def trap(g):
 return step*(.5*g(-9)+sum(g(-9+i*step) for i in range(1,N))+.5*g(9))
c=trap(lambda z:z*math.tanh(z)*normal(z))
aff=[]
for e in [.125,.0625,.03125,.015625]:
 rho=trap(lambda z:.5*(math.sqrt(1+2*e*math.tanh(z))+math.sqrt(1-2*e*math.tanh(z)))*normal(z))
 assert 0<=1-rho<=2*e*e+1e-12
 aff.append(dict(epsilon=e,deficiency=1-rho,bound=2*e*e))
# Reproduce the original-join bias by independent Gaussian increments.
count=200000;vals=[]
sm=sm2=0.
for _ in range(count):
 z=rng.gauss(0,1);d=rng.gauss(0,1);v=rng.random();y=-z if v<=.5+.0625*math.tanh(z) else -d
 sm+=y;sm2+=y*y
mean=sm/count;se=math.sqrt(max(0,sm2/count-mean*mean)/count);target=-c/16
assert abs(mean-target)<5*se
result=dict(filling=dict(ergodic_cycles_checked=len(cases),maximum_steps=max(x['steps'] for x in cases),result='exact Fraction arithmetic PASS',nonergodic_negative_control=control),product_identity=dict(full_enumeration_cases=len(errors),max_absolute_error=max(errors)),example=dict(normal_integral_Z_tanh_Z=c,backward_increment_mean_exact_integral=target,affinity_checks=aff,monte_carlo_count=count,monte_carlo_mean=mean,standard_error=se))
pathlib.Path('second_checks.json').write_text(json.dumps(result,indent=2),encoding='utf8');print(json.dumps(result,indent=2))
