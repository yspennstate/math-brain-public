"""Independent referee: direct characters, literal edges, complete physical references."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from time import perf_counter
import json, sys, hashlib

BASE=Path(__file__).resolve().parents[1]
START=perf_counter(); CHECKS=0
def check(b, label):
    global CHECKS
    CHECKS+=1
    if not b: raise AssertionError(label)
    if perf_counter()-START>55: raise TimeoutError('frozen 55-second wall budget')

def ln_unit(x, terms=18):
    z=(x-1)/(x+1); zz=z*z; power=z; total=F(0)
    for j in range(terms):
        total+=power/F(2*j+1); power*=zz
    lo=2*total
    return lo,lo+2*power/F(2*terms+1)/(1-zz)
LN2=ln_unit(F(2))
@lru_cache(maxsize=20000)
def log2(x):
    assert x>0
    e=x.numerator.bit_length()-x.denominator.bit_length()
    scale=F(2)**e; y=x/scale
    if y<1: e-=1; y*=2
    if y>=2: e+=1; y/=2
    a,b=ln_unit(y)
    lo,hi=F(e)+a/LN2[1],F(e)+b/LN2[0]
    # Outward dyadic rounding preserves certification and prevents giant output fractions.
    scale=2**96
    return F(lo.numerator*scale//lo.denominator,scale),F(-((-hi.numerator*scale)//hi.denominator),scale)

def ce(P,Q):
    lo=hi=F(0)
    for p,q in zip(P,Q):
        if p:
            a,b=log2(q); lo-=p*b; hi-=p*a
    return lo,hi

def spectrum(table):
    # Direct character sums: no imported transform, recurrence or author helper.
    length=len(table)
    return tuple(F(sum(v*(-1 if (x&s).bit_count()%2 else 1)
                       for x,v in enumerate(table)),length) for s in range(length))
def influence(table):
    d=(len(table)-1).bit_length()
    return sum((F(sum(table[x]!=table[x^(1<<j)] for x in range(len(table))),len(table)) for j in range(d)),F(0))
def child(table,j,b):
    return tuple(table[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(table)//2))
def remove_mask(x,j): return (x&((1<<j)-1))|((x>>(j+1))<<j)
def bitmask_insert(x,j,b): return (x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)

def fixture(w,m):
    k=w+2; n=k+m; d=n+1; delta=F(1,2**n); N=2**k
    def g(x): return (-1 if x%(2**w)==0 else 1)*(-1 if (x>>w)%4==0 else 1)
    G=tuple(g(x) for x in range(N)); a=spectrum(G)
    table=tuple(g(x)-2*int(x==2**n) for x in range(2**d))
    coeff=spectrum(table); P=tuple(c*c for c in coeff)
    W=2*delta-N*delta*delta
    Q=tuple((1-W)*a[s]*a[s] if s<N else delta*delta for s in range(2**d))
    check(all(v in (-1,1) for v in table),'Booleanity')
    check(sum(P)==sum(Q)==1 and min(Q)>0,'complete normalization')
    for s,c in enumerate(coeff): check(c==a[s]-delta if s<N else abs(c)==delta,'old signed shift / new magnitude')
    # Signed profile independently accumulated from actual direct-character coefficients.
    A=[F(0),F(0)]; B=[F(0),F(0)]; C=[F(0),F(0)]
    for v in a:
        lo,hi=log2(1/(v*v))
        A[0]+=v*(lo if v>0 else hi); A[1]+=v*(hi if v>0 else lo)
        B[0]+=lo; B[1]+=hi; C[0]+=v*v*lo; C[1]+=v*v*hi
    q=F(2,2**w); b=1-q; lb=log2(b)
    closedA=(2+2*b*lb[0]+(2-q)*(2*w-2),2+2*b*lb[1]+(2-q)*(2*w-2))
    closedB=(-8*lb[1]+2**(w+3)*w-8*w+8,-8*lb[0]+2**(w+3)*w-8*w+8)
    check(A[0]<=closedA[1] and closedA[0]<=A[1],'signed A identity')
    check(B[0]<=closedB[1] and closedB[0]<=B[1],'unsigned B identity')
    rootce=ce(P,Q)
    check(rootce[1]<F(1005,256),'root uniform CE bound')

    # All labelled partial assignments; DP ranges over every adaptive stopping policy.
    @lru_cache(None)
    def states(assignment):
        remaining=[j for j in range(d) if assignment[j]<0]
        tab=[]
        for y in range(2**len(remaining)):
            x=sum(v<<j for j,v in enumerate(assignment) if v>=0)
            for z,j in enumerate(remaining): x|=((y>>z)&1)<<j
            tab.append(table[x])
        return tuple(tab),remaining
    @lru_cache(None)
    def minimum(assignment):
        tab,remaining=states(assignment); result=influence(tab)
        for j in range(w):
            if assignment[j]<0:
                aa=list(assignment); aa[j]=0; bb=list(assignment); bb[j]=1
                choice=(minimum(tuple(aa))+minimum(tuple(bb)))/2
                result=min(result,choice)
                # All directed next-query edges satisfy the exact influence telescope.
                local=remaining.index(j)
                avg=(influence(child(tab,local,0))+influence(child(tab,local,1)))/2
                infj=F(sum(tab[x]!=tab[x^(1<<local)] for x in range(len(tab))),len(tab))
                check(avg==influence(tab)-infj,'every physical influence edge')
        return result
    allfree=(-1,)*d; minI=minimum(allfree)
    check(minI>=F(63,64),'minimum over ALL adaptive stopping trees')
    check(4*minI-rootce[1]>F(3,256),'one-original-bank final expectation')

    # Full normalized reference histories: reverse, outcome-dependent, branch stopping.
    stats={'nodes':0,'leaves':0,'zero_true_fibers':0,'nonunit_normalizers':0}
    def walk(tab,source,Q,labels,policy,depth=0):
        co=spectrum(tab); P=tuple(c*c for c in co); before=ce(P,Q)
        options=[j for j in labels if j<w]
        if not options or (policy==2 and depth>0 and tab[0]<0):
            stats['leaves']+=1
            return influence(tab),before,0,influence(source)
        if policy==0: physical=max(options)
        else: physical=min(options) if tab[0]>0 else max(options)
        j=labels.index(physical); children=[child(tab,j,b) for b in (0,1)]
        Pb=[tuple(v*v for v in spectrum(t)) for t in children]
        p=tuple((x+y)/2 for x,y in zip(*Pb))
        r=tuple(Q[bitmask_insert(t,j,0)]+Q[bitmask_insert(t,j,1)] for t in range(len(p)))
        check(sum(p)==sum(r)==1,'true and reference marginal')
        pi=[tuple(Pb[b][t]/(2*p[t]) if p[t] else F(1,2) for t in range(len(p))) for b in (0,1)]
        raw=[tuple(2*r[t]*pi[b][t] for t in range(len(p))) for b in (0,1)]
        Z=[sum(row) for row in raw]
        check(Z[0]>0 and Z[1]>0 and sum(Z)==2,'both physical normalizers')
        stats['nonunit_normalizers']+=sum(z!=1 for z in Z)
        stats['zero_true_fibers']+=sum(v==0 for v in p)
        Qb=[tuple(v/Z[b] for v in raw[b]) for b in (0,1)]
        for b in (0,1):
            check(sum(Qb[b])==1,'child reference normalization')
            check(all(not pp or qq>0 for pp,qq in zip(Pb[b],Qb[b])),'child true-support coverage')
        if depth==0:
            # An untouched constant terminal has true-zero fibers carrying reference mass.
            Rh=(F(1,3),F(2,3)); Ph=(F(1),F(0))
            for b in (0,1):
                prod_raw=tuple(2*r[t]*Rh[u]*pi[b][t] for t in range(len(p)) for u in (0,1))
                check(sum(prod_raw)==Z[b],'product-compatible zero-fiber extension keeps normalizer')
                check(tuple(v/Z[b] for v in prod_raw)==tuple(q*rh for q in Qb[b] for rh in Rh),'entire terminal reference factors')
            changed=next(t for t in range(len(p)) if p[t] and pi[0][t]!=F(1,2))
            # Global fair fallback on terminal-zero fibers would break this product.
            check(2*r[changed]*Rh[1]*F(1,2)*Rh[0] != 2*r[changed]*Rh[0]*pi[0][changed]*Rh[1], 'adversarial naive-fallback product failure')
            stats['product_zero_fiber_witness']={'core_mask':changed,'actual_pi0':str(pi[0][changed]),'terminal_true':'[1,0]','terminal_reference':'[1/3,2/3]'}
        after=[ce(Pb[b],Qb[b]) for b in (0,1)]
        # For exact equality, verify JS=L=0 and both Z=1 directly.
        zero=Pb[0]==Pb[1] and Z==[F(1),F(1)] and all(
            not p[t] or all(P[bitmask_insert(t,j,b)]*r[t]==Q[bitmask_insert(t,j,b)]*p[t] for b in (0,1)) for t in range(len(p)))
        check(zero or before[0]-(after[0][1]+after[1][1])/2>=0,'complete CE release, no omitted zero fiber')
        newlabels=labels[:j]+labels[j+1:]
        results=[walk(children[b],child(source,j,b),Qb[b],newlabels,policy,depth+1) for b in (0,1)]
        I=(results[0][0]+results[1][0])/2
        C=((results[0][1][0]+results[1][1][0])/2,(results[0][1][1]+results[1][1][1])/2)
        # Count queried edges on the unique all-zero edited path, preserving original reach.
        t=1+results[0][2]
        stats['nodes']+=1
        return I,C,t,(results[0][3]+results[1][3])/2
    policies=[]
    for policy in range(3):
        I,C,t,originalI=walk(table,tuple(g(x) for x in range(2**d)),Q,list(range(d)),policy)
        check(I==originalI+delta*(m-w-1+t),'literal edited-edge debit identity for actual adaptive policy')
        check(originalI-1>=(w-t)*q,'edited-path lower bound retains all other leaves')
        check(C[1]<=rootce[1],'terminal average retains full CE')
        check(4*I-C[1]>F(3,256),'actual policy terminal surplus')
        policies.append({'policy':policy,'mean_I':str(I),'edited_path_t':t,'CE_upper':str(C[1]),'surplus_lower':str(4*I-C[1])})
    return {'w':w,'m':m,'partial_assignments':minimum.cache_info().currsize,'min_mean_I_all_trees':str(minI),'root_CE_upper':str(rootce[1]),'policies':policies,'transport':stats}

def main():
    domain=[(4,0)] if 'pilot' in sys.argv else [(4,0),(4,1),(5,0)]
    rows=[]; status='PASS'; error=None
    try:
        for w,m in domain: rows.append(fixture(w,m))
        for m in range(65): check(16*m+37<=37*2**m,'integer induction boundary diagnostics')
    except Exception as exc:
        status='FAIL_OR_INCOMPLETE'; error=repr(exc)
    result={'status':status,'error':error,'assertions':CHECKS,'runtime_seconds':perf_counter()-START,'domain':domain,'rows':rows,'helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'rung':'exact finite validation; analytic all-parameter reconstruction separate'}
    path=BASE/'out'/('PILOT.json' if 'pilot' in sys.argv else 'EXACT_RESULTS.json'); path.parent.mkdir(exist_ok=True)
    if path.is_file():
        prior=json.loads(path.read_text(encoding='utf-8'))
        if prior.get('error'): (BASE/'out'/'REPRESENTATION_LIMIT_FAILURE.json').write_text(json.dumps(prior,indent=2),encoding='utf-8')
    path.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
    if error: raise SystemExit(1)
if __name__=='__main__': main()
