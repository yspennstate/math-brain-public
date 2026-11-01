import time,math,json,numpy as np
from sandpile_experiment import stabilize,check
for H in [0,-1]:
 n=262144;R=math.ceil(math.sqrt(n))+8;t=time.perf_counter();a,u,steps=stabilize(n,H,R);check(n,H,a,u,R)
 y,x=np.nonzero(u);x=x-R;y=y-R;ax=int(x.max());diag=int((x+y).max())
 row=dict(H=H,n=n,sites=len(x),axis=ax,diag_integer=diag,diag_axis_ratio=diag/(math.sqrt(2)*ax),steps=steps,seconds=time.perf_counter()-t)
 for theta in [0,math.pi/12,math.pi/6,math.pi/4]:row['support_'+str(round(theta*180/math.pi))]=float(np.max(x*math.cos(theta)+y*math.sin(theta))/math.sqrt(n))
 with open('experiments/results.jsonl','a',encoding='utf8') as f:f.write(json.dumps(row)+'\n')
 np.savez_compressed(f'experiments/H{H}_n{n}.npz',height=a,odometer=u,R=R)
 print(json.dumps(row),flush=True)
