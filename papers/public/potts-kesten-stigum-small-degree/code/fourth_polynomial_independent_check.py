"""Independent exact probability and point-evaluation checks; imports no builder."""
import itertools,json,pathlib,math,hashlib
from fractions import Fraction as F
ROOT=pathlib.Path(__file__).resolve().parent
def load(phase):
    data=json.loads((ROOT/f'fourth_poly_{phase}.json').read_text(encoding='utf-8'));poly={tuple(k):v for k,v in data.pop('poly')};return poly,data
def peval(poly,point,deg):
    tables=[];den=1
    for x,n in zip(point,deg):
        a,b=x.numerator,x.denominator;den*=b**n
        tables.append([a**k*b**(n-k) for k in range(n+1)])
    return F(sum(v*math.prod(tables[i][k] for i,k in enumerate(key)) for key,v in poly.items()),den)
def beval(poly,point,deg):
    tables=[];den=1
    for x,n in zip(point,deg):
        a,b=x.numerator,x.denominator;den*=b**n
        tables.append([math.comb(n,k)*a**k*(b-a)**(n-k) for k in range(n+1)])
    return F(sum(v*math.prod(tables[i][k] for i,k in enumerate(key)) for key,v in poly.items()),den)
def vector(t,y):return [(1-t)/3,(1-t)/3+t*y/2,(1-t)/3+t*(1-y/2)]
def direct(point):
    t,s,y,z=point;lam=F(99,140);p=vector(t,y);r=vector(s,z)
    mp=9*lam*lam*sum((v-F(1,3))**2 for v in p);mr=9*lam*lam*sum((v-F(1,3))**2 for v in r)
    output=F(0);D=F(1)
    for rr in itertools.permutations(r):
        prod=[(1-lam+3*lam*p[i])*(1-lam+3*lam*rr[i]) for i in range(3)];S=sum(prod)
        post=[v/S for v in prod];norm=sum((v-F(1,3))**2 for v in post)
        output+=(9*lam*lam)**2*norm*norm*S/F(18)
        D*=(S*4*140**2)**3
    rhs=lam**4*(mp*mp+mr*mr)+F(3,2)*mp*mr
    return rhs-output,D
def main():
    raw,meta=load('raw');bern,bmeta=load('bern4');deg=meta['degrees']
    assert bmeta['status'].startswith('PASS') and len(bern)==math.prod(d+1 for d in deg) and min(bern.values())>=0
    origin=(F(0),)*4;raw0=peval(raw,origin,deg);bern0=beval(bern,origin,deg);scale=bern0/raw0;assert scale>0
    samples=[(F(1,2),)*4,(F(1),F(1),F(0),F(0)),(F(1),F(1),F(1),F(1)),(F(1,4),F(3,4),F(1,2),F(1,4)),(F(3,4),F(1,4),F(1),F(0))]
    rows=[]
    for point in samples:
        value=peval(raw,point,deg);assert beval(bern,point,deg)==scale*value
        gap,D=direct(point)
        restored=value*int(meta['content_divided_out'])*point[0]**2*point[1]**2/(32*140**8*D)
        assert restored==gap and gap>0
        rows.append({'point':[str(x) for x in point],'exact_gap':str(gap)})
    for point in itertools.product([F(0),F(1)],repeat=4):assert beval(bern,point,deg)==scale*peval(raw,point,deg)
    C=F(3001,1000);gamma=F(177,250);t=F(91,400);radius=F(23,2000)
    kappa=2*F(99,140)**4;actual_C=F(3,2)/(1-kappa)
    assert actual_C<C and C/6<gamma*gamma and F(9,2)*radius<t*t
    error=F(2,27)*gamma*t+C/F(27)*t*t+2*C*gamma/F(81)*t**3+C*C/F(486)*t**4
    assert error<F(1,54)
    canonical=F(57830850920489,5066549580791808);assert canonical<radius
    report={'status':'PASS','scope':'five independent exact Bayesian pair evaluations, raw/Bernstein polynomial equality there and at all 16 corners, final all-coefficient integer sign check, exact local-entry constants','degrees':deg,'bernstein_coefficients':len(bern),'all_nonnegative':True,'minimum_scaled_integer_coefficient':str(min(bern.values())),'samples':rows,'kappa':str(kappa),'actual_fixedpoint_C':str(actual_C),'C_upper':str(C),'gamma_upper':str(gamma),'radius':str(radius),'error_at_radius':str(error),'allowed_error':str(F(1,54)),'canonical_tail_upper':str(canonical),'audit':'independent human/model mathematical audit still required'}
    report['sha256']={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in ['fourth_polynomial_certificate.py','fourth_poly_raw.json','fourth_poly_bern4.json','fourth_polynomial_independent_check.py']}
    pathlib.Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2),encoding='utf-8');print(json.dumps({k:v for k,v in report.items() if k not in ['samples','sha256','minimum_scaled_integer_coefficient']}),flush=True)
if __name__=='__main__':main()
