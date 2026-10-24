from fractions import Fraction as Q
from functools import lru_cache
from math import comb
from pathlib import Path
import json
import sys
import time

run=Path(__file__).resolve().parents[1]
start=time.perf_counter()
assertions=0

def test(x):
    global assertions
    assert x
    assertions+=1
    if time.perf_counter()-start>60:
        raise RuntimeError('Frozen 60-second limit exceeded')

# Formal sums coeff*ln(rational). Expand products/quotients before entering.
def add(dst,arg,coeff):
    if arg and arg!=1 and coeff:
        dst[arg]=dst.get(arg,Q(0))+coeff
        if not dst[arg]: del dst[arg]
def plus(*terms):
    dst={}
    for expression,scale in terms:
        for arg,coeff in expression.items(): add(dst,arg,coeff*scale)
    return dst
def entropy(probabilities):
    dst={}
    for p in probabilities: add(dst,p,-p)
    return dst
def eta(p): return entropy([p])

@lru_cache(None)
def reduced_ln(x):
    # x is in [1,2]; z in [0,1/3].
    z=(x-1)/(x+1)
    power=z
    lower=Q(0)
    for j in range(24):
        lower+=2*power/(2*j+1)
        power*=z*z
    tail=2*power/(49*(1-z*z))
    return lower,lower+tail

@lru_cache(None)
def ln_interval(x):
    test(x>0)
    k=x.numerator.bit_length()-x.denominator.bit_length()
    power=Q(2**k) if k>=0 else Q(1,2**(-k))
    y=x/power
    while y<1: y*=2; k-=1
    while y>=2: y/=2; k+=1
    lo,hi=reduced_ln(y)
    l2,u2=reduced_ln(Q(2))
    if k>=0: return lo+k*l2,hi+k*u2
    return lo+k*u2,hi+k*l2

def enclosure(expression):
    lo=hi=Q(0)
    for arg,c in expression.items():
        l,u=ln_interval(arg)
        lo+=c*(l if c>=0 else u)
        hi+=c*(u if c>=0 else l)
    return lo,hi

def nonnegative(expression):
    if not expression: test(True); return
    lo,hi=enclosure(expression)
    test(lo>=0)

def upper(expression,bound):
    lo,hi=enclosure(expression)
    test(hi<=bound)

def walsh(values):
    a=values.copy(); width=1
    while width<len(a):
        for j in range(0,len(a),2*width):
            for k in range(width):
                u,v=a[j+k],a[j+k+width]
                a[j+k],a[j+k+width]=u+v,u-v
        width*=2
    return [Q(v,len(a)) for v in a]

def lift(bits,coords):
    return sum(((bits>>j)&1)<<i for j,i in enumerate(coords))

def audit(values,n,block,certify=True):
    a=walsh(values); p=[v*v for v in a]
    test(sum(p)==1)
    rest=[i for i in range(n) if i not in block]
    full_rows=[]; children=[]
    for y in range(1<<len(block)):
        vals=[values[lift(y,block)|lift(t,rest)] for t in range(1<<len(rest))]
        child_a=walsh(vals); children.append([v*v for v in child_a])
    weight=Q(1,1<<len(block))
    M={}; C={}; Mplus={}; Cplus={}; ell={}
    for t in range(1<<len(rest)):
        row=[p[lift(u,block)|lift(t,rest)] for u in range(1<<len(block))]
        q=sum(row)
        test(q==sum(child[t] for child in children)*weight)
        mr=entropy(row); add(mr,q,q)
        cr={}
        for child in children:
            py=child[t]; add(cr,py,weight*py); add(cr,q,-weight*py)
        M=plus((M,1),(mr,1)); C=plus((C,1),(cr,1))
        if t:
            Mplus=plus((Mplus,1),(mr,1)); Cplus=plus((Cplus,1),(cr,1))
        else: ell=entropy(row[1:])
    H=entropy(p); b=eta(p[0]); K=plus((H,Q(1,2)),(b,Q(-1,2)))
    Hc={}; bc={}; Kc={}
    for child in children:
        Hc=plus((Hc,1),(entropy(child),weight))
        bc=plus((bc,1),(eta(child[0]),weight))
    Kc=plus((Hc,Q(1,2)),(bc,Q(-1,2)))
    deltaH=plus((H,1),(Hc,-1)); deltaK=plus((K,1),(Kc,-1))
    test(plus((deltaH,1),(M,-1),(C,-1))=={})
    test(plus((deltaK,2),(Mplus,-1),(Cplus,-1),(ell,-1))=={})
    test(plus((deltaK,2),(M,-1),(C,-1),(b,1),(bc,-1))=={})
    IB=sum(sum(v for s,v in enumerate(p) if s>>i&1) for i in block)
    Ic=sum(sum(s.bit_count()*v for s,v in enumerate(child)) for child in children)*weight
    I=sum(s.bit_count()*v for s,v in enumerate(p))
    test(I==IB+Ic)
    physical=sum(Q(sum(values[x]!=values[x^(1<<i)] for x in range(1<<n)),1<<n) for i in block)
    test(IB==physical)
    if certify:
        nonnegative(deltaK); nonnegative(M); nonnegative(C)
        upper(C,2*IB)
        if len(block)==1:
            i=block[0]
            test(abs(a[1<<i])<=IB)
            upper(ell,IB) # universal 2/e coefficient is established analytically.
            omitted=plus((M,1),(Mplus,-1))
            upper(omitted,2*IB) # analytic statement in DERIVATION uses 1+2/e.
    return dict(M=M,C=C,Mplus=Mplus,Cplus=Cplus,ell=ell,deltaK=deltaK,deltaH=deltaH,IB=IB,H=H,I=I,p=p)

