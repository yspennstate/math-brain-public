"""Reproducible FEIB25 spectral level calculations. All logs base two."""
import argparse, gzip, hashlib, itertools, json, math, os, time
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parent

def wht(f):
    v = np.asarray(f, dtype=np.float64).copy()
    N = v.shape[-1]
    for j in range(N.bit_length()-1):
        h = 1 << j
        z = v.reshape(*v.shape[:-1], -1, 2, h)
        a, b = z[...,0,:].copy(), z[...,1,:].copy()
        z[...,0,:], z[...,1,:] = a+b, a-b
    return v / N

def plan(n):
    x = np.arange(1<<n)
    wt = np.array([int(i).bit_count() for i in x])
    edges = []
    for i in range(n):
        hi = x[(x & (1<<i)) != 0]
        edges.append((hi, hi^(1<<i), wt[hi]))
    return x, wt, edges

def profile_mu(mu, n, pp=None):
    one = mu.ndim == 1
    if one: mu = mu[None,:]
    x, wt, edges = pp or plan(n)
    W = np.stack([mu[:,wt==d].sum(axis=1) for d in range(n+1)],axis=1)
    A = np.zeros_like(W)
    E = np.zeros(len(mu))
    for hi,lo,wh in edges:
        q,p = mu[:,hi],mu[:,lo]
        with np.errstate(divide='ignore', invalid='ignore'):
            up = np.where(q>0,q*np.log2(1+np.divide(p,q,out=np.zeros_like(p),where=q>0)),0)
            down = np.where(p>0,p*np.log2(1+np.divide(q,p,out=np.zeros_like(q),where=p>0)),0)
        E += (up+down).sum(axis=1)
        for d in range(1,n+1): A[:,d] += up[:,wh==d].sum(axis=1)
    return (W[0], A[0], E[0]) if one else (W,A,E)

def profile(f):
    f=np.asarray(f); n=f.size.bit_length()-1
    mu=wht(f)**2
    W,A,E=profile_mu(mu,n)
    nz=mu>0
    return dict(n=n,W=W.tolist(),A=A.tolist(),dW=(np.arange(n+1)*W).tolist(),
                prev_dW=np.r_[0,np.arange(n)*W[:-1]].tolist(),I=float(np.dot(np.arange(n+1),W)),
                H=float(-np.dot(mu[nz],np.log2(mu[nz]))),E=float(E),G=float(A.sum()))

def candidates(W):
    n=W.shape[-1]-1; d=np.arange(n+1)
    prev=np.concatenate([np.zeros_like(W[...,:1]),W[...,:-1]],axis=-1)
    I=np.sum(d*W,axis=-1,keepdims=True)
    return dict(L1=d*W+np.maximum(d-1,0)*prev,L2=d*W+prev,
                lower_all=d*W+np.cumsum(W,axis=-1)-W,
                tail_linear=d*W+np.maximum(d-1,0)*prev+np.maximum(I-np.cumsum(d*W,axis=-1),0),
                global_I=np.broadcast_to(I,W.shape))

def census():
    out={}; started=time.monotonic()
    for n in range(1,6):
        p=ROOT/f'npn{n}.bin'; reps=np.fromfile(p,dtype='<u4'); N=1<<n
        pp=plan(n); ww=[];aa=[];ee=[]
        maxes={key:dict(ratio=0.) for key in candidates(np.zeros((1,n+1)))}
        for start in range(0,len(reps),4096):
            tt=reps[start:start+4096]
            f=1-2*((tt[:,None]>>np.arange(N,dtype=np.uint32))&1).astype(np.float64)
            mu=wht(f)**2; W,A,E=profile_mu(mu,n,pp)
            assert np.max(np.abs(mu.sum(axis=1)-1))<1e-12
            assert np.max(A.sum(axis=1)-E)<1e-12
            ww.append(np.rint(W*N*N).astype(np.uint32));aa.append(A);ee.append(E)
            for key,den in candidates(W).items():
                # A_1 is separately recorded and excluded from the local d>=2 search.
                ratio=np.divide(A[:,2:],den[:,2:],out=np.zeros_like(A[:,2:]),where=den[:,2:]>1e-15)
                if ratio.size:
                    at=np.unravel_index(np.argmax(ratio),ratio.shape); val=float(ratio[at])
                    if val>maxes[key]['ratio']:
                        row,col=at; d=int(col+2)
                        maxes[key]=dict(ratio=val,d=d,tt=hex(int(tt[row])),A=float(A[row,d]),den=float(den[row,d]),W=W[row].tolist())
        Wnum=np.concatenate(ww); A=np.concatenate(aa); E=np.concatenate(ee)
        np.savez_compressed(ROOT/f'census_n{n}.npz',tt=reps,W_numerator=Wnum,denominator=N*N,A=A,E=E)
        out[str(n)]=dict(classes=len(reps),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),maxima=maxes,
            A1_max=float(A[:,1].max()),elapsed_seconds=time.monotonic()-started)
        (ROOT/'census_summary.json').write_text(json.dumps(out,indent=2))
        print(n,len(reps),maxes,flush=True)

