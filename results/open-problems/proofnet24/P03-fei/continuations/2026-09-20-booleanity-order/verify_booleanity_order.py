#!/usr/bin/env python3
"""Exact finite checks of a failed truncated-Booleanity route to FEI.

The counterexamples are real-valued, NOT Boolean. No full FEI proof is claimed.
Python 3.10+ and NumPy. Assertions are integer/Fraction or rational-interval;
rounded decimal output is for display only. The analytic theorem is REPORT.md.
"""
from __future__ import annotations
from collections import Counter, defaultdict
from decimal import Decimal, localcontext
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import isqrt
from pathlib import Path
import hashlib, json
import numpy as np

SEED=2026092042
Interval=tuple[F,F]
Expr=dict[int,F]

def addint(a:Interval,b:Interval)->Interval:return a[0]+b[0],a[1]+b[1]
def scaleint(c:F,a:Interval)->Interval:return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])

@lru_cache(None)
def lnrange(t:F)->Interval:
    assert 1<=t<=2
    z=(t-1)/(t+1); z2=z*z; power=z; total=F(0); terms=48
    for k in range(terms):
        total+=2*power/(2*k+1);power*=z2
    return total,total+2*power/((2*terms+1)*(1-z2))

@lru_cache(None)
def log2int(x:F)->Interval:
    assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length();t=x/F(2)**k
    if t<1:k-=1;t*=2
    if t>=2:k+=1;t/=2
    a,b=lnrange(t);c,d=lnrange(F(2))
    return F(k)+a/d,F(k)+b/c

@lru_cache(None)
def factors(n:int)->tuple[tuple[int,int],...]:
    assert n>0
    out=[];p=2
    while p*p<=n:
        if n%p==0:
            k=0
            while n%p==0:n//=p;k+=1
            out.append((p,k))
        p=3 if p==2 else p+2
    if n>1:out.append((n,1))
    return tuple(out)

def expr_add(a:Expr,b:Expr,c:F=F(1))->Expr:
    out=dict(a)
    for p,v in b.items():
        out[p]=out.get(p,F(0))+c*v
        if not out[p]:del out[p]
    return out

def logexpr(x:F)->Expr:
    out={p:F(k) for p,k in factors(x.numerator)}
    return expr_add(out,{p:F(k) for p,k in factors(x.denominator)},F(-1))

def htermexpr(p:F)->Expr:
    return {q:-p*c for q,c in logexpr(p).items()} if p else {}

def pairexpr(r:F,s:F)->Expr:
    if not r or not s:return {}
    return expr_add(expr_add(htermexpr(r),htermexpr(s)),htermexpr(r+s),F(-1))

def exprint(a:Expr)->Interval:
    out=(F(0),F(0))
    for p,c in a.items():out=addint(out,scaleint(c,log2int(F(p))))
    return out

def h2int(p:F)->Interval:
    out=(F(0),F(0))
    for q in (p,1-p):
        if q:out=addint(out,scaleint(q,log2int(1/q)))
    return out

def pairint(r:F,s:F)->Interval:
    if not r or not s:return F(0),F(0)
    return scaleint(r+s,h2int(s/(r+s)))

def display(x:F)->str:
    with localcontext() as c:
        c.prec=24
        return str(Decimal(x.numerator)/Decimal(x.denominator))

def fwht(a:np.ndarray)->np.ndarray:
    a=np.asarray(a).copy()
    if a.ndim==1:a=a[None,:]
    N=a.shape[1];assert N and not N&(N-1)
    for i in range(N.bit_length()-1):
        r=a.reshape(len(a),-1,2<<i);u=r[:,:,:1<<i].copy();v=r[:,:,1<<i:].copy()
        r[:,:,:1<<i]=u+v;r[:,:,1<<i:]=u-v
    return a

def base(K:int,w:int)->tuple[dict[int,F],int]:
    q=isqrt(K);assert q*q==K and K>=4 and not K&(K-1) and w>=1
    m=3*K//4;n=K*w+m;a={}
    for z in range(K):
        tag=((1<<w)-1)<<(z*w)
        a[tag]=F(1,2*q)
        for i in range(1,m+1):
            sign=-1 if (z&i).bit_count()%2 else 1
            a[tag|(1<<(K*w+i-1))]=F(sign,K)
    return a,n

