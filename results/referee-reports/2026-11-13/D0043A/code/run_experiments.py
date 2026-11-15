"""Bounded, reproducible evidence; run with one BLAS thread and nice >=10."""
import os
for key in ["OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"]:
    os.environ[key]="1"
import argparse,csv,json,resource,time
from pathlib import Path
import numpy as np
from scipy.special import log_ndtr
from scipy.integrate import quad
from models import profile,bottom,quartic_mode,hmc_chain,hmc_banded,diagnostics

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data';DATA.mkdir(exist_ok=True)

def guard():
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    state=Path.home()/'.claude/compute/compute_state.json'
    if state.exists():
        mode=json.loads(state.read_text())
        if mode.get('status')=='distress':raise RuntimeError('Host compute distress; stopping at checkpoint')
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>3_500_000_000:
        raise MemoryError('3.5 GB RSS limit')

def artificial(draws):
    rng=np.random.default_rng(431301)
    path=DATA/'artificial_eigenvalues.csv'
    with path.open('w',newline='') as f:
        wr=csv.writer(f);wr.writerow(['model','beta','n','h','draw','lambda0','lambda1','lambda2'])
        for beta in [1,2,4]:
            for noise,n,h in [('chi',10000,None),('chi',100000,None),
                              ('gaussian',5120,.025),('gaussian',10240,.0125)]:
                guard();start=time.monotonic()
                for draw in range(draws):
                    d,e,hh=profile(n,beta,rng,noise=noise,h=h)
                    vals=bottom(d,e)
                    wr.writerow([noise,beta,n,hh,draw,*vals]);f.flush()
                print('artificial',beta,noise,n,draws,'seconds',round(time.monotonic()-start,2),flush=True)
    # Deterministic boundary/mesh comparison isolates numerical errors.
    out=[]
    for L in [64,128,256]:
        for h in [.05,.025,.0125]:
            n=int(round(L/h))-1
            d,e,_=profile(n,2,rng,noise='none',h=h)
            out.append(dict(L=L,h=h,eigenvalues=bottom(d,e).tolist()))
    (DATA/'deterministic_mesh.json').write_text(json.dumps(out,indent=2)+'\n')

def quartic(ns,burn,draws,thin,banded=False):
    rng=np.random.default_rng(431302)
    c=6**(2/7)
    prefix='quartic_banded' if banded else 'quartic'
    with (DATA/f'{prefix}_eigenvalues.csv').open('w',newline='') as f:
        wr=csv.writer(f);wr.writerow(['n','beta','chain','draw','top0','top1','top2','cv_scaled_top0','n_scaled_top0'])
        summary=[]
        for n in ns:
            guard();start=time.monotonic()
            saved=DATA/f'quartic_mode_{n}.npz'
            if saved.exists():
                values=np.load(saved);a=values['a'];q=values['q'];modeinfo={'reused':True}
            else:a,q,modeinfo=quartic_mode(n)
            np.savez_compressed(DATA/f'quartic_mode_{n}.npz',a=a,q=q)
            print('quartic mode',n,modeinfo,flush=True)
            for beta in [1,2,4]:
                chains=[];infos=[]
                for chain in [0,1]:
                    guard()
                    if banded:
                        values,info,last=hmc_banded(n,beta,(a,q),rng,burn=burn,draws=draws,thin=thin,chain=chain)
                        np.savez_compressed(DATA/f'{prefix}_sample_{n}_beta{beta}_chain{chain}.npz',
                                            a=last[::2],b=np.exp(last[1::2]))
                    else:values,info=hmc_chain(n,beta,(a,q),rng,burn=burn,draws=draws,thin=thin,chain=chain)
                    infos.append(info);chains.append(c*n**(2/7)*(values[:,0]-2))
                    for j,vals in enumerate(values):
                        wr.writerow([n,beta,chain,j,*vals,c*n**(2/7)*(vals[0]-2),n**(2/7)*(vals[0]-2)])
                    f.flush()
                    print('quartic',n,beta,chain,'accept',round(info['acceptance_post'],3),
                          'mean CV',round(np.mean(chains[-1]),4),flush=True)
                diagnostic=diagnostics(chains)
                entry=dict(n=n,beta=beta,mode=modeinfo,diagnostics=diagnostic,
                           chains=infos,seconds_so_far=time.monotonic()-start,
                           mean_cv=float(np.mean(chains)),sd_cv=float(np.std(chains,ddof=1)))
                summary.append(entry)
                (DATA/f'{prefix}_diagnostics.json').write_text(json.dumps(summary,indent=2)+'\n')
                print('diagnostics',n,beta,diagnostic,flush=True)

def tail():
    # Exact Gaussian probabilities of the explicit Rayleigh-quotient events.
    rows=[]
    for k in [0,1,2]:
        p=1/(2*k+1);a=k/(2*k+1)
        D=quad(lambda x:30*x**(p+2)*(1-x)**2,0,1,epsabs=1e-12)[0]
        C=quad(lambda x:900*x**(4-2*a)*(1-x)**4,0,1,epsabs=1e-12)[0]
        for beta in [1,2,4]:
            for s in [1,2,4,8,16,32,64,128,256,512,1024,2048,4096]:
                z=(11*s+D*s**(-p/2))/((2/np.sqrt(beta))*np.sqrt(C)*s**((1+2*a)/4))
                rows.append([k,beta,s,z,float(log_ndtr(-z)),1.5-a,(4*k+3)/2])
    with (DATA/'rayleigh_tail.csv').open('w',newline='') as f:
        wr=csv.writer(f);wr.writerow(['k','beta','s','z','log_probability','operator_power','kernel_power']);wr.writerows(rows)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('task',choices=['artificial','quartic','tail'])
    parser.add_argument('--draws',type=int,default=96)
    parser.add_argument('--burn',type=int,default=240)
    parser.add_argument('--thin',type=int,default=2)
    parser.add_argument('--ns',type=int,nargs='+',default=[256,1000,10000])
    parser.add_argument('--banded',action='store_true')
    args=parser.parse_args();guard()
    if args.task=='artificial':artificial(args.draws)
    elif args.task=='quartic':quartic(args.ns,args.burn,args.draws,args.thin,args.banded)
    else:tail()
    print('maxrss_bytes',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,flush=True)
