from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict
from itertools import product
from pathlib import Path
import time,json,sys

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
def cap():
    if time.perf_counter()-START>58: raise RuntimeError('Frozen 60-second cap reached; no further cases allowed')
@lru_cache(None)
def ln_interval(x,terms=32):
    x=F(x)
    if x==1:return (F(0),F(0))
    if x<1:
        lo,hi=ln_interval(1/x,terms);return (-hi,-lo)
    exponent=x.numerator.bit_length()-x.denominator.bit_length()
    while x<F(2)**exponent:exponent-=1
    while x>=F(2)**(exponent+1):exponent+=1
    r=x/F(2)**exponent
    y=(r-1)/(r+1); total=F(0)
    for j in range(terms):total+=2*y**(2*j+1)/(2*j+1)
    err=2*y**(2*terms+1)/((2*terms+1)*(1-y*y))
    if exponent:
        # ln2 must be evaluated directly; normalization would recurse.
        z=F(1,3); l2=sum((2*z**(2*j+1)/(2*j+1) for j in range(terms)),F(0))
        e2=2*z**(2*terms+1)/((2*terms+1)*(1-z*z))
        total+=exponent*l2; err+=exponent*e2
    return total,total+err
@lru_cache(None)
def factors(n):
    out=[];p=2
    while p*p<=n:
        e=0
        while n%p==0:n//=p;e+=1
        if e:out.append((p,e))
        p+=1
    if n>1:out.append((n,1))
    return out
def logadd(vec,n,weight):
    if n:
        for p,e in factors(n):vec[p]+=weight*e
def interval_vec(vec):
    for terms in (16,32,48):
        lo=F(0);hi=F(0)
        for p,v in vec:
            a,b=ln_interval(F(p),terms)
            if v>=0:lo+=v*a;hi+=v*b
            else:lo+=v*b;hi+=v*a
        if lo>0 or hi<0 or not vec:return lo,hi,terms
    raise RuntimeError('No certified sign within frozen precision')
@lru_cache(None)
def sign_vec(vec):
    lo,hi,_=interval_vec(vec)
    return 1 if lo>0 else -1 if hi<0 else 0
def walsh(a):
    b=list(a);h=1
    while h<len(b):
        for j in range(0,len(b),2*h):
            for i in range(j,j+h):b[i],b[i+h]=b[i]+b[i+h],b[i]-b[i+h]
        h*=2
    return b
@lru_cache(None)
def histogram_sign(hist,K):
    vec=defaultdict(int)
    for A,D,mult in hist:
        logadd(vec,A+D,mult*(A+D));logadd(vec,A,-mult*A);logadd(vec,D,-mult*D)
        vec[2]-=K*mult*D
    return sign_vec(tuple(sorted((p,v) for p,v in vec.items() if v)))
def split(a,j):
    lo=[];hi=[]
    for x in range(len(a)):
        if not(x>>j&1):lo.append(a[x]);hi.append(a[x|(1<<j)])
    return tuple(lo),tuple(hi)
def influence(a):
    return sum((F(sum(a[x]!=a[x^(1<<j)] for x in range(len(a))),len(a)) for j in range((len(a)-1).bit_length())),F(0))
def face_q(a):
    n=(len(a)-1).bit_length();count=0
    for i in range(n):
        for j in range(i):
            for x in range(len(a)):
                if not(x>>i&1 or x>>j&1):count+=a[x]*a[x^(1<<i)]*a[x^(1<<j)]*a[x^(1<<i)^(1<<j)]==-1
    return F(2*count,len(a))
def node(a,j,K):
    w=walsh(a);hist=defaultdict(int);dsum=0
    for T in range(len(a)):
        if not(T>>j&1):
            A=w[T]**2;D=w[T|(1<<j)]**2;hist[A,D]+=1;dsum+=D
    bad=histogram_sign(tuple(sorted((A,D,m) for (A,D),m in hist.items())),K)>0
    lo,hi=split(a,j);gh=tuple(x*y for x,y in zip(lo,hi))
    return bad,F(dsum,len(a)**2),influence(gh)/2,lo,hi