def square(a:dict[int,F])->dict[int,F]:
    out=defaultdict(F);items=list(a.items())
    for k,(x,u) in enumerate(items):
        out[0]+=u*u
        for y,v in items[k+1:]:out[x^y]+=2*u*v
    return {k:v for k,v in out.items() if v}

def energy(a:dict[int,F])->F:return sum((F(s.bit_count())*v*v for s,v in a.items()),F(0))
def entexpr(a:dict[int,F])->Expr:
    out={}
    for p,count in Counter(v*v for v in a.values()).items():out=expr_add(out,htermexpr(p),F(count))
    return out

def erasure(a:dict[int,F],n:int)->tuple[Expr,list[F],int]:
    p={s:v*v for s,v in a.items()};out={};infs=[F(0) for _ in range(n)];edges=0
    classes=Counter()
    for s,v in p.items():
        for i in range(n):
            if (s>>i)&1:infs[i]+=v
            elif s^(1<<i) in p:
                classes[tuple(sorted((v,p[s^(1<<i)])))]+=1;edges+=1
    for (r,s),count in classes.items():out=expr_add(out,pairexpr(r,s),F(count))
    return out,infs,edges

def restriction_norm(a:dict[int,F],fixed:list[int],bits:int)->F:
    mask=sum(1<<i for i in fixed);values=sum(((bits>>j)&1)<<i for j,i in enumerate(fixed));out=defaultdict(F)
    for s,v in a.items():
        sign=-1 if (s&values).bit_count()%2 else 1
        out[s&~mask]+=sign*v
    return sum((v*v for v in out.values()),F(0))

def base_checks()->dict:
    cases=[];restriction_checks=0;all_edges=0
    rng=np.random.default_rng(SEED)
    for K,w in [(4,1),(4,2),(4,3),(4,5),(16,1),(16,2),(16,3)]:
        a,n=base(K,w);c=square(a);m=3*K//4
        assert c[0]==1
        assert all(s==0 or 2*w<=s.bit_count()<=2*w+2 for s in c)
        fourth=sum((v*v for v in c.values()),F(0))
        assert fourth==3-F(23,4*K)+F(3,K*K)
        assert fourth>1 and fourth<3
        assert energy(a)==w+F(3,4)
        B,infs,edges=erasure(a,n);all_edges+=edges
        assert all(t==F(1,K) for t in infs)
        expected=expr_add({},pairexpr(F(1,4),F(1,K)),F(m))
        assert B==expected
        assert entexpr(a)=={2:F(7,4)*(K.bit_length()-1)+F(1,2)}
        # The lower bound uses the strictly positive second term of B.
        Bint=exprint(B);lower=scaleint(F(3,4),log2int(1+F(K,4)))
        assert Bint[0]>lower[1]
        if K==4 and w<=2:
            for size in range(2*w):
                for fixed in combinations(range(n),size):
                    for assignment in range(1<<size):
                        assert restriction_norm(a,list(fixed),assignment)==1;restriction_checks+=1
        else:
            for _ in range(40):
                size=int(rng.integers(0,2*w));fixed=list(map(int,rng.choice(n,size,replace=False)))
                assignment=int(rng.integers(0,1<<size))
                assert restriction_norm(a,fixed,assignment)==1;restriction_checks+=1
        cases.append({'K':K,'w':w,'dimension':n,'nonzero_amplitudes':len(a),
                      'nonzero_square_coefficients':len(c),'exact_fourth_moment':str(fourth),
                      'exact_energy':str(energy(a)),'erasure_over_energy_midpoint':display(sum(Bint)/2/energy(a))})
    return {'cases':cases,'physical_restriction_norm_checks':restriction_checks,'nonzero_erasure_edges':all_edges,
            'scope':'Exact sparse Fourier convolutions. Large physical cubes were not enumerated.'}

