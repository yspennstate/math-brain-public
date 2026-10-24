"""Exact all-label comb pilot and independent tensor guard; frozen v1 domain."""
from fractions import Fraction as Q
from collections import defaultdict
import itertools,json,time,pathlib
START=time.perf_counter(); COUNT=0
ROOT=pathlib.Path(__file__).resolve().parents[1]
def ck(p):
    global COUNT
    COUNT+=1
    assert p
def fwht(vals):
    a=list(vals); step=1
    while step<len(a):
        for b in range(0,len(a),2*step):
            for i in range(b,b+step):
                u,v=a[i],a[i+step];a[i],a[i+step]=u+v,u-v
        step*=2
    return a
def stop(x,a):
    for j in range(a):
        if not (x>>j)&1:return j
    return a
def suffix(sig):
    a=len(sig)-1; m=[Q(0)]*(a+1);m[a]=Q(sig[a]);r=[Q(0)]*a
    for j in range(a-1,-1,-1):
        r[j]=(1-sig[j]*m[j+1])/2;m[j]=(sig[j]+m[j+1])/2
    return m,r
def formula(sig):
    a=len(sig)-1;m,r=suffix(sig);p=(1+m[0])/2;q=1-p
    # Data labels are y1,y2; signed Fourier coefficients reconstructed.
    coeff={}
    if p:coeff[1<<a]=p
    if q:coeff[1<<(a+1)]=q
    for t in range(1,1<<a):
        j=t.bit_length()-1
        b=Q(sig[j],1<<(j+1))*r[j]*(-1)**(t.bit_count()-1)
        if b: coeff[t|(1<<a)]=b;coeff[t|(1<<(a+1))]=-b
    return coeff,p,q,r
def check_one(sig):
    a=len(sig)-1;n=a+2;coeff,p,q,r=formula(sig)
    vals=[]
    for x in range(1<<n):
        lab=0 if sig[stop(x,a)]==1 else 1
        vals.append(1-2*((x>>(a+lab))&1))
    walsh=fwht(vals)
    ck(coeff=={s:Q(z,len(vals)) for s,z in enumerate(walsh) if z})
    spectrum={s:z*z for s,z in coeff.items()};ck(sum(spectrum.values())==1)
    vs=[Q(1,1<<(j+1))*rr*rr for j,rr in enumerate(r)]
    J=sum(Q(1,1<<(j+1))*rr for j,rr in enumerate(r))
    ck(p*p+q*q+sum(vs)==1);ck(sum(vs)==2*p*q)
    ck(sum((j+2)*v for j,v in enumerate(vs))==2*J)
    ck(sum(z*(s&((1<<a)-1)).bit_count() for s,z in spectrum.items())==J)
    ck(sum(z*(s>>a).bit_count() for s,z in spectrum.items())==1)
    influence=Q(sum(vals[x]!=vals[x^(1<<j)] for x in range(1<<n) for j in range(n)),1<<n)
    ck(influence==1+J)
    hist=defaultdict(Q)
    for s,z in spectrum.items():
        t=s&((1<<a)-1)
        if t:
            j=t.bit_length()-1;hist[j]+=z
            ck(z==Q(1,1<<(2*(j+1)))*r[j]*r[j])
    ck(dict(hist)=={j:v for j,v in enumerate(vs) if v})
    # ceil(log2(1/z)), computed with integer powers only.
    lengths={}
    for s,z in spectrum.items():
        k=0
        while z*(1<<k)<1:k+=1
        lengths[s]=k
        ck(z*(1<<k)>=1)
        if k:ck(z*(1<<(k-1))<1)
    ck(sum(Q(1,1<<k) for k in lengths.values())<=1)
    physical_cost=sum(spectrum[s]*k for s,k in lengths.items())
    ck(physical_cost<=Q(41,8)*(1+J))
    ck(time.perf_counter()-START<60)
    return vals,spectrum,J

treecases=0; tensorcases=0
cache={}; minratio=None; low_boundary=[]
for a in range(1,9):
    for sig in itertools.product((-1,1),repeat=a+1):
        vals,sp,J=check_one(sig);treecases+=1
        if a<=3:cache[(a,sig)]=(vals,sp,J)
        if sig==tuple([1]*a+[-1]):
            low_boundary.append({'a':a,'I_selector':str(J),'expected_depth':str(2*(1-Q(1,1<<a))),'raw_witness_cost':str(4*(1-Q(1,1<<a)))})

