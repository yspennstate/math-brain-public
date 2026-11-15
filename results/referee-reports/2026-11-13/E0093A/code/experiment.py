"""Full-state lazy Cayley walks; exact integer certificates for TV crossing times.

No Monte Carlo walk trajectories are used. Only the generating set is sampled.
One process, one BLAS thread. Outputs are incremental JSONL for recovery/audit.
"""
import os
for key in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS']:
    os.environ[key] = '1'
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)

from collections import Counter, deque
import argparse
from fractions import Fraction
import itertools
import json
import math
from pathlib import Path
import platform
import resource
import time
import numpy as np
import scipy
from scipy.sparse import csr_matrix, eye
from scipy.sparse.linalg import eigsh
from threadpoolctl import threadpool_limits, threadpool_info

ROOT = Path(__file__).resolve().parents[1]

class Group:
    def __init__(self, name, elements, mul, inv, identity, family, parameters):
        self.name, self.elements, self.mul, self.inv = name, elements, mul, inv
        self.index = {x: i for i, x in enumerate(elements)}
        self.e = self.index[identity]
        self.n = len(elements)
        self.family, self.parameters = family, parameters

    def right(self, s):
        return np.fromiter((self.index[self.mul(x,s)] for x in self.elements), dtype=np.int32, count=self.n)

def abelian(moduli):
    elements = list(itertools.product(*(range(q) for q in moduli)))
    return Group('x'.join('C'+str(q) for q in moduli), elements,
                 lambda x,y: tuple((a+b)%q for a,b,q in zip(x,y,moduli)),
                 lambda x: tuple(-a%q for a,q in zip(x,moduli)), (0,)*len(moduli),
                 'abelian', {'moduli':moduli})

def dihedral(p):
    return Group(f'D{2*p}', list(itertools.product(range(p),range(2))),
                 lambda x,y: ((x[0]+(-1 if x[1] else 1)*y[0])%p, x[1]^y[1]),
                 lambda x: ((x[0] if x[1] else -x[0])%p,x[1]), (0,0),
                 'dihedral', {'p':p})

def symmetric(d):
    return Group(f'S{d}',list(itertools.permutations(range(d))),
                 lambda x,y: tuple(x[j] for j in y),
                 lambda x: tuple(x.index(j) for j in range(d)), tuple(range(d)),
                 'symmetric', {'degree':d})

def psl(p):
    def canon(x):
        return min(x,tuple(-a%p for a in x))
    elements=sorted({canon((a,b,c,d)) for a,b,c,d in itertools.product(range(p),repeat=4)
                     if (a*d-b*c)%p == 1})
    def mul(x,y):
        a,b,c,d=x; e,f,g,h=y
        return canon(((a*e+b*g)%p,(a*f+b*h)%p,(c*e+d*g)%p,(c*f+d*h)%p))
    return Group(f'PSL2_{p}',elements,mul,
                 lambda x: canon((x[3],-x[1]%p,-x[2]%p,x[0])), canon((1,0,0,1)),
                 'PSL2', {'p':p})

def heisenberg(p):
    return Group(f'H3_{p}',list(itertools.product(range(p),repeat=3)),
                 lambda x,y: ((x[0]+y[0])%p,(x[1]+y[1])%p,(x[2]+y[2]+x[0]*y[1])%p),
                 lambda x: (-x[0]%p,-x[1]%p,(-x[2]+x[0]*x[1])%p), (0,0,0),
                 'heisenberg', {'p':p})

def generated(maps, e, n):
    seen=np.zeros(n,dtype=bool); seen[e]=True
    stack=[e]
    while stack:
        x=stack.pop()
        for row in maps:
            y=int(row[x])
            if not seen[y]:
                seen[y]=True; stack.append(y)
    return int(seen.sum())==n

def kernel(group, selected):
    signed=Counter()
    for s in selected:
        signed[s]+=1; signed[group.inv(s)]+=1
    support=sorted(signed)
    # Symmetric support permits gathering from predecessors using the same list.
    maps=np.array([group.right(s) for s in support],dtype=np.int32)
    assert all(np.array_equal(np.sort(row),np.arange(group.n)) for row in maps)
    return support,maps,np.array([signed[s] for s in support],dtype=np.int64)

