"""Exact small-cube reconstruction and independently compressed sharpness cases."""
from fractions import Fraction as Q
from functools import lru_cache
from itertools import product
from pathlib import Path
import json,time
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
def cap():
    if time.perf_counter()-START>58:raise RuntimeError('Frozen 60-second pilot cap reached')
def wht(a):
    b=list(a);h=1
    while h<len(b):
        for k in range(0,len(b),2*h):
            for j in range(k,k+h):x,y=b[j],b[j+h];b[j],b[j+h]=x+y,x-y
        h*=2
    return [Q(x,len(b)) for x in b]
def row(x,y):
    m=(x*x+y*y)/2
    if not m:return None
    r=(x+y)**2/(2*(x*x+y*y));r=min(r,1-r)
    return (r,m) if r else None
def add(out,r,m):
    if r and m:out[r]=out.get(r,Q(0))+m
def erasure_coeffs(g,h):
    out={}
    for x,y in zip(g,h):
        item=row(x,y)
        if item:add(out,*item)
    return out
def erasure(g,h):return erasure_coeffs(wht(g),wht(h))
SCALE=1<<128
def outward(lo,hi):
    a=lo*SCALE;b=hi*SCALE
    return Q(a.numerator//a.denominator,SCALE),Q(-((-b.numerator)//b.denominator),SCALE)
@lru_cache(None)
def ln(x):
    x=Q(x)
    if x<1:
        a,b=ln(1/x);return -b,-a
    e=0
    while x>=2:x/=2;e+=1
    def series(t):
        z=(t-1)/(t+1)
        lo=sum((2*z**(2*k+1)/(2*k+1) for k in range(16)),Q(0))
        return lo,lo+2*z**33/(33*(1-z*z))
    a,b=series(x);a2,b2=series(Q(2))
    return outward(a+e*a2,b+e*b2)
def bounds(ledger):
    lo=hi=Q(0)
    for r,m in ledger.items():
        a,b=ln(r);x,y=ln(1-r)
        lo+=m*(-r*b-(1-r)*y);hi+=m*(-r*a-(1-r)*x)
    return lo,hi
def gap(ledger,d,K):
    lo,hi=bounds(ledger);a,b=ln(Q(2))
    return outward(lo-K*d*b,hi-K*d*a)
def influence(a):
    n=(len(a)-1).bit_length()
    return sum(Q(sum(a[x]!=a[x^(1<<j)] for x in range(len(a))),len(a)) for j in range(n))
def point_branch(g,h,j):
    rho=Q(1,1<<(j-1));gamma=Q(sum(x!=y for x,y in zip(g,h)),len(g));d=rho*gamma
    gc,hc=wht(g),wht(h)
    ledger=erasure_coeffs(gc,[x+rho*(y-x) for x,y in zip(gc,hc)])
    add(ledger,Q(1,2),2*(1-rho)*d)
    return ledger,d

def main():
    paircases=0;good6=good7=irrelevant=0;cert=[]
    for gw in range(16):
        g=tuple(-1 if gw>>x&1 else 1 for x in range(4))
        eta=Q(sum(x==-1 for x in g),4)
        for hw in range(16):
            h=tuple(-1 if hw>>x&1 else 1 for x in range(4))
            gamma=Q(sum(x!=y for x,y in zip(g,h)),4)
            for j in range(1,7):
                cap();ledger,d=point_branch(g,h,j)
                # Actual remaining-selector tables, no compressed formula.
                first=g*(1<<(j-1));second=h+g*((1<<(j-1))-1)
                assert ledger==erasure(first,second)
                assert d==Q(sum(x!=y for x,y in zip(first,second)),len(first))
                paircases+=1
                if not gamma:
                    assert not ledger;irrelevant+=1;continue
                K=6 if eta*5<=gamma else 7 if eta<=gamma else None
                if K:
                    lo,hi=gap(ledger,d,K);assert hi<0
                    good6+=K==6;good7+=K==7
                    cert.append({'G_word':gw,'H_word':hw,'selector_remaining':j,'eta':str(eta),'gamma':str(gamma),'K':K,'ln2_gap_lower':str(lo),'ln2_gap_upper':str(hi)})
    sharp=[]
    for m in range(4,22,2):
        delta=Q(1,1<<m);a=Q(1,1<<(m//2));N=1<<m
        ledger={}
        for sign,mult in ((1,(N+(1<<(m//2)))//2),(-1,(N-(1<<(m//2)))//2)):
            r,mass=row(sign*a,sign*a-2*delta);add(ledger,r,mass*mult)
        lo,hi=gap(ledger,delta,m-2);assert lo>0
        sharp.append({'m':m,'eta':'1/2','gamma':str(delta),'contrast':str(Q(1,2)/delta),'lower_price':m-2,'ln2_scaled_surplus_lower':str(lo),'ln2_scaled_surplus_upper':str(hi)})
    # Full direct-cube replay of A023's one-use boundary sublemma.
    review=[]
    cores=((1,-1),tuple((-1 if x&1 else 1)*(-1 if ((x>>1)&1)*((x>>2)&1) else 1) for x in range(8)))
    for L,R,T in product(range(1,4),repeat=3):
        p,q,r=Q(1,1<<L),Q(1,1<<R),Q(1,1<<T)
        eta=p*q*r;beta=q+r-q*r;e=beta-eta;pi=(beta+eta)/2
        JB=(L+R+T)*eta;JC=R*q*(1-r)+T*r*(1-q)
        assert eta/e<=Q(1,5)
        def points(x):
            W=int(x&((1<<L)-1)==0)
            U=int((x>>L)&((1<<R)-1)==0)
            V=int((x>>(L+R))&((1<<T)-1)==0)
            return W*U*V,int(U or V)
        n=L+R+T
        pair=[points(x) for x in range(1<<n)]
        D=[c-b for b,c in pair]
        assert influence([1-2*x for x in D])/2==JB+JC
        for core in cores:
            fp=[1+c*(g-1) for b,c in pair for g in core]
            fm=[1+b*(g-1) for b,c in pair for g in core]
            Ig=influence(core);face=influence([x*y for x,y in zip(fp,fm)])/2
            assert face==(JB+JC+e*Ig)/2
            assert face<=(JB+JC)/2+pi*Ig
            assert influence(tuple(fp)+tuple(fm))==e/2+(JB+JC)/2+pi*Ig
            review.append({'L':L,'R':R,'T':T,'core_dimension':(len(core)-1).bit_length(),'face':str(face),'owned_reserve':str((JB+JC)/2+pi*Ig)})
    out={'status':'PASS','helper_version':'A021-relative-bias-v1','ordered_two_bit_branch_pairs':256,'selector_widths':[1,2,3,4,5,6],'actual_node_decompositions':paircases,'strict_K6_certificates':good6,'strict_K7_certificates':good7,'irrelevant_selector_cases':irrelevant,'sharp_bent_cases':len(sharp),'A023_boundary_reconstructions':len(review),'seconds':time.perf_counter()-START,'arithmetic':'Fraction; exact integer Walsh; natural-log atanh tail and outward dyadic128 intervals; no float sign decisions'}
    assert out['seconds']<60
    for name,obj in [('validation.json',out),('relative_bias_certificates.json',cert),('sharpness_certificates.json',sharp),('A023_boundary_certificates.json',review)]:
        (ROOT/'out'/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