def near_dyadic(K:int,w:int,R:int)->tuple[dict[int,F],int]:
    assert R>=8 and not R&(R-1)
    a0,n0=base(K,w);tag=(1<<w)-1;out={0:1-F(2,R)}
    for j in range(R-1):
        shift=w+j*n0
        for s,v in a0.items():out[tag|(s<<shift)]=F(2,R)*v
    return out,w+(R-1)*n0

def dyadic_checks()->dict:
    cases=[];rng=np.random.default_rng(SEED+1);restrictions=0
    for K,w,R in [(4,1,8),(4,2,8),(4,3,8),(4,2,16)]:
        a,n=near_dyadic(K,w,R);c=square(a);delta=F(4*(R-1),R*R);b=F(2,R)
        assert c[0]==1 and all(s==0 or 2*w<=s.bit_count()<=2*w+2 for s in c)
        assert all(not v.denominator&(v.denominator-1) for v in a.values())
        assert energy(a)==delta*(2*w+F(3,4))
        assert sum(((v-(1 if s==0 else 0))**2 for s,v in a.items()),F(0))==F(4,R)
        q=F(23,8*K)-F(3,2*K*K)
        defect=sum((v*v for s,v in c.items() if s),F(0))
        assert defect==4*delta-2*delta**2-2*(R-1)*b**4*q
        assert 0<defect<4*delta<F(16,R)
        B,infs,edges=erasure(a,n);G,n0=base(K,w);BG,_,_=erasure(G,n0)
        assert B=={p:delta*v for p,v in BG.items()}
        assert all(t<=F(1,2) for t in infs)
        Hexpected=expr_add(htermexpr(delta),htermexpr(1-delta))
        Hexpected=expr_add(Hexpected,logexpr(F(R-1)),delta)
        Hexpected=expr_add(Hexpected,entexpr(G),delta)
        assert entexpr(a)==Hexpected
        for _ in range(24):
            size=int(rng.integers(0,2*w));fixed=list(map(int,rng.choice(n,size,replace=False)))
            assignment=int(rng.integers(0,1<<size))
            assert restriction_norm(a,fixed,assignment)==1;restrictions+=1
        cases.append({'K':K,'w':w,'R':R,'formal_dimension':n,'nonzero_amplitudes':len(a),
                      'square_defect_L2_squared':str(defect),'distance_to_one_L2_squared':str(F(4,R)),
                      'energy':str(energy(a)),'normalized_restrictions_checked':24})
    return {'cases':cases,'physical_restriction_norm_checks':restrictions,
            'scope':'Exact sparse arithmetic; functions are non-Boolean and are not claimed uniformly close to one.'}

