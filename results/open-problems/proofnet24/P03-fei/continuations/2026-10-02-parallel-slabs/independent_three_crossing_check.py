"""Independent exact construction/coefficient checks and high precision display."""
from fractions import Fraction as F
from math import comb,log2
from pathlib import Path
import json
from decimal import Decimal as D,getcontext


def walsh(v):
    out=list(v);width=1
    while width<len(out):
        for left in range(0,len(out),2*width):
            for i in range(left,left+width):
                a,b=out[i],out[i+width]
                out[i],out[i+width]=a+b,a-b
        width*=2
    return out


def coef(N,k):
    if not k%2:return F(0)
    d=(N-1)//2;ell=(k-1)//2
    return (-1)**ell*F(comb(2*d,d),4**d)*F(comb(d,ell),comb(2*d,2*ell))


report={'status':'PASS','scope':'Exact rational checks and finite high-precision entropy displays; asymptotic proof is separate',
        'direct_truth_cases':0,'direct_majority_coefficients':0,'exact_uniform_coefficient_bound_dimensions':0,
        'high_precision_rows':[]}
for N in range(3,16,2):
    size=1<<N;w=N+1
    majority=[1 if 2*x.bit_count()-N>0 else -1 for x in range(size)]
    f=[]
    for z in(-1,1):
        for x in range(size):
            s=w*z+2*x.bit_count()-N
            assert s%2 and -w%2==0 and w%2==0
            v=-1 if s<-w else (1 if s<2 else(-1 if s<w else 1))
            assert v==(1 if z==1 and x==0 else majority[x])
            f.append(v);report['direct_truth_cases']+=1
    assert F(sum(f[x]!=f[x^size]for x in range(2*size)),2*size)==F(1,size)
    c=walsh(majority)
    for S,value in enumerate(c):
        k=S.bit_count()
        assert (-1)**k*F(value,size)==coef(N,k)
        report['direct_majority_coefficients']+=1
    A=[(f[x]+f[x+size])//2 for x in range(size)]
    B=[(f[x+size]-f[x])//2 for x in range(size)]
    assert sum(B)==1 and B[0]==1
    ca,cb=walsh(A),walsh(B);cf=walsh(f)
    assert all(F(cf[s]**2,(2*size)**2)==F(ca[s]**2,size**2)for s in range(size))
    assert all(F(cf[s+size]**2,(2*size)**2)==F(cb[s]**2,size**2)for s in range(size))


for N in range(15,514,2):
    d=(N-1)//2;alpha=F(1,1<<N)
    bound=F(1,(1<<d)*N*(d+1))
    assert bound>=2*alpha
    for ell in range(d+1):
        assert abs(coef(N,2*ell+1))>=bound
        assert comb(2*d,2*ell)<=(d+1)*comb(d,ell)**2
    report['exact_uniform_coefficient_bound_dimensions']+=1


getcontext().prec=400
ln2=D(2).ln()
def asmp(q):return D(q.numerator)/q.denominator
def h(q):
    if q in(0,1):return D(0)
    v=asmp(q)
    return -(v*v.ln()+(1-v)*(1-v).ln())/ln2

for N in(3,15,31,63,127,255,511):
    alpha=F(1,1<<N);delta=D(0)
    even=D(0)
    for k in range(N+1):
        b=(-1)**k*alpha;a=coef(N,k)+b;P=a*a+b*b
        q=b*b/P;r=(a+b)**2/(2*P)
        term=comb(N,k)*asmp(P)*(1+h(q)-h(r))
        delta+=term
        if not k%2:even+=term
    assert abs(even/asmp(alpha)-2)<D('1e-90')
    ratio=delta/asmp(alpha)
    lower=D(N+3)/2-(D(N*(N+1))/2).ln()/ln2
    upper=2*(N+1/ln2)
    if N>=15:assert ratio>=lower
    assert ratio<=upper
    report['high_precision_rows'].append({'N':N,'delta_over_alpha':format(ratio,'.40g'),
        'analytic_lower_ratio_valid_for_N_ge_15':format(lower,'.40g'),
        'analytic_upper_ratio':format(upper,'.40g')})

Path(__file__).with_name('independent_three_crossing_checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
