from pathlib import Path
from fractions import Fraction as Q
import json, time
run=Path(__file__).resolve().parents[1]
old=run.parent/'20261011T233317Z-account05-A066-semigroup-dissipation/code/check_restrictions.py'
ns={'__file__':str(__file__)}
exec(compile(old.read_text().split('mode=sys.argv[1]')[0],str(old),'exec'),ns)
plus,add,enclosure,audit,canonical=[ns[k] for k in ['plus','add','enclosure','audit','canonical']]
test=ns['test']
started=time.perf_counter()

def channel(a,b):
    result={}; q=a*a+b*b
    for p in [(a+b)**2,(a-b)**2]:
        add(result,p,p/2); add(result,q,-p/2)
    return plus((result,1))

def orient(a,b):
    result={}; p=b*b; q=a*a+p
    add(result,q,p); add(result,p,-p)
    return plus((result,1))

def formula(m):
    A=Q(1,1<<m); d=A*A; N=1<<(2*m)
    np=(N+(1<<m))//2; nm=N-np
    C=plus((channel(A-d,d),np-1),(channel(A+d,d),nm))
    ell={}; add(ell,d*d,-d*d)
    P=plus((C,1),(ell,1))
    M=plus((orient(A-d,d),np-1),(orient(A+d,d),nm))
    return C,canonical(ell),P,M,d

def rounded(expression,scale=Q(1)):
    lo,hi=enclosure(expression); lo/=scale; hi/=scale; grid=1<<80
    return {'lower':str(Q(lo.numerator*grid//lo.denominator,grid)),
            'upper':str(Q(-((-hi.numerator*grid)//hi.denominator),grid))}

records=[]
for m in range(1,65):
    C,L,P,M,d=formula(m)
    if m<=8:
        lo,hi=enclosure(P)
        if m>=2: test(lo>2*d)
        if m>=2:
            error=plus((M,1),({Q(2):Q(2*m)*d},-1))
            lower_error,upper_error=enclosure(error)
            test(lower_error>=-8*Q(1,1<<m)*d)
            test(upper_error<=8*Q(1,1<<m)*d)
    # Exact ln2 lower bound proves the family-wide scalar lower bound.
    if m>=2: test(2*m*Q(842,1215)>2/(1-Q(1,1<<m)))
    if m<=8:
        paid=rounded(P,d)
        method='direct exact formula with rational log enclosure'
    else:
        A=Q(1,1<<m)
        lo=2+2*d*(2*m*Q(842,1215)-2/(1-A))
        hi=2-2*d+4*m*d*Q(7,10)
        test(lo>2)
        paid={'lower_exact':str(lo),'upper_exact':str(hi)}
        method='analytic row bounds; ln2 between 842/1215 and 7/10'
    records.append({'m':m,'paid_over_query_influence':paid,'certificate_method':method,'oriented_erasure_over_query_influence':rounded(M,d)})
for m in range(1,5):
    values=[]
    for xz in range(1<<(2*m+1)):
        z=xz&1; x=xz>>1
        parity=sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m))%2
        g=1-2*parity
        values.append(-g if z==1 and x==0 else g)
    r=audit(values,2*m+1,[0],False)
    C,L,P,M,d=formula(m)
    test(r['IB']==d)
    test(r['I']==m+(2*m+1)*d)
    test(plus((r['Cplus'],1),(C,-1))=={})
    test(plus((r['ell'],1),(L,-1))=={})
    # Independently compute oriented bill from the direct spectrum.
    O={}
    for t in range(1,1<<(2*m)):
        a,b=r['p'][2*t],r['p'][2*t+1]
        add(O,a+b,b); add(O,b,-b)
    test(plus((O,1),(M,-1))=={})
test(Q(records[1]['paid_over_query_influence']['lower'])>Q(217,100))
test(ns['ln_interval'](Q(2))[1]<Q(7,10))
out={'assertions':ns['assertions'],'compressed_cases':64,'direct_cases':4,
     'm2_certified_paid_rate_exceeds':'217/100','elapsed_seconds':time.perf_counter()-started,
     'records':records,'arithmetic':'Fraction with rigorous rational log enclosures; outward 80-bit dyadic bounds'}
(run/'out').mkdir(exist_ok=True)
(run/'out/BENT_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='records'}))
