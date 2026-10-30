"""Exact interval certificate for two-core stopping hulls, no fresh flow."""
from check import *
import check as engine
from itertools import combinations,product
from functools import lru_cache
ROOT=Path(__file__).resolve().parents[1]
TYPES=[('P',0)]+[('A',m) for m in range(6)]+[('L',m) for m in range(2,7)]
checks=0
def test(b):
    global checks
    assert b;checks+=1
def truth(t):
    k,m=t
    if k=='P':return (1,)
    return tuple(-1 if x in ({0} if k=='A' else {0,1,2}) else 1 for x in range(1<<m))
def rows(t):
    k,m=t
    if k=='P' or not m:return []
    if k=='A':return [(0,('A',m-1),('P',0))]
    ans=[(0,('A',m-2),('A',m-1))]
    if m>=3:ans.append((2,('L',m-1),('P',0)))
    return ans
def canonical(t):
    # Delete only pointwise equal dummy coordinates. Remaining truth is literal.
    while len(t)>1:
        n=(len(t)-1).bit_length()
        dummy=next((i for i in range(n) if child(t,i,0)==child(t,i,1)),None)
        if dummy is None:break
        t=child(t,dummy,0)
    for typ in TYPES:
        if truth(typ)==t:return typ
    raise AssertionError(('unrecognized',t))
def validate_reduction():
    count=nr=0
    for ass in product([-1,0,1],repeat=6):
        ts=tuple(G[x] for x in range(64) if all(b<0 or x>>i&1==b for i,b in enumerate(ass)))
        typ=canonical(ts);count+=1
        # Every remaining original coordinate is either a literal dummy or a saved row.
        allowed=[tuple(sorted((a,b))) for _,a,b in rows(typ)]
        for i in range((len(ts)-1).bit_length()):
            aa,bb=child(ts,i,0),child(ts,i,1);nr+=1
            if aa==bb:test(canonical(aa)==typ)
            else:test(tuple(sorted((canonical(aa),canonical(bb)))) in allowed)
    return count,nr
def avg(a,b):return scale(plus(a,b),F(1,2))
def negative(s):return max(0,-s[1]),max(0,-s[0])
@lru_cache(None)
def full(pair,a,b):
    ts=[(-1,),(1,)]+[G]*4;ts[pair[0]]=truth(a);ts[pair[1]]=truth(b)
    cs=[core(t) for t in ts];op=outer('J',tuple(c['p'] for c in cs));h,i=composed(op,cs)
    return h,i,sub(const(4*i),h)
@lru_cache(None)
def hull(pair,a,b):
    h,i,s=full(pair,a,b);stop=negative(s);lo,hi=stop;details=[]
    for axis,t in enumerate((a,b)):
        for coord,c0,c1 in rows(t):
            keys=[(c,a) if axis else (c,b) for c in (c0,c1)]
            if axis:keys=[(a,c0),(a,c1)]
            vals=[hull(pair,*k) for k in keys];iv=avg(vals[0][0],vals[1][0])
            # Independently verify the true physical influence telescoping on this row.
            hh=[full(pair,*k) for k in keys]
            q=outer('J',tuple(core(t0)['p'] for t0 in [(-1,),(1,)]+[truth(a) if j==pair[0] else truth(b) if j==pair[1] else G for j in range(2,6)]))['q'][pair[axis]]
            test(i-(hh[0][1]+hh[1][1])/2==q*core(truth(t))['d'][coord])
            lo=max(lo,iv[0]);hi=max(hi,iv[1]);details.append({'axis':axis,'representative_coordinate':coord,'children':keys,'mean_child_hull':iv})
    return (lo,hi),details
def main():
    start=time.perf_counter();reduction=validate_reduction()
    if '--pair' in sys.argv:
        z=sys.argv.index('--pair');pairs=[tuple(map(int,sys.argv[z+1:z+3]))]
    else:pairs=[(2,3)] if '--pilot' in sys.argv else list(combinations(range(2,6),2))
    result=[];allstates=[]
    for pair in pairs:
        for a,b in product(TYPES,repeat=2):hull(pair,a,b)
        root=('L',6);hv,rr=hull(pair,root,root);s=full(pair,root,root)[2];A=negative(s)
        margins=[sub(A,r['mean_child_hull']) for r in rr]
        ok=all(m[0]>0 for m in margins)
        result.append({'pair':pair,'root_S4':s,'supplied_credit':A,'root_hull_enclosure':hv,'root_continuation_margins':margins,'root_stop_strictly_dominates_all_queries':ok,'rows':rr})
        for a,b in product(TYPES,repeat=2):
            hh,ii,ss=full(pair,a,b);rv,rs=hull(pair,a,b)
            allstates.append({'pair':pair,'types':[a,b],'H':hh,'I':str(ii),'S4':ss,'hull':rv,'rows':rs})
        test(time.perf_counter()-start<55)
    tag='PAIR_'+''.join(map(str,pairs[0])) if '--pair' in sys.argv else 'PILOT' if '--pilot' in sys.argv else 'JOINT'
    (ROOT/'out'/f'{tag}_STATES.json').write_text(json.dumps(allstates,indent=2)+'\n',encoding='utf-8')
    summary={'version':'A089-two-core-hull-v1','pairs':len(pairs),'states':len(allstates),'canonical_types':TYPES,'labelled_restrictions_checked':reduction[0],'labelled_query_rows_checked':reduction[1],'all_root_stop_dominance':all(r['root_stop_strictly_dominates_all_queries'] for r in result),'checks':checks,'engine_checks':engine.tests,'runtime_seconds':time.perf_counter()-start,'results':result}
    (ROOT/'out'/f'{tag}_SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in summary.items() if k not in ['results','canonical_types']}))
    print('margins',[[float(F(m[0],Q)) for m in r['root_continuation_margins']] for r in result])
if __name__=='__main__':main()
