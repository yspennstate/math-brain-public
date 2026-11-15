"""Independent referee experiments. No imports or reads from claim_files/.

LP columns are priced by integer programming, not the submission's DP.
Each cell has separate lower/upper endpoints, including exact atom cells.
Run: OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 independent_checks.py
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import csv
import hashlib
import itertools
import json
import math
import resource
import time
import warnings
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import linprog, milp, Bounds, LinearConstraint
from scipy.special import betainc, betaincinv
from threadpoolctl import threadpool_limits, threadpool_info

warnings.filterwarnings('ignore', message='Unrecognized options detected')


class Law:
    def __init__(self, name, atoms, pieces, mean, q, H):
        self.name, self.atoms, self.pieces = name, atoms, pieces
        self.mean, self.q, self.H = mean, q, H
        self.bound = math.ceil((6 / H + 1) / q - 1e-10)

    def cells(self, B):
        # Integer endpoints on mesh 1/B; endpoints of all pieces align.
        lower, upper, mass = [], [], []
        for x, p in self.atoms:
            lower.append(round(B*x)); upper.append(round(B*x)); mass.append(p)
        for a, b, p in self.pieces:
            for j in range(round(a*B), round(b*B)):
                lower.append(j); upper.append(j+1); mass.append(p/(B*(b-a)))
        if self.name == 'quadratic':
            x = np.arange(B+1)/B
            cdf = .1*x + .45*((2*x-1)**3+1)
            lower, upper, mass = list(range(B)), list(range(1, B+1)), list(np.diff(cdf))
        if self.name == 'yin_geometric':
            x = np.arange(B+1)/B
            cdf = self.cdf(x)
            lower, upper, mass = list(range(B)), list(range(1, B+1)), list(np.diff(cdf))
        return np.array(lower), np.array(upper), np.array(mass)

    def cdf(self, x):
        if self.name == 'quadratic':
            return .1*x + .45*((2*x-1)**3+1)
        if self.name == 'yin_geometric':
            z=2*np.asarray(x)-1
            # |2X-1|^2 ~ mixture Beta(m+1/2,1/2), alpha_m=2^-m.
            ans=np.zeros_like(z)
            for m in range(1, 51):
                ans += 2.**(-m) * (.5 + .5*np.sign(z)*betainc(m+.5,.5,z*z))
            return ans/(1-2.**(-50))
        x=np.asarray(x)
        out=np.zeros_like(x)
        for a,p in self.atoms:
            out += p*(x>=a)
        for a,b,p in self.pieces:
            out += p*np.clip((x-a)/(b-a),0,1)
        return out

    def quantiles(self, M):
        u=(np.arange(M)+.5)/M
        if self.name.startswith('atom_uniform'):
            q=self.q
            return np.maximum((u-(1-q))/q, 0)
        if self.name == 'far_uniform':
            return np.where(u<=.9, 0, .9+(u-.9))
        if self.name == 'atomic_ends':
            return np.where(u<.49,0,np.where(u>.51,1,.4+10*(u-.49)))
        lo=np.zeros(M); hi=np.ones(M)
        for _ in range(50):
            mid=(lo+hi)/2
            flag=self.cdf(mid)<u
            lo=np.where(flag,mid,lo); hi=np.where(flag,hi,mid)
        return (lo+hi)/2


def price(low, high, n, target, costs):
    A=np.vstack((np.ones(len(low)),low,high))
    con=LinearConstraint(A, [n,-np.inf,target-1e-9], [n,target+1e-9,np.inf])
    res=milp(costs,integrality=np.ones(len(low)),bounds=Bounds(0,n),
             constraints=con, options={'threads':1, 'mip_rel_gap':0., 'time_limit':15.})
    if res.status == 2:
        return None
    if not res.success:
        raise RuntimeError(('pricing failed',res.message))
    counts=np.rint(res.x).astype(int)
    assert counts.sum()==n and low@counts<=target+1e-7 and high@counts>=target-1e-7
    return counts


def outer_lp(law,n,B):
    low,high,p=law.cells(B)
    assert abs(p.sum()-1)<1e-12 and min(p)>0
    target=B*n*law.mean
    first=price(low,high,n,target,np.zeros(len(p)))
    if first is None:
        return {'lp':'no_tuple', 'lp_l1':None,'lp_lower':None,'columns':0,'B':B}
    columns=[first/n]
    seen={tuple(first)}
    lower_bound=-np.inf
    for step in range(600):
        C=np.array(columns).T; d=len(p); k=len(columns)
        A=np.block([[C,np.eye(d),-np.eye(d)],
                    [np.ones((1,k)),np.zeros((1,2*d))]])
        res=linprog(np.r_[np.zeros(k),np.ones(2*d)],A_eq=A,b_eq=np.r_[p,1],
                    bounds=(0,None),method='highs-ds',
                    options={'threads':1,'dual_feasibility_tolerance':1e-9,
                             'primal_feasibility_tolerance':1e-9})
        if not res.success:
            raise RuntimeError(res.message)
        assert np.all(np.isfinite(res.x)) and np.all(np.isfinite(A))
        u,gamma=res.eqlin.marginals[:-1],res.eqlin.marginals[-1]
        counts=price(low,high,n,target,-u/n)
        reduced=-u@counts/n-gamma
        lower_bound=max(0,float(p@u+gamma+min(0,reduced)))
        if reduced>=-2e-8 or res.fun<1e-10:
            # Positive conclusions require full pricing; feasibility doesn't.
            return {'lp':'excluded' if lower_bound>1e-7 else 'outer_feasible',
                    'lp_l1':float(res.fun),'lp_lower':lower_bound,'columns':len(columns),'B':B,
                    'primal_residual':float(np.max(np.abs(np.sum(A*res.x,axis=1)-np.r_[p,1]))),
                    'reduced_cost':float(reduced)}
        key=tuple(counts)
        if key in seen:
            raise RuntimeError(('pricing duplicated a negative cost column',reduced))
        seen.add(key);columns.append(counts/n)
    raise RuntimeError('column iteration cap')


def rearrange(law,n,M=4000,sweeps=35,restarts=2):
    x=law.quantiles(M)
    best=None
    for restart in range(restarts):
        rng=np.random.default_rng(800000+100*n+restart)
        values=np.column_stack([rng.permutation(x) for _ in range(n)])
        total=values.sum(axis=1)
        previous=np.inf
        for sweep in range(sweeps):
            for j in rng.permutation(n):
                other=total-values[:,j]
                order=np.argsort(other,kind='stable')
                values[order,j]=x[::-1]
                total=other+values[:,j]
            variance=float(np.var(total))
            if previous-variance<1e-17:
                break
            previous=variance
        rms=float(np.sqrt(np.mean((total-n*law.mean)**2)))
        record={'rms':rms,'max_error':float(max(abs(total-n*law.mean))),
                'row_range':float(np.ptp(total)),'sample_mean_bias':float(x.mean()-law.mean),
                'sweeps':sweep+1,'rows':M}
        if best is None or rms<best['rms']:
            best=record
    return best


def self_checks():
    # Exhaustive independent pricing control: every count vector for 5 bins, n=5.
    rng=np.random.default_rng(42)
    low=np.arange(5); high=low+1; n=5; target=12.5
    possibilities=[]
    for indices in itertools.combinations_with_replacement(range(5),n):
        counts=np.bincount(indices,minlength=5)
        if low@counts<=target<=high@counts:
            possibilities.append(counts)
    for _ in range(25):
        costs=rng.normal(size=5)
        found=price(low,high,n,target,costs)
        assert abs(costs@found-min(costs@c for c in possibilities))<1e-8
    control=Law('uniform',[],[(0,1,1)],.5,1,.5)
    assert outer_lp(control,3,20)['lp']=='outer_feasible'
    assert outer_lp(Law('atom_uniform_01',[(0,.9)],[(0,1,.1)],.05,.1,.5),10,40)['lp']=='excluded'
    assert abs(rearrange(control,4,M=200,sweeps=10)['sample_mean_bias'])<1e-12
    return {'exhaustive_mip_pricing_comparisons':25,'uniform_3_lp':'passed',
            'atom_mean_violation_lp':'passed'}


def exact_reservoir_checks():
    # Integrate W exactly by all quantile jump breakpoints, then Y and rounded K.
    rng=np.random.default_rng(717)
    checks=0; nonzero_Ebeta=None
    for case in range(24):
        q=Q(int(rng.integers(1,10)),10)
        H=Q(int(rng.integers(1,4)),10); c=1-H; R=Q(1)
        L=Q(int(rng.integers(0,3)),2)
        support=[Q(0),Q(1,5),Q(1)]
        weights=[Q(1,5),Q(3,10),Q(1,2)]
        mT=sum(x*p for x,p in zip(support,weights)); mE=L/3
        N=math.ceil((3*(2*R+L)/H+1)/q)
        m=N*(1-q); k0=m.numerator//m.denominator
        K=[(k0,1-(m-k0)),(k0+1,m-k0)]
        EC=Q(0); EMbeta=Q(0); Ebeta=Q(0)
        for k,pk in K:
            if not pk:continue
            M=N-k
            assert M>N*q-1 and M>=3
            cuts={Q(0),Q(1)}
            for prob in (weights[0],weights[0]+weights[1]):
                cut=k*prob
                cuts.add(cut-cut.numerator//cut.denominator)
            cuts=sorted(cuts)
            ES=Q(0)
            for left,right in zip(cuts,cuts[1:]):
                w=(left+right)/2
                S=Q(0)
                for j in range(k):
                    u=(j+w)/k
                    S+=support[0] if u<weights[0] else support[1] if u<weights[0]+weights[1] else support[2]
                assert abs(S-k*mT)<=R
                ES+=(right-left)*S
                for Y,pY in ((Q(0),Q(2,3)),(L,Q(1,3))):
                    C=(m-k)*(mT-c)-(S-k*mT)-(Y-mE)
                    beta=3*C/(M*H)
                    assert abs(C)<=2*R+L and abs(beta)<=1
                    probability=pk*(right-left)*pY
                    EC+=probability*C; EMbeta+=probability*M*beta; Ebeta+=probability*beta
                    checks+=1
            assert ES==k*mT
        assert EC==0 and EMbeta==0
        if Ebeta and nonzero_Ebeta is None:
            nonzero_Ebeta={'q':str(q),'N':N,'H':str(H),'L':str(L),'Ebeta':str(Ebeta)}
    return {'finite_states_checked':checks,'cases':24,'failures':0,
            'example_unweighted_tilt_not_zero':nonzero_Ebeta}


def main():
    start=time.monotonic()
    with threadpool_limits(limits=1):
        controls=self_checks()
        exact=exact_reservoir_checks()
        laws=[Law('atom_uniform_01',[(0,.9)],[(0,1,.1)],.05,.1,.5),
              Law('atom_uniform_005',[(0,.95)],[(0,1,.05)],.025,.05,.5),
              Law('quadratic',[],[],.5,.1,.5),
              Law('far_uniform',[(0,.9)],[(.9,1,.1)],.095,.1,.05),
              Law('atomic_ends',[(0,.49),(1,.49)],[(.4,.6,.02)],.5,.02,.1),
              Law('yin_geometric',[],[],.5,1/(8*np.pi*np.sqrt(3)),1/16)]
        # Yin is rescaled from [-1,1] to [0,1]; H halves and R halves.
        specs={
            'atom_uniform_01':[(10,80),(19,80),(20,80),(21,80),(30,80),(130,None)],
            'atom_uniform_005':[(20,80),(39,80),(40,80),(41,80),(260,None)],
            'quadratic':[(3,80),(4,80),(5,80),(7,80),(15,40),(30,40),(130,None)],
            'far_uniform':[(9,80),(10,80),(11,80),(19,80),(20,80),(21,80),(29,80),(30,80),(31,80),(100,40),(1210,None)],
            'atomic_ends':[(3,80),(4,80),(15,80),(49,200),(50,80),(51,200),(149,80),(150,80),(151,80)],
            'yin_geometric':[(3,80),(5,80),(7,80),(11,80),(21,40)]}
        results=[]
        for law in laws:
            for n,B in specs[law.name]:
                tick=time.monotonic()
                record={'law':law.name,'n':n,'theorem2_N':law.bound}
                if B is not None:record.update(outer_lp(law,n,B))
                else:record.update({'lp':'not_run','B':None})
                record.update(rearrange(law,n,M=4000 if n<=260 else 1000,
                                        sweeps=35 if n<=260 else 6,
                                        restarts=2 if n<=260 else 1))
                record['seconds']=time.monotonic()-tick
                results.append(record)
                Path('independent_results.json').write_text(json.dumps({'controls':controls,'exact':exact,'results':results},indent=2))
                print(json.dumps(record),flush=True)
        metadata={'seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                  'numpy':np.__version__,'scipy':scipy.__version__,'threadpools':threadpool_info(),
                  'native_solver_threads':1,'max_workers':1,
                  'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
        Path('independent_results.json').write_text(json.dumps({'controls':controls,'exact':exact,'metadata':metadata,'results':results},indent=2))
        keys=sorted(set().union(*(r.keys() for r in results)))
        with Path('independent_results.csv').open('w') as f:
            writer=csv.DictWriter(f,fieldnames=keys);writer.writeheader();writer.writerows(results)
        print(json.dumps(metadata),flush=True)


if __name__=='__main__':main()