def uniformly_close_check()->dict:
    # K=4,w=2 gives an 11-variable example. Enclose every actual square root,
    # then all normalized Walsh amplitudes by interval butterflies.
    K=4;w=2;G,n=base(K,w);N=1<<n;root=isqrt(K);eps=F(1,8*root);q={s:v/root for s,v in G.items()}
    grid=1<<120
    lows=[];highs=[];root_checks=0; lift_influence=F(0); lift_biases=set(); aux_bits=10; auxN=1<<aux_bits
    for x in range(N):
        Q=sum((v*(-1 if (s&x).bit_count()%2 else 1) for s,v in q.items()),F(0))
        assert abs(Q)<=1
        val=1+eps*Q
        k=isqrt((val.numerator*grid*grid)//val.denominator)
        lo=F(k,grid);hi=F(k+1,grid)
        assert lo*lo<=val<=hi*hi
        assert 1-eps<=lo<=hi<=1+eps
        lows.append(k);highs.append(k+1);root_checks+=1
        # An actual approximate Boolean lift: on the auxiliary cube, take
        # -1 at the lexicographic first c points and +1 elsewhere.
        target_lo,target_hi=lo/(1+eps),hi/(1+eps)
        neg=(1-(target_lo+target_hi)/2)/2
        c=(neg*auxN).numerator//(neg*auxN).denominator
        qlift=F(c,auxN);mean=1-2*qlift
        assert abs(mean-target_lo)<=eps/16 and abs(mean-target_hi)<=eps/16
        assert eps/8<=qlift<=2*eps
        boundary=0
        for bit in range(aux_bits):
            period=2<<(bit);rem=c%period;boundary+=min(rem,period-rem)
        lift_influence+=F(2*boundary,auxN*N);lift_biases.add(c)
    # Endpoints are exact integers on a shared grid, with signed interval arithmetic.
    lo=np.array(lows,dtype=object);hi=np.array(highs,dtype=object)
    for i in range(n):
        L=lo.reshape(-1,2<<i);H=hi.reshape(-1,2<<i)
        al=L[:,:1<<i].copy();ah=H[:,:1<<i].copy()
        bl=L[:,1<<i:].copy();bh=H[:,1<<i:].copy()
        L[:,:1<<i]=al+bl;H[:,:1<<i]=ah+bh
        L[:,1<<i:]=al-bh;H[:,1<<i:]=ah-bl
    ampl={s:(F(int(lo[s]),grid*N),F(int(hi[s]),grid*N)) for s in range(N)}
    checked=0;p_lower={}
    for s,v in q.items():
        target=eps*v/2;a,b=ampl[s]
        bound=eps*eps/F(4*K)
        assert a>=target-bound and b<=target+bound
        if target>0: assert a>=F(15,16)*target
        else: assert b<=F(15,16)*target
        p_lower[s]=min(a*a,b*b) if a*b>0 else F(0)
        assert p_lower[s]>=F(15,16)**2*eps**2*v*v/4
        checked+=1
    # Explicit selected-edge lower bound; actual erasure may include additional edges.
    lowerB=F(0);edgecount=0
    for s,p in p_lower.items():
        for i in range(n):
            t=s^(1<<i)
            if not s&(1<<i) and t in p_lower:
                lowerB+=pairint(p,p_lower[t])[0];edgecount+=1
    Iq=energy(q);Iupper=eps**2*Iq/(4*(1-eps))
    BG,_,_=erasure(G,n);base_ratio=exprint(BG)[1]/energy(G)
    assert lowerB/Iupper>F(4,5)*base_ratio
    square_defect=eps*eps/F(K)
    assert square_defect==F(1,64*K*K)
    robust_reference=F(4,5)*exprint(BG)[1]/(F(w)+F(19,4))
    assert lowerB/(Iupper+square_defect)>robust_reference
    lift_floor=scaleint(eps/4,log2int(8/eps))
    assert lift_influence>lift_floor[1]
    # This numerical example verifies the all-parameter lower bound; divergence
    # follows from the formula rather than ever larger truth-table enumeration.
    return {'K':K,'w':w,'dimension':n,'actual_square_roots_enclosed':root_checks,
            'selected_amplitude_certificates':checked,'selected_erasure_edges':edgecount,
            'epsilon':str(eps),'coefficient_relative_error_upper':'1/16',
            'approximate_boolean_lift_auxiliary_bits':aux_bits,
            'conditional_mean_certificates':N,
            'distinct_lift_negative_counts':sorted(lift_biases),
            'exact_lift_auxiliary_influence':str(lift_influence),
            'universal_lift_influence_floor_upper':display(lift_floor[1]),
            'exact_square_defect_L2_squared':str(square_defect),
            'certified_B_over_energy_plus_square_defect_lower':display(lowerB/(Iupper+square_defect)),
            'certified_erasure_over_energy_lower':display(lowerB/Iupper),
            'required_four_fifths_base_ratio_upper':display(F(4,5)*base_ratio),
            'normalization_and_low_order_constraints':'Exact from U^2=1+epsilon Q; Q has no terms below degree w.',
            'amplitudes_are_dyadic':False,'function_is_Boolean':False}

def rigidity_check()->dict:
    n=4;N=1<<n;T=((np.arange(1<<N,dtype=np.uint64)[:,None]>>np.arange(N,dtype=np.uint64)[None,:])&1).astype(np.int64)
    A=fwht(1-2*T)
    # Two one-bit controls 0,1 and two data bits 2,3.
    allowed={1,1|4,1|8,2,2|4,2|8};outside=[s for s in range(N) if s not in allowed]
    good=np.all(A[:,outside]==0,axis=1);selected=A[good]
    chars=four=0;sharp=0
    for row in selected:
        supp=np.flatnonzero(row);sq=row*row
        assert int(sq.sum())==N*N
        if len(supp)==1:
            assert abs(int(row[supp[0]]))==N;chars+=1
        else:
            assert len(supp)==4 and all(abs(int(row[s]))==N//2 for s in supp)
            I=F(sum(int(s).bit_count()*int(sq[s]) for s in supp),N*N)
            assert I>=F(3,2)
            sharp+=int(I==F(3,2));four+=1
    return {'all_boolean_functions_examined':len(T),'functions_with_required_support':len(selected),
            'characters':chars,'four_coefficient_functions':four,'sharp_ratio_four_thirds_cases':sharp,
            'scope':'Exhaustive n=4 Boolean scan filtered by the precise block-linear/data-affine support hypothesis.'}


def booleanization_check()->dict:
    K=4;w=1;a,n=base(K,w);N=1<<n
    numer=[]
    for x in range(N):
        val=sum((v*(-1 if (x&m).bit_count()%2 else 1) for m,v in a.items()),F(0))
        numer.append(1 if val>=0 else -1)
    f=np.array(numer,dtype=np.int64);W=fwht(f)[0]
    assert int((W*W).sum())==N*N
    x=np.arange(N);control=F(0);total=F(0)
    for i in range(n):
        inf=F(int(np.count_nonzero(f!=f[x^(1<<i)])),N)
        total+=inf
        if i<K:control+=inf
    ln4K=scaleint(F(4),lnrange(F(2)))
    assert 48*control**2*ln4K[0]>K
    aa={j:F(int(v),N) for j,v in enumerate(W) if v}
    B,_,_=erasure(aa,n)
    return {'K':K,'dimension':n,'truth_values_generated':N,
            'tie_rule':'sign(0)=+1','exact_control_influence':str(control),
            'exact_total_influence':str(total),
            'erasure_over_influence_midpoint':display(sum(exprint(B))/2/total),
            'scope':'One exact genuine Boolean threshold example; asymptotic influence lower bound is analytical.'}

def parameter_checks()->dict:
    rows=[]
    for k,w in [(2,1),(4,1),(8,1),(16,1),(64,1),(64,4),(256,4)]:
        K=4**k
        B=addint(scaleint(F(3,4),log2int(1+F(K,4))),scaleint(F(3*K,16),log2int(1+F(4,K))))
        I=w+F(3,4);bound=scaleint(F(3,4*w+3),log2int(1+F(K,4)))
        assert B[0]/I>bound[1]
        rows.append({'k':k,'K':'4^'+str(k),'w':w,
                     'base_ratio_lower':display(B[0]/I),'uniformly_close_ratio_lower':display(F(4,5)*B[0]/I),
                     'uniformly_close_B_over_energy_plus_square_defect_lower':display(F(4,5)*B[0]/(F(w)+F(19,4))),
                     'exact_low_order_cancellation_through_base':2*w-1,
                     'uniformly_close_cancellation_through':w-1})
    assert F(15,16)**3>F(4,5)
    return {'rows':rows,'scope':'Analytic sparse formulas with rational log enclosures; these huge physical truth tables were not generated.'}

def main()->None:
    result={'status':'PASS','date':'2026-09-20','seed':SEED,
            'full_FEI_proved':False,'counterexamples_are_Boolean':False,
            'independent_review':False,'formal_proof_assistant_used':False,
            'base_hadamard':base_checks(),'dyadic_near_boolean':dyadic_checks(),
            'uniformly_close':uniformly_close_check(),'exact_boolean_rigidity':rigidity_check(),
            'genuine_booleanization':booleanization_check(),
            'parameter_formulas':parameter_checks()}
    result['checker_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    text=json.dumps(result,indent=2)+'\n'
    Path(__file__).with_name('verification.json').write_text(text)
    print(text,end='')
if __name__=='__main__':main()
