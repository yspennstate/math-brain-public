import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def ln_interval(x,terms=32):
    x=Fraction(x);k=0
    while x>=2:x/=2;k+=1
    while x<1:x*=2;k-=1
    def series(z):
        t=(z-1)/(z+1)
        lo=2*sum((t**(2*j+1)/Fraction(2*j+1) for j in range(terms)),Fraction(0))
        return lo,lo+2*t**(2*terms+1)/((2*terms+1)*(1-t*t))
    lo,hi=series(x);a,b=series(Fraction(2))
    if k>=0:return lo+k*a,hi+k*b
    return lo+k*b,hi+k*a

def log_interval(x):
    a,b=ln_interval(x);c,d=ln_interval(2)
    return a/d,b/c

def signature_interval(signature):
    lo=hi=Fraction(0)
    for p,a in signature:
        x,y=(Fraction(1),Fraction(1)) if p==2 else log_interval(p)
        lo+=a*(x if a>=0 else y);hi+=a*(y if a>=0 else x)
    return lo,hi

def certify():
    out=[]
    for m in range(1,5):
        data=json.loads((ROOT/'out'/f'covers_m{m}.json').read_text())
        strict=equal=0;min_margin=None
        for row in data['objective_signatures']:
            lo,hi=signature_interval(row['log_signature'])
            margin=Fraction(12*row['influence_numerator'],5)-hi
            if margin==0:equal+=1
            else:
                assert margin>0
                strict+=1
                min_margin=margin if min_margin is None else min(min_margin,margin)
        out.append({'m':m,'bound':'H/I<=12/5 for nonconstant pure two-address product-slice functions','objective_signatures':len(data['objective_signatures']),'strict_signatures':strict,'equality_signatures':equal,'smallest_strict_margin_lower_rounded_1e12':None if min_margin is None else str(Fraction(min_margin*10**12//1,10**12)),'witness_signature':data['best']['signature'],'witness_influence_numerator':data['best']['influence_numerator']})
    (ROOT/'out'/'pure_exact_certificate.json').write_text(json.dumps({'status':'PASS','arithmetic':'rational atanh logarithm intervals,32 terms, remainder proved','results':out},indent=2))
    print(json.dumps(out))
if __name__=='__main__':certify()
