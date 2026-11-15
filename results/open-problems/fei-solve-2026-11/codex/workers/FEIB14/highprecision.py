import os
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
import mpmath as mp,json,time
from pathlib import Path
from experiments import KEYS
mp.mp.dps=70
def ph(a,b):
    def el(x):return mp.mpf(x)*mp.log(x,2) if x else mp.mpf(0)
    return el(a+b)-el(a)-el(b)
def exact(h,n):
    tt=int(h,16);L=1<<n;M=L//2;f=[-1 if tt>>x&1 else 1 for x in range(L)]
    hat=[sum(f[x]*(-1)**((s&x).bit_count()) for x in range(L)) for s in range(L)];mu=[x*x for x in hat]
    I=sum(s.bit_count()*mu[s] for s in range(L));H=mp.mpf(2*n)*L*L-sum(mp.mpf(x)*mp.log(x,2) for x in mu if x);tot=[mp.mpf(0)]*7
    for i in range(n):
        inds=[s for s in range(L) if not s>>i&1];a=[mu[s] for s in inds];b=[mu[s|1<<i] for s in inds]
        def cost(labels):
            cells={}
            for t,l in enumerate(labels):
                aa,bb=cells.get(l,(0,0));cells[l]=(aa+a[t],bb+b[t])
            return sum(ph(aa,bb) for aa,bb in cells.values())
        ps=[[((t&p).bit_count()&1) for t in range(M)] for p in range(M)];ns=[[bool(t&N) for t in range(M)] for N in range(M)]
        v=[min(cost(p) for p in ps),min(cost(p) for p in ns),min(cost(list(zip(p,q))) for p in ps for q in ns),cost([t.bit_count() for t in range(M)]),min(cost([(t&N).bit_count() for t in range(M)]) for N in range(M))]
        tot[0]+=sum(ph(aa,bb) for aa,bb in zip(a,b))
        for j,z in enumerate(v):tot[j+1]+=z
        tot[6]+=min(v)
    return dict(I=mp.mpf(I)/(L*L),ratios=dict(zip(KEYS[1:],[H/I]+[x/I for x in tot])))
def main():
    start=time.time();seen={};res=[];err=0
    for n in range(1,6):
        z=json.loads(Path(f'census{n}.json').read_text())
        for j,r in enumerate(z['maxima']):
            if (n,r['tt']) not in seen:seen[n,r['tt']]=exact(r['tt'],n)
            v=seen[n,r['tt']]['ratios'][KEYS[j+1]];err=max(err,abs(float(v)-r['ratio']));res.append(dict(n=n,key=KEYS[j+1],tt=r['tt'],ratio=mp.nstr(v,65)))
    constants={str(d):mp.nstr((lambda p: -(p*mp.log(p,2)+(1-p)*mp.log(1-p,2))/p if p<1 else mp.mpf(0))(mp.mpf(2)**(1-d)),65) for d in range(1,17)}
    z=dict(rows=res,maximum_binary64_ratio_error=err,degree_constants=constants,C_threshold=mp.nstr(80+460/mp.log(2),65),C_LTF=mp.nstr(mp.log(4+mp.e,2)+2*mp.log(mp.e*mp.pi,2),65),elapsed_seconds=time.time()-start)
    assert err<1e-12;Path('highprecision.json').write_text(json.dumps(z,indent=2)+'\n');print('HIGH PRECISION PASS',err,time.time()-start)
if __name__=='__main__':main()
