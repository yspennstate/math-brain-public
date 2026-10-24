#!/usr/bin/env python3
"""Exact finite checks for polynomial twists of independently supported symmetric cores.

Standard library only. Walsh amplitudes, influences, polynomial structure and
entropy identities are exact. Inequalities use rational logarithm enclosures.
These finite checks supplement, and do not replace, the proof in REPORT.md.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, product
import hashlib
import json
from pathlib import Path
import random

BITS = 90
SERIES_TERMS = 48
SEED = 202609200741

@lru_cache(None)
def factor(n: int) -> tuple[tuple[int, int], ...]:
    if n < 1:
        raise ValueError("Only positive integers can be factored")
    ans = []
    p = 2
    while p*p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p; e += 1
            ans.append((p, e))
        p = 3 if p == 2 else p+2
    if n > 1:
        ans.append((n, 1))
    return tuple(ans)

@lru_cache(None)
def ln_unit(x: F) -> tuple[F, F]:
    """Enclose ln(x), 1 <= x <= 2, using the positive atanh series."""
    assert 1 <= x <= 2
    z = (x-1)/(x+1)
    s = F(0); term = z
    for k in range(SERIES_TERMS):
        s += 2*term/(2*k+1)
        term *= z*z
    tail = 2*term/((2*SERIES_TERMS+1)*(1-z*z))
    D = 1 << BITS
    lower = F((s.numerator*D)//s.denominator, D)
    upper_raw = s+tail
    upper = F(-((-upper_raw.numerator*D)//upper_raw.denominator), D)
    return lower, upper

LN2_LO, LN2_HI = ln_unit(F(2))
C_LO, C_HI = 2/LN2_HI, 2/LN2_LO

@lru_cache(None)
def log_int(n: int) -> tuple[F, F]:
    if n < 1:
        raise ValueError("Logarithm argument must be positive")
    k = n.bit_length()-1
    if n == 1 << k:
        return F(k), F(k)
    lo, hi = ln_unit(F(n, 1 << k))
    return k+lo/LN2_HI, k+hi/LN2_LO

class LogForm:
    """An exact rational linear form in log_2(prime), including log_2(2)=1."""
    def __init__(self, terms=None):
        self.terms = {p:F(c) for p,c in (terms or {}).items() if c}
    def __add__(self, other):
        d = dict(self.terms)
        for p,c in other.terms.items():
            d[p] = d.get(p,F(0))+c
        return LogForm(d)
    def __neg__(self):
        return LogForm({p:-c for p,c in self.terms.items()})
    def __sub__(self, other):
        return self+(-other)
    def __mul__(self, q):
        return LogForm({p:c*q for p,c in self.terms.items()})
    __rmul__ = __mul__
    def interval(self):
        lo=F(0); hi=F(0)
        for p,c in self.terms.items():
            a,b=log_int(p)
            lo+=c*(a if c>=0 else b)
            hi+=c*(b if c>=0 else a)
        return lo,hi
    def zero(self):
        return not self.terms

ZERO = LogForm()
def log_form(n):
    return LogForm(dict(factor(n)))
def constant(q):
    return LogForm({2:F(q)})

@lru_cache(None)
def entropy_counts_key(items: tuple[tuple[int,int],...], den: int) -> LogForm:
    assert sum(w*k for w,k in items)==den
    out=log_form(den)
    for w,k in items:
        if w:
            out=out-log_form(w)*F(w*k,den)
    return out

def entropy_counts(weights) -> LogForm:
    weights=tuple(weights)
    den=sum(weights)
    assert den>0
    items=tuple(sorted(Counter(w for w in weights if w).items()))
    return entropy_counts_key(items,den)

@lru_cache(None)
def binary_entropy(t: F) -> LogForm:
    assert 0<=t<=1
    return entropy_counts((t.numerator,t.denominator-t.numerator))

def nonnegative(e: LogForm, context: str):
    if e.zero():
        return
    lo,hi=e.interval()
    if lo<0:
        raise AssertionError((context,"negative or unresolved enclosure",str(lo),str(hi),e.terms))

def leq_c(e: LogForm, q: F, context: str):
    """Prove e <= (2/ln 2) q, with exact zero handling."""
    assert q>=0
    if q==0:
        nonnegative(-e,context)
    else:
        assert e.interval()[1] <= C_LO*q, (context,e.terms,str(q))

def fwht(values):
    a=list(values); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                x,y=a[k],a[k+h]
                a[k],a[k+h]=x+y,x-y
        h*=2
    return tuple(a)

@lru_cache(maxsize=40000)
def metrics(f: tuple[int,...]):
    N=len(f); n=N.bit_length()-1
    assert N==1<<n and all(x in (-1,1) for x in f)
    a=fwht(f); p=tuple(x*x for x in a)
    assert sum(p)==N*N
    alpha=[]
    for i in range(n):
        count=sum(f[x]!=f[x^(1<<i)] for x in range(N))
        q=F(count,N)
        assert q==F(sum(p[s] for s in range(N) if s&(1<<i)),N*N)
        alpha.append(q)
    j=tuple(min(q,1-q) for q in alpha)
    return a,p,tuple(alpha),j,entropy_counts(p)

def pack(x: int, coords: tuple[int,...]) -> int:
    return sum(((x>>c)&1)<<k for k,c in enumerate(coords))
def expand(x: int, coords: tuple[int,...]) -> int:
    return sum(((x>>k)&1)<<c for k,c in enumerate(coords))

def restriction(f: tuple[int,...], E: tuple[int,...], z: int):
    n=len(f).bit_length()-1
    R=tuple(i for i in range(n) if i not in E)
    fixed=expand(z,E)
    return tuple(f[fixed|expand(y,R)] for y in range(1<<len(R)))

def swap(mask: int, j: int, k: int):
    return mask^((1<<j)|(1<<k)) if ((mask>>j)^(mask>>k))&1 else mask

def derivative(P: frozenset[int], i: int):
    return frozenset(m^(1<<i) for m in P if m&(1<<i))

def phase(P: frozenset[int], n: int):
    return tuple(-1 if sum((x&m)==m for m in P)%2 else 1 for x in range(1<<n))

def restrict_poly(P: frozenset[int], E: tuple[int,...], z: int):
    emask=sum(1<<i for i in E); fixed=expand(z,E)
    out=set()
    for m in P:
        if (m&emask)&~fixed:
            continue
        q=m&~emask
        if q in out: out.remove(q)
        else: out.add(q)
    return frozenset(out)

def classify(P: frozenset[int], cores: tuple[tuple[tuple[int,...],...],...], n: int):
    group={i:t for t,parts in enumerate(cores) for part in parts for i in part}
    assert sorted(group)==list(range(n))
    cross=[]; mixed=[]
    for i in range(n):
        Di=derivative(P,i)
        own=sum(1<<j for j in group if group[j]==group[i])
        if any(m&~own for m in Di):
            cross.append(i); continue
        for part in cores[group[i]]:
            others=tuple(j for j in part if j!=i)
            if any(frozenset(swap(m,j,k) for m in Di)!=Di for j,k in combinations(others,2)):
                mixed.append(i); break
    return tuple(cross),tuple(mixed)

def core_truth(cores,n,rng=None,tables=None):
    if tables is None:
        tables=[]
        for parts in cores:
            keys=list(product(*(range(len(part)+1) for part in parts)))
            tables.append({key:rng.choice((-1,1)) for key in keys})
    f=[]
    for x in range(1<<n):
        v=1
        for parts,tab in zip(cores,tables):
            key=tuple(sum((x>>i)&1 for i in part) for part in parts)
            v*=tab[key]
        f.append(v)
    return tuple(f)

COUNTS=Counter()

def check_structure(P,cores,n):
    cross,mixed=classify(P,cores,n)
    E=tuple(sorted(cross+mixed)); R=tuple(i for i in range(n) if i not in E)
    group={i:t for t,parts in enumerate(cores) for part in parts for i in part}
    # All physical assignments, even when cancellations alter the restricted ANF.
    for z in range(1<<len(E)):
        Q=restrict_poly(P,E,z)
        nonlinear=frozenset(m for m in Q if m.bit_count()>=2)
        for m in nonlinear:
            assert len({group[i] for i in R if m&(1<<i)})==1
        for parts in cores:
            for part in parts:
                residual=tuple(i for i in part if i in R)
                for j,k in combinations(residual,2):
                    assert frozenset(swap(m,j,k) for m in nonlinear)==nonlinear
        COUNTS['restricted_polynomial_structure_assignments']+=1
    COUNTS['polynomial_partition_structures']+=1
    if E and R:
        COUNTS['nontrivial_deleted_and_retained_structures']+=1
    return cross,mixed

def check_twist(P,cores,n,h,struct=False):
    if struct:
        cross,mixed=check_structure(P,cores,n)
    else:
        cross,mixed=classify(P,cores,n)
    q=phase(P,n); f=tuple(a*b for a,b in zip(q,h))
    _,_,alpha,j,H=metrics(f)
    r=max((m.bit_count() for m in P),default=0)
    if cross or mixed:
        assert r>=2
    for i in cross:
        assert j[i]>=F(1,1<<(r-1)),('cross',n,r,P,i,j[i])
        COUNTS['cross_coordinate_gap_checks']+=1
    for i in mixed:
        assert j[i]>=F(1,1<<r),('mixed',n,r,P,i,j[i])
        COUNTS['mixed_coordinate_gap_checks']+=1
    d=max(len(parts) for parts in cores)
    J=sum(j,F(0)); Cbase=constant(F(301,25))+log_form(d)
    base_interval=Cbase.interval()
    if r<=7:
        nonnegative(Cbase*J-H,'constant-preserving theorem')
    else:
        kexpr=binary_entropy(F(1,1<<r))*(1<<r)
        klo=kexpr.interval()[0]+C_LO
        # A certified lower bound on the claimed exact maximum coefficient.
        Klo=max(base_interval[0],klo)
        if J:
            assert H.interval()[1]<=Klo*J
        else:
            assert H.zero()
    COUNTS['twist_parameter_cases']+=1
    COUNTS[f'actual_phase_degree_{r}']+=1
    return f,(cross,mixed)

def check_deletion(f: tuple[int,...], E: tuple[int,...]):
    a,p,alpha,j,H=metrics(f)
    n=len(f).bit_length()-1; N=1<<n
    R=tuple(i for i in range(n) if i not in E)
    marginal=[0]*(1<<len(R))
    for s,w in enumerate(p):
        marginal[pack(s,R)]+=w
    HY=entropy_counts(marginal)
    EH=ZERO; sumj=[F(0)]*len(R)
    branch_square_sum=[0]*(1<<len(R))
    for z in range(1<<len(E)):
        child=restriction(f,E,z)
        ac,pc,alc,jc,hc=metrics(child)
        EH=EH+hc*F(1,1<<len(E))
        for k,v in enumerate(jc): sumj[k]+=v*F(1,1<<len(E))
        for k,v in enumerate(pc): branch_square_sum[k]+=v
    # p uses denominator 2^(2n), the child tables denominator 2^(2|R|).
    assert tuple(v*(1<<len(E)) for v in branch_square_sum)==tuple(marginal)
    A=H-HY; MI=HY-EH
    assert (H-EH-A-MI).zero()
    nonnegative(A,'block conditional entropy')
    nonnegative(MI,'block recombination information')
    JE=sum((j[i] for i in E),F(0))
    leq_c(MI,JE,'block mutual information budget')
    marginal_budget=ZERO
    for i in E: marginal_budget=marginal_budget+binary_entropy(j[i])
    nonnegative(marginal_budget-A,'conditional entropy marginal bound')
    leq_c(H-EH-marginal_budget,JE,'refined block deletion')
    for k,i in enumerate(R): assert sumj[k]<=j[i]
    COUNTS['universal_block_deletion_cases']+=1


def partitions(seq):
    if not seq:
        yield ();return
    first=seq[0]
    for part in partitions(seq[1:]):
        yield ((first,),)+part
        for k in range(len(part)):
            yield part[:k]+((first,)+part[k],)+part[k+1:]


def all_polynomials(n,r,linear=False):
    monos=tuple(m for m in range(1<<n) if (0 if linear else 2)<=m.bit_count()<=r)
    for b in range(1<<len(monos)):
        yield frozenset(m for k,m in enumerate(monos) if b&(1<<k))


def run(part: str):
    rng=random.Random(SEED)
    if part in ('all','exhaustive'):
        for n in range(1,5):
            cores=((tuple(range(n)),),)
            polys=list(all_polynomials(n,min(n,3)))
            for P in polys:
                for b in range(1<<(n+1)):
                    tab={(k,):(-1 if b&(1<<k) else 1) for k in range(n+1)}
                    h=core_truth(cores,n,tables=[tab])
                    check_twist(P,cores,n,h)
                    COUNTS['exhaustive_symmetric_cubic_parameter_cases']+=1
            # All set partitions, as a single multipart core and as separate cores.
            for blocks in partitions(tuple(range(n))):
                options=[(blocks,),tuple((block,) for block in blocks)]
                for cores2 in options:
                    for P in polys:
                        check_structure(P,cores2,n)
        # All nested physical core/part partitions and all core weight tables,
        # through dimension three. Linear phases are covered by the proof of
        # character invariance and are also sampled below.
        for n in range(1,4):
            polys=list(all_polynomials(n,n))
            for outer in partitions(tuple(range(n))):
                for cores in product(*(tuple(partitions(group)) for group in outer)):
                    keys=[tuple(product(*(range(len(block)+1) for block in parts))) for parts in cores]
                    total=sum(len(k) for k in keys)
                    for signs in range(1<<total):
                        offset=0;tables=[]
                        for keylist in keys:
                            tables.append({k:(-1 if signs&(1<<(offset+j)) else 1) for j,k in enumerate(keylist)})
                            offset+=len(keylist)
                        h=core_truth(cores,n,tables=tables)
                        for P in polys:
                            check_twist(P,cores,n,h)
                            COUNTS['exhaustive_nested_core_parameter_cases']+=1
    if part in ('all','deletion'):
        for n in range(0,4):
            for b in range(1<<(1<<n)):
                f=tuple(-1 if b&(1<<x) else 1 for x in range(1<<n))
                for mask in range(1<<n):
                    E=tuple(i for i in range(n) if mask&(1<<i))
                    check_deletion(f,E)
                    COUNTS['exhaustive_deletion_cases']+=1
        for n in range(4,9):
            for _ in range(30):
                f=tuple(rng.choice((-1,1)) for x in range(1<<n))
                E=tuple(i for i in range(n) if rng.randrange(2))
                check_deletion(f,E)
                COUNTS['sampled_deletion_cases']+=1
    if part in ('all','sampled'):
        for n in range(4,13):
            for rep in range(48):
                # Random disjoint cores, and random parts inside each core.
                labels=[rng.randrange(1+rep%3) for _ in range(n)]
                groups=[tuple(i for i in range(n) if labels[i]==t) for t in sorted(set(labels))]
                cores=[]
                for group in groups:
                    labs=[rng.randrange(1+rep%2) for _ in group]
                    blocks=tuple(tuple(i for i,k in zip(group,labs) if k==t) for t in sorted(set(labs)))
                    cores.append(blocks)
                cores=tuple(cores)
                r=2+rep%7
                mons=[m for m in range(1<<n) if 2<=m.bit_count()<=r]
                if rep%3==0:
                    P=set(rng.sample(mons,min(len(mons),1+rep%9)))
                elif rep%3==1:
                    # A large symmetry-preserving background with sparse defects.
                    P=set()
                    for group in groups:
                        for k in range(2,min(r,len(group))+1):
                            if rng.randrange(2):
                                P.update(sum(1<<i for i in A) for A in combinations(group,k))
                    for m in rng.sample(mons,min(len(mons),1+rep%3)):
                        if m in P:P.remove(m)
                        else:P.add(m)
                else:
                    # One controlled high-degree interaction; often retains large cores.
                    P=set(rng.sample(mons,1))
                for i in range(n):
                    if rng.randrange(2):P.add(1<<i)
                if rng.randrange(2):P.add(0)
                P=frozenset(P)
                h=core_truth(cores,n,rng=rng)
                f,(cross,mixed)=check_twist(P,cores,n,h,struct=(n<=10))
                if rep<4:
                    check_deletion(f,tuple(sorted(cross+mixed)))
                COUNTS['sampled_product_parameter_cases']+=1
        # The mixed-coordinate degree gap is attained exactly in every tested degree.
        witnesses=[]
        for r in range(2,11):
            n=r+1; cores=((tuple(range(n)),),)
            h=phase(frozenset({(1<<n)-1}),n)
            P=frozenset({(1<<r)-1})
            f,(cross,mixed)=check_twist(P,cores,n,h,struct=True)
            j=metrics(f)[3]
            assert mixed==tuple(range(r)) and not cross
            assert all(v==F(1,1<<r) for v in j)
            assert sum(x==-1 for x in f)==1
            witnesses.append({'degree':r,'dimension':n,'folded_influence_each':str(j[0]),'mixed_count':len(mixed)})
        COUNTS['sharp_mixed_gap_witnesses']=len(witnesses)
        cross_witnesses=[]
        for r in range(2,11):
            n=r;cut=r//2
            cores=((tuple(range(cut)),),(tuple(range(cut,r)),))
            P=frozenset({(1<<r)-1});h=(1,)*(1<<r)
            f,(cross,mixed)=check_twist(P,cores,n,h,struct=True)
            j=metrics(f)[3]
            assert cross==tuple(range(r)) and not mixed
            assert all(v==F(1,1<<(r-1)) for v in j)
            cross_witnesses.append({'degree':r,'folded_influence_each':str(j[0]),'cross_count':len(cross)})
        COUNTS['sharp_cross_gap_witnesses']=len(cross_witnesses)
    else:
        witnesses=[];cross_witnesses=[]
    constants=[]
    for r in range(2,11):
        kexpr=binary_entropy(F(1,1<<r))*(1<<r)
        lo,hi=kexpr.interval();lo+=C_LO;hi+=C_HI
        # Rationally verify the simple linear envelope.
        assert hi <= F(r)+3/LN2_HI
        if r<=7: assert hi < F(301,25)
        constants.append({'degree':r,'kappa_lower':str(lo),'kappa_upper':str(hi),
                          'below_12_04_certified':hi<F(301,25)})
    return {'status':'PASS','part':part,'full_FEI_proved':False,'independent_audit':False,
            'formal_verification':False,'publication_priority_cleared':False,
            'random_seed':SEED,'arithmetic':'integer Walsh transforms; exact rational influences and prime-log forms; rational outward logarithm enclosures',
            'ln_series_terms':SERIES_TERMS,'outward_rounding_bits':BITS,
            'counts':dict(sorted(COUNTS.items())),
            'degree_constants':constants,'sharp_mixed_gap_witnesses':witnesses,'sharp_cross_gap_witnesses':cross_witnesses,
            'scope':'Parameter families can overlap. Finite checks do not prove unrestricted FEI, nor replace the analytical proof.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--part',choices=('all','exhaustive','deletion','sampled'),default='all')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    out=run(args.part)
    out['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if args.output:args.output.write_text(text,encoding='utf-8')
    print(text)
