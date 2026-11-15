"""Full integer-lattice PMFs by recursive convolution, never pruning tails."""
from common import log,memory_check
import argparse, pathlib, csv, json, math
import numpy as np
from scipy.signal import fftconvolve
from fractions import Fraction
p=argparse.ArgumentParser();p.add_argument('--n',type=int,default=200);p.add_argument('--indices',default='S,C,QC');a=p.parse_args()
data=np.load('moments.npz')['moments']
root=pathlib.Path('pmf');root.mkdir(exist_ok=True)
def toll(name,n,i):return n if name=='S' else abs(n-2*i) if name=='C' else (n-2*i)**2
for name in a.indices.split(','):
    folder=root/name;folder.mkdir(exist_ok=True)
    pm=[None,np.array([1.])];offset=[0,0];h=0.;errors=[];negative=0.
    # An independent, exact rational convolution for small trees.
    rational=[None,{0:Fraction(1)}];hr=Fraction(0)
    for n in range(2,a.n+1):
        h+=1/(n-1)
        lo=min(offset[i]+offset[n-i]+toll(name,n,i) for i in range(1,n))
        hi=max(offset[i]+len(pm[i])-1+offset[n-i]+len(pm[n-i])-1+toll(name,n,i) for i in range(1,n))
        out=np.zeros(hi-lo+1)
        for i in range(1,n//2+1):
            j=n-i;q=n/(h*i*j)*(0.5 if i==j else 1)
            u,v=pm[i],pm[j]
            if min(len(u),len(v))<=32:z=np.convolve(u,v)
            else:z=fftconvolve(u,v)
            start=offset[i]+offset[j]+toll(name,n,i)-lo
            out[start:start+len(z)]+=q*z
        neg=-float(np.sum(out[out<0]));negative=max(negative,neg)
        out[out<0]=0
        mass=float(out.sum());out/=mass
        pm.append(out);offset.append(lo)
        np.save(folder/f'{n:03}.npy',out)
        x=np.arange(lo,hi+1,dtype=float);mu=float(np.sum(out*x));d=x-mu
        vals=[mu,float(np.sum(out*(d*d))),float(np.sum(out*(d**3))),float(np.sum(out*(d**4)))]
        k={'S':0,'C':1,'QC':2}[name]
        rel=[abs(v-float(data[n,k,r]))/max(1,abs(float(data[n,k,r]))) for r,v in enumerate(vals)]
        errors.append([n,lo,hi,mass,neg,*rel])
        if n<=12:
            hr+=Fraction(1,n-1);rr={}
            for i in range(1,n):
                j=n-i;q=Fraction(n,2*i*j)/hr;t=toll(name,n,i)
                for u,pu in rational[i].items():
                    for v,pv in rational[j].items():rr[u+v+t]=rr.get(u+v+t,Fraction(0))+q*pu*pv
            rational.append(rr)
            err=max(abs(float(rr.get(t,Fraction(0)))-out[t-lo]) for t in range(lo,hi+1))
            assert err<1e-12,(name,n,err)
        if n%25==0 or n==a.n:
            memory_check();log(f'Full PMF {name} n={n}, lattice points={len(out)}, mass before normalization={mass:.16g}, negative mass={neg:.3g}, relative moment errors={rel}')
    with open(folder/'offsets.json','w') as f:json.dump(offset,f)
    with open(folder/'checks.csv','w') as f:
        w=csv.writer(f);w.writerow(['n','min','max','mass_before_normalization','negative_mass','relative_mean','relative_variance','relative_central3','relative_central4']);w.writerows(errors)
    log(f'Completed {name} PMFs to {a.n}; exact rational PMF agreement to n=12; maximum negative mass {negative}')
    del pm
