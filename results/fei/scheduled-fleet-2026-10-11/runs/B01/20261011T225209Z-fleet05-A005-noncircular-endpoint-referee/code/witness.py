"""One frozen analytic Boolean witness; rigorous rational logarithm intervals."""
from fractions import Fraction as Q
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]
spec={'helper_version':'A005-witness-v1','family':'F=1+A_8(f^tensor16-1), f is 3-bit one-point defect',
      'domain':{'n':3,'m':16,'k':8,'dimension':56,'K':'5/2','lambda':0},
      'case_count':1,'symmetry':'48 identical data coordinates and 8 identical controls, justified by block/permutation symmetry',
      'arithmetic':'Fraction and 40-term atanh logarithm with explicit remainder',
      'estimated_memory_MB':30,'maximum_runtime_seconds':60,'truth_table_enumeration':False}
(ROOT/'out/WITNESS_FROZEN_SPEC.json').write_text(json.dumps(spec,indent=2))
def plus(a,b): return (a[0]+b[0],a[1]+b[1])
def minus(a,b): return (a[0]-b[1],a[1]-b[0])
def mul(a,c): return (a[0]*c,a[1]*c) if c>=0 else (a[1]*c,a[0]*c)
def ln_unit(r):
    z=(r-1)/(r+1); N=40
    s=2*sum((z**(2*j+1)/Q(2*j+1) for j in range(N)),Q(0))
    e=2*z**(2*N+1)/(Q(2*N+1)*(1-z*z))
    return s,s+e
LN2=ln_unit(Q(2))
def log2(x):
    q=x.numerator.bit_length()-x.denominator.bit_length()
    r=x/(Q(2)**q)
    if r<1: q-=1;r*=2
    lo,hi=ln_unit(r)
    return Q(q)+lo/LN2[1],Q(q)+hi/LN2[0]
def phi(x): return (Q(0),Q(0)) if x==0 else mul(log2(x),-x)
def L(u,v): return minus(plus(phi(u*u),phi(v*v)),phi(u*u+v*v))
start=time.perf_counter();mu=Q(3,4);m=16;k=8;t=Q(1,1<<k);c=mu**m;d=Q(1,4)*mu**(m-1)
Bseed=plus((Q(3,8),Q(3,8)),L(Q(3,4),Q(1,4)))
Bdata=plus(minus(mul(Bseed,t),mul(L(c,d),t)),plus(mul(L(c-1,d),t-t*t),L(1-t+t*c,t*d)))
Bcontrol=plus((t*(1-c*c)+(t-2*t*t)*(1-c)**2,)*2,L(1-t+t*c,t*(c-1)))
seedratio=mul(Bseed,4);dataratio=mul(Bdata,4/t);controlratio=mul(Bcontrol,1/(t*(1-c)))
assert seedratio[0]>Q(5,2)
assert dataratio[0]>Q(5,2)
assert controlratio[1]<Q(5,2)
def record(interval):
    scale=1<<40
    lo=Q((interval[0]*scale).__floor__(),scale)
    hi=Q((interval[1]*scale).__ceil__(),scale)
    assert lo<=interval[0]<=interval[1]<=hi
    return {'lower_rational':str(lo),'upper_rational':str(hi),
            'decimal_display_only':[float(interval[0]),float(interval[1])]}
result={'status':'PASS','seed_Bi_over_Inf':record(seedratio),'all_data_Bi_over_Inf':record(dataratio),
        'all_control_Bi_over_Inf':record(controlratio),'max_influence':str(t*(1-c)),
        'exact_max_influence_less_than':'1/256','threshold':'5/2','elapsed_seconds':time.perf_counter()-start,
        'interpretation':'F admits a control witness at K=5/2, while the seed and every data coordinate of F fail K=5/2. This refutes same-K activation witness transport, not the universal localized endpoint.'}
(ROOT/'out/WITNESS_CERTIFICATE.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k in ['status','max_influence','elapsed_seconds']}))
print('ratios (display only):',*[float(v[0]) for v in [seedratio,dataratio,controlratio]])
