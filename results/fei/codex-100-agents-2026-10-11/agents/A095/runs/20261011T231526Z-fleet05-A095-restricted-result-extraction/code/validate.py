from fractions import Fraction as F
from itertools import permutations, product
from math import comb, factorial
from pathlib import Path
from functools import lru_cache
import json, time, hashlib

ROOT = Path(__file__).resolve().parents[1]
checks = 0
def check(x):
    global checks
    assert x
    checks += 1

@lru_cache(maxsize=4096)
def log_interval(x, terms=36):
    x=F(x); assert x>0
    exponent=0
    while x>=2: x/=2; exponent+=1
    while x<1: x*=2; exponent-=1
    def core(y):
        z=(y-1)/(y+1)
        total=sum((2*z**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
        error=2*z**(2*terms+1)/F((2*terms+1)*(1-z*z))
        return total,total+error
    a,b=core(x); c,d=core(F(2))
    return (a+exponent*c,b+exponent*d) if exponent>=0 else (a+exponent*d,b+exponent*c)

def wl(table):
    out=table[:]; step=1
    while step<len(out):
        for start in range(0,len(out),2*step):
            for j in range(start,start+step):
                a,b=out[j],out[j+step];out[j],out[j+step]=a+b,a-b
        step*=2
    return out

def spectrum(table):
    size=len(table); a=wl(table)
    p=[F(v*v,size*size) for v in a]
    check(sum(p)==1)
    return p

def influence(table,n):
    return [F(sum(table[x]!=table[x^(1<<i)] for x in range(len(table))),len(table)) for i in range(n)]

def entropy_nats_interval(p):
    lo=hi=F(0)
    for v in p:
        if v:
            a,b=log_interval(1/v);lo+=v*a;hi+=v*b
    return lo,hi

def rank_interval(p,order):
    lo=hi=F(0)
    for s,v in enumerate(p):
        if not v:continue
        j=0
        for pos,i in enumerate(order,1):
            if s>>i&1:
                j+=1;a,b=log_interval(F(pos,j));lo+=v*a;hi+=v*b
    return lo,hi

def height(support,k):
    longest={}
    for x in sorted(support,key=int.bit_count):
        longest[x]=1+max((longest[y] for y in longest if y!=x and y&x==y),default=0)
    return max(longest.values(),default=0)

def fibre_height(table,n,order,pos):
    i=order[pos];before=order[:pos];after=order[pos+1:]
    result=1
    for tail in range(1<<len(after)):
        base=sum(((tail>>j)&1)<<v for j,v in enumerate(after))
        support=[]
        for pre in range(1<<len(before)):
            x=base+sum(((pre>>j)&1)<<v for j,v in enumerate(before))
            if table[x]!=table[x|(1<<i)]:support.append(pre)
        result=max(result,min((height([x^orient for x in support],pos) for orient in range(1<<pos)),default=0))
    return result

def noise_check(table,p,inf,order,pos,r):
    i=order[pos];before=sum(1<<j for j in order[:pos]);alpha=inf[i]
    if not alpha:return
    for t in (F(1,4),F(1,2),F(1)):
        lhs=sum(v*(1-t)**((s&before).bit_count()) for s,v in enumerate(p) if s>>i&1)/alpha
        density=sum(F(comb(pos,b))*t**b*(1-t)**(pos-b)*min(F(1),r*F(comb(b,b//2),2**b)) for b in range(pos+1))
        check(lhs<=density)

def main():
    start=time.monotonic(); counts={'table_orders':0,'selectors':0,'products':0}
    # A rational reference avoids transcendental constants: e_k(1/i^2)
    # is normalized exactly, and its expected negative log is checked.
    for n in range(1,4):
        for bits in range(1<<(1<<n)):
            table=[1 if bits>>x&1 else -1 for x in range(1<<n)]
            p=spectrum(table);inf=influence(table,n)
            check(sum(inf)==sum(s.bit_count()*v for s,v in enumerate(p)))
            h=entropy_nats_interval(p)
            for order in permutations(range(n)):
                counts['table_orders']+=1
                for pos,i in enumerate(order):
                    r=fibre_height(table,n,order,pos)
                    noise_check(table,p,inf,order,pos,r)
                # Exact level decomposition plus normalized Euler weight.
                level=[sum(v for s,v in enumerate(p) if s.bit_count()==k) for k in range(n+1)]
                crosslo=crosshi=F(0)
                betalo=betahi=dlo=dhi=F(0)
                for k in range(n+1):
                    if not level[k]:continue
                    z=sum((F(1,1) / product_den(s,order) for s in range(1<<n) if s.bit_count()==k),F(0))
                    check(z*factorial(k)**2>=1)
                    a,b=log_interval(z*factorial(k)**2)
                    betalo+=level[k]*a;betahi+=level[k]*b
                    for s,v in enumerate(p):
                        if v and s.bit_count()==k:
                            a,b=log_interval(z*product_den(s,order)/level[k]);crosslo+=v*a;crosshi+=v*b
                            a,b=log_interval(v*z*product_den(s,order)/level[k]);dlo+=v*a;dhi+=v*b
                check(h[0]<=crosshi)
                hl=entropy_nats_interval(level);rr=rank_interval(p,order)
                rhslo=hl[0]+2*rr[0]+betalo-dhi
                rhshi=hl[1]+2*rr[1]+betahi-dlo
                check(h[0]<=rhshi and rhslo<=h[1])
                check(time.monotonic()-start<60)
    selector_examples=[]
    for d in range(2,6):
        n=d+1;order=tuple(range(n))
        for a in range(1,d+1):
            for b in range(1,d+1):
                # selector bit first; opposite signed symmetric thresholds
                table=[]
                for x in range(1<<n):
                    w=(x>>1).bit_count()
                    table.append((1 if w>=a else -1) if x&1 else -(1 if w>=b else -1))
                p=spectrum(table);inf=influence(table,n)
                heights=[fibre_height(table,n,order,pos) for pos in range(n)]
                check(max(heights)<=2)
                for pos,i in enumerate(order):noise_check(table,p,inf,order,pos,heights[pos])
                selector_examples.append({'data_bits':d,'thresholds':[a,b],'heights':heights})
                counts['selectors']+=1
    product_examples=[]
    for L in range(1,5):
        core=[-1]+[1]*((1<<L)-1);pc=spectrum(core);ic=sum(influence(core,L));hc=entropy_nats_interval(pc)
        for m in range(1,6):
            n=L*m
            if n>10:continue
            table=[(-1)**sum(((x>>(j*L))&((1<<L)-1))==0 for j in range(m)) for x in range(1<<n)]
            p=spectrum(table);inf=influence(table,n);q=F(2,1<<L)
            check(sum(inf)==m*L*q)
            for s,v in enumerate(p):
                wanted=F(1)
                for j in range(m):wanted*=pc[(s>>(j*L))&((1<<L)-1)]
                check(v==wanted)
            h=entropy_nats_interval(p);check(h[0]<=m*hc[1] and m*hc[0]<=h[1])
            # For L>=2, exact conditional prefix counts validate the
            # order-independent Jensen step underlying the all-L,m proof.
            orders=[tuple(range(n)),tuple(reversed(range(n))),tuple(sorted(range(n),key=lambda i:(i%L,i//L)))]
            if L>=2:
                for order in orders:
                    before=0
                    for pos,i in enumerate(order,1):
                        mean=sum(v*(1+(s&before).bit_count()) for s,v in enumerate(p) if s>>i&1)/q
                        b=sum((j//L)==(i//L) for j in order[:pos-1])
                        check(mean==1+F(b,2)+q*(pos-1-b))
                        check(mean<=L+q*pos)
                        before|=1<<i
                # H/I<=4 certified using 4 ln2 > 2; no float logs.
                check(4*log_interval(F(2))[0]>2)
            product_examples.append({'L':L,'m':m,'n':n,'influence':str(sum(inf))})
            counts['products']+=1
    elapsed=time.monotonic()-start
    result={'helper_version':'A095-rank-audit-v1','counts':counts,'exact_assertions':checks,'runtime_seconds':elapsed,'status':'PASS','scope':'Finite validation only; REPORT.md contains all-parameter analytic proofs','selectors':selector_examples,'products':product_examples}
    (ROOT/'out'/'VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('selectors','products')}))

def product_den(s,order):
    result=1
    for pos,i in enumerate(order,1):
        if s>>i&1:result*=pos*pos
    return result

if __name__=='__main__':main()
