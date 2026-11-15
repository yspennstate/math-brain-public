"""Circular-law evidence; one BLAS thread, no matrices retained on disk."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[name]='1'
import argparse, csv, json, math, resource, time
from pathlib import Path
import numpy as np
from scipy.linalg import eigvals
from scipy.special import exp1
from scipy.integrate import quad
from threadpoolctl import threadpool_limits, threadpool_info
ROOT=Path(__file__).resolve().parents[1]

def I(a):
    return 1.0 if a==0 else 1-a*math.exp(a)*float(exp1(a))

def sample(rng,n,eps):
    # Y density proportional to exp(-(2+eps)y)/(1+y)^2, y>=0.
    p=2+eps
    out=np.empty(n*n); pos=0
    while pos<out.size:
        size=min(2*(out.size-pos)+100,1000000)
        y=rng.exponential(1/p,size)
        accepted=y[rng.random(size)<1/(1+y)**2]
        k=min(accepted.size,out.size-pos)
        out[pos:pos+k]=np.exp(accepted[:k]); pos+=k
    out*=rng.choice(np.array([-1.,1.]),size=out.size)
    out/=math.sqrt(I(eps)/I(p))
    return np.asfortranarray(out.reshape(n,n)/math.sqrt(n))

def S(x):
    return np.arcsin(x)+x*np.sqrt(np.maximum(0,1-x*x))

def circular_cdf(x,y):
    x=np.clip(np.asarray(x),-1,1); y=np.clip(np.asarray(y),-1,1)
    a=np.abs(x); b=np.abs(y)
    h=np.minimum(a,np.sqrt(np.maximum(0,1-b*b)))
    area=b*h+(S(a)-S(h))/2
    return .25+(S(x)+S(y))/(2*np.pi)+np.sign(x)*np.sign(y)*area/np.pi

def kolmogorov(z):
    # The continuous reference CDF is monotone on every empirical cell.
    # Its extrema on a cell lie at the lower-left/upper-right corners.
    xs,xi=np.unique(z.real,return_inverse=True)
    ys,yi=np.unique(z.imag,return_inverse=True)
    ys=np.append(ys,np.inf)
    hist=np.zeros(len(ys),dtype=np.int64)
    groups=[[] for _ in xs]
    for i,j in zip(xi,yi):groups[i].append(j)
    ans=0.
    for x,g in zip(np.append(xs,np.inf),groups+[[]]):
        reference=circular_cdf(x,ys)
        exclusive=(np.cumsum(hist)-hist)/len(z)
        ans=max(ans,float(np.max(np.abs(exclusive-reference))))
        np.add.at(hist,g,1)
        inclusive=np.cumsum(hist)/len(z)
        ans=max(ans,float(np.max(np.abs(inclusive-reference))))
    return ans

def radial(z):
    r=np.sort(np.abs(z)); f=np.minimum(r*r,1)
    return float(max(np.max(np.abs(np.arange(1,len(z)+1)/len(z)-f)),
                     np.max(np.abs(np.arange(len(z))/len(z)-f))))

def verify():
    rng=np.random.default_rng(918)
    errors=[]
    for x,y in rng.uniform(-1.5,1.5,(30,2)):
        def integrand(t):
            h=math.sqrt(max(0,1-t*t))
            return max(0,min(y,h)+h)/np.pi
        q=quad(integrand,-1,min(1,max(-1,x)),epsabs=1e-10,
               points=[v for v in [-math.sqrt(max(0,1-y*y)),math.sqrt(max(0,1-y*y))] if -1<v<min(1,max(-1,x))])[0]
        errors.append(abs(q-float(circular_cdf(x,y))))
    assert max(errors)<2e-7,max(errors)
    assert abs(kolmogorov(np.array([0j]))-.75)<1e-12
    assert abs(radial(np.array([0j]))-1)<1e-12
    return {'cdf_vs_quadrature_max_error':max(errors),'origin_one_atom_dK':.75,
            'nice':os.getpriority(os.PRIO_PROCESS,0),'threadpools':threadpool_info()}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--sizes',default='128,256,512,1024,2048')
    ap.add_argument('--eps',default='0.25,0.5,1,2');ap.add_argument('--reps',type=int,default=3)
    ap.add_argument('--seed',type=int,default=1092026);args=ap.parse_args()
    assert os.getpriority(os.PRIO_PROCESS,0)>=10
    # Peak live arrays at n=2048 are well below 4GB. Refuse larger unplanned sizes.
    sizes=list(map(int,args.sizes.split(',')));assert max(sizes)<=2500
    with threadpool_limits(limits=1):
        check=verify();(ROOT/'data'/'verification.json').write_text(json.dumps(check,indent=2))
        path=ROOT/'data'/'simulations.csv'
        fields=['eps','n','rep','seed','dK','radial_discrepancy','outside_unit','spectral_radius','sample_variance','max_entry','seconds','rss_mb']
        with path.open('w') as f:
            w=csv.DictWriter(f,fieldnames=fields);w.writeheader();f.flush()
            for ei,eps in enumerate(map(float,args.eps.split(','))):
                for n in sizes:
                    for rep in range(args.reps):
                        seed=args.seed+ei*100000+n*10+rep
                        rng=np.random.default_rng(seed);t=time.monotonic()
                        a=sample(rng,n,eps)
                        sample_var=float(np.mean(a*a)*n);max_entry=float(np.max(np.abs(a))*math.sqrt(n))
                        z=eigvals(a,overwrite_a=True,check_finite=False);del a
                        row=dict(eps=eps,n=n,rep=rep,seed=seed,dK=kolmogorov(z),radial_discrepancy=radial(z),outside_unit=float(np.mean(np.abs(z)>1)),spectral_radius=float(np.max(np.abs(z))),sample_variance=sample_var,max_entry=max_entry,seconds=time.monotonic()-t,rss_mb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024**2)
                        w.writerow(row);f.flush()
                        np.savetxt(ROOT/'data'/f'eigenvalues_eps{eps}_n{n}_rep{rep}.csv',np.column_stack([z.real,z.imag]),delimiter=',',header='real,imag',comments='')
                        print(json.dumps(row),flush=True)
if __name__=='__main__':main()
