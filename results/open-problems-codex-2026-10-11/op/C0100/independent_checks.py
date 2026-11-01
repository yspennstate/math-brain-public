import ast,pathlib,json,time
# Load only the finite-box stabilizer definition, without rerunning experiments.
src=pathlib.Path('experiments.py').read_text(encoding='utf-8-sig');tree=ast.parse(src)
func=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='stabilize')
from collections import deque
ns={'deque':deque,'time':time,'start':time.monotonic()};exec(compile(ast.Module(body=[func],type_ignores=[]),'experiments.py','exec'),ns)
stabilize=ns['stabilize']
def independent_parallel(n,R):
 L=2*R+1;s=[[0]*L for _ in range(L)];s[R][R]=n;u=[[0]*L for _ in range(L)];steps=0
 while True:
  q=[[v//4 for v in row] for row in s]
  if not any(any(row) for row in q):break
  for y in range(L):
   for x in range(L):
    k=q[y][x];s[y][x]-=4*k;u[y][x]+=k
    if x:s[y][x-1]+=k
    if x+1<L:s[y][x+1]+=k
    if y:s[y-1][x]+=k
    if y+1<L:s[y+1][x]+=k
  steps+=1
 return sum(s,[]),sum(u,[]),steps
checks=[]
for n in [16,64,256,1024]:
 R=int(n**.5)+3;L=2*R+1;a=[0]*L**2;a[R*L+R]=n
 s,u,_=stabilize(a,L);s2,u2,steps=independent_parallel(n,R)
 assert s==s2 and u==u2
 for y in range(L):
  for x in range(L):
   i=y*L+x;lap=-4*u[i]+(u[i-1] if x else 0)+(u[i+1] if x+1<L else 0)+(u[i-L] if y else 0)+(u[i+L] if y+1<L else 0)
   assert s[i]==lap+(n if x==R and y==R else 0)
 checks.append(dict(n=n,parallel_steps=steps,configuration_and_odometer_equal=True,laplacian_identity=True))
pathlib.Path('independent_checks.json').write_text(json.dumps(checks,indent=2));print(json.dumps(checks,indent=2))
