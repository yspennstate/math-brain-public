"""Independent exact dyadic derivatives; NPN census and structured functions.
No shared-project code is imported. All logarithms and reported costs are in bits.
"""
import os
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
import numpy as np
import itertools, math, json, time
from pathlib import Path
KS=(1,2,3,4,6); TS=(.25,.5,.75,1.); TH=(.1,.25,.5)

def fwht(f):
    a=np.array(f,dtype=float,copy=True); h=1
    while h<a.shape[-1]:
        v=a.reshape(*a.shape[:-1],-1,2*h); l=v[...,:h].copy();r=v[...,h:].copy()
        v[...,:h]=l+r;v[...,h:]=l-r;h*=2
    return a

def zeta(mu,u=1.):
    a=mu.copy();n=a.shape[-1].bit_length()-1
    for i in range(n):
        v=a.reshape(*a.shape[:-1],-1,2,1<<i);v[...,0,:]+=u*v[...,1,:]
    return a

def data(f):
    f=np.atleast_2d(f); B,N=f.shape;n=N.bit_length()-1
    mu=(fwht(f)/N)**2;up=zeta(mu);p=np.ones((B,N));gs={0:f.astype(float)}
    for s in range(1,N):
        bit=s&-s;prev=s^bit;i=bit.bit_length()-1
        j=i-(prev&((1<<i)-1)).bit_count()
        v=gs[prev].reshape(B,-1,2,1<<j)
        gs[s]=((v[:,:,0,:]-v[:,:,1,:])/2).reshape(B,-1)
        p[:,s]=np.mean(gs[s]!=0,axis=1)
    pc=np.array([s.bit_count() for s in range(N)])
    return mu,up,p,pc

def logs(x):return -np.log2(np.where(x>0,x,1.))

def metrics(mu,up,p,pc,extra=True):
    I=(mu*pc).sum(1);var=mu[:,1:].sum(1);lp=logs(p);lu=logs(up)
    out={'I':I,'Var':var,'P':(mu*lp).sum(1),'A':(mu*lu).sum(1)}
    for K in KS:out[f'Sp{K}']=(mu*lp*(p<2.**(-K*pc))).sum(1)
    tau={t:(t**pc)*zeta(mu,1-t) for t in TS}
    for t in TS:out[f'T{t:g}']=(tau[t]*lp).sum(1)
    if not extra:return out
    for t in TS:
        for theta in TH:
            out[f'taumom_t{t:g}_th{theta:g}']=np.log2((tau[t]*np.where(p>0,p,1.)**-theta).sum(1))
    for theta in TH:
        weight=(.5**pc)*np.where(p>0,p,1.)**-theta
        out[f'raw_th{theta:g}']=np.log2((up*weight).sum(1))
        for factor in (2,4):
            trunc=zeta(mu*(pc<=np.ceil(factor*I[:,None])))
            out[f'raw_M{factor}I_th{theta:g}']=np.log2((trunc*weight).sum(1))
    for theta in (1.,.5,.25):
        for c in (2.,4.,8.):
            w=(mu[:,1:]*c**(-pc[1:])*np.where(up[:,1:]>0,up[:,1:],1.)**-theta).sum(1)
            # The minimal log2 K required by W <= Var K^(I/Var).
            out[f'W_c{c:g}_th{theta:g}']=np.where(var>0,var*np.log2(np.maximum(w/np.where(var>0,var,1),1e-300)),0.)
    refs={f'tau{r:g}':(r**pc)*zeta(mu,1-r) for r in (.25,.5,.75)}
    refs['mixture3']=sum(refs.values())/3
    # Uniform rho mixture; beta integral = 1/((k+1) binom(k,s)).
    pi=np.zeros_like(mu)
    n=pc.max()
    for s in range(int(n)+1):
        scaled=mu/np.array([(k+1)*math.comb(int(k),s) if k>=s else 1 for k in pc])
        integ=zeta(scaled)
        pi[:,pc==s]=integ[:,pc==s]
    refs['mixture_uniform']=pi
    refs['markov_normalized']=up/up.sum(1)[:,None]
    inf=up[:,[1<<i for i in range(int(n))]]
    productcost=np.log2(1+inf).sum(1)+(inf*logs(inf)).sum(1)
    out['ref_product']=productcost
    for name,pi in refs.items():out['ref_'+name]=(mu*logs(pi)).sum(1)
    out['markov_logZ']=np.log2(up.sum(1))
    out['H']=(mu*logs(mu)).sum(1)
    out['bound_violation']=np.maximum((mu*lp).sum(1)-(mu*lu).sum(1), (mu*lu).sum(1)-(mu*lp).sum(1)-2*(I-var))
    return out

def tt_hex(f):return hex(sum(int(x<0)<<i for i,x in enumerate(f)))