def histogram(a,r,b):
    k=a+(1<<a); D=k+r; delta=Q(1,1<<D); w=1<<b
    A=Q(1,1<<a); support=1<<(2*a)
    mp=(support+(1<<a))//2; mm=(support-(1<<a))//2
    M={}; C={}; Mplus={}; Cplus={}
    for z,count in [(A,mp),(-A,mm),(Q(0),(1<<(D-b))-support)]:
        x=(z-2*delta)**2; s=4*delta**2; q=x+(w-1)*s; cp=(z-2*w*delta)**2
        mr=plus((eta(x),1),(eta(s),w-1)); add(mr,q,q)
        cr={}
        add(cr,cp,cp/w); add(cr,q,-cp/w)
        add(cr,z*z,(1-Q(1,w))*z*z); add(cr,q,-(1-Q(1,w))*z*z)
        M=plus((M,1),(mr,count)); C=plus((C,1),(cr,count))
        kept=count-(1 if z==0 else 0)
        Mplus=plus((Mplus,1),(mr,kept)); Cplus=plus((Cplus,1),(cr,kept))
    H=plus((eta((A-2*delta)**2),mp),(eta((A+2*delta)**2),mm),(eta(4*delta**2),(1<<D)-support))
    dc=w*delta
    Hdef=plus((eta((A-2*dc)**2),mp),(eta((A+2*dc)**2),mm),(eta(4*dc**2),(1<<(D-b))-support))
    Hclean={Q(2):Q(2*a)}
    Hc=plus((Hdef,Q(1,w)),(Hclean,1-Q(1,w)))
    deltaH=plus((H,1),(Hc,-1))
    boundary=plus((eta(4*delta**2),1),(eta(4*dc**2),Q(-1,w)))
    deltaK=plus((deltaH,Q(1,2)),(boundary,Q(-1,2)))
    ell=plus((eta(4*delta**2),w-1))
    test(plus((deltaH,1),(M,-1),(C,-1))=={})
    test(plus((deltaK,2),(Mplus,-1),(Cplus,-1),(ell,-1))=={})
    # Hclean's log(2) atom need not match eta's log(2^-2a) atom formally;
    # exact power-of-two normalization below verifies equivalent log sums.
    return dict(M=M,C=C,Mplus=Mplus,Cplus=Cplus,ell=ell,deltaK=deltaK,deltaH=deltaH,IB=2*b*delta,H=H,I=1+Q(a,2)+2*delta*(D-2))

# Fold pure powers of two for exact comparisons; no prime factorization needed.
def canonical(expression):
    result={}
    for arg,c in expression.items():
        num,den=arg.numerator,arg.denominator
        if num&(num-1)==0 and den&(den-1)==0:
            add(result,Q(2),c*(num.bit_length()-den.bit_length()))
        else: add(result,arg,c)
    return result

# Use canonical log atoms globally so all exact histogram comparisons agree.
raw_plus=plus
def plus(*terms): return canonical(raw_plus(*terms))

