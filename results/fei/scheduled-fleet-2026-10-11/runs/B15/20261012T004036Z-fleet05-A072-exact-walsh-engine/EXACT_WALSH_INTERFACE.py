"""Uniform entropy/erasure extension of the checked A072 baseline.

Log forms are dictionaries prime -> rational coefficient of log2(prime).
All transforms, inverses and edges are checked before constructing log forms.
"""
import importlib.util, math, sys
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
sys.dont_write_bytecode=True
BASE=Path(__file__).resolve().parents[1]/'20261011T220909Z-fleet05-A072-exact-walsh-engine/EXACT_WALSH_INTERFACE.py'
spec=importlib.util.spec_from_file_location('a072_baseline',BASE)
baseline=importlib.util.module_from_spec(spec);spec.loader.exec_module(baseline)
uniform_certificate=baseline.uniform_certificate
VERSION='A072-uniform-erasure/2'

@lru_cache(None)
def factors(n):
    n=int(n)
    if n<1: raise ValueError('Positive factor input required')
    out=[];p=2
    while p*p<=n:
        k=0
        while n%p==0: k+=1;n//=p
        if k:out.append((p,k))
        p=3 if p==2 else p+2
    if n>1:out.append((n,1))
    return tuple(out)

def add(*terms):
    out={}
    for scale,form in terms:
        for p,c in form.items():out[p]=out.get(p,F(0))+scale*c
    return {p:F(c) for p,c in sorted(out.items()) if c}

def log(q):
    q=F(q)
    if q<=0:raise ValueError('Positive logarithm required')
    out={}
    for scale,n in [(1,q.numerator),(-1,q.denominator)]:
        for p,k in factors(n):out[p]=out.get(p,F(0))+scale*k
    return {p:F(c) for p,c in sorted(out.items()) if c}

def entropy(masses):
    assert sum(masses)==1 and all(x>=0 for x in masses)
    return add(*[(-p,log(p)) for p in masses if p])

def phi(a,b):
    if a==0 or b==0:return {}
    return add((a+b,log(a+b)),(-a,log(a)),(-b,log(b)))

def sign(form,max_bits=8000000):
    """Exact sign of sum c_p log2 p by clearing denominators.

    Product bit bound uses log2(p)<p.bit_length(), hence no numerical log.
    """
    if not form:return {'sign':0,'denominator':1,'integer_exponents':{},'bit_bound':0}
    D=math.lcm(*(c.denominator for c in form.values()))
    powers={p:int(c*D) for p,c in form.items()}
    bound=sum(abs(e)*p.bit_length() for p,e in powers.items())
    if bound>max_bits:raise RuntimeError('Frozen integer bit budget exceeded')
    num=den=1
    for p,e in powers.items():
        if e>0:num*=p**e
        elif e<0:den*=p**(-e)
    return {'sign':(num>den)-(num<den),'denominator':D,
            'integer_exponents':powers,'bit_bound':bound,
            'positive_product_bits':num.bit_length(),'negative_product_bits':den.bit_length()}

def uniform_entropy_certificate(table):
    c=uniform_certificate(table)
    n=c['n'];N=len(table);mu=c['spectrum'];H=entropy(mu);rows=[]
    # Children are physical truth tables. Their own transforms/edges/inverses
    # are certified before any entropy or JS expression is assembled.
    for i in range(n):
        childcert=[]
        for z in (0,1):
            ct=[]
            for y in range(N//2):
                lo=y&((1<<i)-1);hi=y>>i
                x=lo|(z<<i)|(hi<<(i+1));ct.append(table[x])
            childcert.append(uniform_certificate(tuple(ct)))
        q=[];B={}
        for s in range(N):
            if s>>i&1:continue
            a,b=mu[s],mu[s|(1<<i)]
            q.append(a+b);B=add((1,B),(1,phi(a,b)))
        cplus,cminus=[cc['spectrum'] for cc in childcert]
        assert q==[(a+b)/2 for a,b in zip(cplus,cminus)]
        Hchildren=[entropy(cc['spectrum']) for cc in childcert]
        JS=add((1,entropy(q)),(F(-1,2),Hchildren[0]),(F(-1,2),Hchildren[1]))
        Delta=add((1,H),(F(-1,2),Hchildren[0]),(F(-1,2),Hchildren[1]))
        assert Delta==add((1,B),(1,JS))
        # Verify the parent/physical-child signed amplitude identities too.
        for t in range(N//2):
            s=(t&((1<<i)-1))|((t>>i)<<(i+1))
            u,v=c['walsh'][s],c['walsh'][s|(1<<i)]
            assert 2*childcert[0]['walsh'][t]==u+v
            assert 2*childcert[1]['walsh'][t]==u-v
        assert [sum(cc['influences'][j] for cc in childcert)/2 for j in range(n-1)]==[
            c['influences'][j] for j in range(n) if j!=i]
        I=c['influences'][i]
        assert sign(B)['sign']>=0 and sign(JS)['sign']>=0
        rows.append({'coordinate':i,'influence':I,'B_prime_log':B,'JS_prime_log':JS,
                     'Delta_prime_log':Delta,'B_over_influence_prime_log':add((1/I,B)) if I else None,
                     'children':childcert,'child_entropy_prime_log':Hchildren})
    return {**c,'entropy_prime_log':H,'coordinates':rows,
            'total_influence':sum(c['influences'],F(0)),
            'total_erasure_prime_log':add(*[(1,r['B_prime_log']) for r in rows])}