def spectrum(group,maps,weights,hold,denom):
    n=group.n
    rows=np.tile(np.arange(n),len(maps))
    vals=np.repeat(weights/denom,n)
    mat=csr_matrix((vals,(rows,maps.ravel())),shape=(n,n))+hold/denom*eye(n,format='csr')
    assert (mat-mat.T).nnz==0
    if n<=160:
        eig,vec=np.linalg.eigh(mat.toarray())
        lam=float(eig[-2]); v=vec[:,-2]
    else:
        eig,vec=eigsh(mat,k=2,which='LA',tol=1e-11,v0=np.linspace(0,1,n),maxiter=5000)
        assert abs(float(max(eig))-1)<1e-9
        order=np.argsort(eig); lam=float(eig[order[-2]]); v=vec[:,order[-2]]
    residual=float(np.linalg.norm(mat@v-lam*v))
    return 1-lam,residual,mat

def tv_and_certificate(group,maps,weights,hold,denom):
    n=group.n
    dist=np.zeros(n);dist[group.e]=1
    levels=[Fraction(9,10),Fraction(1,2),Fraction(1,4),Fraction(1,10)]
    crossing={}; values={}; snapshots={}
    for t in range(100000):
        tv=float(np.abs(dist-1/n).sum()/2)
        for level in levels:
            key=str(level)
            if key not in crossing and tv<=float(level):
                crossing[key]=t;values[key]=tv
                snapshots[t]=tv
        if len(crossing)==len(levels):break
        new=hold*dist
        for perm,w in zip(maps,weights):new+=int(w)*dist[perm]
        dist=new/denom
    else:raise RuntimeError('mixing time cap reached')
    # Integer recurrence with denominator denom**t, on ALL states. Certifies
    # each recorded first crossing and its preceding step, without rounding.
    counts=np.zeros(n,dtype=object);counts[group.e]=1
    power=1;exact={}
    targets={t for t in crossing.values()}|{max(0,t-1) for t in crossing.values()}
    numerators={}
    for t in range(max(crossing.values())+1):
        if t in targets:
            numer=sum(abs(n*int(c)-power) for c in counts)
            numerators[t]=numer
            for level in levels:
                key=str(level)
                if crossing[key]==t:
                    assert numer*level.denominator <= 2*n*power*level.numerator
                    if t>0:
                        assert numerators[t-1]*level.denominator > 2*n*(power//denom)*level.numerator
                    # Save exact sign/margin as rational fractions, no huge raw counts.
                    below=Fraction(level)-Fraction(numer,2*n*power)
                    above=(Fraction(numerators[t-1],2*n*(power//denom))-level) if t else None
                    exact[key]={'time':t,'below_margin':float(below),
                                'previous_above_margin':float(above) if above is not None else None}
        if t<max(crossing.values()):
            new=hold*counts
            for perm,w in zip(maps,weights):new+=int(w)*counts[perm]
            counts=new;power*=denom
    return crossing,values,exact,float(abs(dist.sum()-1))

def analytic_gap(group,selected,support,weights,model):
    if group.family=='abelian':
        mod=group.parameters['moduli'];n=group.n
        gap=1.
        for char in group.elements:
            if all(a==0 for a in char):continue
            ev=0.5
            for s,w in zip(support,weights):
                ev+=float(w)*math.cos(2*math.pi*sum(a*b/q for a,b,q in zip(char,s,mod)))
            gap=min(gap,1-ev)
        return gap
    if group.family=='dihedral' and len(selected)==2:
        p=group.parameters['p']
        if all(s[1] for s in selected):return math.sin(math.pi/(2*p))**2
        # Two nontrivial rotations cannot generate D2p; a mixed pair has a ladder graph.
        return min((1-math.cos(2*math.pi/p))/(3 if model=='union' else 4),1/3 if model=='union' else 1/2)
    return None

def run(args):
    ROOT.joinpath('data').mkdir(exist_ok=True)
    rng=np.random.default_rng(args.seed)
    factories=[]
    for q in [31,101,251]:factories.append(lambda q=q:abelian([q]))
    for p in [5,7,11]:factories.append(lambda p=p:abelian([p,p]))
    for d in [4,6,8]:factories.append(lambda d=d:abelian([2]*d))
    for p in [7,17,31]:factories.append(lambda p=p:dihedral(p))
    for d in range(3,9):factories.append(lambda d=d:symmetric(d))
    for p in [5,7,11]:factories.append(lambda p=p:psl(p))
    for p in [3,5,7]:factories.append(lambda p=p:heisenberg(p))
    out=ROOT/'data'/'samples.jsonl'
    metadata={'seed':args.seed,'samples_per_k':args.samples,'python':platform.python_version(),
              'numpy':np.__version__,'scipy':scipy.__version__,'priority':os.getpriority(os.PRIO_PROCESS,0),
              'threadpools':threadpool_info(),'sampling':'uniform k-subsets of G, rejection until generating',
              'time':'discrete, lazy holding 1/2; both uniform union and signed tuple measures'}
    (ROOT/'data'/'environment.json').write_text(json.dumps(metadata,indent=2))
    with out.open('w') as stream:
      for factory in factories:
        group=factory()
        if args.only and group.name not in args.only:continue
        n=group.n
        ks=sorted(set([2,3,min(n,math.ceil(2*math.log(n)))]))
        if group.family=='abelian' and all(q==2 for q in group.parameters['moduli']):
            d=len(group.parameters['moduli']);ks=[d,d+2,2*d]
        for k in ks:
          for sample in range(args.samples):
            started=time.monotonic();attempts=0
            while True:
                attempts+=1
                if attempts>10000:raise RuntimeError('generation rejection cap')
                selected=[group.elements[i] for i in rng.choice(n,size=k,replace=False)]
                support,maps,multiplicities=kernel(group,selected)
                if generated(maps,group.e,n):break
            for model in ['union','tuple']:
                m=len(maps)
                weights=np.ones(m,dtype=np.int64) if model=='union' else multiplicities
                hold=m if model=='union' else 2*k
                denom=2*hold
                gap,residual,mat=spectrum(group,maps,weights,hold,denom)
                times,tvs,certificates,mass_error=tv_and_certificate(group,maps,weights,hold,denom)
                expected=analytic_gap(group,selected,support,weights/denom,model)
                if expected is not None:assert abs(gap-expected)<2e-9,(group.name,gap,expected)
                bound=math.ceil(math.log(math.sqrt(n-1)/0.5)/(-math.log1p(-gap)))
                assert times['1/4']<=bound
                rec={'group':group.name,'family':group.family,'parameters':group.parameters,
                     'order':n,'k':k,'sample':sample,'attempts_for_this_acceptance':attempts,
                     'generators':selected,'union_size':m,'model':model,'gap':gap,
                     'eigen_residual':residual,'analytic_gap':expected,'times':times,
                     'crossing_tv_float':tvs,'exact_integer_certificates':certificates,
                     'mass_error':mass_error,'spectral_tv_upper':bound,
                     'abelian_quotient_lower':None,'seconds_elapsed':time.monotonic()-started,
                     'peak_rss_raw':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
                if group.family=='abelian':quotient=n
                elif group.family=='heisenberg':quotient=group.parameters['p']**2
                else:quotient=None
                if quotient and model=='tuple':
                    rec['abelian_quotient_lower']=max(0,(max(0,(quotient/2)**(1/k)-1))**2/8)
                    assert times['1/4']+1e-9>=rec['abelian_quotient_lower']
                stream.write(json.dumps(rec)+'\n');stream.flush()
                print(f'{group.name} k={k} sample={sample} {model}: gap={gap:.6g}, t25={times["1/4"]}, exact crossings verified',flush=True)
    print('FINISHED',out,flush=True)

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--seed',type=int,default=930093)
    parser.add_argument('--samples',type=int,default=2);parser.add_argument('--only',nargs='*')
    with threadpool_limits(limits=1):run(parser.parse_args())