def address_values(a,r):
    k=a+(1<<a); D=k+r
    vals=[]
    for x in range(1<<D):
        addr=x&((1<<a)-1)
        # Binary zero represents a +1 coordinate, hence all-plus is x=0.
        value=1 if not x>>(a+addr)&1 else -1
        vals.append(-value if x==0 else value)
    return vals,D

def serialized_bounds(expr,scale=Q(1)):
    lo,hi=enclosure(expr)
    lo/=scale; hi/=scale
    # Preserve rigorous bounds while avoiding enormous LCM-denominator exports.
    grid=1<<80
    lower=Q((lo.numerator*grid)//lo.denominator,grid)
    upper=Q(-((-hi.numerator*grid)//hi.denominator),grid)
    return {'lower':str(lower),'upper':str(upper),'outward_rounding_bits':80,'midpoint_display':float((lo+hi)/2)}

mode=sys.argv[1] if len(sys.argv)>1 else 'pilot'
test(mode in ['pilot','full'])
counts={'exhaustive_blocks':0,'majority_blocks':0,'direct_address_blocks':0,'histogram_blocks':0}
tables=[]
for n in range(1,3 if mode=='pilot' else 4):
    for mask in range(1<<(1<<n)):
        values=[1 if mask>>x&1 else -1 for x in range(1<<n)]
        for block_mask in range(1,1<<n):
            audit(values,n,[i for i in range(n) if block_mask>>i&1])
            counts['exhaustive_blocks']+=1

for n in ([3] if mode=='pilot' else [3,5,7,9]):
    vals=[1 if n-2*x.bit_count()>0 else -1 for x in range(1<<n)]
    for b in range(1,n+1):
        result=audit(vals,n,list(range(b)))
        if b==1:
            alpha=Q(comb(n-1,(n-1)//2),1<<(n-1))
            test(result['IB']==alpha)
            test(result['M']=={} and result['C']=={})
            test(plus((result['deltaK'],1),(eta(alpha*alpha),Q(-1,2)))=={})
        tables.append({'family':'majority','n':n,'block_size':b,'I_B':str(result['IB']),
                       'heat_drop_over_I_B':serialized_bounds(result['deltaK'],result['IB']),
                       'channel_over_I_B':serialized_bounds(result['C'],result['IB']),
                       'erasure_over_I_B':serialized_bounds(result['M'],result['IB']),
                       'level_over_I_B':serialized_bounds(result['ell'],result['IB'])})
        counts['majority_blocks']+=1

for a in ([1] if mode=='pilot' else [1,2]):
    for r in ([1] if mode=='pilot' else range(1,5)):
        vals,D=address_values(a,r)
        for b in range(1,r+1):
            result=audit(vals,D,list(range(D-r,D-r+b)))
            hist=histogram(a,r,b)
            for key in ['M','C','Mplus','Cplus','ell','deltaK','deltaH','H']:
                test(plus((result[key],1),(hist[key],-1))=={})
            test(result['I']==hist['I'] and result['IB']==hist['IB'])
            counts['direct_address_blocks']+=1

if mode=='full':
    for a in [1,2,3]:
        for r in [1,2,4,8,16,32]:
            for b in sorted({1,r}):
                h=histogram(a,r,b)
                nonnegative(h['deltaK']); nonnegative(h['M']); nonnegative(h['C']); upper(h['C'],2*h['IB'])
                tables.append({'family':'defected-addressing','a':a,'r':r,'block_size':b,'I_B':str(h['IB']),
                    'heat_drop_over_I_B':serialized_bounds(h['deltaK'],h['IB']),
                    'channel_over_I_B':serialized_bounds(h['C'],h['IB']),
                    'erasure_over_I_B':serialized_bounds(h['M'],h['IB']),
                    'level_over_I_B':serialized_bounds(h['ell'],h['IB'])})
                counts['histogram_blocks']+=1

result={'status':'PASS','mode':mode,'assertions':assertions,'counts':counts,
        'runtime_seconds':time.perf_counter()-start,'log_terms':24,
        'log_tail':'2*z^(49)/(49*(1-z^2)), after exact power-of-two range reduction',
        'arithmetic':'Integer Walsh; Fraction; exact log atoms; rational intervals',
        'tables':tables,'universal_integrated_residual_status':'OPEN'}
(run/'out').mkdir(exist_ok=True)
(run/'out'/f'CHECK_{mode.upper()}.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({key:value for key,value in result.items() if key!='tables'},indent=2))
