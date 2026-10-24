import itertools,math,random,json
from pathlib import Path
rng=random.Random(8008)
inside=[(0,0),(1,0),(0,1),(1,1)];ids={x:i for i,x in enumerate(inside)}
edges=[];boundary=set()
for x in inside:
 for axis,delta in enumerate([(1,0),(0,1)]):
  for sign in [-1,1]:
   y=(x[0]+sign*delta[0],x[1]+sign*delta[1])
   if y in ids:
    if sign==1:edges.append((x,y,axis))
   else:
    boundary.add(y); edges.append((y,x,axis) if sign==-1 else (x,y,axis))
boundary=sorted(boundary); configs=list(itertools.product(range(-2,3),repeat=4));beta=[1,3]
def H(z,b):
 def v(x):return z[ids[x]] if x in ids else b[x]
 return sum(beta[i]*abs(v(y)-v(x)) for x,y,i in edges)
rows=[]
for trial in range(100):
 b={y:rng.randrange(-3,4) for y in boundary};bp={y:rng.randrange(-3,4) for y in boundary}
 D=sum(beta[i]*abs(b[y]-bp[y]) for x,y,i in edges if y not in ids)+sum(beta[i]*abs(b[x]-bp[x]) for x,y,i in edges if x not in ids)
 a=[H(z,b) for z in configs];c=[H(z,bp) for z in configs]
 maxdiff=max(abs(x-y) for x,y in zip(a,c));assert maxdiff<=D
 logZ=math.log(sum(math.exp(-t) for t in a)); logZp=math.log(sum(math.exp(-t) for t in c));assert abs(logZ-logZp)<=D+1e-12
 rows.append({'trial':trial,'D':D,'max_energy_difference':maxdiff,'log_partition_difference':abs(logZ-logZp)})
result={'seed':8008,'trials':100,'configurations_per_trial':len(configs),'boundary_sites':len(boundary),'couplings':beta,'integer_energy_checks_passed':True,'floating_log_partition_checks_passed':True,'quadratic_failure':[{'z':z,'abs_energy_change':abs(z*z-(z-1)**2)} for z in [1,10,100,1000]],'rows':rows}
Path('experiment_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print({k:v for k,v in result.items() if k!='rows'})
