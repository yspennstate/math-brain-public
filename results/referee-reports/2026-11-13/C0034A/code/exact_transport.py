"""Rational DPP couplings: HiGHS proposes a support; exact integer algebra certifies it.

All certificate validity checks are rational. A failed floating solve is never
reported as an infeasible DPP instance without a verified rational dual.
"""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']:
    os.environ[key]='1'
import resource
# This sandbox rejects setrlimit for both RLIMIT_AS and RLIMIT_DATA.
# Keep matrices tiny and record/check peak resident memory at checkpoints.
assert os.getpriority(os.PRIO_PROCESS,0)>=10
import itertools as it
import json, math, random, time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
from scipy.optimize import linprog, OptimizeWarning
import warnings
warnings.filterwarnings('ignore',message='Unrecognized options detected:.*',category=OptimizeWarning)
from scipy.linalg import qr
import sympy as sp
from sympy.polys.matrices import DomainMatrix

ROOT=Path(__file__).resolve().parents[1]

def dump(path,record):
    peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak<3*1024**3, f'RSS guard: {peak} bytes'
    path.write_text(json.dumps(record,indent=2)+'\n')

def bareiss(a):
    """Integer determinant, including the empty determinant."""
    a=[list(map(int,row)) for row in a]; n=len(a)
    if n==0:return 1
    sign=1; prev=1
    for k in range(n-1):
        if a[k][k]==0:
            j=next((j for j in range(k+1,n) if a[j][k]),None)
            if j is None:return 0
            a[k],a[j]=a[j],a[k];sign=-sign
        pivot=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator%prev==0
                a[i][j]=numerator//prev
        for i in range(k+1,n):a[i][k]=0
        prev=pivot
    return sign*a[-1][-1]

def rational_orthogonal(n,seed,family):
    rng=random.Random(seed)
    if family=='cayley':
        S=sp.zeros(n)
        for i in range(n):
            for j in range(i):
                S[i,j]=sp.Rational(rng.randint(-3,3),3)
                S[j,i]=-S[i,j]
        Q=(sp.eye(n)-S)*(sp.eye(n)+S).inv()
    elif family=='givens':
        Q=sp.eye(n)
        pairs=list(it.combinations(range(n),2));rng.shuffle(pairs)
        for i,j in pairs:
            c,s=rng.choice([(sp.Rational(3,5),sp.Rational(4,5)),(sp.Rational(5,13),sp.Rational(12,13))])
            if rng.randrange(2):s=-s
            G=sp.eye(n);G[i,i]=G[j,j]=c;G[i,j]=-s;G[j,i]=s
            Q=G*Q
    else:raise ValueError(family)
    assert Q.T*Q==sp.eye(n)
    return [[F(x) for x in row] for row in Q.tolist()]

class Instance:
    def __init__(self,Q):
        self.Q=Q; self.n=len(Q);self.cache={}
        self.D=math.lcm(*(x.denominator for row in Q for x in row))
        self.N=[[int(x*self.D) for x in row] for row in Q]
    def law(self,cols):
        cols=tuple(sorted(cols))
        if cols not in self.cache:
            r=len(cols); d=self.D**(2*r)
            self.cache[cols]={B:F(bareiss([[self.N[i][j] for j in cols] for i in B])**2,d)
                             for B in it.combinations(range(self.n),r)}
            assert sum(self.cache[cols].values())==1
        return self.cache[cols]

def transport_structure(n,p,q):
    As=list(it.combinations(range(n),p));Bs=list(it.combinations(range(n),q));Cs=list(it.combinations(range(n),p+q))
    ia={s:i for i,s in enumerate(As)};ib={s:i+len(As) for i,s in enumerate(Bs)};ic={s:i+len(As)+len(Bs) for i,s in enumerate(Cs)}
    pairs=[]; indices=[]
    for C in Cs:
        for A in it.combinations(C,p):
            B=tuple(e for e in C if e not in A)
            pairs.append((A,B));indices.append((ia[A],ib[B],ic[C]))
    M=np.zeros((len(As)+len(Bs)+len(Cs),len(pairs)),dtype=np.int64)
    for j,inds in enumerate(indices):M[list(inds),j]=1
    return As,Bs,Cs,pairs,indices,M

def rational_vertex(M,b,x):
    support=np.flatnonzero(x>1e-12)
    if not len(support):raise ValueError('empty support')
    C=M[:,support]
    _,R,rows=qr(C.T.astype(float),pivoting=True,mode='economic')
    if min(abs(np.diag(R)))<1e-10:raise ValueError('numerically dependent support')
    rows=rows[:len(support)]
    L=math.lcm(*(b[i].denominator for i in rows))
    A=sp.Matrix(C[rows,:].tolist())
    rhs=sp.Matrix([int(b[i]*L) for i in rows])
    numer,den=DomainMatrix.from_Matrix(A).solve_den(DomainMatrix.from_Matrix(rhs))
    values=[F(int(v),int(den)*L) for v in numer.to_Matrix()]
    if min(values)<0:raise ValueError('negative exact coordinate')
    residual=[-v for v in b]
    for j,v in zip(support,values):
        for i in np.flatnonzero(M[:,j]):residual[i]+=v
    if any(residual):raise ValueError('nonzero exact residual')
    return [(int(j),v) for j,v in zip(support,values) if v]

