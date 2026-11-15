import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,math,itertools,json,time,resource
from audit import calc,truth,entropy,info
from pathlib import Path
start=time.time();lookup=[[(np.zeros(2),np.zeros(2)) for policy in range(2)]];out={}
for n in range(1,5):
    count=1<<(1<<n);codes=np.arange(count,dtype=np.uint64);f=truth(codes,n);o=calc(f);pol=[]
    for policy in [0,1]:
        chosen=np.argmax(o['Inf'] if policy==0 else o['D'],1);ht=np.zeros(count);it=np.zeros(count)
        for i in range(n):
            jj=np.flatnonzero(chosen==i);cc=codes[jj];other=[x for x in range(n) if x!=i];ind=np.array([sum(((k>>t)&1)<<x for t,x in enumerate(other)) for k in range(1<<(n-1))],dtype=np.uint64);weights=(np.uint64(1)<<np.arange(1<<(n-1),dtype=np.uint64));plus=(((cc[:,None]>>ind)&1)*weights).sum(1).astype(int);minus=(((cc[:,None]>>(ind+(1<<i)))&1)*weights).sum(1).astype(int);hp,ip=lookup[n-1][1-policy]
            ht[jj]=o['D'][jj,i]+(hp[plus]+hp[minus])/2;it[jj]=o['Inf'][jj,i]+(ip[plus]+ip[minus])/2
        pol.append((ht,it));out[f'adaptive_n{n}_policy{policy}']=dict(functions=count,H_residual=float(abs(ht-o['H']).max()),I_residual=float(abs(it-o['I']).max()))
    lookup.append(pol)
n=4;errH=errI=0.
for startcode in range(0,65536,2048):
    f=truth(np.arange(startcode,startcode+2048,dtype=np.uint64),4);count=len(f);totH=np.zeros(count);totI=np.zeros(count)
    for a in range(1,5):
        for A in itertools.combinations(range(4),a):
            other=[x for x in range(4) if x not in A];v=[]
            for fix in range(1<<(4-a)):
                base=sum(((fix>>t)&1)<<j for t,j in enumerate(other));ind=base+np.array([sum(((u>>t)&1)<<j for t,j in enumerate(A)) for u in range(1<<a)]);v.append(f[:,ind])
            o=calc(np.concatenate(v,axis=0));den=a*math.comb(4,a);totH+=o['D'].sum(1).reshape(-1,count).mean(0)/den;totI+=o['Inf'].sum(1).reshape(-1,count).mean(0)/den
    errH=max(errH,float(abs(totH-entropy(f)).max()));errI=max(errI,float(abs(totI-info(f)).max()))
out['random_order_all4']=dict(functions=65536,H_residual=errH,I_residual=errI)
out['resources']=dict(elapsed_seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes_macos=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path('path_census.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