@lru_cache(None)
def tree(a,order,K):
    cap()
    if not order or all(v==a[0] for v in a):return (F(0),F(0),F(0),0)
    j=order[0];bad,d,c,lo,hi=node(a,j,K)
    next_order=tuple(x-(x>j) for x in order[1:])
    left=tree(lo,next_order,K);right=tree(hi,next_order,K)
    return ((c if bad else 0)+(left[0]+right[0])/2,d+(left[1]+right[1])/2,c+(left[2]+right[2])/2,int(bad)+left[3]+right[3])
def bent(x):return -1 if ((x&1)*((x>>1)&1)+((x>>2)&1)*((x>>3)&1))%2 else 1
def seed(x):
    b=bent(x&15)
    if (x>>4&1) and (x&15)==0:b=-b
    return b*(-1 if x>>5&1 else 1)
def activated(t,k):
    core=[]
    for x in range(1<<(6*t)):
        v=1
        for j in range(t):v*=seed((x>>(6*j))&63)
        core.append(v)
    return tuple(core+[1]*(len(core)*((1<<k)-1)))
def orders(t,k):
    selectors=[6*j+4 for j in range(t)]
    data=[6*j+r for j in range(t) for r in range(4)]
    balances=[6*j+5 for j in range(t)]
    controls=list(range(6*t,6*t+k))
    return tuple(controls+selectors+data+balances),tuple(selectors+data+balances+controls)
def frac(x):return str(x)
def main():
    pilot='--pilot' in sys.argv
    output={'arithmetic':'exact rational intervals and integer spectra','pilot':pilot,'family':[]}
    pairs=[(1,1)] if pilot else [(1,1),(1,2),(1,3),(2,1)]
    for t,k in pairs:
        f=activated(t,k);I=influence(f);cf,df=orders(t,k)
        a=tree(f,cf,4);b=tree(f,df,4);q=F(1,1<<k)
        assert I==q*(F(53,16)*t+k)
        assert a[0]==q*t*F(4,16)
        assert b[0]==q*t*F(k+4,16)
        assert a[1]==b[1]==I
        assert a[2]==b[2]
        # Direct geometric face count is bounded to the pilot/single-copy functions.
        if t==1:assert a[2]==face_q(f)
        output['family'].append({'t':t,'k':k,'dimension':6*t+k,'I':frac(I),'Q_bad_control_first':frac(a[0]),'Q_bad_data_first':frac(b[0]),'ratio_control_first':frac(a[0]/I),'ratio_data_first':frac(b[0]/I),'bad_node_count_cf':a[3],'bad_node_count_df':b[3],'all_face_charge':frac(a[2])})
    if not pilot:
        # Every physical restriction of b4 and its point flip, with every live coordinate.
        splits=0
        for flip in (False,True):
            for state in product((-1,0,1),repeat=4):
                free=[j for j in range(4) if state[j]==-1];table=[]
                for x in range(1<<len(free)):
                    full=sum(((x>>free.index(j)&1) if j in free else state[j])<<j for j in range(4))
                    v=bent(full)
                    table.append(-v if flip and full==0 else v)
                for j in range(len(free)):
                    assert not node(tuple(table),j,4)[0];splits+=1
        assert splits==216;output['seed_restriction_splits']=splits
        # Exact positive sign of the scalar coefficient, never inferred from floating output.
        cert=[]
        for k in range(1,13):
            q=F(1,1<<k);lo,hi=ln_interval(1-q)
            rlo=-2*(1-q)**2*hi-2*q+3*q*q
            rhi=-2*(1-q)**2*lo-2*q+3*q*q
            assert rlo>0
            assert rlo>=2*q**3/3 and rhi<=2*q**3/(3*(1-q))
            cert.append({'k':k,'positive_remainder_nats_interval':[str(rlo),str(rhi)],'analytic_lower':str(2*q**3/3),'analytic_upper':str(2*q**3/(3*(1-q)))})
        output['remainder_certificates']=cert
        selector_vec=((2,192),(3,-180),(5,-200),(13,156))
        lo,hi,terms=interval_vec(selector_vec);assert lo>0
        output['selector_B_minus_4d_certificate']={'natural_numerator_interval':[str(lo),str(hi)],'denominator':256,'prime_log_vector':selector_vec,'atanh_terms':terms}
    output['elapsed_seconds']=time.perf_counter()-START
    output['status']='PASS';output['full_FEI']='OPEN'
    name='pilot.json' if pilot else 'validation.json'
    (ROOT/'out'/name).write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({key:value for key,value in output.items() if key!='remainder_certificates'},indent=2))
if __name__=='__main__':main()
