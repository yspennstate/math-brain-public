"""Exact finite self-checks for rare controls and quadratic rank closure.

Universal assertions rely on the proofs in REPORT.md, not these finite tests.
The unchanged prior_exact_entropy.py supplies rational prime-log intervals.
No Lean or independent audit is claimed. Python standard library only.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import argparse, hashlib, json, random, time
import prior_exact_entropy as E


def add_rank(b, v):
    while v:
        k=v.bit_length()-1
        if k not in b:
            b[k]=v
            return True
        v ^= b[k]
    return False


def rank(vs):
    b={}
    for v in vs: add_rank(b,v)
    return len(b)


def entropy(masses, denominator):
    assert sum(masses)==denominator
    ans=E.LogExpr()
    for w,count in Counter(masses).items():
        if w:
            p=F(w,denominator)
            ans += (-count*p)*E.log_rat(p)
    return ans


def stats(f):
    N=len(f); n=N.bit_length()-1
    assert N==1<<n and set(f)<= {-1,1}
    w=E.fwht(f); masses=[a*a for a in w]
    c=E.fwht(masses)
    assert all(a%N==0 for a in c)
    c=[a//N for a in c]
    def basis_min(fold):
        costs=[N-(abs(a) if fold else a) for a in c]
        b={}; ans=0; vs=[]
        for v in sorted(range(1,N),key=lambda v:(costs[v],v)):
            if add_rank(b,v):
                ans+=costs[v];vs.append(v)
        assert len(vs)==n
        return F(ans,2*N),vs
    M,vs=basis_min(True); L,lv=basis_min(False)
    return dict(n=n,N=N,w=w,masses=masses,den=N*N,c=c,M=M,Ilin=L,basis=vs,
                I=sum((F(N-c[1<<i],2*N) for i in range(n)),F(0)),
                mu=F(sum(f),N),delta=F(sum(v<0 for v in f),N),
                H=entropy(masses,N*N))


def eta(q):
    q=F(q)
    return -q*E.log_rat(q) if q else E.LogExpr()


def gate(f,c,center=0):
    assert c>=1 and 0<=center<1<<c
    return tuple(f[x>>c] if x&((1<<c)-1)==center else 1
                 for x in range((1<<c)*len(f)))


def gate_entropy(data,c):
    p=F(1,1<<c);d=1-data['mu'];t=2*p*d-p*p*d*d
    residue=eta((1-p*d)**2)-p*eta((1-d)**2)+(p-p*p)*eta(d*d)
    total=p*data['H']+2*c*t+residue
    return total,residue


def quadratic(n,edge_mask):
    pairs=list(combinations(range(n),2)); rows=[0]*n
    edges=[e for i,e in enumerate(pairs) if edge_mask>>i&1]
    for i,j in edges:
        rows[i]^=1<<j;rows[j]^=1<<i
    q=tuple(-1 if sum((x>>i&1)*(x>>j&1) for i,j in edges)%2 else 1
            for x in range(1<<n))
    return q,rows


def matrix_apply(rows,v):
    return sum(((r&v).bit_count()%2)<<i for i,r in enumerate(rows))


def tensor(f,g):
    n=len(f)
    return tuple(f[x%n]*g[x//n] for x in range(n*len(g)))


def random_affine(f,extra,rng):
    n=len(f).bit_length()-1;N=n+extra
    rows=[1<<i for i in range(n)]
    # Invertible column operations on n+extra columns preserve row rank.
    for _ in range(4*max(N,1)):
        if N<2:break
        i,j=rng.sample(range(N),2)
        for k,row in enumerate(rows):
            if row>>i&1: rows[k]^=1<<j
    assert rank(rows)==n
    shift=rng.randrange(1<<n); character=rng.randrange(1<<N)
    return tuple(f[matrix_apply(rows,x)^shift]*(-1 if (x&character).bit_count()%2 else 1)
                 for x in range(1<<N)),rows,character


def enforce_nonnegative(expr):
    return expr.nonnegative()


def star_constant_interval():
    lo,hi=E.LN2
    return F(17,4)+F(1,2)/hi,F(17,4)+F(1,2)/lo


def check_star(data):
    if data['M']==0:
        assert data['H'].is_zero();return True
    lo,hi=star_constant_interval(); hlo,hhi=data['H'].interval()
    if hi*data['M']<hlo:return False
    assert lo*data['M']>=hhi
    return True


def exact_gate_checks():
    cases=0;directions=0;sign_sensitive=0;gaps=[]
    for n in range(4):
        for bits in range(1<<(1<<n)):
            f=tuple(-1 if bits>>x&1 else 1 for x in range(1<<n)); sf=stats(f)
            for c in (2,3,4):
                g=gate(f,c);sg=stats(g);p=F(1,1<<c);d=1-sf['mu']
                expected,residue=gate_entropy(sf,c)
                assert (sg['H']-expected).is_zero()
                assert sg['M']==p*(sf['Ilin']+c*d)
                assert sg['I']==p*(sf['I']+c*d)
                for v,corr in enumerate(sg['c']):
                    observed=F(len(g)-corr,2*len(g))
                    true=p*d if v&((1<<c)-1) else p*F(len(f)-sf['c'][v>>c],2*len(f))
                    assert observed==true
                    directions+=1
                enforce_nonnegative(4*p*d-residue)
                enforce_nonnegative(p*sf['H']+4*(c+1)*p*d-sg['H'])
                if c>=4:
                    enforce_nonnegative(5*sg['M']-sg['H']-p*(5*sf['M']-sf['H']))
                    e=p*sf['H']-sg['H']; coeff=sg['M']-p*sf['M']
                    assert coeff>=0
                    assert e.interval()[0]+star_constant_interval()[0]*coeff>=0
                if c>=4 and check_star(sf):
                    assert check_star(sg)
                if sf['Ilin']!=sf['M']:sign_sensitive+=1
                cases+=1
    # A character proves why Ilin cannot be replaced by M.
    sf=stats((-1,1));sg=stats(gate((-1,1),4))
    assert sf['M']==0 and sf['Ilin']==1 and sg['M']==F(5,16)
    return dict(status='PASS',raw_input_tables=278,gated_tables=cases,
                exact_direction_formulas=directions,unfolded_vs_folded_examples=sign_sensitive,
                character_gate=dict(inner_M=str(sf['M']),inner_Ilin=str(sf['Ilin']),gated_M=str(sg['M'])))


def rare_rank_checks():
    rng=random.Random(20260920);items=[]
    for n in range(1,5):
        N=1<<n
        supports=[()]
        if N>=8:supports += [(0,)]
        if N>=16:supports += [(0,v) for v in range(1,N)]
        for support in supports:
            f=tuple(-1 if x in support else 1 for x in range(N))
            for mask in range(1<<(n*(n-1)//2)):
                items.append((f,mask))
    for n in (5,6,7):
        N=1<<n
        for _ in range(12):
            support=set(rng.sample(range(N),rng.randrange(0,N//8+1)))
            f=tuple(-1 if x in support else 1 for x in range(N))
            items.append((f,rng.randrange(1<<(n*(n-1)//2))))
    directions=0;sharp=0;density_checks=0
    for f,mask in items:
        sf=stats(f);q,rows=quadratic(sf['n'],mask);Fq=tuple(a*b for a,b in zip(f,q));ss=stats(Fq)
        delta=sf['delta'];rho=rank(rows)
        assert delta<=F(1,8)
        if 0<delta<=F(1,16):
            ell=E.log_rat(1/delta)
            enforce_nonnegative(4*delta*(sf['n']+ell)-sf['H'])
            enforce_nonnegative(sf['M']-2*delta*ell)
            density_checks+=1
        lower=sf['M']+(F(1,2)-4*delta)*rho
        assert ss['M']>=lower
        if len(f)>=8 and sum(a<0 for a in f)==1:
            assert ss['M']==lower;sharp+=1
        for v,corr in enumerate(ss['c']):
            jf=F(len(f)-abs(corr),2*len(f));alpha=F(len(f)-sf['c'][v],2*len(f))
            assert jf>=alpha
            if matrix_apply(rows,v)==0: assert jf==alpha
            else:assert jf>=F(1,2)-2*delta
            directions+=1
        enforce_nonnegative(sf['H']+rho-ss['H'])
        enforce_nonnegative(ss['H']+rho-sf['H'])
        for C in (4,5):
            enforce_nonnegative(sf['H']-C*sf['M']+(1-C*(F(1,2)-4*delta))*rho-ss['H']+C*ss['M'])
    # Explicit necessity of a small support hypothesis in the perturbation theorem.
    q,rows=quadratic(2,1);sq=stats(q);sprod=stats(tuple(a*a for a in q))
    assert sq['delta']==F(1,4) and sq['M']==1 and sprod['M']==0
    return dict(status='PASS',quadratic_perturbation_pairs=len(items),
                exact_direction_bounds=directions,sharp_single_point_pairs=sharp,
                density_entropy_and_isoperimetry_examples=density_checks,
                dense_base_counterexample=dict(negative_density='1/4',base_M='1',twisted_M='0'))


def scalar_checks():
    ct=0
    for den in (16,32,64):
        for a in range(den+1):
            d=F(2*a,den)
            for c in (2,3,4,8):
                p=F(1,1<<c)
                residue=eta((1-p*d)**2)-p*eta((1-d)**2)+(p-p*p)*eta(d*d)
                enforce_nonnegative(4*p*d-residue);ct+=1
            if d<=F(1,2): enforce_nonnegative(eta((1-d)**2)-eta(d*d))
            elif d<=1: enforce_nonnegative(d-eta(d*d))
    lo,hi=star_constant_interval()
    assert hi<5 and E.LN2[0]>F(2,3)
    return dict(status='PASS',rational_scalar_pairs=ct,
                derived_constant=dict(lower=E.decimal_bound(lo,12,True),upper=E.decimal_bound(hi,12,False)),
                note='Finite scalar checks accompany the interval-wide calculus proof; not a substitute for it.')


def nested_checks():
    rng=random.Random(19422026);rows_out=[];coupled=0;lifts=0
    bases=[(1,),(-1,),(-1,1),tuple(-1 if x==0 else 1 for x in range(8)),E.canonical(E.majority(3))]
    for seed in bases:
        f=seed
        for depth in range(1,3):
            g=gate(f,4);sg=stats(g)
            assert check_star(sg)
            n=sg['n'];q,polar=quadratic(n,rng.randrange(1<<(n*(n-1)//2)))
            twisted=tuple(a*b for a,b in zip(g,q)); st=stats(twisted)
            assert st['M']>=sg['M']+(F(1,2)-4*sg['delta'])*rank(polar)
            assert check_star(st);coupled+=1
            h,_,_=random_affine(twisted,0,rng);sh=stats(h)
            assert sh['M']==st['M'] and (sh['H']-st['H']).is_zero();lifts+=1
            rows_out.append(dict(seed_bits=len(seed).bit_length()-1,depth=depth,variables=n,
                                 polar_rank=rank(polar),M=str(st['M']),H=E.show(st['H'])))
            f=h
    # Two degree-eight terms sharing exactly four gate variables, with cross terms.
    w4=tuple(-1 if x==0 else 1 for x in range(16))
    inner=tensor(w4,w4)
    assert check_star(stats(inner))
    shared=[]
    for i in range(5):
        g=gate(inner,4);sg=stats(g);n=sg['n']
        q,polar=quadratic(n,rng.randrange(1<<(n*(n-1)//2)))
        ff=tuple(a*b for a,b in zip(g,q));sf=stats(ff)
        assert check_star(sf)
        assert sf['M']>=sg['M']+(F(1,2)-4*sg['delta'])*rank(polar)
        shared.append(dict(variables=n,polar_rank=rank(polar),M=str(sf['M']),H=E.show(sf['H'])))
    # Tensor and genuinely rectangular affine lift after a controlled quadratic stage.
    a=gate((-1,1),4);q,_=quadratic(5,137);a=tuple(x*y for x,y in zip(a,q))
    b=gate((-1,),4);f=tensor(a,b);s=stats(f);sa=stats(a);sb=stats(b)
    assert s['M']==sa['M']+sb['M'] and (s['H']-sa['H']-sb['H']).is_zero()
    lift,_,_=random_affine(f,1,rng);sl=stats(lift)
    assert sl['M']==s['M'] and (sl['H']-s['H']).is_zero() and check_star(sl);lifts+=1
    return dict(status='PASS',nested_quadratic_stages=coupled,affine_checks=lifts,
                nested_examples=rows_out,shared_high_degree_examples=shared,
                tensor_and_rectangular_lift=dict(parameters=s['n'],physical_bits=sl['n']))


def minimizing_representative(f):
    sf=stats(f);vs=sf['basis'];n=sf['n'];N=len(f)
    mask=sum((sf['c'][v]<0)<<i for i,v in enumerate(vs))
    def apply(x):
        v=0
        for i,w in enumerate(vs):
            if x>>i&1:v^=w
        return v
    out=tuple(f[apply(x)]*(-1 if (mask&x).bit_count()%2 else 1) for x in range(N))
    so=stats(out)
    assert so['I']==sf['M']==so['M']==so['Ilin']
    return out


def hardness_checks():
    seeds=[tuple(-1 if x==0 else 1 for x in range(4)),tuple(-1 if x==0 else 1 for x in range(8)),
           E.majority(3),tuple(-1 if x in (0,1,4) else 1 for x in range(8))]
    rows=[]
    for seed in seeds:
        f=minimizing_representative(seed);s=stats(f)
        acc=(1,)
        for copies in range(1,4):
            acc=tensor(acc,f);sa=stats(acc)
            assert sa['M']==copies*s['M']==sa['Ilin']
            g=gate(acc,4);sg=stats(g);d=1-s['mu']**copies
            assert sg['M']==F(copies*s['M']+4*d,16)
            assert (gate_entropy(sa,4)[0]-sg['H']).is_zero()
            rows.append(dict(seed_bits=s['n'],copies=copies,gate_bits=4,
                             negative_density=str(sg['delta']),M=str(sg['M']),
                             H_over_M=E.show(sg['H']/sg['M']) if sg['M'] else E.show(0)))
    return dict(status='PASS',tensor_amplified_exact_examples=len(rows),examples=rows,
                scope='These exact formulas support the all-copy analytic limit, not a universal FEI bound.')



def arbitrary_error_checks():
    rng=random.Random(7422026);rows=[]
    for n,repetitions in [(8,8),(12,3)]:
        N=1<<n;size=1<<(n//4)
        for _ in range(repetitions):
            support=set(rng.sample(range(N),size))
            g=tuple(-1 if x in support else 1 for x in range(N));sg=stats(g)
            q,polar=quadratic(n,rng.randrange(1<<(n*(n-1)//2)))
            f=tuple(a*b for a,b in zip(g,q));sf=stats(f)
            assert sg['delta']==F(size,N)<=F(1,16)
            enforce_nonnegative(F(14,3)*sf['M']-sf['H'])
            rows.append(dict(variables=n,error_set_size=size,error_density=str(sg['delta']),
                             quadratic_rank=rank(polar),M=str(sf['M']),H=E.show(sf['H'])))
    return dict(status='PASS',arbitrary_error_sets=len(rows),examples=rows,
                scope='Full truth tables for unstructured error sets at distance 2^(-3n/4) from a quadratic phase; bound 14/3.')

def main():
    p=argparse.ArgumentParser();p.add_argument('--part',choices=['all','gate','rank','scalar','nested','hardness','errors'],default='all')
    p.add_argument('--output',type=Path);a=p.parse_args();start=time.monotonic()
    out=dict(full_FEI_proved=False,independent_audit=False,lean_used=False,
             arithmetic='Integer Walsh transforms; Fraction identities and prime-log rational intervals',
             script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             dependency_sha256=hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest())
    for name,job in [('gate',exact_gate_checks),('rank',rare_rank_checks),('scalar',scalar_checks),
                     ('nested',nested_checks),('hardness',hardness_checks),('errors',arbitrary_error_checks)]:
        if a.part in ('all',name):out[name]=job()
    out['status']='ALL_REQUESTED_CHECKS_PASS';out['elapsed_seconds']=round(time.monotonic()-start,3)
    text=json.dumps(out,indent=2)+'\n'
    if a.output:a.output.write_text(text)
    print(text)

if __name__=='__main__':main()
