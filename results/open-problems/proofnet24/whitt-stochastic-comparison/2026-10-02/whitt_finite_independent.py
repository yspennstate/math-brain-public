"""Independent exact certificate using a killed finite CTMC, not a QBD root.

Only Fraction arithmetic decides the bounds. A slow M/M/2 coupling bounds
the stationary mass outside the finite set. Occupation ratios of the killed
chain bound the stationary conditional probability inside that set.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
import json

def z(n,m): return [[F(0) for _ in range(m)] for _ in range(n)]
def mm(a,b): return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def sub(a,b): return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def inverse(a):
    n=len(a); w=[row[:]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        h=next(i for i in range(j,n) if w[i][j]); w[j],w[h]=w[h],w[j]
        v=w[j][j]; w[j]=[x/v for x in w[j]]
        for i in range(n):
            if i!=j:
                v=w[i][j]; w[i]=[x-v*y for x,y in zip(w[i],w[j])]
    out=[row[n:] for row in w]
    assert mm(a,out)==[[F(i==j) for j in range(n)] for i in range(n)]
    return out
def dec(a):
    with localcontext() as c:
        c.prec=45
        return str(Decimal(a.numerator)/Decimal(a.denominator))

def certificate(name,arrival,small_probability,small_rate,large_rate,N=80):
    la,p,us,ul=map(F,(arrival,small_probability,small_rate,large_rate))
    # Blocks of -Q restricted to counts 0,...,N, killed at an arrival from N.
    dims=[1,2]+[3]*(N-1)
    lower=[None]+[z(dims[n],dims[n-1]) for n in range(1,N+1)]
    diag=[z(d,d) for d in dims]
    upper=[z(dims[n],dims[n+1]) for n in range(N)]+[None]
    diag[0][0][0]=la
    upper[0][0]=[-la*p,-la*(1-p)]
    for j,u in enumerate((us,ul)):
        diag[1][j][j]=la+u
        lower[1][j][0]=-u
        # At count 1, j=0 is small, j=1 is large.
        old_small=1-j
        upper[1][j][old_small+1]=-la*p
        upper[1][j][old_small]=-la*(1-p)
    for n in range(2,N+1):
        for small_count in range(3):
            i=small_count
            diag[n][i][i]=la+i*us+(2-i)*ul
            if n<N: upper[n][i][i]=-la
            for completed_small in (False,True):
                count=i if completed_small else 2-i
                rate=us if completed_small else ul
                if not count: continue
                remaining_small=i-int(completed_small)
                if n==2:
                    # Count 1 phase index: small=0, large=1.
                    lower[n][i][1-remaining_small]-=count*rate
                else:
                    lower[n][i][remaining_small+1]-=count*rate*p
                    lower[n][i][remaining_small]-=count*rate*(1-p)
    # Verify rows including the killing rate conserve mass.
    for n in range(N+1):
        for i in range(dims[n]):
            rs=sum(diag[n][i],F(0))
            if n: rs+=sum(lower[n][i],F(0))
            if n<N: rs+=sum(upper[n][i],F(0))
            assert rs==(la if n==N else 0)
    reward=[[[F(1),F(n>=2)] for _ in range(dims[n])] for n in range(N+1)]
    binv=[]; transformed=[]
    for n in range(N+1):
        b=diag[n]; r=reward[n]
        if n:
            mult=mm(lower[n],binv[-1])
            b=sub(b,mm(mult,upper[n-1]))
            r=sub(r,mm(mult,transformed[-1]))
        binv.append(inverse(b)); transformed.append(r)
    occupation=[None]*(N+1)
    for n in reversed(range(N+1)):
        r=transformed[n]
        if n<N: r=sub(r,mm(upper[n],occupation[n+1]))
        occupation[n]=mm(binv[n],r)
    # Independently check exact backward equations and positivity.
    for n in range(N+1):
        lhs=mm(diag[n],occupation[n])
        if n:
            t=mm(lower[n],occupation[n-1]); lhs=[[x+y for x,y in zip(a,b)] for a,b in zip(lhs,t)]
        if n<N:
            t=mm(upper[n],occupation[n+1]); lhs=[[x+y for x,y in zip(a,b)] for a,b in zip(lhs,t)]
        assert lhs==reward[n]
        assert all(a>0 and 0<b<a for a,b in occupation[n])
    ratios=[b/a for a,b in occupation[N]]
    # Couple every service with an Exp(ul) service, sharing the Exp(1)
    # multiplier and arrival order. Kiefer-Wolfowitz recursion gives earlier
    # starts and departures in the original queue, hence lower total count.
    assert us>=ul
    rho=la/(2*ul); assert 0<rho<1
    slow_delay=2*rho*rho/(1+rho)
    tail=slow_delay*rho**(N-1)  # slow M/M/2 probability count>N
    lo=(1-tail)*min(ratios)
    hi=max(ratios)+tail
    assert 0<lo<hi<1
    return lo,hi,{
        'model':name,'maximum_count':N,'arithmetic':'Fraction exact rational',
        'method':'killed finite CTMC occupation / mass outside bound',
        'stationary_outside_mass_upper_display':dec(tail),
        'entry_phase_delay_ratios_display':[dec(v) for v in ratios],
        'delay_lower_display':dec(lo),'delay_upper_display':dec(hi),
        'checks':['generator rows','exact backward equations','positive occupations',
                  'slow M/M/2 count domination','stationary flux occupation identity']}

if __name__=='__main__':
    al,au,a=certificate('base',F(11,10),F(3,7),F(5),F(5,8))
    bl,bu,b=certificate('spread',F(121,140),F(3,11),F(5,2),F(5,8))
    gap=al-bu
    assert gap>F(11,10000)
    print(json.dumps({'models':[a,b],'gap_lower_display':dec(gap),
                      'exact_claim':'P_delay(base)-P_delay(spread)>11/10000'},indent=2))
