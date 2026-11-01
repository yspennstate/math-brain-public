"""Rational checks for the balanced-substitution FEI continuation.

The universal conclusions depend on the proofs in REPORT.md. This program is a
finite self-check, not Lean or independent review. It does not claim full FEI.
Only standard-library modules are used. Accepted entropy inequalities use
rational linear forms in prime logarithms and outward rational log intervals.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from math import comb
from pathlib import Path
import argparse
import hashlib
import json
import random
import time

@lru_cache(None)
def factors(n: int):
    if n < 1:
        raise ValueError('Expected positive integer')
    out = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0)+1
            n //= d
        d = 3 if d == 2 else d+2
    if n > 1:
        out[n] = out.get(n, 0)+1
    return tuple(out.items())

class LogExpr:
    """Exact rational linear combination of log_2(prime)."""
    def __init__(self, terms=None):
        self.terms = {p: F(c) for p,c in (terms or {}).items() if c}
    def __add__(self, other):
        if not isinstance(other, LogExpr):
            other = LogExpr({2:F(other)})
        out = self.terms.copy()
        for p,c in other.terms.items():
            out[p] = out.get(p,F(0))+c
        return LogExpr(out)
    __radd__ = __add__
    def __neg__(self):
        return LogExpr({p:-c for p,c in self.terms.items()})
    def __sub__(self, other):
        return self+(-other if isinstance(other, LogExpr) else -F(other))
    def __rsub__(self, other):
        return -self+other
    def __mul__(self, c):
        c=F(c)
        return LogExpr({p:c*v for p,v in self.terms.items()})
    __rmul__=__mul__
    def __truediv__(self,c):
        return self* (1/F(c))
    def interval(self):
        lo=hi=F(0)
        for p,c in self.terms.items():
            a,b=log2_prime(p)
            if c>=0:
                lo+=c*a; hi+=c*b
            else:
                lo+=c*b; hi+=c*a
        return lo,hi
    def nonnegative(self):
        if not self.terms:
            return True
        lo,hi=self.interval()
        if lo>=0:
            return True
        raise AssertionError(f'Uncertified entropy comparison: [{float(lo)}, {float(hi)}]')
    def is_zero(self):
        return not self.terms

@lru_cache(None)
def ln_unit(q:F):
    if not 1<=q<=2:
        raise ValueError('Argument outside range reduction')
    z=(q-1)/(q+1); z2=z*z
    power=z; val=F(0)
    for k in range(64):
        val+=2*power/(2*k+1); power*=z2
    err=2*power/(129*(1-z2))
    return val,val+err

LN2=ln_unit(F(2))

@lru_cache(None)
def log2_prime(p:int):
    if p==2: return F(1),F(1)
    k=p.bit_length()-1
    lo,hi=ln_unit(F(p,1<<k))
    return k+lo/LN2[1],k+hi/LN2[0]

def log_rat(q:F):
    q=F(q)
    if q<=0: raise ValueError('Positive logarithm argument required')
    d=defaultdict(F)
    for p,e in factors(q.numerator): d[p]+=e
    for p,e in factors(q.denominator): d[p]-=e
    return LogExpr(d)

def entropy_weights(weights,den):
    assert sum(weights)==den
    out=LogExpr()
    for w in weights:
        if w:
            p=F(w,den)
            out+=(-p)*log_rat(p)
    return out

def decimal_bound(q:F,digits:int,lower:bool):
    v=q*10**digits
    z=v.numerator//v.denominator
    if not lower and v.denominator!=1: z+=1
    sign='-' if z<0 else ''; z=abs(z)
    a,b=divmod(z,10**digits)
    return f'{sign}{a}.{b:0{digits}d}'

def show(x,digits=12):
    lo,hi=x.interval() if isinstance(x,LogExpr) else (F(x),F(x))
    return {'lower':decimal_bound(lo,digits,True),'upper':decimal_bound(hi,digits,False)}

def fwht(a):
    a=list(a); k=1
    while k<len(a):
        for i in range(0,len(a),2*k):
            for j in range(i,i+k):
                u,v=a[j],a[j+k]
                a[j],a[j+k]=u+v,u-v
        k*=2
    return a

def canonical(f):
    return tuple(x*f[0] for x in f)

def derivative(f,z):
    return canonical(tuple(f[x]*f[x^z] for x in range(len(f))))

@lru_cache(None)
def basic(f):
    N=len(f); n=N.bit_length()-1
    assert N==1<<n and set(f)<= {-1,1}
    w=fwht(f); masses=tuple(v*v for v in w); den=N*N
    assert sum(masses)==den
    H=entropy_weights(masses,den)
    influences=[]; C=F(0)
    for i in range(n):
        u=tuple(f[x]*f[x^(1<<i)] for x in range(N))
        influences.append(F(sum(a==-1 for a in u),N))
        wu=fwht(u)
        C+=sum((F(wu[s]**2,den*(1+s.bit_count())) for s in range(1,N)),F(0))
    j=tuple(min(x,1-x) for x in influences)
    Q=sum((x*x*log_rat(1/x) for x in j if x),LogExpr())
    return {'n':n,'masses':masses,'den':den,'H':H,'I':tuple(influences),'C':C,'Q':Q,
            'Var':1-F(masses[0],den),'J':sum(j)}

@lru_cache(None)
def information(f,block_size=0):
    data=basic(f); den=data['den']; pairden=den*den
    supp=[(s,w) for s,w in enumerate(data['masses']) if w]
    xor=defaultdict(int); statuses=defaultdict(int)
    jointY_U=defaultdict(int); jointWo_Z=defaultdict(int)
    def mask(s):
        return sum((bool((s>>(b*block_size))&((1<<block_size)-1))<<b)
                   for b in range(data['n']//block_size))
    masks={s:mask(s) for s,w in supp} if block_size else {}
    for s,p in supp:
        for t,q in supp:
            u=s^t; w=s&t; weight=p*q
            xor[u]+=weight; statuses[(u,w)]+=weight
            if block_size:
                a,b=masks[s],masks[t]
                jointY_U[(u,a^b,a&b)]+=weight
                jointWo_Z[(u,w,a&b)]+=weight
    Hxor=entropy_weights(tuple(xor.values()),pairden)
    Hstatus=entropy_weights(tuple(statuses.values()),pairden)
    out={'A':2*data['H']-Hstatus,'L':2*data['H']-Hxor}
    if block_size:
        out['defect_L']=entropy_weights(tuple(jointY_U.values()),pairden)-Hxor
        out['defect_A']=entropy_weights(tuple(jointWo_Z.values()),pairden)-Hstatus
    return out

@lru_cache(None)
def Dcross(f):
    return 2*basic(f)['H']-sum((basic(derivative(f,z))['H'] for z in range(len(f))),LogExpr())/len(f)

def increasing(f):
    n=len(f).bit_length()-1
    return all(f[x]<=f[x|(1<<i)] for x in range(len(f)) for i in range(n) if not x&(1<<i))

def small_checks():
    raw=0; monotone4=0; inequalities=0; distinct=set()
    for n in range(4):
        for bits in range(1<<(1<<n)):
            raw+=1
            distinct.add(canonical(tuple(1 if bits&(1<<x) else -1 for x in range(1<<n))))
    for bits in range(1<<16):
        f=tuple(1 if bits&(1<<x) else -1 for x in range(16))
        if increasing(f):
            monotone4+=1; distinct.add(canonical(f))
            b=basic(canonical(f))
            assert b['C']==4*(b['Var']-sum(x*x for x in b['I']))
    rng=random.Random(190926)
    for _ in range(64):
        distinct.add(canonical(tuple(rng.choice((-1,1)) for _ in range(16))))
    for f in distinct:
        b=basic(f); info=information(f); D=Dcross(f)
        assert b['C']+4*sum(x*x for x in b['I'])>=4*b['Var']
        for expr in [info['A'],info['L']-info['A'],D-info['L'],2*info['L']-D,
                     2*info['A']+7*b['Q']-D]:
            expr.nonnegative(); inequalities+=1
        assert (info['L']-info['A']).interval()[0]>=0 or (info['L']-info['A']).is_zero()
        if len(f)>1:
            # Character multiplication leaves allocation entropy and D unchanged.
            char_mask=1
            g=canonical(tuple(v*(-1 if (x&char_mask).bit_count()%2 else 1) for x,v in enumerate(f)))
            assert (information(g)['A']-info['A']).is_zero()
    return {'status':'PASS','all_truth_tables_dimension_0_to_3':raw,
            'all_increasing_functions_dimension_4':monotone4,
            'distinct_canonical_functions_total':len(distinct),
            'certified_entropy_inequalities':inequalities,
            'checks':'Monotone C identity; general variance bound; A<=L<=D<=2L; D<=2A+7Q; character invariance'}

def majority(m):
    assert m%2
    return tuple(1 if 2*x.bit_count()>m else -1 for x in range(1<<m))

def compose(f,g):
    m=len(f).bit_length()-1; b=len(g).bit_length()-1; mask=(1<<b)-1
    return canonical(tuple(f[sum((g[(x>>(i*b))&mask]==1)<<i for i in range(m))]
                           for x in range(1<<(m*b))))

def composition_checks():
    g=majority(3); bg=basic(g); gi=information(g)
    Ccount=0; Ecount=0; Acnt=0; sample=[]
    # Every Boolean outer function on three variables up to output sign.
    for bits in range(128):
        f=canonical(tuple(1 if (bits<<1)&(1<<x) else -1 for x in range(8)))
        Fg=compose(f,g); bh=basic(f); bc=basic(Fg)
        assert bc['C']+4*sum(x*x for x in bc['I'])==bh['C']+4*sum(x*x for x in bh['I'])
        assert sum(bc['I'])==sum(bh['I'])*sum(bg['I'])
        assert (bc['H']-bh['H']-sum(bh['I'])*bg['H']).is_zero()
        Ccount+=1; Ecount+=1
    outer=[canonical(tuple(1 if bits&(1<<x) else -1 for x in range(4))) for bits in range(16)]
    outer=list(set(outer))+[canonical(majority(3)),canonical(tuple(1 if x==7 else -1 for x in range(8)))]
    for f in outer:
        Fg=compose(f,g); bi=basic(f); fi=information(f); ci=information(Fg,3)
        p2=sum(x*x for x in bi['I'])
        assert (ci['L']-fi['A']-p2*gi['L']-ci['defect_L']).is_zero()
        assert (ci['A']-fi['A']-p2*gi['A']-ci['defect_A']).is_zero()
        ci['defect_L'].nonnegative(); ci['defect_A'].nonnegative()
        Acnt+=1
        if len(f)==8:
            sample.append({'outer_bits':3,'outer_entropy':show(bi['H']),
                           'outer_A':show(fi['A']),'composite_A':show(ci['A']),
                           'composition_A_defect':show(ci['defect_A']),
                           'composite_C':str(basic(Fg)['C'])})
    return {'status':'PASS','exact_C_and_influence_substitution_examples':Ccount,
            'exact_entropy_composition_examples':Ecount,
            'exact_allocation_and_XOR_composition_examples':Acnt,
            'selected_examples':sample}

def compose_variable(f, inners):
    widths=[len(g).bit_length()-1 for g in inners]
    assert len(inners)==len(f).bit_length()-1
    shifts=[]; shift=0
    for w in widths:
        shifts.append(shift); shift+=w
    return canonical(tuple(f[sum((g[(x>>a)&((1<<w)-1)]==1)<<i
                                  for i,(g,a,w) in enumerate(zip(inners,shifts,widths)))]
                           for x in range(1<<shift)))

def extra_composition_checks():
    maj=majority(3); leaf=(-1,1)
    shapes=[compose_variable(maj,[maj,leaf,leaf]),
            compose_variable(maj,[maj,leaf,maj]),
            compose_variable(maj,[leaf,maj,leaf]),compose_variable(maj,[maj,maj,maj])]
    shape_rows=[]
    for f in shapes:
        b=basic(f); info=information(f)
        assert (info['A']-F(3,4)*b['C']).is_zero()
        (F(3,2)*b['C']+7*b['Q']-Dcross(f)).nonnegative()
        shape_rows.append({'variables':b['n'],'C':str(b['C']),'A':show(info['A'])})
    # A balanced monotone inner function that is not odd/self-dual.
    tie={3,12,5}
    g4=tuple(1 if x.bit_count()>=3 or x in tie else -1 for x in range(16))
    assert sum(g4)==0 and increasing(g4)
    assert any(g4[x]==g4[x^15] for x in range(16))
    bg=basic(g4); count=0
    for bits in range(8):
        f=canonical(tuple(1 if (bits<<1)&(1<<x) else -1 for x in range(4)))
        cf=basic(compose(f,g4)); bf=basic(f)
        assert cf['C']+4*sum(x*x for x in cf['I'])==bf['C']+4*sum(x*x for x in bf['I'])
        count+=1
    # The non-odd balanced four-bit gate tests a strictly positive correction.
    mux=g4
    h=tuple(1 if x==3 else -1 for x in range(4))
    Fh=compose(h,mux); hi=information(h); ig=information(mux); ci=information(Fh,4)
    weight=sum(p*p for p in basic(h)['I'])
    assert (ci['A']-hi['A']-weight*ig['A']-ci['defect_A']).is_zero()
    assert (ci['L']-hi['A']-weight*ig['L']-ci['defect_L']).is_zero()
    assert ci['defect_A'].interval()[0]>0
    return {'status':'PASS','unequal_ternary_tree_shapes':shape_rows,
            'nonodd_balanced_monotone_common_inner_examples':count,
            'nonodd_allocation_defect_example':show(ci['defect_A']),
            'scope':'Checks exact odd-inner closure and a strictly positive general correction'}

@lru_cache(None)
def central(r):
    return F(comb(2*r,r),4**r)

def majority_bound(m):
    r=(m-1)//2
    q=[F(m)*central(r)*central(s)*central(r-s)/(2*s+1) for s in range(r+1)]
    assert sum(q)==1
    tail=F(0); minimum=F(1)
    for s in range(r,0,-1):
        tail+=q[s]; minimum+=2*tail*tail
    W1=m*central(r)**2
    bound=minimum-W1
    harmonic=sum((F(1,i) for i in range(1,r+1)),F(0))
    assert bound>=harmonic/18+F(1,36)
    assert F(1,2)<=W1<=F(3,4)
    return bound,harmonic/18+F(1,36),q

def family_checks():
    weights_checked=[]
    for m in [3,5,7,9,11]:
        f=canonical(majority(m)); b=basic(f); r=(m-1)//2
        bound,lower,q=majority_bound(m)
        for s in range(r+1):
            actual=sum(w for k,w in enumerate(b['masses']) if k.bit_count()==2*s+1)
            assert F(actual,b['den'])==q[s]
        # Exact information calculations for the two smallest nontrivial cases.
        if m<=5:
            (information(f)['A']-bound).nonnegative()
        weights_checked.append(m)
    rows=[]
    for m in [3,5,9,17,33,65,129,257,513,1025]:
        b,lower,q=majority_bound(m)
        rows.append({'outer_majority_bits':m,'rational_allocation_lower':show(b),
                     'harmonic_lower':show(lower)})
    # Finite rational parameter checks underpin the all-d monotonic bound.
    for d in range(13,257):
        v=F(3*d+1)*(F(3,4)**d)
        assert v<1
        assert F(3*(d+1)+1)*(F(3,4)**(d+1))<v
        if d>=20: assert v<F(1,4)
    # Section 5.2: lower log bound LN2 > 2/3, no giant truth table.
    assert LN2[0]>F(2,3)
    d=1026
    Qupper=F(3,8)*(3*d+1)*(F(3,4)**d)
    assert Qupper<F(1,4)
    Dlower=F(1024,27)+F(1,36)
    ratio=Dlower/F(17,4)
    assert Dlower==F(4099,108) and ratio==F(4099,459) and ratio>8
    return {'status':'PASS','majority_spectral_weight_truth_table_checks':weights_checked,
            'rational_lower_bound_examples':rows,
            'Q_parameter_checks_d_13_through_256':244,
            'symbolic_K8_witness':{'r':'2^1024','m':'2^1025+1','d':d,
                                  'D_strict_lower':'4099/108','C_plus_Q_strict_upper':'17/4',
                                  'ratio_strict_lower':'4099/459',
                                  'ratio_lower_decimal':show(ratio),
                                  'scope':'Proof-based symbolic witness; NO truth-table enumeration at this dimension'}}

def main():
    p=argparse.ArgumentParser(); p.add_argument('--output',type=Path)
    p.add_argument('--part',choices=['all','small','composition','extra','family'],default='all')
    args=p.parse_args(); start=time.monotonic()
    out={'full_FEI_proved':False,'full_resolvent_pointwise_candidate':'REFUTED by the accompanying analytic family',
         'independent_audit':False,'lean_used':False,
         'acceptance_arithmetic':'Integers and Fraction linear forms in prime logarithms; 64-term outward logarithm bounds',
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    for name,job in [('small',small_checks),('composition',composition_checks),('extra',extra_composition_checks),('family',family_checks)]:
        if args.part in ('all',name): out[name]=job()
    out['status']='ALL_REQUESTED_CHECKS_PASS'; out['elapsed_seconds']=round(time.monotonic()-start,3)
    text=json.dumps(out,indent=2)+'\n'
    if args.output: args.output.write_text(text)
    print(text)
if __name__=='__main__': main()
