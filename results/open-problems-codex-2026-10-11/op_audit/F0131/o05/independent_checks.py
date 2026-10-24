from pathlib import Path
from collections import defaultdict, deque
import random, math, json
ROOT=Path(__file__).resolve().parent
D=((1,0),(-1,0),(0,1),(0,-1))
def nbr(x): return [(x[0]+a,x[1]+b) for a,b in D]
def run(H,n):
 h=defaultdict(lambda:-H); h[0,0]+=n
 u=defaultdict(int); last={}; q=deque([(0,0)]); queued={(0,0)}; clock=0
 while q:
  x=q.popleft(); queued.remove(x); t=h[x]//4
  if t<=0: continue
  h[x]-=4*t; u[x]+=t; clock+=t; last[x]=clock
  for y in nbr(x):
   h[y]+=t
   if h[y]>=4 and y not in queued: q.append(y); queued.add(y)
 sites=set(h)|set(u)
 assert all(h[x]<=3 for x in sites)
 assert sum(h[x]+H for x in sites)==n
 assert all(h[x]==-H+n*(x==(0,0))-4*u[x]+sum(u[y] for y in nbr(x)) for x in list(sites))
 fired={x for x in u if u[x]>0}
 for x in fired:
  assert h[x]>=sum(last.get(y,0)>last[x] for y in nbr(x) if y in fired)
  assert u[x]==u[-x[0],x[1]]==u[x[1],x[0]]
  if x[0]>0: assert u[x]<=u[x[0]-1,x[1]]
  if x[1]>0: assert u[x]<=u[x[0],x[1]-1]
 # Verify reflected candidate directly, including both parity crossing edges.
 for k in range(1,9):
  def v(x): return u[x] if 2*x[0]<=k else min(u[x],u[k-x[0],x[1]])
  test=set(sites)|{(k-x[0],x[1]) for x in sites}
  test|={y for x in list(test) for y in nbr(x)}
  assert all(-H+n*(x==(0,0))-4*v(x)+sum(v(y) for y in nbr(x))<=3 for x in test)
  assert all(v(x)==u[x] for x in test)
 for j in range(12):
  phi={x:random.randrange(8) for x in sorted(fired)}
  edges={tuple(sorted((x,y))) for x in fired for y in nbr(x)}
  rhs=sum(min(phi.get(x,0),phi.get(y,0)) for x,y in edges)
  var=sum(abs(phi.get(x,0)-phi.get(y,0)) for x,y in edges)
  assert 2*rhs==4*sum(phi.values())-var
  assert sum(h[x]*w for x,w in phi.items())>=rhs
 return {'H':H,'n':n,'fired':len(fired),'firings':clock,'checks':'passed'}
random.seed(13105)
out=[run(H,n) for H in [-2,-1,0,1,2] for n in [128,512,2048]]
for k in [2,3,4,10,100,1000000]:
 val=math.sin(math.pi/(2*k)); assert val>1/k
 out.append({'k':k,'sin':val,'one_over_k':1/k})
assert math.isclose(math.sin(5*math.pi/6),.5)
out.append({'H0_polygon_side_lower_bound':2*math.pi/math.asin(1/3)})
try:
 import sympy as s
 r=s.symbols('r',positive=True); f=s.Function('f')(r); F=r**2*f
 expr=s.diff(F,r,2)+s.diff(F,r)/r-4*F/r**2
 assert s.simplify(r**3*expr-s.diff(r**5*s.diff(f,r),r))==0
 t=s.sqrt(3); c=(20+8*t)/13; v=s.Matrix([t/2,s.Rational(1,2)]); P=s.Matrix([[2,1],[1,1]]); B=c*v*v.T
 assert s.simplify(B.det())==0 and s.simplify((P-B).det())==0
 assert 2<float(c)<8/3 and float((P-B)[0,0])>0
 theta,alpha=s.symbols('theta alpha',real=True)
 assert s.integrate(s.cos(2*theta),(theta,-s.pi/4,s.pi/4))==1
 assert s.simplify(s.integrate(s.cos(2*theta),(theta,-alpha/2,alpha/2))-s.sin(alpha))==0
 out.append({'symbolic':'Fourier ODE, angular integrals, matrix determinants passed'})
except ImportError: out.append({'symbolic':'sympy unavailable'})
(ROOT/'independent_checks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2),flush=True)
