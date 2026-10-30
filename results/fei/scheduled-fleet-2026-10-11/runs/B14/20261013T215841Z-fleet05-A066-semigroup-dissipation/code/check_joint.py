from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial
import hashlib, json, sys, time

run=Path(__file__).resolve().parents[1]
old=run.parent/'20261011T233317Z-fleet05-A066-semigroup-dissipation'/'code'/'check_restrictions.py'
source=old.read_text(encoding='utf-8')
ns={'__file__':str(__file__)}
exec(compile(source.split('mode=sys.argv[1]')[0],str(old),'exec'),ns)
audit,plus,add,canonical,enclosure=[ns[k] for k in ['audit','plus','add','canonical','enclosure']]
test=ns['test']
mode=sys.argv[1]
test(mode in ['pilot','full'])
started=time.perf_counter()
maxn=2 if mode=='pilot' else 3
el=sum((Q(1,factorial(k)) for k in range(21)),Q(0))
eu=el+Q(1,factorial(21))/(1-Q(1,22))
beta_lo=2+2/eu**2
beta_hi=2+2/el**2
gain_lo=2/eu-2/el**2
test(gain_lo>Q(46,100))

def rounded(x,up=False):
    grid=1<<80
    val=-((-x.numerator*grid)//x.denominator) if up else (x.numerator*grid)//x.denominator
    return str(Q(val,grid))

@lru_cache(None)
def block_audit(values,block):
    n=(len(values)-1).bit_length()
    return audit(list(values),n,list(block),False)

def child(values,i,y):
    n=(len(values)-1).bit_length()
    return tuple(values[(x&((1<<i)-1))|((x>>i)<<(i+1))|(y<<i)] for x in range(1<<(n-1)))

@lru_cache(None)
def refine(values,order):
    if not order: return {},{},Q(0)
    i=order[0]
    r=block_audit(values,(i,))
    paid=plus((r['Cplus'],1),(r['ell'],1))
    _,paid_hi=enclosure(paid)
    test(paid_hi<=beta_lo*r['IB'])
    p=r['p'][1<<i]
    _,channel_hi=enclosure(r['Cplus'])
    test(channel_hi<=2*(r['IB']-p))
    R,P,D=r['Mplus'],paid,r['IB']
    next_order=tuple(j-(j>i) for j in order[1:])
    for y in (0,1):
        rc,pc,dc=refine(child(values,i,y),next_order)
        R=plus((R,1),(rc,Q(1,2)))
        P=plus((P,1),(pc,Q(1,2)))
        D+=dc/2
    return R,P,D

counts={'function_block_order':0,'singleton_root_rows':0,'compressed_defects':0,'direct_defects':0}
for n in range(1,maxn+1):
    for truth in range(1<<(1<<n)):
        values=tuple(1 if (truth>>x)&1 else -1 for x in range(1<<n))
        for size in range(1,n+1):
            for block in combinations(range(n),size):
                b=block_audit(values,block)
                if size==1: counts['singleton_root_rows']+=1
                for order in permutations(block):
                    R,P,D=refine(values,order)
                    test(D==b['IB'])
                    transfer=plus((R,1),(b['Mplus'],-1))
                    originalpaid=plus((b['Cplus'],1),(b['ell'],1))
                    test(plus((originalpaid,1),(P,-1),(transfer,-1))=={})
                    test(plus((b['deltaK'],2),(R,-1),(P,-1))=={})
                    _,phi=enclosure(P)
                    test(phi<=beta_lo*D)
                    counts['function_block_order']+=1
test(counts['function_block_order']==(68 if mode=='pilot' else 3908))
test(counts['singleton_root_rows']==(36 if mode=='pilot' else 804))

def defect_coeffs(n):
    q=Q(1,1<<n)
    influence=n*2*q
    erasure=channel=Q(0)
    level=Q(0)
    for k in range(1,n+1):
        qk=Q(1,1<<k)
        w=Q(1,1<<(n-k))
        erasure+=w*((1<<(k-1))-1)*8*qk*qk
        channel+=w*((1<<(k-1))-1)*8*qk*qk
        level+=w*4*qk*qk*(2*k-2)
    blocklevel=((1<<n)-1)*4*q*q*(2*n-2)
    test(erasure/influence==2-Q(4,n)*(1-q))
    test(channel==erasure)
    test(level/influence==Q(4,n)*(1-(n+1)*q))
    test((channel+level)/influence==2*(1-2*q))
    test(blocklevel/influence==4*(1-Q(1,n))*(1-q))
    test(erasure+channel+level==blocklevel)
    return erasure,channel+level,influence

for n in range(1,(16 if mode=='pilot' else 128)+1):
    defect_coeffs(n)
    counts['compressed_defects']+=1
for n in range(1,(4 if mode=='pilot' else 8)+1):
    q=Q(1,1<<n)
    values=(-1,)+(1,)*((1<<n)-1)
    a=block_audit(values,tuple(range(n)))
    test(a['IB']==n*2*q)
    test(canonical(a['ell'])=={Q(2):((1<<n)-1)*4*q*q*(2*n-2)} if n>1 else not a['ell'])
    singleton=block_audit(values,(0,))
    mc=((1<<(n-1))-1)*8*q*q
    test(canonical(singleton['Mplus'])==({Q(2):mc} if mc else {}))
    test(canonical(singleton['Cplus'])==({Q(2):mc} if mc else {}))
    counts['direct_defects']+=1

ln2lower=Q(842,1215)
ratio_coeff=4*Q(127,128)*(1-Q(1,1<<128))
gap=ratio_coeff*ln2lower-Q(11,4)
test(gap>0)
test(Q(8,3)==sum((Q(1,factorial(k)) for k in range(4)),Q(0)))
test(2+2/Q(8,3)==Q(11,4))
test(beta_hi<Q(11,4))
out={'mode':mode,'counts':counts,'assertions':ns['assertions'],'elapsed_seconds':time.perf_counter()-started,
     'helper_sha256':hashlib.sha256(old.read_bytes()).hexdigest(),
     'beta_interval':{'lower':rounded(beta_lo),'upper':rounded(beta_hi,True)},
     'improvement_lower':rounded(gain_lo),'improvement_exceeds':'46/100',
     'n128_block_rate_lower':rounded(ratio_coeff*ln2lower),'old_price_upper_strict':'11/4',
     'n128_gap_exact':str(gap),'proper_block_extension':'Append one irrelevant coordinate: spectrum only empty residual row, identical charges and influence.',
     'certificate_arithmetic':'All assertions Fraction/formal log; only elapsed time is floating point; outward 80-bit serialization.'}
(run/'out').mkdir(exist_ok=True)
(run/'out'/('CHECK_'+mode.upper()+'.json')).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
