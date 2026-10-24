"""Small exact controls for the assigned open-problem batch; all writes are local."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
import json, math, random, time, sys

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'measurements'
OUT.mkdir(exist_ok=True)

def save(name, result, started):
    result.update(experiment=name, seconds=round(time.perf_counter()-started, 4),
                  command='python -X utf8 experiments.py '+name)
    (OUT/(name+'.json')).write_text(json.dumps(result, indent=2), encoding='utf-8')
    with (ROOT/'MEASUREMENTS.jsonl').open('a', encoding='utf-8') as f:
        f.write(json.dumps(result)+'\n')
    print(name, json.dumps(result), flush=True)

def fill_run(perm, target, steps=60):
    n=len(perm); a=[F(1)]*n; b=list(target)
    positions=list(range(n)); survival=[F(1)]*n; landed=[F(0)]*n
    for stage in range(steps):
        m=[min(x,y) for x,y in zip(a,b)]
        h=[m[i]/a[i] if a[i] else F(0) for i in range(n)]
        for origin in range(n):
            y=positions[origin]
            landed[y]+=survival[origin]*h[y]/n
            survival[origin]*=1-h[y]
            positions[origin]=perm[y]
        remaining=[a[i]-m[i] for i in range(n)]
        pushed=[F(0)]*n
        for i in range(n): pushed[perm[i]]=remaining[i]
        a=pushed; b=[b[i]-m[i] for i in range(n)]
        assert sum(a)==sum(b)==sum(survival)
        if not sum(a): break
    return landed, sum(a)/n, stage+1

def filling():
    start=time.perf_counter(); rng=random.Random(330); checked=0; max_steps=0
    for trial in range(160):
        sizes=[rng.randint(1,12) for _ in range(1+trial%4)]
        n=sum(sizes); perm=list(range(n)); target=[F(0)]*n; base=0
        for size in sizes:
            weights=[rng.randint(0,9) for _ in range(size)]; weights[-1]+=1
            for j in range(size):
                perm[base+j]=base+(j+1)%size
                target[base+j]=F(size*weights[j],sum(weights))
            base+=size
        law,residual,stages=fill_run(perm,target)
        assert residual==0 and law==[x/n for x in target]
        checked+=1; max_steps=max(max_steps,stages)
    law,residual,stages=fill_run([1,2,3,0,5,6,7,4],[F(2)]*4+[F(0)]*4)
    assert residual==F(1,2) and sum(law)==F(1,2)
    save('filling',dict(balanced_cases=checked,max_stages=max_steps,exact_law_error='0',
         unbalanced_remaining_mass=str(residual),note='Finite controls; not an infinite-space proof'),start)

def harmonic(n): return sum((F(1,i) for i in range(1,n+1)),F(0))
def split(n,i): return F(n,2*i*(n-i))/harmonic(n-1)

def brownian_lengths():
    start=time.perf_counter(); rng=random.Random(328); checks=0
    times=[F(-9,4),F(-1,3),F(0),F(2,5),F(7,3)]
    for case in range(32):
        intervals=[]
        for sign in [-1,1]:
            bound=F(0)
            while bound<3:
                length=F(rng.randint(1,12),rng.randint(1,10))
                if sign>0: intervals.append((bound,bound+length))
                else: intervals.append((-bound-length,-bound))
                bound+=length
        for s in times:
            for t in times:
                lo=max(min(s,0),min(t,0)); hi=min(max(s,0),max(t,0))
                actual=sum((max(F(0),min(b,hi)-max(a,lo)) for a,b in intervals),F(0))
                expected=min(abs(s),abs(t)) if s*t>0 else F(0)
                assert actual==expected; checks+=1
    save('brownian_lengths',dict(length_configurations=32,covariance_entries=checks,
         exact_covariance_error='0',scope='Externally chosen lengths independent of every driver'),start)

def balance():
    start=time.perf_counter(); laws={1:{(0,0):F(1)}}; mus={1:(F(0),F(0))}; variances={1:(F(0),F(0),F(0))}
    for n in range(2,10):
        law=defaultdict(F)
        for i in range(1,n):
            q=split(n,i)
            for (s1,c1),p1 in laws[i].items():
                for (s2,c2),p2 in laws[n-i].items():
                    law[n+s1+s2,abs(n-2*i)+c1+c2]+=q*p1*p2
        assert sum(law.values())==1
        assert all(s>=c and (s-c)%2==0 for s,c in law)
        u=sum(s*p for (s,c),p in law.items()); v=sum(c*p for (s,c),p in law.items())
        moments=(sum((s-u)**2*p for (s,c),p in law.items()),
                 sum((c-v)**2*p for (s,c),p in law.items()),
                 sum((s-u)*(c-v)*p for (s,c),p in law.items()))
        rec=[F(0),F(0),F(0)]
        for i in range(1,n):
            j=n-i; q=split(n,i)
            ds=n+mus[i][0]+mus[j][0]-u; dc=abs(n-2*i)+mus[i][1]+mus[j][1]-v
            for k,t in enumerate([ds*ds,dc*dc,ds*dc]):
                rec[k]+=q*(variances[i][k]+variances[j][k]+t)
        assert tuple(rec)==moments
        laws[n]=dict(law); mus[n]=(u,v); variances[n]=moments
    for n in range(2,101):
        h=harmonic(n-1); qs=[split(n,i) for i in range(1,n)]
        assert sum(qs)==1
        emin=sum(min(i,n-i)*qs[i-1] for i in range(1,n))
        formula=F(n)/h*(h-harmonic(n//2)+(F(1,n) if n%2==0 else 0))
        assert emin==formula
        assert sum((n-2*i)**2*qs[i-1] for i in range(1,n))==n*n-F(2*n*(n-1))/h
    data=[dict(s=s,c=c,p=str(p)) for (s,c),p in sorted(laws[9].items())]
    (OUT/'balance_joint_n9.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    save('balance',dict(exact_joint_sizes='1..9',one_split_sizes='2..100',
        joint_n9_support=len(data),normalization_error='0',moment_error='0',
        n9_mean_S=str(mus[9][0]),n9_mean_C=str(mus[9][1]),
        scope='Finite laws and moments; no limiting law claimed'),start)

def parts(n, maxpart=None):
    if n==0: yield (); return
    if maxpart is None: maxpart=n
    for a in range(min(n,maxpart),0,-1):
        for tail in parts(n-a,a): yield (a,)+tail

def hook_product(shape):
    product=1
    for i,row in enumerate(shape):
        for j in range(row):
            below=sum(r>j for r in shape[i+1:])
            product*=row-j+below
    return product

def dimension(shape): return math.factorial(sum(shape))//hook_product(shape)

@lru_cache(None)
def tableau_recurrence(shape):
    if not shape: return 1
    total=0
    for i,a in enumerate(shape):
        if i+1==len(shape) or a>shape[i+1]:
            child=list(shape); child[i]-=1
            if child[i]==0: child.pop(i)
            total+=tableau_recurrence(tuple(child))
    return total

def young():
    start=time.perf_counter(); cases=[]
    for b in range(2,101):
        a=b+4; before=(a,a-1)+(1,)*b; after=(a-1,a-1)+(1,)*(b+1)
        ratio=F(dimension(after),dimension(before)); predicted=F(a*(a+b-1),2*(a+b)*(b+1))
        assert ratio==predicted and ratio<1
        cases.append(dict(b=b,n=3*b+7,ratio=str(ratio)))
    for a in range(2,9):
        for b in range(5):
            assert F(dimension((a-1,a-1)+(1,)*(b+1)),dimension((a,a-1)+(1,)*b))==F(a*(a+b-1),2*(a+b)*(b+1))
    assert dimension((6,5,1,1))==5720 and dimension((5,5,1,1,1))==5005
    (OUT/'young_family_exact.json').write_text(json.dumps(cases,indent=2),encoding='utf-8')
    save('young',dict(family_cases=len(cases),boundary_cases=35,ratio_error='0',
         first_dimensions=[5720,5005],last_ratio=cases[-1]['ratio'],
         scope='Infinite family proved separately; numeric checks are finite'),start)

def hammersley():
    start=time.perf_counter(); comparisons=0
    for n in range(1,13):
        dims=[]
        for shape in parts(n):
            d=dimension(shape); assert d==tableau_recurrence(shape)
            comparisons+=1; dims.append(d)
        assert sum(d*d for d in dims)==math.factorial(n)
    bounds=[]
    for m in [8,12,16,20]:
        tail2=F(1,math.factorial(m))
        tail3=F(sum(dimension(p)**2 for p in parts(m) if p[0]<3),math.factorial(m))
        assert tail3==F(math.comb(2*m,m)//(m+1),math.factorial(m))
        mass2=sum((F(b-1,math.factorial(b)) for b in range(2,m+1)),F(0))
        assert 1-mass2==tail2
        bounds.append(dict(M=m,k2_tail_exact=str(tail2),k2_tail=float(tail2),
                           k3_tail_exact=str(tail3),k3_tail=float(tail3)))
    save('hammersley',dict(hook_vs_tableau_comparisons=comparisons,
        plancherel_mass_sizes='1..12',bounds=bounds,
        scope='Certified omitted mixture mass, conditional on the established representation'),start)

def dgff():
    start=time.perf_counter(); eps=0.25
    phases=[]
    for k in [1,3,6,10]:
        vals=[]
        for angle in [math.pi/2,3*math.pi/2]:
            h=angle+2*math.pi*k
            vals.append(math.floor(math.exp(h)*(1+eps*math.sin(h)))*math.exp(-h))
        phases.append(dict(k=k,normalized=vals))
    residues=[dict(delta=d,value=1+eps*d/(d*d+1)) for d in [0.1,0.01,0.001]]
    save('dgff',dict(derivative_lower_factor=1-eps*math.sqrt(2),phases=phases,
        unrounded_abelian_residues=residues,
        scope='Generic counting-function counterexample to a Tauberian route, not to DGFF'),start)

def one_arm():
    start=time.perf_counter(); sums=0; n=0; endpoints=[]
    for k in range(6):
        length=10**(2**(k+1)); a=1+k%2; sums+=a*length; n+=length
        survival=F(1,1+sums)
        assert F(1,1+2*n)<=survival<=F(1,1+n)
        endpoints.append(dict(block=k,a=a,n=str(n),n_survival=float(n*survival)))
    q=F(1); sums=0
    for k in range(50):
        a=1+k%2; q=q/(1+a*q); sums+=a
        assert q==F(1,1+sums)
    save('one_arm',dict(composition_checks=50,endpoints=endpoints,
        scope='Critical branching in varying environment; not a homogeneous percolation counterexample'),start)

def coefficients():
    start=time.perf_counter(); prefix=[1,-1,2,-5]; m=len(prefix)-1
    polynomial=lambda n: prefix[n] if n<=m else 0
    factorial_tail=lambda n: prefix[n] if n<=m else math.factorial(n)
    assert all(polynomial(n)==factorial_tail(n) for n in range(m+1))
    roots=[dict(n=n,root=math.exp(math.lgamma(n+1)/n)) for n in [10,20,40,80]]
    save('coefficients',dict(demo_prefix=prefix,identical_prefix_terms=4,tail_roots=roots,
        scope='Arbitrary-prefix nonidentifiability proof; demo coefficients are not SAW data'),start)

def folner():
    start=time.perf_counter(); rows=[]
    for L in [2,4,8,16,32]:
        s={(x,y) for x in range(L) for y in range(L)}
        s|={(x,y) for x in range(2*L,3*L) for y in range(L)}
        s|={(x,0) for x in range(L,2*L)}
        boundary=sum((x+dx,y+dy) not in s for x,y in s for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)])
        assert len(s)==2*L*L+L and boundary==10*L-2
        rows.append(dict(L=L,volume=len(s),boundary=boundary,ratio=boundary/len(s),
                         corridor_open_upper_bound=0.75**(L+1)))
    nested=[]
    previous=set()
    for L in [1,8,64]:
        s={(x,y) for x in range(-L,L) for y in range(-L,L)}
        s|={(x,y) for x in range(3*L,5*L) for y in range(-L,L)}
        s|={(x,-L) for x in range(L,3*L)}
        assert previous<=s and len(s)==8*L*L+2*L
        boundary=sum((x+dx,y+dy) not in s for x,y in s for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)])
        assert boundary==20*L-2
        nested.append(dict(L=L,volume=len(s),boundary=boundary))
        previous=s
    save('folner',dict(exact_geometry_cases=5,rows=rows,nested_exhaustion_cases=nested,
        scope='Connected Folner geometry does not force internal coarse connectivity'),start)

def arcs():
    start=time.perf_counter()
    crossings=[dict(first_m_circles=m,forced_crossings=m) for m in [1,10,100,1000]]
    save('arcs',dict(nested_circle_controls=crossings,
        scope='Deterministic compact-set obstruction by the intermediate value theorem, not Brownian evidence'),start)

FUNCTIONS={k:globals()[k] for k in ['filling','balance','young','brownian_lengths','hammersley','dgff','one_arm','coefficients','folner','arcs']}
if __name__=='__main__':
    selected=sys.argv[1:] or list(FUNCTIONS)
    for name in selected: FUNCTIONS[name]()
