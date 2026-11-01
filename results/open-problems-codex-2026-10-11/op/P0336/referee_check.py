import itertools,math,json,pathlib
import numpy as np
from scipy.optimize import linear_sum_assignment
rng=np.random.default_rng(2336);checks=[]
for n in range(2,8):
 a=rng.random((n,2));b=rng.random((n,2));b[:,0]+=2
 d=b[None,:,0]-a[:,None,0];h=b[None,:,1]-a[:,None,1]
 cost=np.hypot(d,h);e=h*h/(cost+d);q=h*h/(2*d);C=math.sqrt(10)+3
 i,j=linear_sum_assignment(e)
 values=[]
 for p in itertools.permutations(range(n)):
  p=np.array(p);values.append(float(np.mean(cost[np.arange(n),p])))
 opt=float(np.mean(cost[i,j]));best=min(values)
 assert abs(opt-best)<1e-12
 assert np.max(np.abs(e-(cost-d)))<1e-14
 assert np.all(e+1e-15>=h*h/C)
 assert np.all(e<=h*h/2+1e-15)
 assert np.all(q-e>=-1e-15)
 assert np.all(q-e<=h**4/(8*d**3)+1e-15)
 ia=np.argsort(a[:,1]);ib=np.argsort(b[:,1]);sn=float(np.mean((a[ia,1]-b[ib,1])**2));en=float(np.mean(e[i,j]));vn=float(np.mean(h[i,j]**2))
 assert sn/C<=en+1e-14 and en<=sn/2+1e-14
 assert sn<=vn+1e-14 and vn<=C*en+1e-14
 checks.append({'n':n,'permutations':math.factorial(n),'cost':opt,'excess':en,'sorted_vertical_quadratic':sn,'optimizer_vertical_quadratic':vn,'passed':True})
out={'finite_assignments':checks,'constant_C':math.sqrt(10)+3,'constant_L':math.log(27/16),'lower_excess_coefficient':1/(3*(math.sqrt(10)+3)),'upper_excess_coefficient':math.log(27/16)/6,'lower_vertical_coefficient':1/3,'upper_vertical_coefficient':(math.sqrt(10)+3)*math.log(27/16)/6,'note':'Floating-point checks corroborate algebra; they are not substitutes for proofs.'}
pathlib.Path('referee_checks.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
