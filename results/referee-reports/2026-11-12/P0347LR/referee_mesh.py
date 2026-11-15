"""Fresh Riemann-mesh/endpoint stress checks, independent of finite tree recursion."""
import os
for v in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[v]='1'
import json,math
import numpy as np
z=math.pi**2/6
result=[]
for n in [1000,8000,64000,512000]:
    x=np.arange(1,n,dtype=float)/n;y=1-x;lx=np.log(x);ly=np.log1p(-x)
    measure=1/(2*n*x*y);g=(x*lx+y*ly)/z;L=math.log(n)
    endpoint=(x<n**(-.5))|(y<n**(-.5))
    row={'n':n,'entropy_mass':float(np.sum(-g*measure)),'defects':{},'shrinking_endpoint_mass':{}}
    for k in range(2,7):
        defect=1-x**k*(1+lx/L)**k-y**k*(1+ly/L)**k
        row['defects'][str(k)]=float(np.sum(defect*measure))
    kernels={'g_abs':-g,'g2':g*g,'cross22':x*x*y*y,'linear_k3':g*(x*x+y*y-1)}
    for name,kernel in kernels.items():row['shrinking_endpoint_mass'][name]=float(np.sum((kernel*measure)[endpoint]))
    result.append(row)
json.dump(result,open('referee_mesh.json','w'),indent=2)
print(json.dumps(result,indent=2))
