"""A035 v1. Integer Walsh spectra and rational logarithm enclosures."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
import json,time,sys,hashlib,math
ROOT=Path(__file__).resolve().parents[1]
PILOT='--pilot' in sys.argv
LIMIT=8 if PILOT else 16
START=time.perf_counter()
def fwht(a):
    a=list(a);h=1
    while h<len(a):
        for b in range(0,len(a),2*h):
            for j in range(b,b+h):
                x,y=a[j],a[j+h];a[j],a[j+h]=x+y,x-y
        h*=2
    return a
def ln_unit(q,terms=24):
    z=(q-1)/(q+1);v=z;s=F(0)
    for j in range(terms):s+=v/F(2*j+1);v*=z*z
    lo=2*s;err=2*v/F(2*terms+1)/(1-z*z)
    return lo,lo+err
L2=ln_unit(F(2))
@lru_cache(None)
def log2_int(w):
    k=w.bit_length()-1;q=F(w,1<<k)
    if q==1:return F(k),F(k)
    a,b=ln_unit(q)
    return F(k)+a/L2[1],F(k)+b/L2[0]
def dec_interval(pair,places=12):
    scale=10**places;lo,hi=pair
    l=lo.numerator*scale//lo.denominator
    u=-((-hi.numerator*scale)//hi.denominator)
    return [str(F(l,scale)),str(F(u,scale))]
def certify(hist,n,influence):
    D=1<<(2*n);assert sum(w*c for w,c in hist.items())==D
    Hlo=Hhi=F(0)
    for w,c in hist.items():
        if not w:continue
        l,u=log2_int(w);p=F(w*c,D)
        Hlo+=p*(2*n-u);Hhi+=p*(2*n-l)
    pmax=max(hist);l,u=log2_int(pmax)
    hinf=(2*n-u,2*n-l);gap=(Hlo-hinf[1],Hhi-hinf[0])
    if influence:
        ratios=[dec_interval((a/influence,b/influence)) for a,b in [(Hlo,Hhi),hinf,gap]]
    else:
        assert Hlo==Hhi==0;ratios=None
    return dict(histogram={str(w):c for w,c in sorted(hist.items())},I=str(influence),H=dec_interval((Hlo,Hhi)),Hinf=dec_interval(hinf),gap=dec_interval(gap),ratios_H_Hinf_gap=ratios,
                gap_le_4I=gap[1]<=4*influence,Hinf_le_2I=hinf[1]<=2*influence)
checks=0
def exact_table(n,fn):
    global checks
    N=1<<n;t=[fn(x) for x in range(N)];assert set(t)<= {-1,1}
    a=fwht(t);hist=Counter(x*x for x in a if x)
    I=F(sum(s.bit_count()*v*v for s,v in enumerate(a)),N*N)
    edges=sum(t[x]!=t[x^(1<<j)] for x in range(N) for j in range(n))
    assert I==F(edges,N);checks+=1
    # Fourier convolution via a separately executed inverse transform.
    recovered=fwht(a);assert recovered==[N*v for v in t]
    conv=fwht([v*v for v in recovered]);assert conv==[N**3]+[0]*(N-1);checks+=1
    return hist,I,a
records=[]
def save_record(family,parameters,n,hist,I):
    r=dict(family=family,parameters=parameters,n=n,**certify(hist,n,I));records.append(r)
    with (ROOT/'out'/('pilot_records.jsonl' if PILOT else 'payment_records.jsonl')).open('a',encoding='utf-8') as out:out.write(json.dumps(r)+'\n')
    return r
for n in range(1,LIMIT+1):
    N=1<<n;hist=Counter({(N-2)**2:1,4:N-1}) if n!=2 else Counter({4:4})
    if n==1:hist=Counter({4:1})
    hist.pop(0,None)
    actual,I,a=exact_table(n,lambda x: -1 if x==0 else 1)
    assert actual==hist and I==F(2*n,N);checks+=1
    base=save_record('point_defect',{'n':n},n,hist,I)
    for copies in range(2,17):
        records.append(dict(family='point_defect_tensor',parameters={'n':n,'copies':copies},n=n*copies,I=str(I*copies),base_record_index=len(records)-1,ratios_H_Hinf_gap=base['ratios_H_Hinf_gap'],gap_le_4I=base['gap_le_4I'],Hinf_le_2I=base['Hinf_le_2I'],certificate='H,Hinf,gap,I multiply by copies under disjoint tensor product'))
for n in range(1,LIMIT+1):
    h,I,a=exact_table(n,lambda x:1 if 2*x.bit_count()<=n else -1)
    save_record('majority_tie_positive',{'n':n},n,h,I)
for w in range(1,LIMIT+1):
    for m in range(1,LIMIT//w+1):
        n=w*m;mask=(1<<w)-1
        h,I,a=exact_table(n,lambda x:1 if any(((x>>(j*w))&mask)==mask for j in range(m)) else -1)
        q=F(1,1<<w);assert I==2*w*m*q*(1-q)**(m-1);checks+=1
        save_record('tribes',{'w':w,'m':m},n,h,I)
for k in range(2,LIMIT+1,2):
    for n in range(k,LIMIT+1):
        N=1<<n;b=N//(1<<(k//2))
        hist=Counter()
        hist[(b-2)**2]+=(1<<k)+(1<<(k//2));hist[(b-2)**2]//=2
        hist[(b+2)**2]+=((1<<k)-(1<<(k//2)))//2
        hist[4]+=N-(1<<k);hist=Counter({w:c for w,c in hist.items() if w and c})
        for r in range(k+1):
            I=F(k,2)+F(2*(n-2*r),N)
            if n<=8 or (n==LIMIT and k in [2,LIMIT] and r in [0,k]):
                point=(1<<r)-1
                def f(x):
                    sign=(-1)**sum(((x>>(2*j))&3)==3 for j in range(k//2))
                    return -sign if x==point else sign
                actual,J,a=exact_table(n,f);assert actual==hist and I==J;checks+=1
            save_record('bent_point_surgery',{'k':k,'dummy_bits':n-k,'point_weight_in_core':r},n,hist,I)
# Direct signed and unsigned convolution, not only inverse-transform verification.
cancellation=[]
for n in [2,4,6]:
    if n>LIMIT:continue
    h,I,a=exact_table(n,lambda x:(-1)**sum(((x>>(2*j))&3)==3 for j in range(n//2)))
    N=1<<n
    for U in range(1,N):
        signed=sum(a[S]*a[S^U] for S in range(N));unsigned=sum(abs(a[S]*a[S^U]) for S in range(N))
        assert signed==0 and unsigned==N*N;checks+=1
    cancellation.append(dict(n=n,I=str(I),signed_each_nonzero_shift='0',unsigned_each_nonzero_shift='1',unsigned_total=str(N-1),unsigned_total_over_I=str(F(2*(N-1),n))))
    save_record('bent',{'n':n},n,h,I)
bad_gap=[r for r in records if not r['gap_le_4I']]
bad_fmei=[r for r in records if not r['Hinf_le_2I']]
def upper(r,index):
    return F(r['ratios_H_Hinf_gap'][index][1]) if r['ratios_H_Hinf_gap'] else F(-1)
summary=dict(helper_version='A035-payment-v1',pilot=PILOT,case_count=len(records),exact_checks=checks,runtime_seconds=time.perf_counter()-START,
             counts=dict(Counter(r['family'] for r in records)),gap_4_violations=bad_gap,Hinf_2_violations=bad_fmei,
             maxima={name:max(records,key=lambda r:upper(r,i)) for i,name in enumerate(['H_over_I','Hinf_over_I','gap_over_I'])},cancellation=cancellation,
             log_certificate=dict(series_terms=24,reduction='integer w -> 2^k*m, 1<=m<2',tail='2*z^(49)/(49*(1-z^2)); z=(m-1)/(m+1) in [0,1/3]',division='positive denominator: [a,b]/[c,d]=[a/d,b/c]',export='outward rational grid 10^-12'))
(ROOT/'out'/('pilot_summary.json' if PILOT else 'SIGNED_PAYMENT_TESTS.json')).write_text(json.dumps(summary,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k not in ['maxima','gap_4_violations','Hinf_2_violations']},indent=2))
print('violations gap4, Hinf2:',len(bad_gap),len(bad_fmei))
for name,r in summary['maxima'].items():print(name,r['family'],r['parameters'],r['ratios_H_Hinf_gap'])
