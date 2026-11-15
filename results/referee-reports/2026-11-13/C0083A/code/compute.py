"""Reproducible, sequential susceptibility checks. See REPORT.md for limits."""
import argparse
import csv
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import time

for variable in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS']:
    os.environ[variable] = '1'
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
EXE = ROOT / 'code' / 'percolation'
OUT = ROOT / 'data'
SEED = 8300311

def run(*args):
    global SEED
    SEED += 1
    p = subprocess.run([str(EXE), *map(str,args)],capture_output=True,text=True,check=True)
    return json.loads(p.stdout)

def sample(n,d,ps,count):
    return run('sample',n,d,SEED,*[v for p in ps for v in (p,count)])

def chi_exact(a,p):
    return math.fsum(v*p**k*(1-p)**(a['E']-k) for k,v in enumerate(a['root_sum']))

def root_exact(a,lam):
    target=lam*a['V']**(1/3)
    if not 1<=target<=a['V']:return None
    lo,hi=0.,1.
    for _ in range(70):
        mid=(lo+hi)/2
        if chi_exact(a,mid)<target:lo=mid
        else:hi=mid
    return (lo+hi)/2

def exact_checks():
    results=[]
    for n,d in [(3,1),(2,2),(2,3),(3,2)]:
        a=run('exact',n,d)
        assert a['count']==[math.comb(a['E'],k) for k in range(a['E']+1)]
        assert a['square_sum']==[a['V']*v for v in a['root_sum']]
        a['roots']={str(lam):root_exact(a,lam) for lam in [0.5,0.75,1.,1.5]}
        if (n,d)==(3,1):
            for p in [.1,.3,.7]:assert abs(chi_exact(a,p)-(1+2*p+2*p*p-2*p**3))<1e-12
        checks=sample(n,d,[.1,.2,.3],200000)
        for p,c in zip([.1,.2,.3],checks):
            c['p']=p;c['exact_chi']=chi_exact(a,p)
            c['z']=(c['mean']-c['exact_chi'])/c['se']
            assert abs(c['z'])<6
        a['mc_validation']=checks
        (OUT/f'exact_n{n}_d{d}.json').write_text(json.dumps(a,indent=2)+'\n')
        results.append({'n':n,'d':d,'E':a['E'],'pc_lambda1':a['roots']['1.0'],
                        'max_abs_z':max(abs(c['z']) for c in checks)})
    print(json.dumps(results,indent=2),flush=True)

def interpolate(ps,cs,target,width,degree):
    center=ps[len(ps)//2]
    x=(np.array(ps)-center)/width
    y=np.array([1/c['mean'] for c in cs])
    err=np.array([c['se']/c['mean']**2 for c in cs])
    X=np.vander(x,degree+1,increasing=True)
    information=(X/err[:,None]).T@(X/err[:,None])
    cov=np.linalg.inv(information)
    beta=cov@((X/err[:,None]).T@(y/err))
    polynomial=beta.copy();polynomial[0]-=1/target
    roots=np.polynomial.polynomial.polyroots(polynomial)
    candidates=[v.real for v in roots if abs(v.imag)<1e-8 and min(x)-.1<=v.real<=max(x)+.1]
    if not candidates:raise ValueError('root not bracketed by fitted curve')
    z=min(candidates,key=lambda v:abs(v))
    v=np.array([z**i for i in range(degree+1)])
    deriv=sum(i*beta[i]*z**(i-1) for i in range(1,degree+1))
    pc=center+z*width
    se=math.sqrt(float(v@cov@v))*width/abs(deriv)
    chisq=float(np.sum(((X@beta-y)/err)**2))
    return {'pc':pc,'se':se,'chisq':chisq,'dof':len(ps)-degree-1,'degree':degree}

def locate(n,d,lam,count):
    V=n**d;m=d*(n-1);target=lam*V**(1/3);width=1/(m*V**(1/3))
    assert 1<target<V
    lo,hi=0.,min(1.,2/m)
    for _ in range(13):
        mid=(lo+hi)/2
        c=sample(n,d,[mid],4000)[0]
        if c['mean']<target:lo=mid
        else:hi=mid
    center=(lo+hi)/2
    for attempt in range(3):
        radius=(0.6 if lam==1 else 1.2)*(1.7**attempt)
        ps=[max(1e-10,min(1-1e-10,center+width*radius*j/3)) for j in range(-3,4)]
        cs=sample(n,d,ps,count)
        try:
            fit=interpolate(ps,cs,target,width,2)
            if cs[0]['mean']<target<cs[-1]['mean']:break
        except ValueError:pass
        center=min(zip(ps,cs),key=lambda a:abs(a[1]['mean']-target))[0]
    else:raise ValueError('failed to bracket target')
    # Restrict the main interpolation to the five points around the crossing.
    j=min(range(7),key=lambda i:abs(cs[i]['mean']-target));start=max(0,min(2,j-2))
    local=interpolate(ps[start:start+5],cs[start:start+5],target,width,2)
    cubic=interpolate(ps,cs,target,width,3)
    A=(2*d*d-1)/(2*(d-1)**2)
    a2=1/d+A/d**2
    result={'n':n,'d':d,'V':V,'lambda':lam,'target_chi':target,'window_scale':width,
            'pc':local['pc'],'se':local['se'],'global_quadratic':fit,'local_quadratic':local,
            'global_cubic':cubic,'interpolation_spread':max(abs(local['pc']-fit['pc']),abs(local['pc']-cubic['pc'])),
            'leading':1/(d*n),'a2_n':a2,'two_terms_n':1/(d*n)+a2/n**2,
            'two_terms_m':1/m+A/m**2,'curve':[{'p':p,**c} for p,c in zip(ps,cs)]}
    (OUT/f'mc_n{n}_d{d}_lambda{lam:g}.json').write_text(json.dumps(result,indent=2)+'\n')
    print(f'd={d} n={n} lambda={lam:g}: pc={local["pc"]:.9g} se={local["se"]:.2g} spread={result["interpolation_spread"]:.2g}',flush=True)
    return result

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--mode',choices=['exact','mc'],required=True)
    ap.add_argument('--count',type=int,default=20000);ap.add_argument('--dimension',type=int)
    args=ap.parse_args()
    if os.getpriority(os.PRIO_PROCESS,0)<10:os.setpriority(os.PRIO_PROCESS,0,10)
    OUT.mkdir(exist_ok=True)
    start=time.time()
    if args.mode=='exact':exact_checks()
    else:
        grid={3:[8,16,32,64],4:[4,8,12,16,24],5:[3,4,6,8,10],6:[3,4,5,6,8]}
        if args.dimension:grid={args.dimension:grid[args.dimension]}
        for d,ns in grid.items():
            for n in ns:
                for lam in [1.,.5]:locate(n,d,lam,args.count)
    info={'elapsed_seconds':time.time()-start,'nice':os.getpriority(os.PRIO_PROCESS,0),
          'threads':1,'seed_start':8300311,'seed_end':SEED,'mode':args.mode,
          'dimension':args.dimension,'final_samples_per_p':200000 if args.mode=='exact' else args.count,
          'maxrss_self':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
          'maxrss_children':resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
          'platform':os.uname().sysname,'maxrss_units':'bytes on macOS'}
    (OUT/f'run_{args.mode}_{args.dimension or "all"}.json').write_text(json.dumps(info,indent=2)+'\n')
    print(json.dumps(info),flush=True)

if __name__=='__main__':main()