for bits in range(16):
    seed=[1-2*((bits>>x)&1) for x in range(4)]
    sw=fwht(seed);seedsp={s:Q(z*z,16) for s,z in enumerate(sw) if z}
    seedI=sum(s.bit_count()*v for s,v in seedsp.items())
    for (a,sig),(vals,sp,J) in cache.items():
        total=[v*h for h in seed for v in vals]
        w=fwht(total);n=a+2
        got={s:Q(z*z,len(total)**2) for s,z in enumerate(w) if z}
        want={s|(t<<n):p*q for s,p in sp.items() for t,q in seedsp.items()}
        ck(got==want)
        ck(sum(s.bit_count()*v for s,v in got.items())==1+J+seedI)
        # Pushforward complete subprobability seed reference = seed spectrum/2.
        reference={s:p/2 for s,p in want.items()}
        ck(sum(reference.values())==Q(1,2))
        ck(all(reference[s]==sp[s&((1<<n)-1)]*seedsp[s>>n]/2 for s in reference))
        tensorcases+=1
        ck(time.perf_counter()-START<60)

# Exact structural all-a recurrence instances, with no truth-table escalation.
for a in range(1,65):
    sig=tuple([1]*a+[-1]);m,r=suffix(sig);p=(1+m[0])/2;q=1-p
    ck(q==Q(1,1<<a));ck(all(r[j]==Q(1,1<<(a-j-1)) for j in range(a)))
    J=sum(Q(1,1<<(j+1))*rr for j,rr in enumerate(r));ck(J==Q(a,1<<a))
    vs=[Q(1,1<<(j+1))*rr*rr for j,rr in enumerate(r)]
    ck(sum(vs)==2*p*q);ck(sum((j+2)*v for j,v in enumerate(vs))==2*J)

# Rational log intervals: range reduction to [1,2], atanh expansion, outward remainder.
def ln_series(z,terms=48):
    # Only 1<=z<=2; 0<=t<=1/3.
    t=(z-1)/(z+1);t2=t*t; power=t; lo=Q(0)
    for k in range(terms):lo+=2*power/(2*k+1);power*=t2
    return lo,lo+2*power/((2*terms+1)*(1-t2))
LN2=ln_series(Q(2))
def log2_interval(z):
    if z==1:return Q(0),Q(0)
    k=0
    while z<1:z*=2;k-=1
    while z>=2:z/=2;k+=1
    lo,hi=ln_series(z)
    return Q(k)+lo/LN2[1],Q(k)+hi/LN2[0]
def entropy_interval(sp):
    lo=hi=Q(0)
    for z in sp.values():
        a,b=log2_interval(1/z);lo+=z*a;hi+=z*b
    return lo,hi
certificates=[]
fixtures=[(2,(1,1,-1)),(3,(1,1,1,-1)),(8,tuple([1]*8+[-1])),(8,tuple(1 if j%2==0 else -1 for j in range(9))),(8,tuple([1]*9))]
for a,sig in fixtures:
    coeff,p,q,r=formula(sig);sp={s:c*c for s,c in coeff.items()};J=sum(Q(1,1<<(j+1))*rr for j,rr in enumerate(r))
    lo,hi=entropy_interval(sp);ck(hi<=Q(41,8)*J)
    certificates.append({'a':a,'signs':list(sig),'I_selector':str(J),'H_lower':str(lo),'H_upper':str(hi),'bound_41_over_8_I_selector':str(Q(41,8)*J),'margin_lower':str(Q(41,8)*J-hi)})
result={'helper_version':'a011-comb-output-v1','comb_cases':treecases,'tensor_cases':tensorcases,'recurrence_cases':64,'exact_assertions':COUNT,'runtime_seconds':time.perf_counter()-START,'low_boundary_combs':low_boundary,'certificate_count':len(certificates),'arithmetic':'integer FWHT, Fraction, outward rational atanh intervals'}
ck(treecases==1020);ck(tensorcases==448)
result['exact_assertions']=COUNT
(ROOT/'out'/'EXACT_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
(ROOT/'out'/'LOG_CERTIFICATES.json').write_text(json.dumps({'method':'48-term atanh series after power-of-two reduction; explicit positive-tail bound; positive denominator interval','certificates':certificates},indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='low_boundary_combs'},indent=2))
