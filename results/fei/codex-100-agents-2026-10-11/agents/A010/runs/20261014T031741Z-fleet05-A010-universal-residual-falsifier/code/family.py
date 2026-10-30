from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
from math import factorial
from collections import defaultdict
from functools import lru_cache
import json,time,sys
from logs import log2_bounds as logs,dyadic,z_bounds
OUT=Path(__file__).resolve().parents[1]/'out'; ZLO,ZHI=z_bounds()

def fwht(a):
    h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h): a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
        h*=2
    return a
def wstar(m,hub,k,z):
    lam=Q(1,m)
    if not hub: return (lam/8)**k
    if not k: return Q(1,8)
    return Q(factorial(k),2**(k+3))*lam**k*(z**(k-1)+(m-k)*lam*z**k)
def nstar(m,hub,k):
    if not hub: return Q(1,32*m)**k
    if not k: return Q(1,32)
    return Q(factorial(k-1),3*8**k*m**k*k*(k+1))
def direct_star_poly(m,A):
    hub=A&1; leaves=[j-1 for j in range(1,m+1) if A>>j&1]; terms=defaultdict(Q)
    if not hub:
        return {(len(leaves),0):Q(1,8)**len(leaves)}
    for root in range(m):
        used=set(leaves)|{root}; children=sorted(used-{root}); rank_power=sum(j!=root for j in leaves)
        alpha=Q(1,4) if root in leaves else Q(1,2); alpha*=Q(1,2)**len(children)
        # All children attach at the selected hub; actual chronological draws distinguish permutations.
        for sequence in permutations(children):
            terms[len(used),rank_power]+=alpha/4
    return dict(terms)
def closed_star_poly(m,hub,k):
    if not hub: return {(k,0):Q(1,8)**k}
    if not k: return {(1,0):Q(m,8)}
    p={(k,k-1):Q(factorial(k),2**(k+3))}
    if m>k: p[k+1,k]=Q((m-k)*factorial(k),2**(k+3))
    return p
@lru_cache(maxsize=4096)
def logarithm_interval(x): return logs(x)

