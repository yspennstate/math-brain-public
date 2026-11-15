"""Independent Walsh/zeta census and structured-family calculations for FEIB11.
Set thread environment before importing numpy. All truth tables use 1 <=> f=-1.
"""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[k]='1'
import argparse, csv, itertools, json, math, time, resource
from pathlib import Path
import numpy as np
QS=[1.,.5,.25,.1,.05,.01,0.]

def walsh(f):
    a=np.asarray(f,dtype=np.float64).copy(); N=a.shape[-1]
    for h in (1<<np.arange(N.bit_length()-1)):
        b=a.reshape(*a.shape[:-1],-1,2,int(h))
        u=b[...,0,:].copy();v=b[...,1,:].copy()
        b[...,0,:]=u+v;b[...,1,:]=u-v
    return a

def zeta(m):
    a=m.copy();N=a.shape[-1]
    for h in (1<<np.arange(N.bit_length()-1)):
        b=a.reshape(*a.shape[:-1],-1,2,int(h))
        b[...,0,:]+=b[...,1,:]
    return a

def metrics(f):
    f=np.atleast_2d(f);N=f.shape[-1];n=N.bit_length()-1
    c=walsh(f);m=c*c/(N*N);u=zeta(m)
    pc=np.array([s.bit_count() for s in range(N)])
    lu=np.log2(np.where(u>0,u,1));lm=np.log2(np.where(m>0,m,1))
    H=-(m*lm).sum(axis=1);A=-(m*lu).sum(axis=1)
    I=(m*pc).sum(axis=1);v=1-m[:,0];wc=(m*u).sum(axis=1)
    # expm1/log1p avoids cancellation for q approaching zero.
    L=np.array([-np.log1p((m*np.expm1(q*lu*np.log(2))).sum(axis=1))/(q*np.log(2)) if q else A for q in QS]).T
    return dict(H=H,A=A,I=I,var=v,WC=wc,L=L,mu=m,up=u,c=c)

