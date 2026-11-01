"""Exact self-checks for quadratic coupling of independent affine clauses.
No full FEI proof, Lean verification, or independent audit is claimed.
All accepted entropy comparisons use Fraction/log intervals in the included,
unchanged prior_exact_entropy.py. Numerical drift probes are NOT proof evidence.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from pathlib import Path
import argparse, hashlib, json, random, time
import prior_exact_entropy as E

def rank_add(basis,v):
    while v:
        i=v.bit_length()-1
        if i not in basis:
            basis[i]=v;return True
        v^=basis[i]
    return False

def rank(vectors):
    b={}
    for v in vectors:rank_add(b,v)
    return len(b)

def mul(rows,v):
    return sum(((r&v).bit_count()%2)<<i for i,r in enumerate(rows))

def quadratic(n,edges):
    rows=[0]*n
    for i,j in edges:rows[i]^=1<<j;rows[j]^=1<<i
    vals=tuple(-1 if sum(((x>>i)&1)*((x>>j)&1) for i,j in edges)%2 else 1 for x in range(1<<n))
    return vals,rows

def spectral(f):
    N=len(f);w=E.fwht(f);m=[x*x for x in w]
    assert sum(m)==N*N
    c=E.fwht(m);assert all(x%N==0 for x in c)
    c=[x//N for x in c]
    weights=[F(N-abs(x),2*N) for x in c]
    basis={};cost=F(0);chosen=[]
    for v in sorted(range(1,N),key=lambda v:(weights[v],v)):
        if rank_add(basis,v):cost+=weights[v];chosen.append(v)
    return dict(w=w,m=m,den=N*N,c=c,j=weights,M=cost,basis=chosen,
                H=E.entropy_weights(m,N*N))

def clause_product(n,widths,centres=None):
    if centres is None:centres=[0]*len(widths)
    assert sum(widths)<=n
    ranges=[];off=0
    for w,b in zip(widths,centres):
        assert 0<=b<1<<w
        ranges.append((off,w,b));off+=w
    vals=tuple((-1)**sum(((x>>o)&((1<<w)-1))==b for o,w,b in ranges) for x in range(1<<n))
    return vals,ranges,off

def coset_key(s,rows):
    basis={}
    for r in rows:rank_add(basis,r)
    for i in sorted(basis,reverse=True):
        if (s>>i)&1:s^=basis[i]
    return s

def block_masses(m,rows,shift=0):
    out={}
    for s,w in enumerate(m):
        if w:
            c=coset_key(s^shift,rows)
            out[c]=out.get(c,0)+w
    return out

def check_entropy_gate(f,q,rows,do_intervals=True):
    Fq=tuple(a*b for a,b in zip(f,q));df=spectral(f);dq=spectral(q);dg=spectral(Fq)
    rho=rank(rows);supp=[s for s,w in enumerate(dq['m']) if w]
    shift=supp[0]
    assert len(supp)==1<<rho
    assert all(coset_key(s^shift,rows)==0 for s in supp)
    assert len({dq['m'][s] for s in supp})==1
    assert block_masses(df['m'],rows)==block_masses(dg['m'],rows,shift)
    if do_intervals:
        (rho-dg['H']+df['H']).nonnegative()
        (rho-df['H']+dg['H']).nonnegative()
    return df,dg,rho

def gate_tests():
    cases=0;sharp=[]
    for n in range(4):
        pairs=list(combinations(range(n),2))
        for qmask in range(1<<len(pairs)):
            q,rows=quadratic(n,[e for j,e in enumerate(pairs) if qmask>>j&1])
            for bits in range(1<<(1<<n)):
                f=tuple(-1 if bits>>x&1 else 1 for x in range(1<<n))
                check_entropy_gate(f,q,rows);cases+=1
    for n in [2,4,6,8]:
        q,rows=quadratic(n,[(i,i+1) for i in range(0,n,2)])
        a,b,rho=check_entropy_gate((1,)*(1<<n),q,rows)
        assert (b['H']-n).is_zero()
        sharp.append({'dimension':n,'rank':rho,'entropy_increase':E.show(b['H']-a['H'])})
    return {'status':'PASS','arbitrary_function_quadratic_pairs':cases,
            'full_coset_mass_identity_checked':True,'sharp_examples':sharp}

def predicted_abs(v,rows,ranges,used,n):
    ell=mul(rows,v)
    if ell>>used:return F(0)
    p=F(1)
    for off,w,b in ranges:
        vv=(v>>off)&((1<<w)-1);ll=(ell>>off)&((1<<w)-1);a=F(1,2**(w-1))
        if not vv:
            if ll:return F(0)
        elif not ll:p*=1-2*a
        elif (vv&ll).bit_count()%2:return F(0)
        else:p*=2*a
    return p

def family_case(n,widths,edges,centres=None):
    G,ranges,used=clause_product(n,widths,centres);q,rows=quadratic(n,edges)
    bg,bf,rho=check_entropy_gate(G,q,rows)
    M0=sum((F(w,2**(w-1)) for w in widths),F(0))
    assert bg['M']==M0
    a=max((F(1,2**(w-1)) for w in widths),default=F(0))
    comparisons=0
    for v in range(1<<n):
        assert F(abs(bf['c'][v]),1<<n)==predicted_abs(v,rows,ranges,used,n)
        assert bf['j'][v]>=bg['j'][v]
        if mul(rows,v):assert bf['j'][v]>=F(1,2)-a
        comparisons+=1
    assert bf['M']>=M0 and bf['M']>=(F(1,2)-a)*rho
    assert bf['M']>=M0+(F(1,2)-2*a)*rho
    (4*bf['M']-bf['H']).nonnegative()
    if len(widths)==1 and widths[0]==n:
        assert rho%2==0
        beta=F(1,2**(rho//2))
        np=(2**rho+2**(rho//2))//2; nm=(2**rho-2**(rho//2))//2
        expected=Counter()
        expected[(beta-a)**2]+=np
        expected[(beta+a)**2]+=nm
        expected[a*a]+=2**n-2**rho
        expected=Counter({mass:count for mass,count in expected.items() if count})
        assert Counter(F(w,bf['den']) for w in bf['m'])==expected
        assert bf['M']==n*a+(F(1,2)-2*a)*rho
    return {'n':n,'widths':widths,'rank':rho,'base_M':str(M0),'coupled_M':str(bf['M']),
            'entropy':E.show(bf['H']),'ratio':E.show(bf['H']/bf['M']) if bf['M'] else None},comparisons

def class_tests():
    rng=random.Random(2026091907);count=comparisons=0;selected=[]
    # Exhaust all homogeneous quadratic perturbations for one four-bit clause.
    pairs=list(combinations(range(4),2))
    for mask in range(64):
        row,c=family_case(4,[4],[e for i,e in enumerate(pairs) if mask>>i&1])
        count+=1;comparisons+=c
    # Unbounded-class proofs are in the report; these are finite stress tests.
    plans=[(3,[3],8),(5,[5],24),(6,[3,3],32),(7,[3,4],24),
           (8,[4,4],40),(9,[4,4],24),(10,[4,6],16),(10,[3,3,4],16),
           (11,[4,5],8),(12,[4,4,4],6)]
    for n,widths,repeat in plans:
        edges=list(combinations(range(n),2))
        for _ in range(repeat):
            chosen=[e for e in edges if rng.getrandbits(1)]
            centres=[rng.randrange(1<<w) for w in widths]
            row,c=family_case(n,widths,chosen,centres)
            comparisons+=c;count+=1
        selected.append(row)
    # Explicit dependence: the quadratic x0*x4 uses variables of both clauses.
    row,c=family_case(8,[4,4],[(0,4)])
    selected.append({'explicit_cross_block_case':row});count+=1;comparisons+=c
    return {'status':'PASS','coupled_class_examples':count,
            'all_direction_formula_comparisons':comparisons,'selected_examples':selected}

def random_surj(rows,cols,rng):
    while True:
        a=[rng.randrange(1<<cols) for _ in range(rows)]
        if rank(a)==rows:return a

def affine_tests():
    rng=random.Random(190920261);count=0
    for n,widths in [(6,[3,3]),(8,[4,4]),(9,[4,4])]:
        edges=list(combinations(range(n),2))
        for k in range(6):
            q,polar=quadratic(n,[e for e in edges if rng.getrandbits(1)])
            G,_,_=clause_product(n,widths);f=tuple(a*b for a,b in zip(G,q));bf=spectral(f)
            N=n+(k%2);A=random_surj(n,N,rng);trans=rng.randrange(1<<n);char=rng.randrange(1<<N)
            lift=tuple(f[mul(A,x)^trans]*(-1 if (char&x).bit_count()%2 else 1) for x in range(1<<N))
            bl=spectral(lift)
            assert (bl['H']-bf['H']).is_zero() and bl['M']==bf['M']
            ordinary=sum(bl['j'][1<<i] for i in range(N))
            assert bl['M']<=ordinary
            count+=1
    return {'status':'PASS','surjective_affine_and_character_examples':count}

def cubic_core_tests():
    rng=random.Random(2026091988);count=0;direction_count=0;rows_out=[]
    for k,widths,free,repeats in [(3,[],1,16),(3,[4],0,24),(5,[4],0,12),
                                  (6,[4],0,8),(3,[4,4],0,4),(5,[4],1,4),
                                  (6,[],2,8)]:
        m=sum(widths)+free;n=k+m
        triples=list(combinations(range(k),3))
        pairlist=list(combinations(range(k),2))
        for _ in range(repeats):
            while True:
                terms=[e for e in triples if rng.getrandbits(1)]
                contractions=[sum((1<<v) for v in range(k) if tuple(sorted((i,j,v))) in terms
                                  and v!=i and v!=j) for i,j in pairlist]
                if rank(contractions)==k:break
            g=tuple((-1)**sum(all(x>>i&1 for i in e) for e in terms) for x in range(1<<k))
            core_derivatives=[]
            for v in range(1<<k):
                co=E.fwht(tuple(g[x]*g[x^v] for x in range(1<<k)))
                if v:assert max(abs(z) for z in co)<=(1<<(k-1))
                core_derivatives.append(co)
            G,wranges,used=clause_product(m,widths)
            q,polar=quadratic(n,[e for e in combinations(range(n),2) if rng.getrandbits(1)])
            vals=tuple(g[x&((1<<k)-1)]*G[x>>k]*q[x] for x in range(1<<n))
            bf=spectral(vals);bg=spectral(G)
            rho_y=rank(polar[k:]);A=bg['M']
            eps=max((F(1,2**(w-1)) for w in widths),default=F(0))
            lower=F(k,4)+A+(F(1,2)-2*eps)*rho_y
            assert bf['M']>=lower
            (4*bf['M']-bf['H']).nonnegative()
            (k+bg['H']+rho_y-bf['H']).nonnegative()
            for v,j in enumerate(bf['j']):
                bv=mul(polar,v)
                if j<F(1,4):assert v&((1<<k)-1)==0 and bv==0
                if j<F(1,2)-eps:assert bv>>k==0
                cv=v&((1<<k)-1);cy=v>>k
                pred=F(abs(core_derivatives[cv][bv&((1<<k)-1)]),1<<k)
                ly=bv>>k
                if ly>>used:pred=F(0)
                for off,w,b in wranges:
                    vv=(cy>>off)&((1<<w)-1);ll=(ly>>off)&((1<<w)-1)
                    a=F(1,2**(w-1))
                    if not vv:
                        if ll:pred=F(0)
                    elif not ll:pred*=1-2*a
                    elif (ll&vv).bit_count()%2:pred=F(0)
                    else:pred*=2*a
                assert pred==F(abs(bf['c'][v]),1<<n)
                direction_count+=1
            # Exact wide-label marginal coset conservation.
            marginal=[0]*(1<<m)
            for s,w in enumerate(bf['m']):marginal[s>>k]+=w
            Erows=[row>>k for row in polar[k:]]
            Dimages=[(mul(polar,1<<i)>>k) for i in range(k)]
            W=Erows+Dimages
            qy,_=quadratic(m,[(i,j) for i in range(m) for j in range(i+1,m) if Erows[i]>>j&1])
            pq=spectral(qy);shift=next(i for i,w in enumerate(pq['m']) if w)
            left=block_masses(marginal,W,shift);right=block_masses(bg['m'],W)
            assert left=={c:w*(1<<(2*k)) for c,w in right.items()}
            count+=1
        rows_out.append({'core_dimension':k,'widths':widths,'free_variables':free,
                         'output_wide_polar_rank':rho_y,'M_lower':str(lower),
                         'M_actual':str(bf['M']),'entropy':E.show(bf['H'])})
    return {'status':'PASS','nondegenerate_cubic_core_examples':count,
            'directional_correlations_checked':direction_count,
            'conditional_coset_masses_checked':count,'selected_examples':rows_out}


def radical_tests():
    """Check the adapted-basis removal of all affine-derivative directions."""
    rng=random.Random(19092631);checked=0;hist=Counter()
    for n in range(1,7):
        masks=[m for m in range(1,1<<n) if m.bit_count()<=3]
        for _ in range(32):
            terms=[m for m in masks if rng.getrandbits(1)]
            vals=tuple((-1)**sum((x&m)==m for m in terms) for x in range(1<<n))
            R=[]
            for v in range(1<<n):
                dw=E.fwht(tuple(vals[x]*vals[x^v] for x in range(1<<n)))
                if max(abs(c) for c in dw)==1<<n:R.append(v)
            basis={};rad=[]
            for v in R:
                if rank_add(basis,v):rad.append(v)
            assert len(R)==1<<len(rad)
            extra=[]
            for i in range(n):
                if rank_add(basis,1<<i):extra.append(1<<i)
            columns=extra+rad;k=len(extra)
            def image(x):
                y=0
                for i,c in enumerate(columns):
                    if x>>i&1:y^=c
                return y
            tr=tuple(vals[image(x)] for x in range(1<<n))
            anf=[int(v<0) for v in tr]
            for i in range(n):
                for x in range(1<<n):
                    if x>>i&1:anf[x]^=anf[x^(1<<i)]
            cubics=[m for m,c in enumerate(anf) if c and m.bit_count()>=3]
            assert all(m.bit_count()==3 and m>>k==0 for m in cubics)
            core=tuple((-1)**sum((x&m)==m for m in cubics) for x in range(1<<k))
            for v in range(1,1<<k):
                dw=E.fwht(tuple(core[x]*core[x^v] for x in range(1<<k)))
                assert max(abs(c) for c in dw)<=1<<(k-1)
            hist[str(k)]+=1;checked+=1
    return {'status':'PASS','cubic_polynomials_with_possible_radical':checked,
            'residual_core_dimension_histogram':dict(sorted(hist.items())),
            'checks':'Exact affine-derivative subspace, adapted ANF, removal of all radical cubic terms, and residual one-half spectral gap'}

def direct_log_interval(q):
    q=F(q);power=0
    while q<1:q*=2;power-=1
    while q>=2:q/=2;power+=1
    lo,hi=E.ln_unit(q)
    return F(power)+lo/E.LN2[1],F(power)+hi/E.LN2[0]

def base_sharpness():
    values=[]
    for r in [4,8,16,32,64,128]:
        a=F(1,2**(r-1));lo,hi=direct_log_interval(1-a)
        part=(4*a-2*a*a)*(r-1);factor=-2*(1-a)**2
        hlo,hhi=factor*hi+part,factor*lo+part
        assert hhi<4*r*a
        values.append({'r':r,'H_over_M':{
            'lower':E.decimal_bound(hlo/(r*a),12,True),
            'upper':E.decimal_bound(hhi/(r*a),12,False)}})
    return {'status':'PASS','values':values,'scope':'Closed-form evaluations, not giant truth-table enumeration'}

def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);p.add_argument('--part',default='all',choices=['all','gate','class','affine','core','radical','sharp'])
    a=p.parse_args();start=time.monotonic()
    out={'full_FEI_proved':False,'independent_audit':False,'lean_used':False,
         'arithmetic':'Integers, Fraction, exact logarithmic forms with outward rational intervals',
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'dependency_sha256':hashlib.sha256(Path(E.__file__).read_bytes()).hexdigest()}
    for name,fun in [('gate',gate_tests),('class',class_tests),('affine',affine_tests),('core',cubic_core_tests),('radical',radical_tests),('sharp',base_sharpness)]:
        if a.part in ('all',name):out[name]=fun()
    out['status']='ALL_REQUESTED_CHECKS_PASS';out['elapsed_seconds']=round(time.monotonic()-start,3)
    text=json.dumps(out,indent=2)+'\n'
    if a.output:a.output.write_text(text)
    print(text)
if __name__=='__main__':main()
