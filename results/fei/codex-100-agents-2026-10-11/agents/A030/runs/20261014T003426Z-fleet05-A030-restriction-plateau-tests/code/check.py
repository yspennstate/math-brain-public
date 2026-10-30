"""Frozen A030 selector collision reserve transport, v1."""
from pathlib import Path
import json, hashlib, time
from fractions import Fraction as F
from itertools import permutations
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parents[1]/'runs/20261013T212321Z-fleet05-A030-restriction-plateau-tests/code/check.py'
ns={'__file__':str(OLD)}
exec(OLD.read_text(encoding='utf-8').split('for n in (1,2,3):')[0],ns)
expr,add,const,stats,child,reserve,positive,ck=[ns[k] for k in ('expr','add','const','stats','child','reserve','positive','ck')]
ZERO=()
def phi(p):
    if not p:return ZERO
    d={}
    for a,e in ns['factors'](p.denominator).items():d[a]=p*e
    for a,e in ns['factors'](p.numerator).items():d[a]=d.get(a,F(0))-p*e
    return expr(d)
def mean(t):return F(sum(t),len(t))
def correction(b):
    return add((1,phi((1+b)**2/4)),(1,phi((1-b)**2/4)),(1,const(1-b*b)),(-F(1,2),phi(b*b)))
def bank(b):return add((1,phi((1+b)/2)),(1,phi((1-b)/2)))
def wrapper(t):
    n=len(t).bit_length()-1
    return tuple(-1 if (x>>(n+(t[x&((1<<n)-1)]<0)))&1 else 1 for x in range(4*len(t)))
counts=dict(roots=0,faces=0,tree_price_pairs=0,balanced_pairs=0)
for n in (1,2,3):
    for mask in range(1<<(1<<n)):
        t=tuple(-1 if mask>>x&1 else 1 for x in range(1<<n)); f=wrapper(t)
        h,di=stats(t); hf,dif=stats(f); b=mean(t); a=correction(b)
        ck(hf==add((F(1,2),h),(1,a)))
        ck(sum(dif)==1+sum(di)/2)
        ck(positive(add((-1,a)))==ZERO);ck(positive(add((1,a),(-1,const(2))))==ZERO)
        counts['roots']+=1
        for i in range(n):
            ts=[child(t,i,v) for v in (0,1)]; fs=[child(f,i,v) for v in (0,1)]
            dh=add((1,h),(-F(1,2),stats(ts[0])[0]),(-F(1,2),stats(ts[1])[0]))
            df=add((1,hf),(-F(1,2),stats(fs[0])[0]),(-F(1,2),stats(fs[1])[0]))
            da=add((1,a),(-F(1,2),correction(mean(ts[0]))),(-F(1,2),correction(mean(ts[1]))))
            release=add((1,bank(b)),(-F(1,2),bank(mean(ts[0]))),(-F(1,2),bank(mean(ts[1]))))
            ck(df==add((F(1,2),dh),(1,da)))
            ck(dif[i]==di[i]/2)
            ck(positive(add((-1,release)))==ZERO)
            ck(positive(add((1,release),(-1,const(di[i]))))==ZERO)
            ck(positive(add((1,da),(-1,const(4*di[i]))))==ZERO)
            counts['faces']+=1
        for order in permutations(range(n)):
            for C in (0,1,4):
                q=reserve(t,order,C)
                qf=reserve(f,order+(n,n+1),C)
                ck(positive(add((1,qf),(-F(1,2),q),(-1,a)))==ZERO)
                lower=positive(add((F(1,2),q),(1,a),(-1,const(2))))
                ck(positive(add((1,lower),(-1,qf)))==ZERO)
                if b==0:
                    ck(positive(add((F(1,2),q),(-1,qf)))==ZERO)
                    counts['balanced_pairs']+=1
                counts['tree_price_pairs']+=1
    stats.cache_clear();reserve.cache_clear()
# Sharp additive-two witness, and explicit control erasure not paid by bank release alone.
t=(1,-1); f=wrapper(t)
ck(reserve(f,(0,1,2),0)==const(2)); ck(reserve(t,(0,),0)==ZERO)
ck(add((1,stats(f)[0]),(-1,bank(F(0))))==const(1))
result=dict(status='PASS',helper_version='A030-selector-collision-v1',checks=ns['checks'],counts=counts,certified_nonzero_signs=ns['signs'],exact_zero_signs=ns['zeros'],elapsed_seconds=time.perf_counter()-ns['START'],arithmetic='integer Walsh; Fraction prime-log equality; rational 40-term atanh sign intervals',helper_sha256=hashlib.sha256(OLD.read_bytes()).hexdigest(),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(ROOT/'out/VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
