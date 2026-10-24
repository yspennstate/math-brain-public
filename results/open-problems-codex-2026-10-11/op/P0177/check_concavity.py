import random,math,json,pathlib
import numpy as np
from scipy.optimize import root
rng=random.Random(177);rows=[]
for trial in range(30):
 n=rng.randint(2,7);x=np.array([rng.gauss(0,1)*10**rng.uniform(-1,3) for _ in range(n)]);w=np.array([10**rng.uniform(-7,0) for _ in range(n)]);w/=w.sum();x-=np.dot(w,x);v=np.dot(w,x*x)
 if not v:continue
 B=(math.sqrt(2)+2)*math.sqrt(v);A=B*B+v;t=7*A*1.01
 def eq(a):
  u,R=a;q=u-x;d=R+q*q
  return [np.dot(w,t/d)-1,np.dot(w,q*(t/d)**2)]
 res=root(eq,[0,t-v],tol=1e-10);u,R=res.x
 zgrid=np.linspace(-B,B,301);curves=np.array([np.dot(w,(R-3*(z-x)**2)/(R+(z-x)**2)**3) for z in zgrid]);lower=R**-2*(1-6*A/R)
 row={'trial':trial,'variance':v,'t':t,'u':u,'R':R,'residual':float(max(abs(np.array(eq(res.x))))),'localized':bool(abs(u)<=B),'min_curvature_integrand_expectation':float(curves.min()),'proved_lower_bound':lower,'bound_holds':bool(float(curves.min())>=lower*(1-1e-10))}
 rows.append(row)
assert all(r['localized'] and r['bound_holds'] for r in rows)
pathlib.Path('concavity_stress.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
print(len(rows),'random atomic laws at 1.01 times the sufficient threshold: localization and strict-concavity bound passed; these finite grids are numerical checks only.')