def update(rec,out,f):
    B=len(f);rec['count']=rec.get('count',0)+B;I=out['I'];ok=I>0
    for key,a in out.items():
        if key in ('I','Var','bound_violation'):continue
        ratios=np.divide(a,I,out=np.full(B,-np.inf),where=ok)
        j=int(np.argmax(ratios));value=float(ratios[j])
        if value>rec.get(key,{}).get('ratio',-np.inf)+1e-13:
            rec[key]={'ratio':value,'tt':tt_hex(f[j]),'n':f.shape[1].bit_length()-1,'I':float(I[j]),'value':float(a[j])}
    if 'bound_violation' in out:rec['max_bound_violation']=max(rec.get('max_bound_violation',0.),float(out['bound_violation'].max()))

def census():
    result={};start=time.time()
    for n in range(1,6):
        reps=np.fromfile(f'npn{n}.bin',dtype='<u4');rec={}
        for lo in range(0,len(reps),1024):
            tt=reps[lo:lo+1024]
            f=1-2*((tt[:,None]>>np.arange(1<<n,dtype=np.uint32))&1).astype(np.int8)
            update(rec,metrics(*data(f)),f)
        result[f'npn{n}']=rec
        Path('census.json').write_text(json.dumps(result,indent=2))
        print('npn',n,'count',len(reps),'P/I',rec['P']['ratio'],'elapsed_seconds',time.time()-start,flush=True)
    rng=np.random.default_rng(20261110)
    for n in (6,7):
        rec={};N=1<<n
        for batch in range(20):
            f=rng.choice([-1,1],(256,N)).astype(np.int8)
            for j in range(256):
                if j%4==1:
                    f[j]=1;f[j,rng.choice(N,N//2,replace=False)]=-1
                elif j%4==2:
                    f[j]=1;k=int(np.exp(rng.uniform(0,np.log(N/2))))
                    f[j,rng.choice(N,max(1,k),replace=False)]=-1
                elif j%4==3:
                    x=np.arange(N);w=rng.normal(size=n)
                    f[j]=np.where(sum(w[i]*(1-2*((x>>i)&1)) for i in range(n))>=0,1,-1)
            update(rec,metrics(*data(f)),f)
        result[f'sample{n}']=rec
        Path('census.json').write_text(json.dumps(result,indent=2))
        print('sample',n,rec['count'],'P/I',rec['P']['ratio'],'elapsed_seconds',time.time()-start,flush=True)

def functions():
    for n in (1,2,3,4,5,6,7,9,11):
        x=np.arange(1<<n);pc=np.array([int(v).bit_count() for v in x])
        yield f'AND_{n}',np.where(x==(1<<n)-1,-1,1)
        if n%2:yield f'majority_{n}',np.where(pc>n//2,-1,1)
    for w,m in ((1,4),(2,2),(2,3),(2,4),(3,2),(3,3),(4,2)):
        n=w*m;x=np.arange(1<<n);event=np.zeros(1<<n,dtype=bool)
        for j in range(m):event|=((x>>(j*w))&((1<<w)-1))==(1<<w)-1
        yield f'tribes_w{w}_m{m}',np.where(event,-1,1)
    for a in (1,2,3):
        n=a+(1<<a);x=np.arange(1<<n);address=x&((1<<a)-1)
        yield f'address_{a}',1-2*((x>>(a+address))&1)
    x=np.arange(512);event=np.zeros(512,dtype=bool)
    for perm in itertools.permutations(range(3)):
        mask=sum(1<<(3*i+perm[i]) for i in range(3));event|=(x&mask)==mask
    yield 'PM_K33',np.where(event,-1,1)
    rng=np.random.default_rng(13013)
    for L,k in ((1,2),(1,3),(2,1),(2,2),(3,1)):
        m=(1<<L)*k;n=L+k+m;g=rng.choice([-1,1],1<<k)
        # Balance g exactly, to match the analytic large-family formulas.
        g[:]=1;g[rng.choice(1<<k,1<<(k-1),replace=False)]=-1
        x=np.arange(1<<n);sel=(x&((1<<L)-1))==(1<<L)-1
        par=np.array([(-1)**int(v).bit_count() for v in (x>>(L+k))])
        yield f'MUX_L{L}_k{k}_m{m}',np.where(sel,par,g[(x>>L)&((1<<k)-1)])

def structured():
    result=[]
    for name,f in functions():
        d=data(f);out=metrics(*d);row={'name':name,'n':int(math.log2(len(f))),'tt':tt_hex(f)}
        row.update({k:float(v[0]) for k,v in out.items()})
        mu,up,p,pc=d;idx=np.where(mu[0]*logs(p[0])>0)[0]
        row['sparse_carriers']={str(K):[{'S':hex(int(s)),'size':int(pc[s]),'mu':float(mu[0,s]),'p':float(p[0,s]),'cost':float(mu[0,s]*logs(p[0,s]))} for s in sorted(idx,key=lambda s:-mu[0,s]*logs(p[0,s])) if p[0,s]<2.**(-K*pc[s])][:30] for K in KS}
        result.append(row);Path('structured.json').write_text(json.dumps(result,indent=2))
        print(name,'I',row['I'],'P/I',row['P']/row['I'],flush=True)

if __name__=='__main__':
    import sys
    {'census':census,'structured':structured}[sys.argv[1]]()
