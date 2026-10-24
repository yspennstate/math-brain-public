"""Strictly positive service counterexample: exact finite CTMC certificate.

General unordered service phase construction; no QBD root is used.
Requires whitt_finite_independent.py for elementary Fraction matrix helpers.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
import json
from whitt_finite_independent import z,mm,sub,inverse,dec

def certify(name,arrival,probabilities,rates,N=80):
    la=F(arrival); p=list(map(F,probabilities)); mu=list(map(F,rates))
    k=len(p); assert k==len(mu) and sum(p)==1 and min(p)>0 and min(mu)>0
    pairs=list(combinations_with_replacement(range(k),2)); pairidx={a:i for i,a in enumerate(pairs)}
    d=len(pairs); dims=[1,k]+[d]*(N-1)
    A=[None]+[z(dims[n],dims[n-1]) for n in range(1,N+1)]
    B=[z(v,v) for v in dims]; C=[z(dims[n],dims[n+1]) for n in range(N)]+[None]
    B[0][0][0]=la
    for a in range(k):
        C[0][0][a]=-la*p[a]
        B[1][a][a]=la+mu[a]; A[1][a][0]=-mu[a]
        for b in range(k): C[1][a][pairidx[tuple(sorted((a,b)))]]-=la*p[b]
    for n in range(2,N+1):
        for i,pair in enumerate(pairs):
            B[n][i][i]=la+sum(mu[a] for a in pair)
            if n<N: C[n][i][i]=-la
            for slot in range(2):
                completing=pair[slot]; remaining=pair[1-slot]
                if n==2: A[n][i][remaining]-=mu[completing]
                else:
                    for b in range(k): A[n][i][pairidx[tuple(sorted((remaining,b)))]]-=mu[completing]*p[b]
    for n in range(N+1):
        for i in range(dims[n]):
            rs=sum(B[n][i],F(0))
            if n: rs+=sum(A[n][i],F(0))
            if n<N: rs+=sum(C[n][i],F(0))
            assert rs==(la if n==N else 0)
    rhs=[[[F(1),F(n>=2)] for _ in range(dims[n])] for n in range(N+1)]
    bi=[]; rt=[]
    for n in range(N+1):
        b=B[n]; r=rhs[n]
        if n:
            t=mm(A[n],bi[-1]); b=sub(b,mm(t,C[n-1])); r=sub(r,mm(t,rt[-1]))
        bi.append(inverse(b)); rt.append(r)
    h=[None]*(N+1)
    for n in reversed(range(N+1)):
        r=rt[n]
        if n<N: r=sub(r,mm(C[n],h[n+1]))
        h[n]=mm(bi[n],r)
    for n in range(N+1):
        lhs=mm(B[n],h[n])
        for t in ([mm(A[n],h[n-1])] if n else [])+([mm(C[n],h[n+1])] if n<N else []):
            lhs=[[x+y for x,y in zip(a,b)] for a,b in zip(lhs,t)]
        assert lhs==rhs[n]
        assert all(a>0 and 0<b<a for a,b in h[n])
    r=[b/a for a,b in h[N]]
    rho=la/(2*min(mu)); assert rho<1
    tail=2*rho*rho/(1+rho)*rho**(N-1)
    # Outside the finite set every state has both servers busy, so the exact
    # stationary delay probability is rbar+delta*(1-rbar).
    lo=min(r); hi=max(r)+tail*(1-max(r))
    return lo,hi,{'model':name,'arrival':str(la),'probabilities':list(map(str,p)),
                 'rates':list(map(str,mu)),'maximum_count':N,'busy_phases':d,
                 'slow_queue_tail_upper_display':dec(tail),
                 'delay_lower_display':dec(lo),'delay_upper_display':dec(hi),
                 'entry_phase_ratios_display':[dec(a) for a in r],
                 'checks':['all generator rows','exact backward equations',
                           'positive occupations','slow exponential service domination',
                           'stationary incoming flux / occupation identity']}

if __name__=='__main__':
    base_lo,base_hi,a=certify('base_positive_H2',F(11,10),[F(3,7),F(4,7)],[F(5),F(5,8)])
    spread_lo,spread_hi,b=certify('spread_positive_H3',F(11,10),[F(3,14),F(3,14),F(4,7)],[F(1000),F(1000,399),F(5,8)])
    assert base_lo>F(39287,100000)
    assert base_hi<F(39290,100000)
    assert spread_lo>F(39172,100000)
    assert spread_hi<F(39175,100000)
    gap=base_lo-spread_hi; assert gap>F(11,10000)
    print(json.dumps({'arithmetic':'exact Fraction; displayed decimals are not used to decide assertions',
                      'models':[a,b],'gap_lower_display':dec(gap),
                      'exact_assertions':['.39287<P_delay(base)<.39290',
                                          '.39172<P_delay(spread)<.39175',
                                          'P_delay(base)-P_delay(spread)>11/10000'],
                      'service_distributions':'strictly positive exponential mixtures',
                      'convex_order':'on short branch replace .2E by .001E or .399E with probability 1/2 each; unchanged long branch'},indent=2))
