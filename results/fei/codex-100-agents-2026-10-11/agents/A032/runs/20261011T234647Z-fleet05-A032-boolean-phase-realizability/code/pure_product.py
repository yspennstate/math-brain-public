import argparse, itertools, math, json, time
from pathlib import Path
from collections import Counter
from decimal import Decimal, localcontext
ROOT=Path(__file__).resolve().parents[1]
VERSION='A032-pure-product-v1'

def fwht(values):
    a=list(values); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                u,v=a[j],a[j+h];a[j],a[j+h]=u+v,u-v
        h*=2
    return a

def entropy_numerator(hist,N):
    with localcontext() as ctx:
        ctx.prec=40
        return sum(Decimal(v)*count*(Decimal(N*N).ln()-Decimal(v).ln())/Decimal(2).ln() for v,count in hist if v)

def magnitude_templates(m):
    N=1<<m
    primitive=[(a,b,a*a+b*b) for a in range(1,N+1) for b in range(1,N+1) if math.gcd(a,b)==1 and a*a+b*b<=N*N]
    def tuples(r,limit,prefix=(),factor=1):
        if len(prefix)==r:
            yield prefix,factor;return
        for a,b,q in primitive:
            if factor*q*2**(r-len(prefix)-1)<=limit:
                yield from tuples(r,limit,prefix+((a,b),),factor*q)
    for r in range(m+1):
        for active in itertools.combinations(range(m),r):
            outside=[i for i in range(m) if i not in active]
            for fixedbits in itertools.product((0,1),repeat=m-r):
                shift=sum(b<<i for b,i in zip(fixedbits,outside))
                labels=[shift^sum(((mask>>j)&1)<<i for j,i in enumerate(active)) for mask in range(1<<r)]
                for c in [1<<i for i in range(m+1)]:
                    for ratios,factor in tuples(r,N*N//(c*c)):
                        norm=c*c*factor
                        if norm%N:continue
                        magnitudes=[c*math.prod(ratios[j][(mask>>j)&1] for j in range(r)) for mask in range(1<<r)]
                        yield active,labels,magnitudes,norm//N

def generate(m,seconds):
    started=time.monotonic();N=1<<m;records={};templates=phases=ternary=0
    for active,labels,magnitudes,k in magnitude_templates(m):
        r=len(active);fixed={0}|{1<<j for j in range(r)}
        free=[j for j in range(1<<r) if j not in fixed]
        templates+=1
        for mask in range(1<<len(free)):
            phases+=1
            if phases%1000==0 and time.monotonic()-started>seconds:raise RuntimeError('FROZEN_RUNTIME_LIMIT')
            coeff=[0]*N
            for s,a in zip(labels,magnitudes):coeff[s]=a
            for j,pos in enumerate(free):
                if mask>>j&1:coeff[labels[pos]]*=-1
            inverse=fwht(coeff)
            if any(v not in (-N,0,N) for v in inverse):continue
            ternary+=1
            truth=[v//N for v in inverse]
            assert sum(v*v for v in truth)==k
            assert fwht(truth)==coeff
            hist=tuple(sorted(Counter(v*v for v in coeff if v).items()))
            influence=sum(s.bit_count()*v*v for s,v in enumerate(coeff))
            h_num=str(entropy_numerator(hist,N))
            for tmask in range(1<<r):
                translation=sum(((tmask>>j)&1)<<i for j,i in enumerate(active))
                shifted=[truth[x^translation] for x in range(N)]
                support=sum((v!=0)<<x for x,v in enumerate(shifted))
                key=(support,hist)
                old=records.get(key)
                if old is None or influence<old['influence_numerator']:
                    records[key]={'support':support,'size':k,'truth':shifted,'histogram':hist,'influence_numerator':influence,'entropy_numerator_decimal':h_num}
    output={'m':m,'helper':VERSION,'templates':templates,'gauge_phases':phases,'ternary_phase_representatives':ternary,'records':list(records.values()),'seconds':time.monotonic()-started,'status':'COMPLETE'}
    (ROOT/'out'/f'slices_m{m}.json').write_text(json.dumps(output,separators=(',',':')))
    print(json.dumps({k:v for k,v in output.items() if k!='records'}))
    print(json.dumps({'slice_records':len(records),'physical_supports':len({r['support'] for r in records.values()}),'sizes':dict(Counter(r['size'] for r in records.values()))}),flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--m',type=int,nargs='+',required=True);p.add_argument('--seconds',type=int,default=60);args=p.parse_args()
    for m in args.m:assert m in (1,2,3,4);generate(m,args.seconds)
