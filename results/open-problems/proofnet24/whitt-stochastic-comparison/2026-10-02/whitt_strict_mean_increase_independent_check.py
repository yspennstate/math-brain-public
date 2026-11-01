"""Independent exact audit of the strict-mean Whitt witness.

Builds phases by small-job counts, rather than unordered class pairs.
Derives rates from the literal service means and uses independent block
linear solves without importing the production certificate helpers.
"""
from fractions import Fraction as F
import json
from decimal import Decimal, localcontext

def zero(n,m):return [[F(0) for _ in range(m)] for _ in range(n)]
def multiply(a,b):
    return [[sum((x*b[k][j] for k,x in enumerate(row)),F(0))
             for j in range(len(b[0]))] for row in a]
def subtract(a,b):return [[x-y for x,y in zip(ar,br)]for ar,br in zip(a,b)]
def solve(a,b):
    n=len(a); width=len(b[0]); rows=[ar.copy()+br.copy() for ar,br in zip(a,b)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if rows[i][j])
        rows[j],rows[pivot]=rows[pivot],rows[j]
        v=rows[j][j]; rows[j]=[x/v for x in rows[j]]
        for i in range(n):
            if i!=j:
                v=rows[i][j]; rows[i]=[x-v*y for x,y in zip(rows[i],rows[j])]
    answer=[row[n:n+width] for row in rows]
    assert multiply(a,answer)==b
    return answer
def display(x):
    with localcontext() as ctx:
        ctx.prec=55
        return str(Decimal(x.numerator)/Decimal(x.denominator))

def certificate(arrival,probability,small_mean,large_mean,N=80):
    la,p,a,b=map(F,(arrival,probability,small_mean,large_mean))
    us,ul=1/a,1/b
    dims=[1,2]+[3]*(N-1)
    down=[None]+[zero(dims[n],dims[n-1])for n in range(1,N+1)]
    diagonal=[zero(d,d)for d in dims]
    up=[zero(dims[n],dims[n+1])for n in range(N)]+[None]
    reward=[[[F(1),F(n>=2)]for _ in range(d)]for n,d in enumerate(dims)]
    for n,d in enumerate(dims):
        for i in range(d):
            busy=min(n,2)
            rate=i*us+(busy-i)*ul
            diagonal[n][i][i]=la+rate
            if n<N:
                if n<2:
                    up[n][i][i+1]-=la*p
                    up[n][i][i]-=la*(1-p)
                else:up[n][i][i]=-la
            if n:
                if n<=2:
                    if i:down[n][i][i-1]-=i*us
                    if busy-i:down[n][i][i]-=(busy-i)*ul
                else:
                    if i:
                        down[n][i][i]-=i*us*p
                        down[n][i][i-1]-=i*us*(1-p)
                    if 2-i:
                        down[n][i][i+1]-=(2-i)*ul*p
                        down[n][i][i]-=(2-i)*ul*(1-p)
    for n,d in enumerate(dims):
        for i in range(d):
            rowmass=sum(diagonal[n][i],F(0))
            if n:rowmass+=sum(down[n][i],F(0))
            if n<N:rowmass+=sum(up[n][i],F(0))
            assert rowmass==(la if n==N else 0)
    transfer=[]; constant=[]
    for n in range(N+1):
        aa=diagonal[n]
        rr=reward[n]
        if n:
            aa=subtract(aa,multiply(down[n],transfer[n-1]))
            rr=subtract(rr,multiply(down[n],constant[n-1]))
        outgoing=up[n]if n<N else zero(dims[n],0)
        combined=[x+y for x,y in zip(outgoing,rr)]
        result=solve(aa,combined)
        w=len(outgoing[0])
        transfer.append([row[:w]for row in result])
        constant.append([row[w:]for row in result])
    occupation=[None]*(N+1)
    for n in range(N,-1,-1):
        occupation[n]=constant[n]if n==N else subtract(constant[n],multiply(transfer[n],occupation[n+1]))
    for n in range(N+1):
        lhs=multiply(diagonal[n],occupation[n])
        if n:
            add=multiply(down[n],occupation[n-1])
            lhs=[[x+y for x,y in zip(ar,br)]for ar,br in zip(lhs,add)]
        if n<N:
            add=multiply(up[n],occupation[n+1])
            lhs=[[x+y for x,y in zip(ar,br)]for ar,br in zip(lhs,add)]
        assert lhs==reward[n]
        assert all(0<g<h for h,g in occupation[n])
    ratios=[g/h for h,g in occupation[N]]
    rho=la*max(a,b)/2
    assert rho<1
    tail=2*rho*rho/(1+rho)*rho**(N-1)
    lo=min(ratios); hi=max(ratios)+tail*(1-max(ratios))
    return lo,hi,{'arrival':str(la),'small_probability':str(p),
                  'small_service_mean':str(a),'large_service_mean':str(b),
                  'mean_service':str(p*a+(1-p)*b),
                  'derived_small_rate':str(us),'derived_large_rate':str(ul),
                  'lower':display(lo),'upper':display(hi),'tail':display(tail)}

if __name__=='__main__':
    la=F(11,10);beta=F(10001,10000)
    al,au,a=certificate(la,F(3,7),F(1,5),F(8,5))
    bl,bu,b=certificate(la,F(200,533),F(1,1000)*beta,F(8,5)*beta)
    # An additional exact time-rescaling binding check uses changed arrival
    # and original target service means. Its enclosure must be identical.
    cl,cu,c=certificate(la*beta,F(200,533),F(1,1000),F(8,5))
    assert bl==cl and bu==cu
    assert F(b['mean_service'])==beta
    gap=al-bu
    assert gap>F(12,5000)
    h=F(1,100000)
    assert gap-10*h>F(23,10000)
    print(json.dumps({'arithmetic':'independent exact Fraction generator and solver',
                      'base':a,'scaled_target':b,'time_rescaled_control':c,
                      'exact_binding':'target enclosure equals unchanged target at arrival lambda*beta',
                      'gap_lower_display':display(gap),
                      'positive_threshold_gap_lower_display':display(gap-10*h),
                      'checks':['independently generated all killed-generator rows',
                                'independent block solve','all backward equations',
                                'actual scaled service means and rates',
                                'exact time-rescaling equality','gap>12/5000',
                                'positive-threshold gap>23/10000']},indent=2))
