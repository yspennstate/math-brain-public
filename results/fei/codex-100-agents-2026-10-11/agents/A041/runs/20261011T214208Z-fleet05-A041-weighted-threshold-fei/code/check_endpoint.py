"""A041 endpoint v1. Rational log intervals, range-reduced atanh series."""
from fractions import Fraction as F
from pathlib import Path
import json, time
root = Path(__file__).resolve().parents[1]
start = time.monotonic()
def ln_core(x):
    z = (x-1)/(x+1)
    assert 1<=x<=2
    v = 2*sum(z**(2*k+1)/F(2*k+1) for k in range(24))
    err = 2*z**49/(49*(1-z*z))
    return v,v+err
LN2 = ln_core(F(2))
def ln(x):
    assert x>0
    exponent=0
    while x<1:
        x*=2; exponent-=1
    while x>2:
        x/=2; exponent+=1
    a,b=ln_core(x)
    c,d=LN2
    return (a+exponent*c,b+exponent*d) if exponent>=0 else (a+exponent*d,b+exponent*c)
def log2(x):
    a,b=ln(x); c,d=LN2
    corners=(a/c,a/d,b/c,b/d)
    return min(corners),max(corners)
def entropy(ps):
    assert all(p>=0 for p in ps) and sum(ps)==1
    a=b=F(0)
    for p in ps:
        if p:
            c,d=log2(p); a-=p*d; b-=p*c
    return a,b
rows=[]
for k in range(2,8):
    p=F(1,2**k); q=F(1,4); v=4*q*(1-q)
    ps=((1-2*p*q)**2,4*p*(1-p)*q*q,p*p*v,p*(1-p)*v)
    assert sum(ps)==1
    # Derivative coefficients from truth-table f=1-2XY are -2q,-2p,-2.
    assert ps[1]==(-2*q)**2*p*(1-p)
    assert ps[2]==(-2*p)**2*q*(1-q)
    assert ps[3]==(-2)**2*p*(1-p)*q*(1-q)
    hs=entropy(ps); hy=entropy((1-p*v,p*v)); hc=entropy((1-v,v))
    margin=(2*hy[0]-hs[1]-p*hc[1],2*hy[1]-hs[0]-p*hc[0])
    assert margin[0]>0 and margin[0]<=margin[1]
    ratio=(margin[0]/(p*k),margin[1]/(p*k))
    rows.append({'p':str(p),'q':str(q),'spectrum':[str(s) for s in ps],
                 'J_minus_M_lower_rational':str(margin[0]),
                 'J_minus_M_upper_rational':str(margin[1]),
                 'normalized_ratio_interval_rational':[str(a) for a in ratio]})
out={'helper_version':'A041-endpoint-v1','case_count':6,'status':'PASS',
     'arithmetic':'Exact Fraction atanh intervals, 24 terms after range reduction; signed division by four corners',
     'rows':rows,'elapsed_seconds':time.monotonic()-start,
     'asymptotic_status':'Analytic proof, not extrapolation from these finite rows'}
(root/'out'/'ENDPOINT_VALIDATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