def threshold(m,t):
    x,wt,_=plan(m)
    return np.where(wt>=t,-1.,1.)

def pm33():
    x=np.arange(512); event=np.zeros(512,dtype=bool)
    for perm in itertools.permutations(range(3)):
        mask=sum(1<<(3*i+perm[i]) for i in range(3))
        event |= (x&mask)==mask
    return np.where(event,-1.,1.)

def tribes(n,w):
    assert n%w==0
    x=np.arange(1<<n);event=np.zeros(1<<n,dtype=bool)
    for off in range(0,n,w): event |= ((x>>off)&((1<<w)-1))==((1<<w)-1)
    return np.where(event,-1.,1.)

def families():
    import sys
    sys.path.insert(0,str(Path.home()/'fei_solve_agent/code'))
    from mono_hidden import build
    rng=np.random.default_rng(20261110); rows=[]
    def add(name,f):
        row=profile(f); row['name']=name; rows.append(row)
        (ROOT/'families.json').write_text(json.dumps(rows,indent=2))
    for n in [5,7,9,11,13,15,17]: add(f'majority_{n}',threshold(n,(n+1)//2))
    for n,w in [(6,2),(8,2),(10,2),(12,2),(14,2),(16,2),(18,2),(9,3),(12,3),(15,3),(18,3),(16,4)]:add(f'tribes_{w}x{n//w}',tribes(n,w))
    for a in [1,2,3,4]:
        n=a+(1<<a); x=np.arange(1<<n);address=x&((1<<a)-1)
        add(f'address_{a}',np.where(((x>>(a+address))&1)!=0,-1.,1.))
    for n in [4,8,12,16,18]:
        x=np.arange(1<<n);par=np.zeros(len(x),dtype=np.int8)
        for j in range(0,n,2):par ^= ((x>>j)&(x>>(j+1))&1).astype(np.int8)
        add(f'bent_{n}',1.-2.*par)
    add('PM_K33',pm33())
    # Full tower spectra are computed separately without 2^81 truth tables.
    for k in [3,5,7,9,11,13,15,17]: n,f=build(k);add(f'hidden_{k}',f)
    for n in [6,8,10,12,14,16]:
        for p in [.5,.1,.01]:add(f'random_n{n}_p{p}',np.where(rng.random(1<<n)<p,-1.,1.))
    for m in [4,6,8,10,12,14]:
        t=int(math.ceil(m/2+math.sqrt(m)/2));h=threshold(m,t)
        for r in [0,1,2]:
            f=np.concatenate([((-1.)**j.bit_count())*h for j in range(1<<r)])
            add(f'parity{r}_threshold_m{m}_t{t}',f)
    for m in [3,5,7,9,11,13]:
        maj=threshold(m,(m+1)//2)
        h=np.concatenate([maj,np.ones_like(maj)])
        for r in [0,1,2]:
            f=np.concatenate([((-1.)**j.bit_count())*h for j in range(1<<r)])
            add(f'parity{r}_selector_majority{m}',f)
    print('families',len(rows),flush=True)

def audit():
    rng=np.random.default_rng(251110); worst=0.;count=0
    for n in range(1,9):
        x,wt,edges=plan(n);N=1<<n
        for rep in range(12):
            f=rng.choice([-1.,1.],N); c=wht(f)
            direct=np.array([np.mean(f*np.array([(-1.)**int(s&int(xx)).bit_count() for xx in x])) for s in x])
            worst=max(worst,float(np.max(np.abs(c-direct))))
            row=profile(f); A=np.zeros(n+1);I=0.
            mu=c*c
            for s in range(N):
                for i in range(n):
                    if s>>i&1 and mu[s]>0:A[s.bit_count()]+=mu[s]*math.log2(1+mu[s^(1<<i)]/mu[s])
            worst=max(worst,float(np.max(np.abs(A-row['A']))))
            for i in range(n):I+=np.mean(f!=f[x^(1<<i)])
            assert abs(I-row['I'])<1e-12
            assert row['G']<=row['E']+1e-12<=row['H']+1e-12
            assert row['E']<=row['G']+I/math.log(2)+1e-12
            assert row['A'][1]<=math.sqrt(row['W'][0])*I/math.log(2)+1e-12
            if n>=2:assert row['A'][2]<=I*I/math.log(2)+1e-12
            count+=1
    result=dict(cases=count,max_absolute_discrepancy=worst,checks='direct Walsh, direct edge sums, pivotal influence, erasure sandwich, Han, A1, A2')
    (ROOT/'audit.json').write_text(json.dumps(result,indent=2));print(result)

if __name__=='__main__':
    action=argparse.ArgumentParser();action.add_argument('action',choices=['census','families','audit']);args=action.parse_args()
    globals()[args.action]()
