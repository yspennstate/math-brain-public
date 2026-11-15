import os
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
import numpy as np,json,math,time,resource
from audit import calc,truth,h
from pathlib import Path
start=time.time();out={};rows=[]
for k in [1,2,3]:
    maximum=0.;ires=0.;vmax=0.;minimum=1e100
    for s in range(0,65536,512):
        f=truth(np.arange(s,s+512,dtype=np.uint64),4);n=4;orig=calc(f);N=1<<(n+k+1);ids=np.arange(N);gate=((ids>>n)&((1<<k)-1))==0;z=1-2*((ids>>(n+k))&1)
        g=np.where(gate[None,:],f[:,ids&15],z[None,:]);new=calc(g);delta=2**(-k)
        maximum=max(maximum,float(abs(new['E'][:,:n]-delta*orig['E']).max()));expect=delta*orig['I']+1-delta+k*delta;ires=max(ires,float(abs(new['I']-expect).max()))
        minimum=min(minimum,float((new['E'].sum(1)-delta*orig['E'].sum(1)).min()))
    rows.append(dict(k=k,base_functions=65536,original_coordinate_erasure_residual=maximum,influence_residual=ires,minimum_total_erasure_surplus=minimum))
out['gated_switch']=rows
# Exact random-order integral by summing all restrictions: an alive set A of size a has integrated weight 1/(a*C(n,a)).
# For fixed A, average over outside answers. Each coordinate node is counted at its deletion time.
from itertools import combinations
from audit import make_bank,entropy,info
rrows=[]
for n in [4,6,7,8]:
    errh=erri=0.;count=8 if n<8 else 4;f=make_bank(n,count,17400+n)
    totalsH=np.zeros(count);totalsI=np.zeros(count);ids=np.arange(1<<n)
    for a in range(1,n+1):
        for A in combinations(range(n),a):
            others=[j for j in range(n) if j not in A];v=np.zeros((count*(1<<(n-a)),1<<a))
            for fix in range(1<<(n-a)):
                base=sum(((fix>>t)&1)<<j for t,j in enumerate(others));ind=base+np.array([sum(((u>>t)&1)<<j for t,j in enumerate(A)) for u in range(1<<a)])
                v[fix*count:(fix+1)*count]=f[:,ind]
            o=calc(v);totalsH+=o['D'].sum(1).reshape(-1,count).mean(0)/(a*math.comb(n,a));totalsI+=o['Inf'].sum(1).reshape(-1,count).mean(0)/(a*math.comb(n,a))
    rrows.append(dict(n=n,count=count,entropy_residual=float(abs(totalsH-entropy(f)).max()),influence_residual=float(abs(totalsI-info(f)).max())))
out['random_order_integral']=rrows
# Nondegenerate block counterexample: f=i times AND_4, all coordinates relevant.
f0=np.ones(16);f0[-1]=-1;f=np.r_[f0,-f0];o=calc(f[None,:]);mu=o['mu'][0];i=4;N=1;A=sum(mu[j] for j in range(32) if j&N);eta=sum(mu[j] for j in range(32) if j>>i&1 and not j&N);delta=o['Inf'][0,i]
bad=delta*math.log2(math.e*A/delta)+eta*math.log2(math.e/eta)
out['nondegenerate_block_counterexample']=dict(n=5,i=i,N=N,A=A,eta=eta,delta=delta,E=o['E'][0,i],bad_rhs=bad)
out['resource']=dict(elapsed_seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes_macos=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
Path('reductions.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
