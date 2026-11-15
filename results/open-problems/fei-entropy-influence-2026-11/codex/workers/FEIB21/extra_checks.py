import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import sys,json,math,time,resource
import numpy as np
import mpmath as mp
sys.path.insert(0,os.path.abspath('inputs'))
from experiment import wht,masses,phi
from window_search import window_cost,block_cost
from tensor_windows import Moments,bounds
mp.mp.dps=110

def P(p,q):
    p,q=mp.mpf(p),mp.mpf(q)
    if not p or not q:return mp.mpf(0)
    return (p*mp.log1p(q/p)+q*mp.log1p(p/q))/mp.log(2)

def max_coordinate():
    rows=[]
    for depth in [0,1,2]:
        sz=3**depth;n=1+2*sz
        ids=np.arange(1<<n,dtype=np.int64)
        def majblock(start):
            if depth==0:return (ids>>start)&1
            bits=np.array([(ids>>(start+j))&1 for j in range(sz)],dtype=np.int8)
            for _ in range(depth):bits=(bits.reshape(-1,3,len(ids)).sum(axis=1)>=2).astype(np.int8)
            return bits[0]
        y0=majblock(1);y1=majblock(1+sz);root=ids&1
        B=1-2*(y0&y1);f=np.where((y0==0)&(y1==0),1-2*root,B)
        mu=wht(f)**2;inf=[];ers=[]
        for i in range(n):
            p,q=masses(mu,i);inf.append(float(q.sum()));ers.append(float(phi(p,q).sum())/inf[-1])
        p,q=masses(mu,0);er=float(phi(p,q).sum())/inf[0]
        rows.append(dict(depth=depth,n=n,root_E_ratio=er,min_E_ratio=min(ers),root_influence=inf[0],other_max=max(inf[1:]),root_unique_max=inf[0]>max(inf[1:]),parseval=float(mu.sum())))
    assert abs(rows[0]['root_E_ratio']-rows[-1]['root_E_ratio'])<1e-12
    assert rows[-1]['root_unique_max']
    return rows

def pm_blocks():
    spec=np.load('inputs/pm_record_spectrum.npy');mu=spec**2
    assert spec[0]==0
    p,q=masses(mu,0);aa=mp.mpf(57)/256
    assert float(q.sum())==float(aa)
    pairs,counts=np.unique(np.stack([p,q],axis=1),axis=0,return_counts=True)
    E=[mp.mpf(0)];d=mp.mpf(1)
    for depth in range(1,41):
        inc=sum(int(c)*P(float(x),d*d*mp.mpf(float(y))) for (x,y),c in zip(pairs,counts)) / (aa*d)
        E.append(E[-1]+inc);d*=aa
    rows=[]
    for depth in [1,2,3,5,10,20,40,100,1000]:
        for kind,k in [('fixed',1),('growing',min(depth,max(1,math.ceil(2*math.log(max(1,depth))/(-math.log(float(aa)))))))]:
            assert k<len(E)
            dk=aa**k;alpha=aa**(depth-k)
            val=E[k]+P(1-alpha,alpha*dk*dk)/(alpha*dk)
            rows.append(dict(depth=depth,kind=kind,bottom_depth=k,block_coordinates=str(18**k-1),block_ratio=float(val),inner_E=float(E[k]),influence=str(aa**depth)))
    src=json.load(open('inputs/pm_prior.json'))['data']['rows']
    residual=max(abs(float(E[r['depth']])-r['states'][-1]['E']) for r in src)
    return dict(rows=rows,gate_E=float(E[1]),core_alpha=float(aa),distinct_pairs=len(pairs),E_recursion_residual=residual,optimized_filtration_depth20=src[-1]['F'])

def block_certificate():
    rows=[]
    for L,D in [(15,55),(31,9848),(79,777472127994)]:
        m=Moments(L,D);dd=float(m.delta);A=float(m.A);b=float(m.b);s=float(m.nn[0]);eta=D*b/s
        ell=((1-float(m.q)**2)/2)**L
        e=A*eta*math.sqrt(eta)*(1+math.sqrt(1+eta))+A*D*(D-1)*(ell/s)**2
        # Compute e in Decimal/mp arithmetic for tiny values without loss in q.
        vv=mp.mpf(str(m.b/m.nn[0]));AA=mp.mpf(str(m.A));qq=mp.mpf(str(m.q));et=D*vv
        el=((1-qq*qq)/2)**L;ss=mp.mpf(str(m.nn[0]));ed=AA*et*mp.sqrt(et)*(1+mp.sqrt(1+et))+AA*D*(D-1)*(el/ss)**2
        u=min(mp.mpf(str(m.delta)),AA*et*mp.mpf(2)**(-L)+ed)
        bound=bounds(L,D)
        oldempty=dd*math.log2(math.e*(1+dd**-2))
        blockerr=bound['erasure_error_bound']-oldempty+float(P(1,u)/mp.mpf(str(m.delta)))
        rows.append(dict(L=L,D=D,block_interval=[max(0,2-blockerr),2+blockerr],error=blockerr,q_empty_bound=float(u),same_erasure_error=bound['erasure_error_bound']))
    return rows

if __name__=='__main__':
    start=time.time();out=dict(max_coordinate=max_coordinate(),pm=pm_blocks(),block_certificate=block_certificate(),seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    json.dump(out,open('extra_checks.json','w'),indent=2);print(json.dumps(out,indent=2))
