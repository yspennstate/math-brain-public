"""A068 stage 2: independent cyclic replay and edit-reference certificates."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter,defaultdict
from math import comb
from functools import lru_cache
import json,hashlib,time,argparse
ROOT=Path(__file__).resolve().parents[1]
checks=0
def check(ok):
    global checks
    checks+=1
    if not ok:
        raise AssertionError(checks)
def transform(vals):
    a=list(vals)
    size=2
    while size<=len(a):
        half=size//2
        for base in range(0,len(a),size):
            for k in range(half):
                l,r=a[base+k],a[base+k+half]
                a[base+k],a[base+k+half]=l+r,l-r
        size*=2
    return a
def gf2rank(rows):
    rows=list(rows)
    r=0
    for col in range(len(rows)):
        pivot=next((j for j in range(r,len(rows)) if rows[j] >> col & 1),None)
        if pivot is None:
            continue
        rows[r],rows[pivot]=rows[pivot],rows[r]
        for j in range(len(rows)):
            if j!=r and rows[j] >> col & 1:
                rows[j]^=rows[r]
        r+=1
    return r
def sign_character(mask,v): return -1 if (mask & v).bit_count()%2 else 1
def ln_mantissa(y,terms=22):
    # 1 <= y <= 2, so |t| <= 1/3.
    t=(y-1)/(y+1)
    total=sum((2*t**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    rem=2*t**(2*terms+1)/(F(2*terms+1)*(1-t*t))
    return total,total+rem
LN2=ln_mantissa(F(2))
@lru_cache(maxsize=None)
def log2_interval(y):
    check(y>=1)
    if y==1:
        return F(0),F(0)
    power=0
    while y>=2:
        y/=2
        power+=1
    lo,hi=ln_mantissa(y)
    lower,upper=power+lo/LN2[1],power+hi/LN2[0]
    # Outward rounding to a common dyadic denominator avoids enormous
    # denominators when thousands of certified logarithms are added.
    scale=1 << 64
    return F(lower.numerator*scale//lower.denominator,scale),F(-((-upper.numerator*scale)//upper.denominator),scale)
def interval_sum_hist(hist,den):
    lo=hi=F(0)
    for sq,count in hist.items():
        if sq:
            l,u=log2_interval(F(den,sq))
            weight=F(sq*count,den)
            lo+=weight*l
            hi+=weight*u
    return lo,hi
def lower_decimal(v): return str(F(v.numerator*10**12//v.denominator,10**12))
def upper_decimal(v): return str(F(-((-v.numerator*10**12)//v.denominator),10**12))
def entropy_bounds(hist,den):
    lo,hi=interval_sum_hist(hist,den)
    return {'lower':lower_decimal(lo),'upper':upper_decimal(hi)},(lo,hi)
def build(q):
    h=[1 if q-2*x.bit_count()>0 else -1 for x in range(1 << q)]
    bh=transform(h)
    truth=[]
    for z in range(1 << q):
        orientation=sum(((z >> i & 1)*(z >> ((i+1)%q) & 1)) << i for i in range(q))
        truth.extend(h[x ^ orientation] for x in range(1 << q))
    raw=transform(truth)
    D=1 << (2*q)
    actual_edges=[sum(truth[v]!=truth[v ^ (1 << i)] for v in range(D)) for i in range(2*q)]
    c=F(comb(q-1,(q-1)//2),1 << (q-1))
    for i in range(2*q):
        check(F(actual_edges[i],D)==(c if i<q else F(3,4)*c))
        check(sum(a*a for t,a in enumerate(raw) if t >> i & 1)==actual_edges[i]*D)
    weights={s:F(1) for s in range(1 << q)}
    normalizers=defaultdict(F)
    levelmass=defaultdict(F)
    for s in weights:
        for i in range(q):
            if s >> i & 1:
                weights[s]/=(i+1)**2
        k=s.bit_count()
        normalizers[k]+=weights[s]
        levelmass[k]+=F(bh[s]**2,1 << (2*q))
    ref=[F(0)]*D
    expected=[0]*D
    ranks=[]
    for s in range(1 << q):
        edges=[(i,(i+1)%q) for i in range(q) if s >> i & 1]
        polar=[0]*q
        for i,j in edges:
            polar[i]^=1 << j
            polar[j]^=1 << i
        r=gf2rank(polar)
        ranks.append(r)
        phase=[(-1)**sum((z >> i & 1)*(z >> j & 1) for i,j in edges) for z in range(1 << q)]
        ar=transform(phase)
        support=[t for t,a in enumerate(ar) if a]
        check(len(support)==1 << r)
        check(all(ar[t]**2==1 << (2*q-r) for t in support))
        mass=levelmass[s.bit_count()]*weights[s]/normalizers[s.bit_count()]
        for t,a in enumerate(ar):
            full=s | (t << q)
            expected[full]=bh[s]*a
            if a:
                ref[full]=mass/(1 << r)
    check(raw==expected)
    check(sum(ref)==1)
    check(all(ref[t]>0 for t,a in enumerate(raw) if a))
    check(sum(a*a for a in raw)==D*D)
    return truth,raw,ref,c,ranks
def edited(q,d,x,z,data,verify_fwht=False):
    truth,raw,ref,c,ranks=data
    D0=len(raw)
    N=2*q+d
    D=1 << N
    delta=F(1,D)
    edit=x | (z << q)
    f0=truth[edit]
    updated=[a*(1 << d)-2*f0*sign_character(t,edit) for t,a in enumerate(raw)]
    if verify_fwht:
        actual=list(truth)
        actual[edit]*=-1
        check(transform(actual)==updated)
    check(sum(a*a for a in updated)+4*(D-D0)==D*D)
    influences=[]
    for i in range(N):
        original=c if i<q else F(3,4)*c if i<2*q else F(0)
        disagree=i<2*q and truth[edit]!=truth[edit ^ (1 << i)]
        physical=original+2*delta*(1-2*disagree)
        if i<2*q:
            spectral=F(sum(a*a for t,a in enumerate(updated) if t >> i & 1)+2*(D-D0),D*D)
        else:
            spectral=F(2,D)
        check(physical==spectral)
        influences.append(physical)
    Ix=sum(influences[:q],F(0))
    Iz=sum(influences[q:],F(0))
    hist=Counter(a*a for a in updated)
    hist[4]+=D-D0
    hbox,hinterval=entropy_bounds(hist,D*D)
    # Q_delta=(1-delta)*rank-reference+delta*uniform, fully normalized.
    unique=set(ref)
    costs={r:log2_interval(1/((1-delta)*r+delta/D)) for r in unique}
    grouped=defaultdict(int)
    for a,r in zip(updated,ref):
        grouped[r]+=a*a
    grouped[F(0)]+=4*(D-D0)
    lower=upper=F(0)
    for r,sqmass in grouped.items():
        lo,hi=costs[r]
        lower+=F(sqmass,D*D)*lo
        upper+=F(sqmass,D*D)*hi
    check(sum(((1-delta)*r+delta/D for r in ref),F(0))+(D-D0)*delta/D==1)
    check(hinterval[1]<=lower) # Certifies Gibbs independently with outward intervals.
    # C_reg>8 by (4+e)e^2 pi^2>6*7*9>256.
    target=8*Ix+2*Iz
    check(target-upper>0)
    check(target-hinterval[1]>0)
    zeros=sum(a==0 for a in raw)
    full_support=all(a for a in updated) # Outside this original slice all coefficients are +/-2.
    check(full_support)
    return {'q':q,'padding':d,'N':N,'x0':x,'z0':z,'I_x':str(Ix),'I_z_including_padding':str(Iz),
            'entropy_bits':hbox,'full_reference_cost_bits':{'lower':lower_decimal(lower),'upper':upper_decimal(upper)},
            'margin_to_8Ix_plus_2Iz_lower':lower_decimal(target-upper),
            'entropy_margin_to_8Ix_plus_2Iz_lower':lower_decimal(target-hinterval[1]),
            'original_zero_coefficients':zeros,'edited_spectrum_full_support':full_support,
            'edited_squared_coefficient_histogram':{str(k):v for k,v in sorted(hist.items())}}
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--pilot',action='store_true')
    args=ap.parse_args()
    start=time.perf_counter()
    rows=[]
    base=[]
    for q in ([5] if args.pilot else [5,7]):
        data=build(q)
        truth,raw,ref,c,ranks=data
        base.append({'q':q,'I_x':str(q*c),'I_z':str(F(3,4)*q*c),
                     'polar_ranks':ranks,'raw_walsh_sha256':hashlib.sha256(json.dumps(raw).encode()).hexdigest(),
                     'zero_coefficients':sum(a==0 for a in raw)})
        xs=[0,(1 << q)-1,1,(1 << (q//2))-1]
        zs=[0,(1 << q)-1,1,sum(1 << i for i in range(0,q,2))]
        for d in ([0] if args.pilot else [0,2,4]):
            for x in xs:
                for z in zs:
                    if args.pilot and len(rows)>=2:
                        break
                    rows.append(edited(q,d,x,z,data,verify_fwht=d==0))
                    if time.perf_counter()-start>170:
                        raise TimeoutError('frozen 180-second cap')
                if args.pilot and len(rows)>=2:
                    break
    # Exact constants in the analytic paid-mixture estimate.
    a,b,costcross,loss=F(1,640),F(1,24),F(5,4),F(11,192)
    check(4*b*(9+a)<=costcross**2)
    check(F(3,2)-a-b-costcross-loss==F(287,1920))
    result={'helper_version':2,'pilot':args.pilot,'status':'PASS','base_cases':base,'edit_case_count':len(rows),
            'assertions':checks,'arithmetic':'integer Walsh, F2 rank, exact Fraction influence and reference; outward rational log intervals',
            'log_series_terms':22,'outward_dyadic_bits':64,'cases':rows,'runtime_seconds':time.perf_counter()-start,
            'analytic_slack_coefficient':str(F(287,1920)),'independent_reviewer':False}
    name='pilot_v2.json' if args.pilot else 'validation.json'
    (ROOT/'out'/name).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['cases','base_cases']},indent=2))
if __name__=='__main__': main()