def case(m):
    n=m+3; ssize=1<<(m+1); size=1<<n
    star=[1 if x&1 and x>>1 else -1 for x in range(ssize)]; astar=fwht(star[:])
    pairfalse=fwht([1,1,1,0]); table=[1 if (x&1 and ((x>>1)&((1<<m)-1))) or (x>>(m+1))==3 else -1 for x in range(size)]; a=fwht(table[:])
    u=Q(1,1<<m); q=(1+u)/2; istar=1+(m-1)*u; I=Q(3,4)*istar+q; V=3*q*(1-Q(3,4)*q); eta=Q(3,4)*q
    assert I==Q(5,4)+Q(3*m-1,4)*u and I<=Q(25,16)
    assert sum(c*c for c in a)==size*size
    groups=defaultdict(Q)
    for A,c in enumerate(a):
        As=A&(ssize-1); Ap=A>>(m+1)
        hs=q if not As else -Q(astar[As],2*ssize); hp=Q(pairfalse[Ap],4)
        expected=1-2*hs*hp if not A else -2*hs*hp
        assert Q(c,size)==expected
        if not A: continue
        k=(As>>1).bit_count(); h=bool(As&1); pt=Ap.bit_count(); p=Q(c*c,size*size)
        groups[h,k,pt]+=p
    assert sum(groups.values())==V
    assert sum(p*(k+h+pt) for (h,k,pt),p in groups.items())==I
    assert sum(p for (h,k,pt),p in groups.items() if pt)==eta
    edge_counts=[sum(table[x]!=table[x^(1<<j)] for x in range(size) if not(x>>j&1)) for j in range(n)]
    assert sum(Q(c,1<<(n-1)) for c in edge_counts)==I
    assert Q(edge_counts[0],1<<(n-1))==Q(3,4)*(1-u)
    assert all(Q(c,1<<(n-1))==Q(3,4)*u for c in edge_counts[1:m+1])
    assert all(Q(c,1<<(n-1))==q/2 for c in edge_counts[m+1:])
    if m<=4:
        for As in range(1,ssize): assert direct_star_poly(m,As)==closed_star_poly(m,bool(As&1),(As>>1).bit_count())
    Ds=(1+Q(1,4*m))**m-1; Du=(1+Q(1,4*m))**(m+1)-1; Dr=(1+Ds)*Q(5,4)-1
    beta=4*eta*Ds/((1+Ds)*(V-eta)); assert Q(8,15)<beta<Q(8,9)
    assert beta==Q(4,3)*Ds/((1+Ds)*(1-q))
    # Exact derivative numerator vanishes at the rational global slice optimizer.
    assert (V-eta)*(1+Ds)*beta/4-eta*Ds==0
    result={}
    for name,b in [('uniform',Q(1,m)),('repair',Q(1)),('slice_optimum',beta)]:
        D=Ds+(1+Ds)*b/4; dl,dh=logs(D); rlo,rhi=V*dl,V*dh; clo,chi=V*dl,V*dh
        for (hub,k,pt),p in groups.items():
            wl,wh=wstar(m,hub,k,ZLO),wstar(m,hub,k,ZHI)
            ns=nstar(m,hub,k)
            if pt: wl*=b/(8 if pt==1 else 16); wh*=b/(8 if pt==1 else 16); ns*=b/(32 if pt==1 else 48)
            ll,_=logarithm_interval(wl); _,hh=logarithm_interval(wh)
            nl,nh=logarithm_interval(ns)
            rlo-=p*hh; rhi-=p*ll; clo-=p*nh; chi-=p*nl
        assert chi<=11*I
        assert rhi<=chi and rlo>=-logs(Q(72))[1]*I
        result[name]={'lambda_isolated':str(b),'R_over_I_interval':[str(dyadic(rlo/I,False)),str(dyadic(rhi/I,True))],'complete_star_cost_over_I_interval':[str(dyadic(clo/I,False)),str(dyadic(chi/I,True))],'display_R_over_I':float((rlo+rhi)/(2*I))}
    # Exact posterior transfer: only the isolated-edge sector picks up beta.
    transfer_lo=eta*logs(Q(m))[0]+V*logs(Du/Dr)[0]
    transfer_hi=eta*logs(Q(m))[1]+V*logs(Du/Dr)[1]
    diff_lo=Q(result['uniform']['R_over_I_interval'][0])*I-Q(result['repair']['R_over_I_interval'][1])*I
    diff_hi=Q(result['uniform']['R_over_I_interval'][1])*I-Q(result['repair']['R_over_I_interval'][0])*I
    assert diff_lo<=transfer_hi and transfer_lo<=diff_hi
    assert eta/I>=Q(7,25)
    log2_bounds_cache=logarithm_interval.cache_info().currsize
    return {'m':m,'n':n,'physical_inputs':size,'I':str(I),'variance':str(V),'isolated_sector_mass':str(eta),'exact_slice_optimum':str(beta),'vectors':result,'complete_posterior_transfer_interval':[str(dyadic(transfer_lo,False)),str(dyadic(transfer_hi,True))]}

if __name__=='__main__':
    pilot='pilot' in sys.argv; start=time.monotonic(); rows=[]
    for m in range(2,4 if pilot else 11):
        assert time.monotonic()-start<(60 if pilot else 300)
        rows.append(case(m)); (OUT/'family_checkpoint.json').write_text(json.dumps(rows,indent=2))
        logarithm_interval.cache_clear(); logs.cache_clear()
    scalar=[]
    for m in range(2,129):
        assert (42*m-89)<=5*2**m
        assert (m+1)*(m+6)<=6*2**m
        Ds=(1+Q(1,4*m))**m-1; q=(1+Q(1,1<<m))/2
        beta=Q(4,3)*Ds/((1+Ds)*(1-q)); assert Q(8,15)<beta<Q(8,9)
        scalar.append({'m':m,'slice_optimum':str(beta)})
    result={'cases':len(rows),'physical_inputs':sum(r['physical_inputs'] for r in rows),'rows':rows,'scalar_optima':scalar,'z_interval':[str(ZLO),str(ZHI)],'elapsed_seconds':time.monotonic()-start,'uniform_all_posterior_lower':'R/I > (7/25)log2 m-9; m=2^(25t) gives >7t-9','variational_repair':'Same primes and orders; R<=C_MS<=11I, all m>=2','slice_scope':'Exact global optimum in isolated-edge positive weight with star weights held at1/m, not all edge weights'}
    (OUT/('family_pilot.json' if pilot else 'family.json')).write_text(json.dumps(result,indent=2)); print(json.dumps({k:v for k,v in result.items() if k not in ['rows','scalar_optima']},indent=2))
