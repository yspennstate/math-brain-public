"""Independent Bayesian restoration and exact transform checks of the new gap."""
import gc,hashlib,itertools,json,math,pathlib,time
from fractions import Fraction as F
from ternary_moment_independent_check import evaluate,verify_axis,sorted_posterior
ROOT=pathlib.Path(__file__).resolve().parent

def load(phase):
    data=json.loads(ROOT.joinpath(f'cubic_invariant_full_{phase}.json').read_text(encoding='utf-8'))
    return {tuple(k):v for k,v in data.pop('poly')},data

def direct(point):
    p=sorted_posterior(point[0],point[2]);r=sorted_posterior(point[1],point[3])
    a=[3*v-1 for v in p];b=[3*v-1 for v in r]
    m=sum(v*v for v in a);n=sum(v*v for v in b);t=sum(v**3 for v in a);h=sum(v**3 for v in b)
    output=weight=F(0);D=F(1);B=140
    for rr in itertools.permutations(r):
        products=[9*p[i]*rr[i] for i in range(3)];S=sum(products)
        D*=(4*B*B*S)**2
        if not S:continue
        posterior=[v/S for v in products];w=S/18
        output+=w*sum((3*v-1)**3 for v in posterior);weight+=w
    assert weight==1
    gap=output-(1-n/6)*t-(1-m/6)*h
    return gap,576*B**5*D,m,n

def main():
    start=time.monotonic();raw,meta=load('raw');deg=meta['degrees'];previous=raw
    for number,axis in enumerate((2,3,0,1),1):
        current,bmeta=load(f'bern{number}');verify_axis(previous,current,axis,deg[axis])
        previous=current;gc.collect()
    bern=current;assert bmeta['status'].startswith('PASS') and min(bern.values())>0
    tensor_size=math.prod(n+1 for n in deg);assert len(bern)<=tensor_size
    origin=(F(0),)*4;factor=evaluate(bern,origin,deg,True)/evaluate(raw,origin,deg);assert factor>0
    points=[(F(1,2),)*4,(F(1,4),F(3,4),F(1,2),F(1,4)),
            (F(3,4),F(1,4),F(1),F(0)),(F(1),F(1,2),F(0),F(3,4)),
            (F(1,2),F(1),F(3,4),F(0)),(F(1),F(2887,5000),F(1,9),F(0))]
    L=F(meta['raw_domain_t_upper']);R=F(meta['raw_domain_s_upper']);lam=F(99,140)
    multiplier=L.denominator**deg[0]*R.denominator**deg[1]
    rows=[];control=None
    for normalized in points:
        value=evaluate(raw,normalized,deg);assert evaluate(bern,normalized,deg,True)==factor*value
        original=(L*normalized[0],R*normalized[1],normalized[2],normalized[3])
        # Domain scaling cancels the artificial common eigenvalue exactly.
        actual=(lam*original[0],lam*original[1],original[2],original[3])
        gap,denominator,m,n=direct(actual);assert gap>=0 and denominator>0
        restored=value*int(meta['raw_gcd_divided_out'])/multiplier*original[0]**2*original[1]**2
        assert restored==gap*denominator
        rows.append({'point':list(map(str,normalized)),'gap':str(gap)})
        if normalized==points[-1]:
            control=gap-m*n/6;assert control<0
    for corner in itertools.product((F(0),F(1)),repeat=4):
        assert evaluate(bern,corner,deg,True)==factor*evaluate(raw,corner,deg)
        gap,_,_,_=direct(corner);assert gap>=0
    report={'status':'PASS independent exact arithmetic; external mathematical audit pending',
            'degrees':deg,'full_tensor_size':tensor_size,'strictly_positive_coefficients':len(bern),
            'implicit_zero_coefficients':tensor_size-len(bern),'negative_coefficients':0,
            'scope':'every axis conversion, six direct Bayesian gap restorations, all 16 corners, counterexample to the stronger +M_left*M_right/6 version',
            'samples':rows,'stronger_false_gap':str(control),'raw_bernstein_positive_scale':str(factor),
            'wall_seconds':time.monotonic()-start,
            'sha256':{name:hashlib.sha256(ROOT.joinpath(name).read_bytes()).hexdigest() for name in ['cubic_invariant_certificate.py','cubic_invariant_full_raw.json','cubic_invariant_full_bern4.json','cubic_invariant_independent_check.py']}}
    ROOT.joinpath('cubic_invariant_independent_check.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ['samples','sha256','raw_bernstein_positive_scale']}),flush=True)

if __name__=='__main__':main()
