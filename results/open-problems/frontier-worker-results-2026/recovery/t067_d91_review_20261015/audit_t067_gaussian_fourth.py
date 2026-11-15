"""Own full signed-grid Arb integral of Q, with complete tails and checkpoints."""
from pathlib import Path
from datetime import datetime
from fractions import Fraction as F
import argparse,json,hashlib,time
from flint import arb,ctx
HERE=Path(__file__).resolve().parent;OUT=HERE/'t067_gaussian_fourth_own';OUT.mkdir(exist_ok=True)
ap=argparse.ArgumentParser();ap.add_argument('--index',type=int,default=42)
ap.add_argument('--all',action='store_true');ap.add_argument('--seconds',type=int,default=240)
args=ap.parse_args();assert 0<=args.index<=85
ctx.prec=180
source=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
derivative=json.loads((HERE/'T067_FOURTH_DERIVATIVES_LEAD_RECEIPT.json').read_text(encoding='utf-8'))
assert derivative['status'].startswith('PASS')
def A(q):
    q=F(q);return arb(q.numerator)/q.denominator
def upper(q):
    m,e=q.upper().man_exp();m=int(m);e=int(e)
    return F(m*(1<<e)) if e>=0 else F(m,1<<(-e))
def lower(q):return -upper(-q)
def save(p,d):
    tmp=p.with_suffix('.part');tmp.write_bytes((json.dumps(d,indent=2)+'\n').encode('utf-8'));tmp.replace(p)
norm=(2*arb.pi()).sqrt();sqrt2=arb(2).sqrt()
def phi(z):return (-z*z/2).exp()/norm
bins=[]
for j in range(-96,96):
    a,b=A(F(j,16)),A(F(j+1,16))
    weight=((b/sqrt2).erf()-(a/sqrt2).erf())/2
    first=phi(a)-phi(b);second=weight+a*phi(a)-b*phi(b)
    mean=first/weight;variance=second-first*first/weight
    assert weight>0 and variance>0 and a<mean and mean<b
    bins.append((weight,mean,variance))
P=sum((w for w,_,_ in bins),arb(0));D=sum((v for _,_,v in bins),arb(0))
assert 0<P and P<1 and D>0
started=time.monotonic();completed=0
for index in (range(86) if args.all else [args.index]):
    point=F(10,100-index);dest=OUT/f'endpoint_{index:03d}.json'
    if dest.exists():
        old=json.loads(dest.read_text(encoding='utf-8'))
        assert old['source_sha256']==source and old['s']==str(point)
        continue
    begin=time.monotonic();signal=A(point)
    alpha=3*(3*signal).sqrt()/2;beta=3*signal.sqrt()/2
    coshes=[(beta*m).cosh() for _,m,_ in bins]
    cc=[2*c*c-1 for c in coshes]
    total=arb(0)
    for wi,mi,_ in bins:
        ratio=(-9*signal/2-alpha*mi).exp();ratio2=ratio*ratio
        row=arb(0)
        for (wj,_,_),c,c2 in zip(bins,coshes,cc):
            denominator=1+2*ratio*c
            square_sum=(1+2*ratio2*c2)/(denominator*denominator)
            radial=9*square_sum-3
            row+=wj*radial*radial
        total+=wi*row
    # The Gaussian logit map has squared operator norm9s/2.
    # Global Hessian(Q)<=20 gives Hessian_z(Q)<=90s.
    error=90*signal*P*D
    lo=lower(total-error);hi=upper(total+error+36*(1-P*P))
    assert lo<hi and hi>0 and lo<36
    record={'s':str(point),'UG_lower':str(lo),'UG_upper':str(hi),
            'raw_lower':str(lower(total)),'raw_upper':str(upper(total)),
            'bin_error_upper':str(upper(error)),
            'whole_tail_upper':str(upper(36*(1-P*P))),
            'source_sha256':source,'precision':180,'full_signed_bins':192,
            'seconds':time.monotonic()-begin,'at':datetime.now().astimezone().isoformat()}
    save(dest,record);completed+=1
    print(json.dumps({'index':index,'seconds':record['seconds'],'UG_upper':float(hi)}),flush=True)
    if time.monotonic()-started>args.seconds:break
files=sorted(OUT.glob('endpoint_*.json'));rows=[]
for path in files:
    row=json.loads(path.read_text(encoding='utf-8'));assert row['source_sha256']==source
    rows.append(row)
summary={'at':datetime.now().astimezone().isoformat(),'completed':len(rows),'expected':86,
         'new_this_run':completed,'source_sha256':source,
         'source_files':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
         'status':'PASS all86 own full-integral upper/lower enclosures' if len(rows)==86 else 'PILOT/PARTIAL only; no complete gate',
         'derivative_receipt_sha256':hashlib.sha256((HERE/'T067_FOURTH_DERIVATIVES_LEAD_RECEIPT.json').read_bytes()).hexdigest(),
         'scope':'Gaussian fourth moment only, full conditional-mean quadrature and entire tail. No BP composition or frontier admission.',
         'seconds':time.monotonic()-started}
save(HERE/'T067_GAUSSIAN_FOURTH_OWN_SUMMARY.json',summary)
print(json.dumps({k:summary[k] for k in ['status','completed','new_this_run','seconds']}),flush=True)