def solve_instance(inst,cols1,cols2,seed=0):
    n=inst.n;p=len(cols1);q=len(cols2)
    As,Bs,Cs,pairs,inds,M=transport_structure(n,p,q)
    a=inst.law(cols1); b=inst.law(cols2); c=inst.law(tuple(sorted(cols1+cols2)))
    rhs=[a[A] for A in As]+[b[B] for B in Bs]+[c[C] for C in Cs]
    bf=np.array(list(map(float,rhs)))
    rng=np.random.default_rng(seed)
    errors=[]
    for attempt in range(8):
        cost=np.zeros(len(pairs)) if attempt==0 else rng.normal(size=len(pairs))
        # Very small marginal masses can be rounded away by the LP; exact
        # reconstruction rejects any resulting missing mass or negativity.
        result=linprog(cost,A_eq=M,b_eq=bf,bounds=(0,None),method='highs-ds',
                       options={'primal_feasibility_tolerance':1e-9,'dual_feasibility_tolerance':1e-9,
                                'threads':1,'parallel':False})
        if not result.success:
            errors.append(result.message);continue
        try:
            vertex=rational_vertex(M,rhs,result.x)
            cert={'n':n,'columns1':list(cols1),'columns2':list(cols2),
                  'Q':[[str(x) for x in row] for row in inst.Q],
                  'coupling':[{'A':list(pairs[j][0]),'B':list(pairs[j][1]),'mass':str(v)} for j,v in vertex],
                  'method':'HiGHS support + fraction-free exact integer solve + all rational marginal checks',
                  'exact_residual':'0','attempt':attempt}
            return cert
        except ValueError as e:errors.append(str(e))
    raise RuntimeError(f'Uncertified n={n}, p={p}, q={q}: {errors}')

def run():
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--quick',action='store_true');args=parser.parse_args()
    out=ROOT/'data/certificates';out.mkdir(exist_ok=True)
    summary=[];t0=time.monotonic()
    ns=range(2,5) if args.quick else range(2,8)
    families=['cayley'] if args.quick else ['cayley','givens','cayley']
    for n in ns:
        for rep,family in enumerate(families):
            seed=340000+n*100+rep
            inst=Instance(rational_orthogonal(n,seed,family))
            for p in range(1,n):
                for q in range(1,n-p+1):
                    name=f'n{n}_{family}{rep}_p{p}_q{q}'
                    cert=solve_instance(inst,tuple(range(p)),tuple(range(p,p+q)),seed+p*11+q)
                    cert.update({'family':family,'seed':seed,'suite':'all_rank_splits'})
                    dump(out/f'{name}.json',cert)
                    summary.append({'name':name,'n':n,'p':p,'q':q,'support':len(cert['coupling']),'attempt':cert['attempt'],'suite':'all_rank_splits'})
            dump(ROOT/'data/exact_summary.json',{'certified':len(summary),'elapsed_seconds':time.monotonic()-t0,'instances':summary})
            print(f'n={n} {family}{rep}: cumulative {len(summary)} certified, {time.monotonic()-t0:.1f}s',flush=True)
    if not args.quick:
        # Every column allocation of the only rank triples not already covered
        # by rank-one/duality at n=6,7, modulo permutation of the three colors.
        for n,sizes in [(6,(2,2,2)),(7,(2,2,3))]:
            inst=Instance(rational_orthogonal(n,340000+n*100,'cayley'))
            count=0
            for A in it.combinations(range(n),2):
                rest=tuple(x for x in range(n) if x not in A)
                for B in it.combinations(rest,2):
                    C=tuple(x for x in rest if x not in B)
                    if not (A<B):continue
                    if n==6 and not B<C:continue
                    name=f'n{n}_allalloc_A'+''.join(map(str,A))+'_B'+''.join(map(str,B))
                    cert=solve_instance(inst,A,B,340+n*100+count)
                    cert.update({'family':'cayley','seed':340000+n*100,'suite':'all_unsettled_column_allocations'})
                    dump(out/f'{name}.json',cert)
                    summary.append({'name':name,'n':n,'p':2,'q':2,'support':len(cert['coupling']),'attempt':cert['attempt'],'suite':'all_unsettled_column_allocations'})
                    count+=1
                    if count%15==0:print(f'n={n}: {count} column allocations certified',flush=True)
            assert count=={6:15,7:105}[n]
            dump(ROOT/'data/exact_summary.json',{'certified':len(summary),'elapsed_seconds':time.monotonic()-t0,'instances':summary})
    resources={'nice':os.getpriority(os.PRIO_PROCESS,0),'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
               'thread_env':{key:os.environ[key] for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS']},
               'highs_threads':1,'highs_parallel':False}
    dump(ROOT/'data/exact_resources.json',resources)
    print('DONE',len(summary),time.monotonic()-t0,resources,flush=True)

if __name__=='__main__':run()
