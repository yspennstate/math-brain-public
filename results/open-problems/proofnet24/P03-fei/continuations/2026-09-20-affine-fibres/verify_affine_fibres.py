#!/usr/bin/env python3
"""Reproduce the 2026-09-20 affine-fibre FEI continuation checks.
Requires Python >=3.10 and NumPy. Integer Walsh transforms, rational influence
identities, and outward rational logarithm enclosures are used. Finite checks
are not a substitute for the all-dimensional proofs in REPORT.md.
Run: python verify_affine_fibres.py --output verification.json
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import json
from pathlib import Path
import random
import numpy as np
SEED = 20260920417

def fwht(a: np.ndarray) -> np.ndarray:
    a=np.asarray(a,dtype=np.int64).copy(); n=a.shape[-1]
    assert n and n&(n-1)==0
    step=1
    while step<n:
        v=a.reshape(*a.shape[:-1],-1,2*step)
        l,r=v[...,:step].copy(),v[...,step:].copy()
        v[...,:step],v[...,step:]=l+r,l-r
        step*=2
    return a

def signs(mask: int,n: int) -> np.ndarray:
    return np.array([1-2*((mask>>j)&1) for j in range(1<<n)],dtype=np.int64)

def entropy_expr(a: np.ndarray) -> dict[int,F]:
    """Exact linear form in log2(odd integers); key 1 is the constant."""
    N=len(a); n=N.bit_length()-1; w=fwht(a)
    assert int(w@w)==N*N
    d: dict[int,F]={1:F(2*n)}
    for t,multiplicity in Counter(abs(int(x)) for x in w if x).items():
        v=(t&-t).bit_length()-1; odd=t>>v; c=F(-2*multiplicity*t*t,N*N)
        d[1]+=c*v
        if odd!=1:d[odd]=d.get(odd,F(0))+c
    return {k:v for k,v in d.items() if v}

def add_expr(a:dict[int,F],b:dict[int,F],scale:F=F(1))->dict[int,F]:
    c=dict(a)
    for k,v in b.items():c[k]=c.get(k,F(0))+scale*v
    return {k:v for k,v in c.items() if v}

@lru_cache(None)
def ln_unit_interval(x:F)->tuple[F,F]:
    assert 1<=x<=2
    z=(x-1)/(x+1); z2=z*z; power=z; total=F(0); terms=48
    for j in range(terms):
        total+=2*power/(2*j+1);power*=z2
    tail=2*power/((2*terms+1)*(1-z2))
    return total,total+tail

@lru_cache(None)
def log2_interval(k:int)->tuple[F,F]:
    assert k>=1
    e=k.bit_length()-1
    if k==1<<e:return F(e),F(e)
    low,high=ln_unit_interval(F(k,1<<e)); l2,h2=ln_unit_interval(F(2))
    return F(e)+low/h2,F(e)+high/l2

def enclosure(d:dict[int,F])->tuple[F,F]:
    low=high=d.get(1,F(0))
    for k,c in d.items():
        if k==1:continue
        l,h=log2_interval(k)
        if c>=0:low,high=low+c*l,high+c*h
        else:low,high=low+c*h,high+c*l
    return low,high

def nonpositive(d:dict[int,F],label:str)->None:
    lo,hi=enclosure(d)
    assert hi<=0,(label,'positive or unresolved enclosure',float(lo),float(hi))

def basis(vectors:list[int])->list[int]:
    pivots:dict[int,int]={};out:list[int]=[]
    for original in vectors:
        v=original
        while v:
            j=v.bit_length()-1
            if j in pivots:v^=pivots[j]
            else:pivots[j]=v;out.append(original);break
    return out

def span(bs:list[int])->list[int]:
    out=[0]
    for b in bs:out+=[x^b for x in out]
    return out

def affine(mask:int,m:int)->bool:
    if not mask:return False
    p=(mask&-mask).bit_length()-1
    pts=[i^p for i in range(1<<m) if mask>>i&1]
    return 1<<len(basis(pts))==len(pts)

@lru_cache(None)
def all_partitions(m:int)->tuple[tuple[int,...],...]:
    N=1<<m;aff=[a for a in range(1,1<<N) if affine(a,m)]
    @lru_cache(None)
    def rec(rem:int)->tuple[tuple[int,...],...]:
        if not rem:return ((),)
        b=rem&-rem
        return tuple((a,)+t for a in aff if a&b and a&rem==a for t in rec(rem^a))
    return rec((1<<N)-1)

def cell_data(mask:int,m:int)->dict:
    pts=[i for i in range(1<<m) if mask>>i&1];anchor=pts[0];V={p^anchor for p in pts}
    js=[i for i in range(m) if 1<<i in V];standard=[1<<i for i in js]
    bs=basis(standard+sorted(V));us=span(bs[len(standard):]);zs=span(standard)
    return dict(points=pts,anchor=anchor,J=js,kappa=m-len(js),r=m-len(bs),
                d=len(bs)-len(js),us=us,zs=zs,coords=[anchor^v for v in span(bs)])

def anf(bits:list[int])->list[int]:
    out=list(bits);n=len(bits).bit_length()-1
    for i in range(n):
        for s in range(len(bits)):
            if s>>i&1:out[s]^=out[s^(1<<i)]
    return out

@lru_cache(None)
def quad_rank(mask:int,d:int)->int:
    co=anf([(mask>>s)&1 for s in range(1<<d)])
    if any(c and s.bit_count()>2 for s,c in enumerate(co)):return -1
    rows=[0]*d
    for i in range(d):
        for j in range(i+1,d):
            if co[(1<<i)|(1<<j)]:rows[i]^=1<<j;rows[j]^=1<<i
    return len(basis(rows))

def table_from_cells(g:np.ndarray,cells:list[dict],labels:list[int],k:int,m:int)->np.ndarray:
    pi=[0]*(1<<m)
    for c,a in zip(cells,labels):
        for y in c['points']:pi[y]=a
    return np.array([int(g[y])*(-1 if (x&pi[y]).bit_count()%2 else 1)
                     for x in range(1<<k) for y in range(1<<m)],dtype=np.int64)

def influence_counts(f:np.ndarray)->list[int]:
    N=len(f);ids=np.arange(N)
    return [int(np.count_nonzero(f!=f[ids^(1<<i)])) for i in range(N.bit_length()-1)]

def folded(f:np.ndarray)->F:
    N=len(f)
    return F(sum(min(c,N-c) for c in influence_counts(f)),N)

def exhaustive_quadratic()->dict:
    totals=Counter();per=[]
    for m in range(4):
        Ny=1<<m;G=np.array([signs(t,m) for t in range(1<<Ny)]);cases=0
        for partition in all_partitions(m):
            cs=[cell_data(a,m) for a in partition];k=(len(cs)-1).bit_length();N=1<<(m+k)
            valid=np.ones(len(G),dtype=bool);expected=np.zeros(len(G),dtype=np.int64)
            for c in cs:
                d=len(c['coords']).bit_length()-1;ranks=[]
                for g in G:
                    t=sum(int(g[p]<0)<<j for j,p in enumerate(c['coords']))
                    ranks.append(quad_rank(t,d))
                r=np.array(ranks);valid&=r>=0;expected+=len(c['points'])*(2*c['r']+r)
            gv=G[valid];expected=expected[valid];labels=list(range(len(cs)))
            tag=table_from_cells(np.ones(Ny,dtype=np.int64),cs,labels,k,m)
            fs=gv[:,np.arange(N)%Ny]*tag[None,:];W=fwht(fs);absw=np.abs(W)
            assert np.all((absw==0)|((absw&(absw-1))==0))
            logs=np.zeros_like(absw)
            for j in range(m+k+1):logs[absw==(1<<j)]=j
            Hnum=np.sum(W*W*(2*(m+k)-2*logs),axis=1)
            assert np.array_equal(Hnum,expected*(N*N//Ny))
            counts=np.array([np.count_nonzero(fs!=fs[:,np.arange(N)^(1<<i)],axis=1)
                             for i in range(m)],dtype=np.int64).reshape(m,len(fs))
            Jy_num=np.sum(np.minimum(counts,N-counts),axis=0)
            assert np.all(Hnum<=4*N*Jy_num)
            cases+=len(fs);totals['walsh_coordinate_checks']+=m*len(fs)
        totals['functions']+=cases
        per.append(dict(y_dimension=m,affine_partitions=len(all_partitions(m)),functions=cases))
    return dict(**totals,per_dimension=per)

def random_affine_partition(m:int,rng:random.Random)->list[int]:
    cells=[list(range(1<<m))]
    for _ in range(rng.randint(0,min(7,m+2))):
        choices=[j for j,c in enumerate(cells) if len(c)>1]
        if not choices:break
        j=rng.choice(choices);cell=cells.pop(j)
        while True:
            a=rng.randrange(1,1<<m);left=[y for y in cell if (a&y).bit_count()%2==0]
            if 0<len(left)<len(cell):break
        right=[y for y in cell if (a&y).bit_count()%2];cells.extend([left,right])
    return [sum(1<<y for y in c) for c in cells]

def quadratic_signs(k:int,rng:random.Random)->tuple[np.ndarray,int]:
    rows=[0]*k;pairs=[]
    for i in range(k):
        for j in range(i+1,k):
            if rng.randrange(2):pairs.append((i,j));rows[i]^=1<<j;rows[j]^=1<<i
    linear=rng.randrange(1<<k);const=rng.randrange(2)
    q=np.array([1-2*(((x&linear).bit_count()+const+
                     sum(((x>>i)&1)*((x>>j)&1) for i,j in pairs))%2)
                for x in range(1<<k)],dtype=np.int64)
    return q,len(basis(rows))

def generic_and_twist_checks()->dict:
    rng=random.Random(SEED);out=Counter()
    for case in range(240):
        m=rng.randint(1,7)
        part=list(rng.choice(all_partitions(m))) if m<=3 else random_affine_partition(m,rng)
        cs=[cell_data(c,m) for c in part];k=(len(cs)-1).bit_length()+rng.randrange(2)
        labels=rng.sample(range(1<<k),len(cs));g=np.array([rng.choice([-1,1]) for _ in range(1<<m)],dtype=np.int64)
        f=table_from_cells(g,cs,labels,k,m);h=entropy_expr(f);exact_rhs={};bound_rhs={};lowerJ=F(0)
        for c in cs:
            weight=F(len(c['points']),1<<m);intr=g[c['coords']]
            exact_rhs=add_expr(exact_rhs,{1:F(2*c['r'])},weight)
            exact_rhs=add_expr(exact_rhs,entropy_expr(intr),weight)
            bound_rhs=add_expr(bound_rhs,{1:F(2*c['kappa'])},weight);lowerJ+=weight*F(c['kappa'],2)
            for u in c['us']:
                section=g[[c['anchor']^u^z for z in c['zs']]];w=weight/F(len(c['us']))
                bound_rhs=add_expr(bound_rhs,entropy_expr(section),w);lowerJ+=w*folded(section)
                out['physical_sections']+=1
        assert not add_expr(h,exact_rhs,F(-1)),'affine-fibre identity'
        nonpositive(add_expr(h,bound_rhs,F(-1)),'section deletion bound')
        count=influence_counts(f);N=len(f);Jy=F(sum(min(c,N-c) for c in count[:m]),N)
        assert lowerJ<=Jy
        pi=np.zeros(1<<m,dtype=np.int64)
        for c,a in zip(cs,labels):pi[c['points']]=a
        ids=np.arange(1<<m)
        for i in range(m):
            changed=pi!=pi[ids^(1<<i)];same_disagree=(~changed)&(g!=g[ids^(1<<i)])
            prediction=F(int(np.count_nonzero(changed)),2*(1<<m))+F(int(np.count_nonzero(same_disagree)),1<<m)
            assert prediction==F(count[i],N);out['exact_boundary_coordinates']+=1
        q,rho=quadratic_signs(k,rng);ft=f*np.repeat(q,1<<m);ht=entropy_expr(ft)
        nonpositive(add_expr(add_expr(ht,h,F(-1)),{1:F(-rho)}),'quadratic entropy increase')
        ct=influence_counts(ft);assert ct[:m]==count[:m]
        Jx=F(sum(min(c,N-c) for c in ct[m:]),N);assert 2*Jx>=rho
        out['arbitrary_core_cases']+=1;out['quadratic_twist_cases']+=1
        gq=np.ones(1<<m,dtype=np.int64)
        for c in cs:
            d=len(c['coords']).bit_length()-1;sq,_=quadratic_signs(d,rng);gq[c['coords']]=sq
        fq=table_from_cells(gq,cs,labels,k,m)*np.repeat(q,1<<m)
        nonpositive(add_expr(entropy_expr(fq),{1:-4*folded(fq)}),'constant four with quadratic tag')
        out['quadratic_cell_and_tag_cases']+=1
    return dict(out)

def addressing_checks()->list[dict]:
    results=[]
    for m in (1,2,3):
        cs=[cell_data(1<<y,m) for y in range(1<<m)];k=1<<m
        f=table_from_cells(np.ones(1<<m,dtype=np.int64),cs,[1<<a for a in range(1<<m)],k,m)
        h=entropy_expr(f);assert h=={1:F(2*m)};assert folded(f)==F(m,2)+1
        results.append(dict(address_bits=m,total_variables=m+k,entropy_bits=2*m,
                            folded_influence=str(folded(f)),ratio=str(F(2*m)/folded(f))))
    return results

def endpoint_scalar_probe()->list[dict]:
    # Decimal is an exploratory display only. The asymptotic proof is analytic.
    from decimal import Decimal,localcontext
    out=[]
    with localcontext() as ctx:
        ctx.prec=120
        def psi(n:int,t:Decimal)->Decimal:return Decimal(n)*(t**(Decimal(2)-Decimal(1)/n)-t*t)
        for n in (4,8,16,32,64):
            d=Decimal(2)**(1-n)
            value=(psi(n,1-d)+psi(n,d)-psi(n-1,1-2*d)/2)/(d*d)
            out.append(dict(n=n,minority_amplitude=f'2^({1-n})',scalar_charge_over_v_squared=str(+value)))
    return out

def main()->None:
    p=argparse.ArgumentParser();p.add_argument('--output',default='verification.json');args=p.parse_args()
    result={'status':'PASS','scope':'Finite exact checks; not proof of unrestricted FEI.','seed':SEED,
            'integer_arithmetic':'int64 Walsh transforms; exact rational influence and rank checks',
            'logarithms':'48-term atanh series with explicit outward rational remainder; common terms canceled first',
            'exhaustive_quadratic_affine_fibres':exhaustive_quadratic(),
            'generic_fibres_and_twists':generic_and_twist_checks(),'addressing_sharpness':addressing_checks(),
            'endpoint_scalar_probe_decimal_not_certificate':endpoint_scalar_probe()}
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    Path(args.output).write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
