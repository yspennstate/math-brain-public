import exact as x
import json,sys,time,itertools,hashlib
from fractions import Fraction as Q
from pathlib import Path
run=Path(__file__).resolve().parents[1]
pilot='--pilot' in sys.argv
children=[(1,)*8]+[tuple(-1 if j==k else 1 for j in range(8)) for k in range(8)]
controllers=[]
for n in range(3):
    controllers += [a for a in itertools.product((-1,1),repeat=1<<n) if x.neg(a)<=Q(1,2)]
controllers.append((-1,)+(1,)*7)
if pilot: controllers=[(-1,1)]
def selector(g,h): return tuple(g[j//2] if j%2==0 else h[j//2] for j in range(2*len(g)))
def band(d): return d<=Q(1,2) and 1-8*d+8*d*d>=0
cases=0
def test(g,h,a):
    global cases
    u=selector(g,h); f=x.identity(u,a); fg=x.identity(g,a); fh=x.identity(h,a)
    p=x.neg(a); d=x.neg(u); d0=x.neg(g); d1=x.neg(h)
    eps=Q(sum(z!=t for z,t in zip(g,h)),len(g))
    x.check(x.inf(f,0)==p*eps,'physical selector influence')
    x.check(x.I(f)-(x.I(fg)+x.I(fh))/2==p*eps,'retained terminal influence')
    actual=x.add((1,x.H(f)),(Q(-1,2),x.H(fg)),(Q(-1,2),x.H(fh)),(-p,x.H(u)),(p/2,x.H(g)),(p/2,x.H(h)))
    error=x.add((1,x.R(p,d)),(Q(-1,2),x.R(p,d0)),(Q(-1,2),x.R(p,d1)))
    x.check(actual==error,'actual signed entropy cancellation')
    if band(d0) and band(d1):
        x.check(x.bounds(error)[1]<=0,'certified nonpositive activation correction')
    cases+=1
    return error
for g,h in itertools.product(children,repeat=2):
    for a in controllers: test(g,h,a)
fixed=[]
if not pilot:
    for size,k0,k1,label in [(64,8,9,'near-boundary safe'),(16,3,4,'quarter-band refutation')]:
        g=tuple(-1 if j<k0 else 1 for j in range(size)); h=tuple(-1 if j<k1 else 1 for j in range(size))
        error=test(g,h,(-1,1)); lo,hi=x.bounds(error)
        x.check(hi<0 if label.startswith('near') else lo>0,label+' strict certificate')
        fixed.append({'label':label,'child_biases':[str(x.neg(g)),str(x.neg(h))],'controller_p':'1/2','signed_prime_log':{str(k):str(v) for k,v in error.items()},'interval':[str(lo),str(hi)],'physical_dimensions':(2*size).bit_length()})
    def log(q): return x.add((1,x.factor(q.numerator)),(-1,x.factor(q.denominator)))
    bterms={}
    for p in [Q(1,2),Q(1,4),Q(1,8),Q(1,3),Q(2,5)]:
        for d in [Q(k,64) for k in range(1,10)]:
            v=4*p*(1-p)
            # Coefficients of b=1/ln2 independently cancel before log comparison.
            x.check(-6*v-24*p*p+24*p==0,'exact curvature ln2 reciprocal cancellation')
            raw=x.add((-8,x.eta(p*p)),(-4*v,{2:Q(1)}),(-4*v,log(d)),(-16*p*p,log(1-2*p*d)),(16*p,log(1-2*d)))
            formula=x.add((16*p,log(1-2*d)),(-16*p*(1-p),log(2*d)),(-16*p*p,log(1-2*p*d)),(16*p*p,log(p)))
            x.check(raw==formula,'independent exact curvature formula')
            x.check(x.bounds(formula)[0]>0,'certified positive curvature rational grid')
result={'status':'PASS','cases':cases,'exhaustive_cases':81*len(controllers),'controllers':len(controllers),'assertions':sum(x.counts.values()),'counts':x.counts,'elapsed_seconds':time.monotonic()-x.START,'fixed_certificates':fixed,'helper_sha256':hashlib.sha256((run/'code'/'exact.py').read_bytes()).hexdigest()}
(run/'out'/('pilot.json' if pilot else 'validation.json')).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ('fixed_certificates','counts')}))
