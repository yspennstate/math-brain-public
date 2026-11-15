"""Seeded finite witness experiments. All masks refer to T after deleting i."""
import os
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',MKL_NUM_THREADS='1')
import ctypes as ct,json,time,resource,itertools
from pathlib import Path
import numpy as np
KEYS=['I','H','Hm','parity','meets','both','size','countN','union']
lib=ct.CDLL(str(Path('witness.dylib').resolve()));lib.init()
lib.evaluate.argtypes=[ct.POINTER(ct.c_int8),ct.c_int,ct.c_int,ct.POINTER(ct.c_double),ct.POINTER(ct.c_int)]
def calc(f,mode=1):
    f=np.ascontiguousarray(f,dtype=np.int8);n=f.size.bit_length()-1
    o=np.zeros(9);p=np.zeros((n,5,2),dtype=np.int32)
    lib.evaluate(f.ctypes.data_as(ct.POINTER(ct.c_int8)),n,mode,o.ctypes.data_as(ct.POINTER(ct.c_double)),p.ctypes.data_as(ct.POINTER(ct.c_int)))
    return dict(zip(KEYS,map(float,o))),p
def hex_tt(f):return hex(sum((int(v)<0)<<x for x,v in enumerate(f)))
def unpack(h,n):return np.array([-1 if int(h,16)>>x&1 else 1 for x in range(1<<n)],dtype=np.int8)
def row(f,tag,mode=1,meta=None):
    o,p=calc(f,mode);o.update(tag=tag,n=len(f).bit_length()-1,tt=hex_tt(f),mode=mode,params=p.tolist())
    if meta:o['meta']=meta
    return o
def summarize(rows,only_optimized=True):
    valid=[r for r in rows if r['I']>0]
    ans={}
    for k in KEYS[1:]:
        rr=[r for r in valid if not only_optimized or r['mode']==1 or (r['mode']==3 and k in ['H','Hm','parity','size']) or (r['mode']==0 and k in ['H','Hm','size'])]
        if rr:ans[k]=max((dict(ratio=r[k]/r['I'],tag=r['tag'],n=r['n'],tt=r['tt']) for r in rr),key=lambda x:x['ratio'])
    return ans
def save(name,rows,extra=None):
    z=dict(count=len(rows),maxima=summarize(rows),candidate_maxima=summarize(rows,False),maxima_scope='Only optimized fields: mode 1 all fields; mode 3 H,Hm,parity,size; mode 0 H,Hm,size. Other stored costs are valid upper bounds, not optimized minima.',rows=rows)
    if extra:z.update(extra)
    Path(name+'.json').write_text(json.dumps(z,indent=2)+'\n')
def signs(n):return 1-2*((np.arange(1<<n)[:,None]>>np.arange(n))&1)
def random_monotone(n,rng):
    L=1<<n;z=np.zeros(L,dtype=bool);level=int(rng.integers(1,n+1));
    masks=rng.choice(np.arange(1,L),size=int(rng.integers(1,3*n+1)),replace=True)
    for t in masks:z|=(np.arange(L)&t)==t
    if rng.random()<.5:
        masks=[t for t in range(L) if t.bit_count()==level]
        z[:]=False
        for t in masks:
            if rng.random()<.5:z|=(np.arange(L)&t)==t
    return 1-2*z.astype(np.int8)
def general():
    rng=np.random.default_rng(141426);rows=[]
    for n in range(6,11):
        X=signs(n)
        for j in range(96):
            typ=j%6
            if typ==0:f=1-2*rng.integers(0,2,1<<n,dtype=np.int8);tag='uniform'
            elif typ==1:f=1-2*(rng.random(1<<n)<10**rng.uniform(-2,-.3)).astype(np.int8);tag='biased'
            elif typ==2:f=random_monotone(n,rng);tag='monotone'
            elif typ==3:
                w=rng.normal(size=n);theta=rng.normal()*np.linalg.norm(w);f=np.where(np.sum(X*w,axis=1)>=theta,1,-1);tag='LTF'
            elif typ==4:
                # Random read-once binary AND/OR/XOR/MAJ3 tree.
                pool=[X[:,i].copy() for i in range(n)]
                while len(pool)>1:
                    rng.shuffle(pool);k=3 if len(pool)>=3 and rng.random()<.3 else 2;v=pool[:k];pool=pool[k:]
                    gate=int(rng.integers(0,3))
                    if k==3:y=np.where(sum(v)>=0,1,-1)
                    elif gate==0:y=np.minimum(*v)
                    elif gate==1:y=np.maximum(*v)
                    else:y=v[0]*v[1]
                    pool.append(y)
                f=pool[0];tag='read_once'
            else:
                # A few random input minterms, with arbitrary literal signs.
                f=np.ones(1<<n,dtype=np.int8)
                for _ in range(int(rng.integers(1,3*n))):
                    mask=int(rng.integers(1,1<<n));target=int(rng.integers(1<<n))&mask
                    f[(np.arange(1<<n)&mask)==target]=-1
                tag='DNF'
            rows.append(row(f,f'{tag}_{n}_{j}'))
        save('samples',rows,dict(seed=141426,per_dimension=96))
        print('samples',n,flush=True)
def ltf():
    rng=np.random.default_rng(141427);rows=[]
    for n in range(2,15):
        X=signs(n)
        for j in range(64):
            w=rng.normal(size=n) if j%2 else rng.lognormal(0,1.5,size=n)
            theta=0 if j%4==0 else rng.uniform(-1.5,1.5)*np.linalg.norm(w)
            f=np.where(np.sum(X*w,axis=1)>=theta,1,-1)
            rows.append(row(f,f'LTF_{n}_{j}',1 if n<=10 else 3,dict(weights=w.tolist(),threshold=float(theta))))
        save('ltf',rows,dict(seed=141427,per_dimension=64,scope='all five optimized through n=10; exact Hm,size and optimized parity at n=11..14; remaining modes are unconditional bounds'))
        print('LTF',n,flush=True)
def monotone():
    # All upper sets: recurse on slices (a,b) with a <= b pointwise.
    prev=[0,1];rows=[];counts={0:2}
    for n in range(1,6):
        L=1<<(n-1);now=[a|(b<<L) for a in prev for b in prev if a&~b==0];prev=now;counts[n]=len(now)
        rows += [row(unpack(hex(t),n),f'monotone_all_{n}_{t}') for t in now]
    save('monotone_all5',rows,dict(counts=counts))
    rng=np.random.default_rng(141428);rows=[]
    for j in range(4096):rows.append(row(random_monotone(6,rng),f'monotone_sample_6_{j}'))
    save('monotone6',rows,dict(seed=141428,scope='sample, not Dedekind enumeration'))
def extrema():
    rows=[]
    for n in range(1,6):
        z=json.loads(Path(f'census{n}.json').read_text())
        for j,e in enumerate(z['maxima']):
            r=row(unpack(e['tt'],n),f'census{n}_{KEYS[j+1]}');assert abs(r[KEYS[j+1]]/r['I']-e['ratio'])<1e-12;rows.append(r)
    save('census_extrema',rows)
if __name__=='__main__':
    import sys
    start=time.time();globals()[sys.argv[1]]();print(json.dumps(dict(elapsed_seconds=time.time()-start,maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,nice=os.getpriority(os.PRIO_PROCESS,0),threads=1)))