def truth_hex(f):
    return format(sum(int(x<0)<<i for i,x in enumerate(f)),'0%dx'%((len(f)+3)//4))

def fhex(t,n):
    return np.array([1-2*((t>>i)&1) for i in range(1<<n)],dtype=np.int8)

def record(f,d,j):
    return dict(tt_hex=truth_hex(f),H_bits=float(d['H'][j]),A_bits=float(d['A'][j]),I=float(d['I'][j]),
                Var=float(d['var'][j]),WC=float(d['WC'][j]),Lq_bits={str(q):float(d['L'][j,k]) for k,q in enumerate(QS)})

def scan(n,batches,kind):
    best={str(q):dict(ratio=-1) for q in QS};bal={str(q):dict(ratio=-1) for q in QS}
    aux={k:dict(ratio=-1) for k in ['H/I','A/I','H/(I-1)','A/(I-1)']}
    count=0;balanced=0;worst={k:0. for k in ['WC_below_collision','collision_below_max_square','L1_above_A','A_above_H','quadratic_bound','level1_bound']}
    for f in batches:
        d=metrics(f);I=d['I'];valid=I>0;b=(d['var']==1)&(I>1);balanced+=int(b.sum());count+=len(f)
        for k,q in enumerate(QS):
            for den,mask,target in [(I,valid,best[str(q)]),(I-1,b,bal[str(q)])]:
                ratios=np.divide(d['L'][:,k],den,out=np.full(len(f),-1.),where=mask)
                j=int(np.argmax(ratios))
                if ratios[j]>target['ratio']+1e-12:target.update(ratio=float(ratios[j]),**record(f[j],d,j))
        for name,field,den,mask in [('H/I','H',I,valid),('A/I','A',I,valid),('H/(I-1)','H',I-1,b),('A/(I-1)','A',I-1,b)]:
            ratios=np.divide(d[field],den,out=np.full(len(f),-1.),where=mask);j=int(np.argmax(ratios))
            if ratios[j]>aux[name]['ratio']+1e-12:aux[name].update(ratio=float(ratios[j]),**record(f[j],d,j))
        m,u=d['mu'],d['up'];collision=(m*m).sum(axis=1)
        singleton=u[:,1<<np.arange(n)]
        mint=np.min(np.where((np.arange(1<<n)[None,:,None]&(1<<np.arange(n))[None,None,:])!=0,singleton[:,None,:],1),axis=2)
        Aone=-(m*np.log2(np.where(mint>0,mint,1))).sum(axis=1)
        errors=dict(WC_below_collision=collision-d['WC'],collision_below_max_square=m.max(axis=1)**2-collision,
                    L1_above_A=d['L'][:,0]-d['A'],A_above_H=d['A']-d['H'],
                    quadratic_bound=d['L'][:,0]-(16*I*I+13*I),
                    level1_bound=Aone-3.520226*I)
        for name,err in errors.items():worst[name]=max(worst[name],float(err.max()))
    result=dict(n=n,kind=kind,count=count,balanced_non_dictator_count=balanced,best_over_I=best,best_balanced_over_I_minus_1=bal,comparisons=aux,max_positive_violation=worst)
    Path(f'census_n{n}_{kind}.json').write_text(json.dumps(result,indent=2));print(n,kind,count,{q:best[q]['ratio'] for q in best},flush=True)
    return result

def from_tables(tables,n,batch=2048):
    tables=np.asarray(tables,dtype=np.uint64)
    for st in range(0,len(tables),batch):
        t=tables[st:st+batch];yield (1-2*((t[:,None]>>np.arange(1<<n,dtype=np.uint64)[None,:])&1).astype(np.int8))

def random_batches(n,count,seed):
    rng=np.random.default_rng(seed);N=1<<n
    for st in range(0,count,1024):
        size=min(1024,count-st);bits=rng.integers(0,2,size=(size,N),dtype=np.int8)
        # Half unbiased independent; half uniform among exactly balanced tables.
        for j in range(size//2,size):
            bits[j,:]=0;bits[j,rng.choice(N,N//2,replace=False)]=1
        yield 1-2*bits

def family_rows():
    rng=np.random.default_rng(20261110);rows=[]
    def add(name,f,**kw):
        f=np.asarray(f,dtype=np.int8);d=metrics(f);row=dict(name=name,n=len(f).bit_length()-1,**kw,**record(f,d,0))
        row['L_over_I']=float(d['L'][0,0]/d['I'][0]) if d['I'][0] else None
        row['L_over_I_minus_1']=float(d['L'][0,0]/(d['I'][0]-1)) if d['var'][0]==1 and d['I'][0]>1 else None
        rows.append(row);Path('families.json').write_text(json.dumps(rows,indent=2))
    for n in range(1,19):
        N=1<<n;x=np.arange(N,dtype=np.uint32);f=np.ones(N,dtype=np.int8);f[-1]=-1;add('AND',f)
        if n%2:
            weights=np.array([int(s).bit_count() for s in x],dtype=np.int16);add('majority',1-2*(weights>n//2))
        if n%2==0:
            bits=np.zeros(N,dtype=np.uint8)
            for k in range(0,n,2):bits^=((x>>k)&1)&((x>>(k+1))&1)
            add('bent_quadratic_pairs',1-2*bits.astype(np.int8))
    for w,t in [(1,1),(2,2),(2,3),(3,4),(3,5),(3,6),(4,4)]:
        n=w*t;x=np.arange(1<<n,dtype=np.uint32);out=np.zeros(1<<n,dtype=bool)
        for j in range(t):out|=((x>>(w*j))&((1<<w)-1))==((1<<w)-1)
        add('tribes',1-2*out,width=w,tribes=t)
    for k in range(1,4):
        n=k+(1<<k);x=np.arange(1<<n,dtype=np.uint32);address=x&((1<<k)-1);val=(x>>(k+address))&1
        add('address_MUX',1-2*val.astype(np.int8),address_bits=k)
    # Random full trees, disjoint leaves, binary AND/OR/XOR and random leaf negations.
    def tree(cols):
        if len(cols)==1:return cols[0] ^ bool(rng.integers(2))
        cut=int(rng.integers(1,len(cols)));a=tree(cols[:cut]);b=tree(cols[cut:]);op=int(rng.integers(3))
        return (a&b) if op==0 else ((a|b) if op==1 else (a^b))
    for n in [6,7,10,14]:
        x=np.arange(1<<n,dtype=np.uint32);cols=[((x>>j)&1).astype(bool) for j in range(n)]
        for rep in range(50):add('random_read_once_AND_OR_XOR',1-2*tree(cols),rep=rep)
        for rep in range(10):add('random_uniform',1-2*rng.integers(0,2,size=1<<n,dtype=np.int8),rep=rep)
    for coins in [False,True]:
        n=18 if coins else 9;x=np.arange(1<<n,dtype=np.uint32);core=x&511;val=np.zeros(len(x),dtype=bool)
        for p in itertools.permutations(range(3)):
            mask=sum(1<<(3*r+p[r]) for r in range(3));val|=(core&mask)==mask
        if coins:
            for e in range(9):
                r,c=divmod(e,3);cross=sum(1<<j for j in range(9) if j//3==r or j%3==c)
                site=(core==cross)|(core==(cross^(1<<e)));val|=site&(((x>>(9+e))&1)>0)
        add('PM_K33_plus_9_coins' if coins else 'PM_K33',1-2*val)
    return rows

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['small','npn5','samples','families']);a=p.parse_args();start=time.time()
    if a.mode=='small':
        for n in range(1,5):scan(n,from_tables(np.arange(1<<(1<<n),dtype=np.uint64),n),'all')
    if a.mode=='npn5':scan(5,from_tables([int(t,16) for t in Path('npn5.txt').read_text().split()],5),'npn')
    if a.mode=='samples':
        for n in [6,7]:scan(n,random_batches(n,200000,20261110+n),'sample')
    if a.mode=='families':family_rows()
    usage=dict(wall_seconds=time.time()-start,max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,nice=os.getpriority(os.PRIO_PROCESS,0),numeric_threads=1)
    Path(f'resources_{a.mode}.json').write_text(json.dumps(usage,indent=2));print(json.dumps(usage),flush=True)
